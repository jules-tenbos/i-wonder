# Mycelium XPath — Draft

Combined draft: ref lib page content + post notes.

---

## Ref lib page: docs/engineering/mycelium/xpath.md

### XPath as Fabric Language

XPath is the addressing and query language over the mycelium fabric's logical structure. The same path expression serves as both direct address to a known location and as a pattern that resolves against the fabric structure. One scheme navigates contexts, accesses records, and reaches metadata.

### Traversal

Navigation walks the path from root to target. At each segment, the traversal checks for context definitions — metadata. These are merged into an accumulator as the path is walked. Nearest distance wins: metadata defined closer to the target overrides metadata from further up the path.

Mutability, changelog mode, enforcement, and all other behavioural properties are driven by metadata accumulated during traversal. The path determines the rules. Different paths to different targets accumulate different metadata, producing different behaviour. The fabric is not uniformly configured — it is locally shaped.

### Point of View

Two levels of POV operate in the fabric:

- **Subject reality POV** — the repo root. The subject's overall perspective and the ceiling for functional resolution.
- **Process POV** — the invocation context (cwd). The data root for all queries.

### Addressing

All data addressing uses absolute syntax. `/` means the process POV (cwd) — there is no data concept of "above." Every query is absolute from where the process stands. No relative vs absolute distinction. The addressing language reflects the design: POV determines your reality.

### Data Scope and Functional Resolution

The fabric has two directional axes, each with strict visibility:

- **Data scope** — forward from process POV into self and descendants. `/` is the root. No data visibility outside this scope.
- **Functional resolution** — from process POV up the ancestor axis to subject reality POV (repo root). Nearest ancestor wins. No functional visibility outside this scope.

The functional axis connects process POV to subject reality POV. The data axis extends forward from process POV. The two axes never cross: data does not look up, function does not look down.

### Portability

This makes subtrees completely portable — data and functionality. A subtree's data scope is self-contained (everything below). Its functional context is accumulated from above. Addressing holds because `/` is always the process POV, not a fixed location. Lift a subtree, place it elsewhere in the fabric — same data, different ancestor axis, different functional resolution. The subtree doesn't need to know where it sits.

### Flat and Hierarchical Results

The default navigation of the tree is from context node to context node, flattening all simple (non-context) nodes. The query syntax does not change — what changes is the shape of the result set: flat or hierarchical. A node whose interior has no contexts returns a flat list. A node with nested contexts returns structure.

### Data Protocols

Six protocol contexts, all fabric. Three opaque, three schema-aware. Same three operations across all six: get, put, remove.

| Protocol | Visibility | Content |
|-----|-----------|---------|
| datauri | data nodes | opaque bytes |
| metadatauri | metadata nodes | opaque bytes |
| rawuri | all nodes | opaque bytes |
| data | data nodes | schema-interpreted |
| metadata | metadata nodes | schema-interpreted |
| raw | all nodes | schema-interpreted |

The uri level is purely structural — navigate, retrieve, place, remove. The schema-aware level adds content interpretation through discovered schemas. Both are base layer / fabric.

Separation is structural: data for data nodes only, metadata for metadata nodes only, raw for all nodes. No mixing of concerns.

The metadata dimension maps directly to protocol visibility: datauri sees data trees, metadatauri sees metadata subtrees, rawuri sees everything.

| Operation | Input | Output |
|-----------|-------|--------|
| get | keys | key-values |
| put | key-values | key-values |
| remove | keys | key-values |

### Design Principles

- **Protocol as context** — "get, in the context of datauri." The context shapes the behaviour.
- **Raw is full visibility** — the unfiltered physical reality. Data and metadata are lenses.
- **Opaque at uri level** — purely structural.
- **Structure is behaviour** — resolution envelope as schema fact. No configuration, no flags.
- **Bulk only** — no singular case.

---

## Post notes

### What makes this a post

The mycelium data fabric post (May 20) promises "a separate post on the base layer data protocols." This is that post. XPath over a logical structure — not the XML query language repurposed, but the addressing pattern applied to the fabric's own tree of records and contexts.

### Key angles for narrative

- **Why XPath?** — The fabric is a tree. XPath is a language for addressing trees. Not borrowed from XML — discovered as the natural fit for navigating contexts and records. Path expression as both address and query.

- **Traversal as accumulation** — Walking a path isn't just getting to a destination. Each step accumulates context. The path you take determines the rules that apply when you arrive. Different paths, different metadata, different behaviour. The fabric is locally shaped, not globally configured.

- **Six protocols, one pattern** — Three scope filters (data, metadata, raw) times two interpretation levels (opaque, schema-aware). Same three operations everywhere. The combinatorics are small and complete. No special cases.

- **Two POVs** — Subject reality POV (repo root) is the ceiling. Process POV (cwd) is the data root. `/` means here. Functional resolution connects the two; data extends forward from process POV.

- **Two axes, strict visibility** — Data looks down (self and descendants only). Function looks up (self and ancestors only). They never cross. Position in the tree determines both what you can do and what you can do it on.

- **Flat vs hierarchical** — Default navigation is context-to-context. Simple nodes flatten. The query doesn't change — the result shape does. This is a natural property of the structure, not a mode switch.

- **Raw as ground truth** — Raw sees everything. Data and metadata are lenses that filter. The physical reality is always accessible underneath.

### Connects to

- Mycelium Data Fabric post (May 20) — fulfils the "separate post on data protocols" promise
- Schema page — the three schema-aware protocols depend on schema discovery
- Layering — layers declared in context metadata, discovered during traversal
