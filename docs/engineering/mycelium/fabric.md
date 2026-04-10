[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Mycelium](./) > Fabric

# Mycelium Fabric

The base data structure of the mycelium fabric.

## Records

Key-value records. Content is opaque bytes. Records are immutable — once written, they do not change. A record that is part of an open transaction is dirty and can still change. When the transaction closes, the record becomes immutable.

## Navigation

Path addressing navigates the data tree. Addressing is always local — mycelium hides referencing. The subject sees only local paths, never remote locations.

XPath provides querying capability across the tree structure.

## What sits on top

Everything beyond records and navigation is higher-level mycelium functionality built on top of the fabric:

- Mutable structures (tables, indexes, document libraries) — process-layer projections maintained by embedded processes
- Data referencing structures — read-only references, shared write with record-level ownership
- Data-specific metadata — provenance, historicity, and other enrichment
- Access interfaces — different data access styles exposed on the fabric
- Schema contracts — a process concern, the record-process contract. Not a fabric concern

## Subject dynamic

Processes are triggered by data state, not by orchestration. The data state drives progression. Schema is a process concern — the contract between a record and the process that operates on it.

## Data APIs

Three APIs are planned on the fabric, each serving a different access pattern:

- **Data** — structured data access
- **Metadata** — fabric metadata access
- **Raw** — direct byte-level access

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
