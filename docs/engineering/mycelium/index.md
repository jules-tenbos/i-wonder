[Home](/) > [Engineering](../) > Mycelium

# Mycelium

The data fabric — the engineering foundation from which the other fabrics build upward. It provides the base layer for data state repositories within Splectrum's three-fabric architecture: reality (data), language, and process (persona).

A mycelium repository is a data tree structure in a distributed version control system wrapper. The tree structure provides categorisation. The version control wrapper provides historicity, cloning, and merging. Together they form the core storage element.

The git repository is the hard boundary — a distinct entity with its own identity, history, and integrity. The repository IS the subject's reality. There is no central data world. Only subject realities exist. The totality of data is a logical concept, never a physical repository. Shared reality is produced through shared data state, not through process.

Mycelium operates at the intersection of three committed languages: AVRO (structure), git (historicity), and Kafka (mobility). Each addresses one orthogonal concern. None is mycelium. Mycelium is where they meet.

- [Fabric](fabric) — the static substrate: identifier points, property bags, contexts
- [Identifier Grammar](identifier-grammar) — dot/underscore primitives, property bags, namespace resolution, defined vs applied
- [XPath](xpath) — addressing, traversal, protocol namespace hierarchy
- [Layers](layers) — layered data access, read modes, synchronisation, safe mode
- [Protocol](protocol) — meaning context for operations, defined and applied operators
- [Message](message) — the tree in motion: Kafka record onion, headers, dispatch, noop
- [Subject Reality](subject-reality) — the git repo as living subject: boundary, POV, references, self-contained from birth
- [Mutability](mutability) — the interrogative protocol: regime discovery, replication characteristics
- [Mutable](mutable) — the operational protocol: living surfaces from immutable queues
- [AVRO Design Scope](avro-design-scope) — committed language for structure: schema, conformance, type system, resolution
- [Git Design Scope](git-design-scope) — committed language for historicity: identity, boundary, decentralised exchange
- [Kafka Design Scope](kafka-design-scope) — committed language for mobility: streaming, the Kafka record, logical type spectrum

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
