---
title: Mycelium — The Data Fabric
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# Mycelium — The Data Fabric
Labels: mycelium, engineering, Splectrum

<img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Mycelium data fabric" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More on mycelium in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium area of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@christopher__burns">Christopher Burns</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Opening
- Thread from splectrum engineering post (May 16) — three pillars introduced there
- All three pillars are fabric implementations: reality (data), language, process (persona)
- The design: visible data state, processes operating on state, meaningful languages connecting them
- Mycelium is the base — the engineering foundation, fabric for data state repositories

### 2. Top layer design
- Mycelium repo: a data tree structure in a distributed version control system wrapper
- Tree structure for categorisation, version control for historicity, cloning, merging — core storage element
- A tree of data nodes. A node becomes a context when metadata nodes are added to it
- Metadata nodes are for process and other encapsulation — separate design, not covered here
- Git repo as the hard boundary — distinct entity with identity, history, integrity
- Mycelium runs in a trusted environment, within a secure boundary. Boundary = context (consistent with Splectrum's context model throughout)
- Subject reality — the repo IS the subject's reality. WYSIWYG: what you see is what there is. No hidden data, no hidden process, no encapsulated state
- No central data world — only subject realities. The whole is logical, never physical
- Shared reality through shared data state, not through process
- Writer owns data — only one owning reality per record
- Data referencing structures (read only, shared write with record-level ownership) — higher-level mycelium, not covered here
- Data-specific metadata (provenance, historicity) — higher-level mycelium, not covered here

### 3. Core layer
- Key-value records, opaque bytes, immutable or dirty (while part of an open transaction)
- Why opaque bytes — fabric doesn't interpret content. Any data, any language, any process can sit on top. Universal by design
- Navigation: path addressing (always local) and XPath for querying. Mycelium hides referencing
- All other structures built on top — higher-level mycelium functionality
- Schema contracts are a process concern — record-process contract, not core
- Specific operations not covered in this post

### 4. Subject dynamic
- Data state triggered processes
- Schema is process concern (record-process contract)

### 5. Philosophical alignment
- Show how the design choices follow from the seed principles — not asserted, visible through the design

### 6. Close
- Gesture forward — higher-level mycelium (referencing, metadata, access interfaces), the process nature, and the higher-level fabrics (language, persona)

---

## Reference page — docs/engineering/mycelium/index.md

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > Mycelium

# Mycelium — The Data Fabric

Mycelium is the data fabric — the engineering foundation from which the other fabrics build upward. It provides the base layer for data state repositories within Splectrum's three-fabric architecture: reality (data), language, and process (persona).

## Design

A mycelium repository is a data tree structure in a distributed version control system wrapper. The tree structure provides categorisation. The version control wrapper provides historicity, cloning, and merging. Together they form the core storage element.

The tree is made of data nodes. A node becomes a context when metadata nodes are added to it. Metadata nodes handle process embedding and other encapsulation — they have their own design, described separately.

### The boundary

The git repository is a hard boundary — a distinct entity with its own identity, history, and integrity. This boundary is a context, consistent with Splectrum's context model throughout.

Mycelium runs in a trusted environment, within a secure boundary.

### Subject reality

The repository IS the subject's reality. WYSIWYG — what you see is what there is. No hidden data, no hidden process, no encapsulated state.

There is no central data world. Only subject realities exist. The totality of data is a logical concept, never a physical repository. Shared reality is produced through shared data state, not through process.

### Ownership

The writer owns the data — only one owning reality per record.

### Why opaque bytes

Record content is opaque — the fabric does not interpret it. This means any data, any language, any process can sit on top of the core layer. The fabric is universal by design.

## Components

- [Core](core) — the base data structure: immutable key-value records, path addressing, XPath querying

### Planned

- **Higher-level mycelium** — data referencing structures (read-only, shared write with record-level ownership), data-specific metadata (provenance, historicity), access interfaces
- **Process integration** — data state triggered processes, schema as record-process contract

## Philosophical alignment

The design choices follow from the seed principles. The boundary expresses P0 (being implies language — an entity with identity). Subject realities express P2 (language is the medium through which a subject experiences reality — each subject has its own). Shared data state expresses P3 (where subjects share knowledge — through data, not process). Opaque content honours P4 (equal standing — no language imposed by the fabric).

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*

---

## Reference page — docs/engineering/mycelium/core.md

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Mycelium](./) > Core

# Mycelium Core

The base data structure of the mycelium fabric.

## Records

Key-value records. Content is opaque bytes. Records are immutable — once written, they do not change. A record that is part of an open transaction is dirty and can still change. When the transaction closes, the record becomes immutable.

## Navigation

Path addressing navigates the data tree. Addressing is always local — mycelium hides referencing. The subject sees only local paths, never remote locations.

XPath provides querying capability across the tree structure.

## What sits on top

Everything beyond records and navigation is higher-level mycelium functionality built on top of the core:

- Mutable structures (tables, indexes, document libraries) — process-layer projections maintained by embedded processes
- Data referencing structures — read-only references, shared write with record-level ownership
- Data-specific metadata — provenance, historicity, and other enrichment
- Access interfaces — different data access styles exposed on the core
- Schema contracts — a process concern, the record-process contract. Not a core concern

## Subject dynamic

Processes are triggered by data state, not by orchestration. The data state drives progression. Schema is a process concern — the contract between a record and the process that operates on it.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*

---

## Engineering index update — docs/engineering/index.md

Add to index:
- [Mycelium](mycelium/) — the data fabric, foundation layer for data state repositories

---

## Vocabulary updates

Review and update `docs/vocabulary.md` entries for:
- **Mycelium** — current entry is brief, may need enriching with fabric/foundation framing
- **Subject reality** — not currently a separate entry
- **Fabric** — not currently defined

---

## Tasks on scheduling

- [ ] Create docs/engineering/mycelium/index.md
- [ ] Create docs/engineering/mycelium/core.md
- [ ] Update docs/engineering/index.md — add mycelium link
- [ ] Update docs/vocabulary.md
- [ ] Delete submission submissions/mycelium-data-fabric.md
- [ ] Final image selection
- [ ] Schedule on Blogger
- [ ] Delete draft
