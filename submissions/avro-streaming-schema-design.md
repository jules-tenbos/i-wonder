# AVRO and Streaming Schema Design
## Submission — design session 2026-04-15

This submission captures a design conversation about how AVRO schemas, logical types, and Kafka records relate in the mycelium architecture. It clarifies several concepts that were previously conflated and establishes cleaner separations.

---

## 1. AVRO Logical Types — Properly Scoped

AVRO logical types annotate physical types at the field level. `{"type": "int", "logicalType": "date"}` — the physical type is `int`, the logical type says how to interpret those bytes. This is a schema-level annotation, not a data-level value. It extends a physical type description — it does not introduce a separate type system.

Logical types operate at the property level, not the schema level. You cannot put a logicalType on a record — only on primitive and fixed types within fields. Records get their identity from namespace + name.

**Consequence for mycelium:** AVRO logical types are the right mechanism for field-level meaning annotations within structured data. `date`, `decimal`, `timestamp` — these extend field descriptions with interpretation context. They are NOT the right mechanism for what mycelium has been calling "logical types" in the streaming context (operator dispatch, record type identification). These are two different concepts that were sharing one name.

---

## 2. Record Type — Replacing "Logical Type" in Streaming

What mycelium has been calling the "logical type" in the message dispatch context (`headers.record.logicalType`) is actually the **record type** — the type of the Kafka record. It identifies what the record IS and what should happen with it. It lives in the data (as a value in a property bag), not in the schema (as an annotation on a physical type).

The record type concept goes beyond operators — it covers interpretation, transformation, and intent. All are Kafka records. The name "record type" reflects this scope.

