---
title: "Message and Identifier Structure"
type: substantial
status: in-progress
destinations: engineering
---

# Message and Identifier Structure

Discussion notes from spl5 sessions 2026-04-14.
Working through the message format, identifier
grammar, property bag model, and record structure
for the AVRO RPC server implementation.

---

## The Identifier Tree

The mycelium fabric is an identifier structure with
property bags attached to it. Nodes are not files or
folders — they are identifier points. Everything a
node *has* is properties in bags.

A file is a leaf node with property bags, one
property being file contents. The distinction between
data and metadata is not structural — it is a schema
distinction. Content is a property whose schema
namespaces it as content. Metadata is a property
whose schema namespaces it as metadata. The fabric
does not know the difference. The schemas do.

The fabric primitive is: identifier point mapped to
property bags. The key is the address. The properties
are the reality.

---

## Identifier Grammar — Two Primitives

The grammar has exactly two structural moves:

**Dot** — navigates the identifier tree. Each
segment is the next step in the address space. The
parent is the namespace for the child. The name is
namespaced by its position in the tree.

**Underscore** — opens a property bag at the current
node. A lateral move, not a deeper one. The bag is
*at* the node, not *below* it. Inside the bag,
property names get their namespace from the bag's
AVRO schema, not from tree position.

No overlap between them. Dot walks the address
space. Underscore opens the property space.
Everything else is schema content.

### Property Bags as Contexts

A property bag is a context. It is a boundary that
contains properties and assigns namespace within it.
The same structural pattern as a mycelium context:
boundary, containment, meaning assignment.

The `_` boundary is P0 — the creation. Opening a
property bag creates a context. The bag has identity
(its schema), a world (its properties), and the
relational between them is the namespace assignment.

Property bags nest the same way contexts nest in the
fabric. A bag within a bag is a subcontext. Inner
schemas can override namespace for names the outer
schema also defines. Resolution follows the same
ancestor pattern.

### Namespace Resolution — Two Mechanisms

**Tree-positional (dot)** — the name inherits its
namespace from the tree path. `xpath.data.uri` —
each segment is namespaced by its parent. The path
*is* the qualification.

**Schema-assigned (underscore)** — the AVRO schema
of the containing bag assigns namespace to the short
names within it. The schema is the authority. A
property named `record` inside a headers bag gets its
fully qualified identity from the headers schema.

This is the real meaning of the `_` primitive:
switch namespace resolution from tree-positional to
schema-assigned.

### Short Names and Fully Qualified Identifiers

Properties use short names that are meaningful within
context. `headers`, `record`, `args`, `value` — plain
words that read naturally. The AVRO schema carries
the namespace. The message carries readable names.

The fully qualified identifier contains all the
reality information of the property. The namespace
chain from any property back through its containing
schemas is the explanation of what it is. The
namespace is not a prefix in the trivial sense of a
string prepended for uniqueness — it is the reality
context. Strip segments away and you lose information
about what the thing is.

The system has three faces of the same structure:

- **Human-readable** — short names, contextually
  meaningful.
- **Machine-resolvable** — schema-assigned
  namespaces, fully qualified identities.
- **Self-describing** — any node can answer "what am
  I?" by resolving its name through its schema chain.

### Self-Description and Architecture of Absence

The system can function without full schema
description. Code runs with short names. Properties
hold values. The system is "dirty" with respect to
its own self-knowledge — it functions, it just does
not know what it is.

Adding schemas is the same move as adding mutability
metadata to a dirty fabric. The system gains insight
into itself incrementally. No hard boundary between
"not ready" and "ready." Insight-first — if the
thinking is clear, the naming is good from the start.
The formal description catches up to what was already
understood.

Full description is needed for shared knowledge (P3).
The insight is real without schemas (P2, experienced
reality). For it to become shared, it must pass
through language interaction. Premature formalisation
produces shared confusion, not shared knowledge.
Description absent until the insight is genuine, then
describe.

---

## Defined vs Applied — Dot and Underscore Operators

The identifier tree carries definitional structure.
Nodes are defined within the tree by their parent.
The parent-child relationship is part of the
identity. The meaning of "defines" shifts depending
on what both parent and child are:

