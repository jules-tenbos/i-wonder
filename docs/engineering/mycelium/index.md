[In Wonder - The World of Splectrum](../../) > [Engineering](../) > Mycelium

# Mycelium

The data fabric — the engineering foundation from which the other fabrics build upward. It provides the base layer for data state repositories within Splectrum's three-fabric architecture: reality (data), language, and process (persona).

A mycelium repository is a data tree structure in a distributed version control system wrapper. The tree structure provides categorisation. The version control wrapper provides historicity, cloning, and merging. Together they form the core storage element.

The git repository is the hard boundary — a distinct entity with its own identity, history, and integrity. The repository IS the subject's reality. There is no central data world. Only subject realities exist. The totality of data is a logical concept, never a physical repository. Shared reality is produced through shared data state, not through process.

Constitutive dependencies: git (identity, history, boundary) and AVRO (schema, conformance, protocol, interface).

- [Fabric](fabric) — the base data structure: immutable key-value records, path addressing, XPath querying, data APIs
- [Subject Reality](subject-reality) — the git repo as living subject: boundary, POV, references, self-contained from birth
- [AVRO Design Scope](avro-design-scope) — constitutive dependency alongside git: schema, conformance, protocol, interface
- [Git Design Scope](git-design-scope) — constitutive dependency alongside AVRO: historicity, identity, boundary, decentralised exchange

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
