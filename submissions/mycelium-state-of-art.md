---
title: "Mycelium — State of the Art"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium — State of the Art

Substantial submission. Where mycelium sits relative to current data architectures.

---

### Immutable Data Architectures

Event sourcing, lakehouse table formats (Iceberg, Delta Lake, Hudi), and immutable databases (Datomic, EventStoreDB) all use immutability — but as a feature of specific components. Mycelium places immutability at the base layer of the entire fabric. Everything mutable is derived. A stronger commitment than any current approach.

### Decentralised Data

Data mesh distributes ownership across human teams. Mycelium distributes data itself across autonomous reality bubbles — ontological decentralisation, not organisational. Data fabric creates a unified integration layer; mycelium has no unified layer, only coupling between realities through shared immutable records. IPFS is infrastructure (storage/retrieval); mycelium is a data model that could use IPFS as a physical layer.

### Version-Controlled Data

Dolt applies git semantics to tables within a database. Mycelium makes the git repo the fundamental unit of data existence and layers multiple access interfaces on top. Versioning is intrinsic to the fabric, not a feature bolted onto a database. Compared to lakehouse time travel, git provides a full graph of evolution across parallel lines, not just point-in-time snapshots.

### Blockchain and Trust

Most systems are either blockchain-native or blockchain-free. Mycelium is blockchain-ready at the boundary without being blockchain-dependent at the core. The transaction lifecycle is structurally identical regardless of the consensus mechanism. Blockchain slots in as optional consensus for hostile environments without changing the architecture.

### Access Interface Pluralism

Lakehouse formats expose one paradigm (tables) to multiple engines. Mycelium exposes one immutable base to multiple paradigms — file, XPath, RDBMS, document. The consumer doesn't choose an engine; they choose their entire data model. No access format is privileged.

### Summary

| Dimension | State of Art | Mycelium |
|---|---|---|
| Immutability | Feature of components | Base layer of fabric |
| Decentralisation | Organisational or infrastructural | Ontological — autonomous reality bubbles |
| Versioning | Applied to tables or snapshots | Intrinsic via git as boundary |
| Blockchain | Native dependency or absent | Optional consensus at boundaries |
| Access | Multi-engine, one paradigm | Multi-paradigm, one base |
| Trust | Binary — trusted or trustless | Trust-agnostic, hardened at boundaries |
| Data world | Assumed queryable whole | Logical totality; only realities instantiated |
| Grounding | None | Splectrum seed principles |

Mycelium does not compete with any single technology. It operates at a different level of abstraction — a data fabric design that could be implemented using combinations of existing tools while making architectural commitments none make individually.
