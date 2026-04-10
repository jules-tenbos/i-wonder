[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Mycelium](./) > Fabric

# Mycelium Fabric

The base data structure of the mycelium fabric. Structure is behaviour — what you build is how it behaves, what you don't build can't happen. Architecture of absence. No configuration, no flags.

## Records

Key-value records. Content is opaque bytes — the fabric does not interpret content. Any data, any language, any process can sit on top. The fabric is universal by design.

Records are immutable — once written, they do not change. A record that is part of an open transaction is dirty and can still change. When the transaction closes, the record becomes immutable. The source of truth is always immutable records.

## Contexts

A node in the tree becomes a context when metadata nodes are added to it. The context is where behaviour lives — process definitions, schemas, language declarations. All embedded in the metadata, all discoverable during traversal.

## Navigation

Path addressing navigates the data tree. Addressing is always local — mycelium hides referencing. The subject sees only local paths, never remote locations.

XPath provides querying capability across the tree structure.

## Mutable Structures

Mutable structures — tables, indexes, document libraries — are projections maintained by embedded processes. They are not primary data. You can throw them away and rebuild them from the immutable base.

## What sits on top

Everything beyond records, contexts, and navigation is higher-level mycelium functionality built on top of the fabric:

- Data referencing structures — read-only references, shared write with record-level ownership
- Data-specific metadata — provenance, historicity, and other enrichment
- Access interfaces — different data access styles exposed on the fabric
- Schema contracts — a process concern, the record-process contract. Not a fabric concern

## Subject dynamic

Processes are triggered by data state, not by orchestration. The data state drives progression. Schema is a process concern — the contract between a record and the process that operates on it. The process declares what it needs through its reader schema. The data either conforms or it doesn't.

## Data APIs

Three APIs are planned on the fabric, each serving a different access pattern:

- **Data** — structured data access
- **Metadata** — fabric metadata access
- **Raw** — direct byte-level access

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
