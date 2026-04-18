[Home](/) > [Engineering](/engineering/) > [Mycelium](/engineering/mycelium/) > Identifier Grammar

# Identifier Grammar

The mycelium fabric is an identifier structure with property bags attached to it. Nodes are not files or folders — they are identifier points. Everything a node *has* is properties in bags. The fabric primitive is: identifier point mapped to property bags. The key is the address. The properties are the reality.

The grammar has exactly two structural moves.

## Dot — Tree Navigation

Dot navigates the identifier tree. Each segment is the next step in the address space. The parent is the namespace for the child. The name is namespaced by its position in the tree.

`xpath.data.uri` — three segments, each namespaced by its parent. The path *is* the qualification.

The meaning of "defines" shifts depending on what both parent and child are. `xpath` to `data` — a system contains a domain. `data` to `uri` — a domain contains a sub-protocol. `uri` to `get` — a protocol defines an operation. Three different relationships, same dot grammar. The schemas at both ends tell you what kind of relationship it is.

## Underscore — Property Bag

Underscore opens a property bag at the current node. A lateral move, not a deeper one. The bag is *at* the node, not *below* it. Inside the bag, property names get their namespace from the bag's AVRO schema, not from tree position.

No overlap between dot and underscore. Dot walks the address space. Underscore opens the property space. Everything else is schema content.

## Property Bags as Contexts

A property bag is a context. It is a boundary that contains properties and assigns namespace within it. The same structural pattern as a mycelium context: boundary, containment, meaning assignment.

The `_` boundary is P0 — the creation. Opening a property bag creates a context. The bag has identity (its schema), a world (its properties), and the relational between them is the namespace assignment.

Property bags nest the same way contexts nest in the fabric. A bag within a bag is a subcontext. Inner schemas can override namespace for names the outer schema also defines. Resolution follows the same ancestor pattern.

## Namespace Resolution

Two mechanisms, one for each primitive.

**Tree-positional (dot)** — the name inherits its namespace from the tree path. `xpath.data.uri` — each segment is namespaced by its parent. The path *is* the qualification.

**Schema-assigned (underscore)** — the AVRO schema of the containing bag assigns namespace to the short names within it. The schema is the authority. A property named `record` inside a headers bag gets its fully qualified identity from the headers schema.

The underscore primitive switches namespace resolution from tree-positional to schema-assigned.

## Short Names and Fully Qualified Identifiers

Properties use short names that are meaningful within context. `headers`, `record`, `args`, `value` — plain words that read naturally. The AVRO schema carries the namespace. The message carries readable names.

The fully qualified identifier contains all the reality information of the property. The namespace chain from any property back through its containing schemas is the explanation of what it is. The namespace is not a prefix in the trivial sense of a string prepended for uniqueness — it is the reality context. Strip segments away and you lose information about what the thing is.

The system has three faces of the same structure:

- **Human-readable** — short names, contextually meaningful.
- **Machine-resolvable** — schema-assigned namespaces, fully qualified identities.
- **Self-describing** — any node can answer "what am I?" by resolving its name through its schema chain.

## Defined vs Applied Operators

Operators that a protocol *defines* — `get`, `put`, `delete` — are part of the protocol's identity. They belong in the tree. Dot-navigated. Namespaced by position. Without them, it is a different protocol.

Operators that are *applied to* a node — `_is`, `_noop` — come from outside. They are not part of what makes the node what it is. Any node can be asked `_is`. These belong in property bags. Underscore. Namespaced by schema. They are visitors, not constituents.

The test: does this operator exist because *this specific node* declares it, or because a schema brought it from a base interface?

The tree does not enforce categories. The schema at each node tells you what kind of thing it is. Whether a protocol can also be an operator is a schema question, not a structural one. Nothing in the grammar prevents a node from carrying multiple schema identities.

## Self-Description and Architecture of Absence

The system can function without full schema description. Code runs with short names. Properties hold values. The system is "dirty" with respect to its own self-knowledge — it functions, it just does not know what it is.

Adding schemas is the same move as adding mutability metadata to a dirty fabric. The system gains insight into itself incrementally. No hard boundary between "not ready" and "ready." Insight-first — if the thinking is clear, the naming is good from the start. The formal description catches up to what was already understood.

Full description is needed for shared knowledge (P3). The insight is real without schemas (P2, experienced reality). For it to become shared, it must pass through language interaction. Premature formalisation produces shared confusion, not shared knowledge. Description absent until the insight is genuine, then describe.