`xpath` to `data` — a system contains a domain.
`data` to `uri` — a domain contains a sub-protocol.
`uri` to `get` — a protocol defines an operation.

Three different relationships, same dot grammar. The
schemas at both ends tell you what kind of
relationship it is.

Operators that a protocol *defines* — `get`, `put`,
`delete` — are part of the protocol's identity. They
belong in the tree. Dot-navigated. Namespaced by
position. Without them, it is a different protocol.

Operators that are *applied to* a node — `_is`,
`_noop` — come from outside. They are not part of
what makes the node what it is. Any node can be asked
`_is`. These belong in property bags. Underscore.
Namespaced by schema. They are visitors, not
constituents.

The test: does this operator exist because *this
specific node* declares it, or because a schema
brought it from a base interface?

The tree does not enforce categories. The schema at
each node tells you what kind of thing it is. Whether
a protocol can also be an operator is a schema
question, not a structural one. Nothing in the
grammar prevents a node from carrying multiple schema
identities.

---

## Protocol Namespace Structure

The original flat six-API design used compound names
(`datauri`, `metadatauri`, `rawuri`) that hid
structural relationships in naming convention.
Breaking them into tree structure makes the
relationships explicit.

The protocol hierarchy with defined operators:

```
xpath.data.uri.get
xpath.data.uri.put
xpath.data.uri.delete
xpath.data.get
xpath.data.put
xpath.data.delete

xpath.metadata.uri.get
xpath.metadata.uri.put
xpath.metadata.uri.delete
xpath.metadata.get
xpath.metadata.put
xpath.metadata.delete

xpath.raw.uri.get
xpath.raw.uri.put
xpath.raw.uri.delete
xpath.raw.get
xpath.raw.put
xpath.raw.delete
```

Every level is the same definitional move. `xpath`
defines three visibility domains. Each domain
defines `uri` as an opaque sub-protocol. Both the
domain and the sub-protocol define `get`, `put`,
`delete` as operators. The schemas at each node
distinguish sub-protocol from operator.

Applied operators — `_is`, `_noop`, and whatever base
interface emerges — are in property bags at any
identifier point. They compose through the schema
inheritance mechanism, not through the tree.

---

## Tree at Rest, Tree in Motion — The Kafka Record

The tree is the universal structure. It sits still
or it moves. What container it sits in at rest is a
storage question — a file, a database, an in-memory
structure. When it moves — when it becomes active —
it goes into a Kafka record.

The Kafka record does not introduce new structure. It
introduces *directionality*. The tree is symmetric.
The Kafka record says: this part is the question,
this part is the answer. Same structure, now
polarised.

**Headers** — the piece of tree that describes *what
you want done*. Context, intent, operator arguments.
Tree structure serving as input.

**Value** — the piece of tree that holds *the
result*. Starts empty, fills during execution. Tree
structure serving as output.

A pure data transfer is not a special case. Every
message is an operator invocation. Pure data transfer
is `noop` — an operator with fully qualified identity
`spl.splectrum.operator.noop`, a specific contract
(value passes through unchanged), and `args: null` as
its legitimate interface. The RPC server has exactly
one code path.

---

## Message Shape — The Onion

Every message is a nested Kafka record. Each layer
has the same two sides: headers and value. Peel a
layer — same structure underneath.

The outer layer is the execution envelope. The inner
layer is the protocol operator. Both are Kafka
records. Same shape at every nesting level.

### Headers as Property Bag

Headers is a property bag — a context with an AVRO
schema assigning namespace to short names within it.
Properties inside headers are just properties. Fully
qualified or not, based on the schema.

The headers schema contains:

**record** — a property whose schema identifies the
operator and its arguments. `record` is itself a
property bag. Its schema gives `logicalType` and
`args` their namespace.

Additional properties alongside `record` carry
execution context — tracing, routing, processing
metadata. These get their namespace from the headers
schema.

```
headers: {
  record: {
    logicalType: 'spl.splectrum.operator.noop',
    args: null
  },
  spl.trace.id: ...,
  spl.mycelium.context: ...
}
```

The `record` property is the *what* — the operation.
Everything else in headers is the *how* — execution
context. Two concerns, cleanly separated within the
same property bag.

Dispatch reads one path: `headers.record.logicalType`.
That is the routing key.

### Schema as Namespace Authority at Every Level