**Renaming:**
- `headers.record.logicalType` → `headers.record.type` (or equivalent — the field name is a design choice)
- "Logical type" in the streaming/dispatch context → "record type"
- "Logical type" in the AVRO field annotation context → stays "logical type" (AVRO's own term)

---

## 3. The Kafka Record — Logical Structure

The mycelium Kafka record is a logical concept. The physical representation must be compatible but is an implementation concern. The logical structure is:

- **Key** — identity. What makes this datum addressable.
- **Headers** — a tree structure with property bags. Carries context, metadata, schema references, the record type.
- **Value** — the data payload. AVRO-serialized with a declared schema.

The headers are the self-describing layer. They carry everything needed to interpret the record.

---

## 4. JSON as Logical Structure, AVRO as Conformance

All structured data in mycelium can be thought of logically as JSON — tree-structured, readable, open, navigable. AVRO schemas provide conformance — validation, typing, schema evolution — where precision is needed. How the data is physically represented (binary AVRO, JSON on disk, Kafka header bytes) is an implementation concern below this line.

Three concerns, cleanly separated:
- **Logical:** JSON tree with property bags. Readable, open, navigable.
- **Conformance:** AVRO schemas validating extracts. Typed where declared, open where not.
- **Physical:** whatever representation suits the context. Binary for performance, JSON for readability, Kafka bytes for streaming.

avsc (the JavaScript AVRO implementation) validates JavaScript objects natively. JSON.parse gives JavaScript objects. So: parse JSON, extract a subtree, validate against an AVRO schema with `type.isValid()`. The AVRO schema is a validation tool for parts of the JSON tree — not necessarily the serialization format.

---

## 5. Kafka Record Headers — Fabric Grammar

Kafka record headers are physically a flat list of key-value pairs (string key, byte[] value). But logically, the header key names form a tree structure — the same identifier grammar as the fabric.

Individual key-value pairs can be added to Kafka's native header mechanism. Each key is a namespace path. Each value is bytes that can have a schema declared for it. The headers are a property bag using Kafka's own structure, with schema declarations layered on top.

For the flexible/extensible parts of the headers, JSON is the right carrier — readable, tree-structured, open to extensions, no schema needed to parse. Specific extracts of the JSON can be validated against AVRO schemas where conformance is needed.

The header tree IS fabric in motion. The same grammar applies: dot-navigated tree structure, underscore-prefixed property bags at nodes. The streaming language doesn't introduce new structure — it carries the existing structure.

---

## 6. AVRO Schemas as the Namespace Assignment Mechanism

AVRO schemas are the single mechanism that assigns namespace to field names. That is their role. Everything else follows.

- A field name is a short name
- The AVRO schema gives it a fully qualified identity (namespace + name)
- Property bags in the fabric, headers in the Kafka record, fields in structured data — all the same thing: a set of short names with an AVRO schema assigning namespace

### Node path = schema name

When navigating the tree (dot) and encountering underscore-prefixed fields at a node, the node's dot-navigated name IS the physical AVRO schema name for that set of fields. The tree path and the schema name are the same string. Schema discovery is free — the identifier grammar gives it to you.

### Structured data restarts the tree

When entering a structured data set (AVRO-encoded content in key, value, or any payload), the tree restarts. New root, new schema, new navigation. The outer tree got you there. The inner tree is its own world.

### Field logical types prefix into new namespace

Within structured data, a field's AVRO logical type shifts that field's name into a different namespace. The physical schema gives the carrier (the bytes). The logical type prefixes into the meaning namespace (the interpretation). This can point to another physical AVRO schema — which has its own fields, which can have their own logical types. Recursive, unlimited depth.

The mechanism at every level:
1. Physical AVRO schema defines fields (a tree of names with namespace)
2. A field's logical type can prefix into a new namespace → identifying another physical schema
3. That schema defines its own fields → another tree
4. Recursive

---

## 7. Record Type and AVRO Schema — Same String, Different Roles

The record type string (e.g. `spl.mycelium.xpath.data.uri.get`) and an AVRO named type with the same fully qualified name can coexist. They live in different identifier spaces in AVRO — the named type is in the type registry, the record type is a data value. No collision.

However, making them intentionally identical is not the right default. If every record type needed its own AVRO schema as the physical type before `{`, we would need to alias a physical type for every record type — structurally identical schemas differing only in name. This breaks the one-code-path principle.

**The RPC server design:**
- The RPC server accepts any Kafka record through a single base schema
- The base schema defines the common structure: record type (string), args, value
- Specific schemas narrow the base — single-symbol enum constrains the record type, typed args and value
- Deserialization and validation are different: deserialization uses the writer schema (always available via handshake or headers), validation uses reader schemas for conformance checking
- The base schema gets you in the door. The specific schema gets you typed processing.

---

## 8. Aliases — Repo Scope, Colocated with Protocols

AVRO supports aliases on both types and fields. During schema resolution, aliases are checked — if a name matches any alias, it resolves. This gives:
- Multiple readings of the same schema through different namespace paths
- Schema evolution — rename without breaking existing references
- Cross-namespace references — one language's concept addressable through another's naming

Aliases are declared on the schema definition (one `aliases` array per type/field). This makes them repo-scoped — the subject reality declares its schemas and their aliases as part of its own commitments.

This is the right scope. Schemas are a repo concern, not a local node concern. They belong colocated with the mycelium protocols at the repo root — the protocols define what operations are available, the schemas define the structure of what those protocols operate on, the aliases define the names by which they're known. All one package.

**Growth path:** A process invoked on a tree node has visibility of self-or-descendant data only. It only needs schemas and aliases that are in scope. While the starting point is repo-level (all schemas at the root), the architecture supports more local placement — schemas in context metadata at specific nodes, discovered during traversal. This is a process management maturity progression, not a structural change.

---

## 9. The Static/Dynamic Schema Distinction

**Static schema** — AVRO schema definition. Fixed structure. Defines what the bytes are. Lives in repo metadata. Conformance is reader vs writer schema resolution.

**Dynamic schema** — a structured data description of a Kafka record instance. Describes what this specific record is for — the record type, the input args, the output schema. Travels with the record. Not an AVRO schema annotation — data about data, self-description in motion.

AVRO logical types (date, decimal) belong in static land — they extend physical type descriptions at the field level.

Record types belong in dynamic land — they are data values in the Kafka record's header tree, identifying what the record is and dispatching to the right handler.

---

## Impact on Reference Library

This submission affects:
- **avro-design-scope.md** — type system section needs rework. Separate AVRO logical types (field-level, static) from record types (streaming, dynamic). Update governing principles with JSON-as-logical-structure and three-concern separation.
- **message.md** — rename logicalType references to record type. Update the concrete message examples. Clarify that the message structure is logically JSON with AVRO conformance.
- **kafka-design-scope.md** — update "Logical Types and the Kafka Record" section. The logical type spectrum (interpretation/transformation/intent) applies to record types, not AVRO logical types. Add the headers-as-fabric-grammar concept.
- **identifier-grammar.md** — add the structured-data-restarts-tree and field-logical-type-as-namespace-prefix patterns. The recursive mechanism.
- **fabric.md** — node dot-name = schema name for underscore fields. Strengthen the schema-as-namespace-assignment framing.
- **protocol.md** — schemas and aliases colocated with protocols at repo scope.

## Impact on Scheduled Posts

Posts already scheduled may reference "logical type" in contexts where "record type" is now the correct term. Review needed for:
- Data in Motion (June 20) — most affected, dispatch discussion
- Two Moves (June 8) — physical/logical section
- Three Languages (June 12) — protocol operations as data in motion
- AVRO — The Language of Articulation (June 4) — type system mention in storyline (not in narrative)

The protocol post (The Meaning of Get) draft should incorporate this thinking — the protocol/operator binary, record types, the base interface.
