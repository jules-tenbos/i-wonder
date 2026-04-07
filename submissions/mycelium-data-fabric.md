---
title: "Mycelium — The Data Fabric"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium — The Data Fabric

Substantial submission. Introductory engineering post on mycelium — what it is and how it works. Combines the data fabric definition with the behavioural principles.

---

## What Mycelium Is

Mycelium is a data fabric used to create process-colocated data structures — it weaves data and process together. These structures are placed within a git repo which contains and manages the repository structure and optionally its operation. Within Splectrum the base-level repositories are called subject realities (conforming P2). They have a partial view of available data. The totality of data is never a physical repository, only a logical repository. Mycelium repositories are dynamic and self-contained at the base level with local embedding of processes.

## The Fabric

The fabric is built from one primitive:

**Record** = key → content (opaque bytes).
**Context** = bounded area that contains records.
Records can themselves be contexts.

Content is opaque — the fabric does not interpret it. Keys are local to the context where the process is instantiated. Schema contracts — the specific structure of data — are a concern of the embedded process layer, not the fabric. The fabric uses a Common Data Model (CDM) for data; specific schema contracts sit between the embedded process and the data structure it operates on.

Proven sufficient across 18 projects. No extensions required.

The mycelium fabric is concerned with:
- How data and process are mixed — colocation, embedding
- Data navigation — XPath-style base layer
- Data referencing — cascading references, read wide write local
- Data layering — cascading context notes with local override

### Operations

Seven operations act on the fabric:

| Operation | Category | Description |
|---|---|---|
| list | read | Keys in a context |
| read | read | Content of a record |
| create | write | New record |
| update | write | Overwrite existing record |
| del | write | Remove a record |
| move | compound | Relocate across contexts |
| copy | compound | Duplicate across contexts |

Compound operations compose from primitives. The operation set is minimal and complete.

## The Boundary

The repository — a git repository — is a hard boundary. It constitutes the subject reality as a distinct entity with its own identity, history, and integrity. There is no hidden data — data is part of the subject reality if it exists in the mycelium data fabric within the git repo. Data that is referenced in from outside is localised in terms of access keys. There is no notion of accessing remote data. From the subject's perspective, everything is local. Mycelium does data WYSIWYG — what you see is what you get, nothing behind it.

## Subject Realities

There is no data world sitting somewhere as a single system. The data world is a logical totality — the sum of everything across the fabric. What actually exists is always mycelium fabric expressed as subject realities within git repos.

Each subject reality is a scoped, working implementation. The whole emerges from partial couplings between realities — shared reality is produced by interaction, not discovered behind it.

## Record Types

Base-layer mycelium has only two types of records:

- **Immutable** — settled, permanent, referenceable. A complete fact that arrives whole and stays whole.
- **Dirty** — in-flight, part of an open transaction, can change. Becomes immutable when the transaction closes.

Mutable structures — tables, indexes, document libraries — are created by mycelium-native process that reads immutable data change records and maintains projections. This is process layer embedded in mycelium, not an external concern. Projections exist for practical work but are never the source of truth. They can be discarded and rebuilt from the immutable records.

Mycelium defines a small set of native record schemas — fabric schemas — for its own operations: data change records, reference records, transaction records. These are mycelium's own language, needed for fabric-level functionality. Application schemas are a concern of the embedded process layer — the fabric stays opaque at the content level except for its own native types.

Higher-level mycelium contexts define further structure (tables, indexes, data access interfaces) built on top of the base layer. These are not base-layer concerns.

## Transaction Lifecycle

Open state before consensus, settled state after. Dirty records serve as working space during a transaction and become immutable at its close. The consensus mechanism is pluggable — a simple local commit or a full blockchain protocol.

## Security Model

Mycelium runs by design in a trusted environment. The hard security boundary sits around the trusted environment and is responsible for security. Standard subject realities within the trusted environment do not have their own hard security boundary.

Deployment in a public environment — outside the trusted boundary, not peer-to-peer — uses subject realities with hard security boundaries. These are reinforced bubbles: the underlying data remains in the trusted fabric, the bubble is a disposable projection. Blockchain is an optional consensus mechanism at the hard boundary, not a structural dependency.

---

## Mycelium Context

A fabric node with embedded metadata is a mycelium context — the reference point for the embedded metadata artefacts (processes, schema definitions, etc). Contexts cascade: inner context overrides outer. Definitions reside closest to their realisation.

**Data-triggered processing.** Data state drives progression. Presence/absence determines what happens next. Stateless steps, data as checkpoint.

### Notes — implementation detail

**Structure is behavior.** No flags, no configuration. A context with a bin has soft delete. A flat context skips interior traversal. What you build is how it behaves. What you don't build doesn't exist as a possibility. Architecture of absence — desirable properties emerge from what is not present rather than from what is policed.

**Traversal** — walk the path from root to target. At each segment, check for context definitions (metadata). Merge into accumulator. Nearest distance wins.

**Flat contexts** — a context marked flat treats its interior as content, not sub-contexts. Traversal hops over physical structure to the resource directly.

**Metadata-driven behavior** — mutability, changelog mode, and enforcement are driven by metadata accumulated during traversal.

### Notes — point of view

The working directory sets the point of view (POV). POV determines what you can see and how you identify it. Resources are relative to POV — paths go forward, never backward above POV. Functionality (protocol operations) is root-relative — all registered operations available regardless of where you stand.

### Notes — references

References bring remote resources into view by creating a local identity. Read-only — modification uses copy-on-write to the local context. Read wide, write local. The graph of references defines the reachable set from any POV. No reference, no access — structure determines visibility, not permissions.

## Interaction Modes

**Default mode:** data state propagation. Subjects react to state changes in the fabric. Decoupled, reactive, no direct communication needed.

**Conversational mode:** direct protocols between subjects. A CDM-level process concern, not a fabric concern.

The mycelium is a propagation medium operating in a trusted environment. Boundary gating — trust decisions about what crosses between contexts — is handled by higher-level process.

## Addressing

Addressing is solved by ownership. The subject reality that creates data owns it, identified by the repo's unique endpoint. Cross-references from other realities trace back to the originating identifier. Fully decentralised, no central registry.

Within a subject, XPath-style addressing navigates contexts, accesses records, and reaches metadata through one uniform scheme.