The namespace resolution is uniform at every level
of the message:

- Kafka record has an AVRO schema. That schema gives
  `headers` its namespace. `headers` becomes
  `spl.mycelium.message.headers`.
- Headers is a property bag with an AVRO schema. That
  schema gives `record` its namespace. `record`
  becomes `spl.mycelium.operator.record`.
- Record is a property bag with an AVRO schema. That
  schema gives `logicalType` and `args` their
  namespace.

Each schema is the namespace authority for the names
it contains. No level is special. No level resolves
differently. One mechanism applied recursively.

### The Concrete Message

An RPC server execution envelope wrapping a get
request:

```
spl.mycelium.process.execute.exec {
  headers: {
    record: {
      logicalType: 'spl.mycelium.process.execute',
      args: { mode: 'sync' }
    }
  },
  key: "/blog/submissions",
  value: xpath.data.uri.get {
    headers: {
      record: {
        logicalType: 'spl.splectrum.operator.get',
        args: { filter: ... }
      }
    },
    key: "/blog/submissions",
    value: <output>
  }
}
```

The outer layer is the execution envelope — its
headers identify the execution operator and mode. Its
value carries the inner operator as a complete
computation record.

The inner layer is the protocol operation — its
headers identify the data access operator and args.
Its value starts empty and fills with the retrieved
data.

### Processing Pipeline

```
arrive   -> headers: args          value: empty
validate -> headers: args          value: validated input + output schema
execute  -> headers: args          value: output
error    -> headers: args + error  value: partial/empty
```

Same pattern at both levels. The pipeline is uniform
because the entry point is always the same shape.
Validation is: does the logical type resolve to a
known operator schema? Do the args conform?

### Request and Response

The response returns the request enriched with the
result. No separate response message. The same
message at every stage, just more resolved.

**get** — request: args in headers, value empty.
Response: value filled with retrieved data.

**put** — request: args in headers, value carries
data to write. Response: value confirmed.

**delete** — request: args in headers, value empty.
Response: value carries what was removed.

**noop** — request: args null, value carries data
payload. Response: value passed through unchanged.

### Design Properties

**Self-contained** — pick the message up at any
stage, read what was asked (headers) and how far it
got (value).

**Enrichment not replacement** — the message
accumulates. Request context preserved.

**Errors don't break the shape** — error conditions
add metadata to headers. No separate error envelope.

**Same shape sync and async** — the echo-back pattern
works whether response returns immediately or via a
queue.

**Uniform dispatch** — every message is an operator
invocation. No branching on message category. The
logical type in `headers.record` is the single
dispatch mechanism.

---

## Summary of Structural Decisions

**Two grammar primitives.** Dot navigates the
identifier tree. Underscore opens a property bag.
No overlap, no exceptions.

**Property bag is a context.** Same structural
pattern as a mycelium context. Boundary, containment,
namespace assignment.

**AVRO schema is the sole namespace authority within
bags.** Short names get their fully qualified identity
from the containing schema. The tree grammar handles
navigation. AVRO handles identity.

**Defined operators use dot, applied operators use
underscore.** `xpath.data.uri.get` — defined by the
protocol, part of its identity. `xpath.data.uri._is`
— applied from outside, universal capability.

**Every message is an operator invocation.** Pure data
transfer is `noop`. One code path in the RPC server.

**Headers is a property bag with structured
dispatch.** `headers.record.logicalType` is the
routing key. Additional properties carry execution
context.

**Tree at rest, tree in motion.** The Kafka record
is tree structure with directionality applied.
Headers are the question. Value is the answer.

**Self-description is incremental.** The system
functions with short names. Schemas add self-knowledge
progressively. Architecture of absence until insight
is genuine.

---

## Open Areas

**Base interface operators.** The vocabulary of
universally applied operators (`_is`, `_noop`, and
others) needs definition as a schema set.

**Headers base schema.** The minimum headers
structure that every message must conform to, with
extension points for protocol-specific additions.

**Data change record format.** The mutable protocol
applies data change records but their format is not
yet defined.

**Queue protocol.** The immutable queue that feeds
the mutable protocol needs its own protocol identity.

**Prototyping.** Whether the protocol hierarchy holds
during actual resolution. Whether the message format
performs under real execution conditions.
