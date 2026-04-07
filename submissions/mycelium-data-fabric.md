---
title: "Mycelium — The Data Fabric"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium — The Data Fabric

Substantial submission. Introductory engineering post on mycelium. What it is, the primitive, immutability at the base, subject realities as reality bubbles.

---

## What Mycelium Is

Mycelium is the fabric from which realities are created. It creates repo constructions that model subject reality. It weaves data and process together.

The dynamic of a subject consists of an algorithmically driven process triggering based on data state.

## The Fabric

The mycelium is a data fabric into which data and process are woven through a Common Data Model (CDM). The CDM structures data using a file/folder tree with cascading context notes. Each node carries metadata covering structure requirements, process requirements, and search. Context notes cascade downward with local override, scoping what can happen at each level.

### The Primitive

The fabric is built from one primitive:

**Record** = key → content (opaque bytes).
**Context** = bounded area that contains records.
Records can themselves be contexts.

Keys are meaningful only within their containing context. Content is opaque — the model does not interpret it. Everything else is layered above.

Proven sufficient across 18 projects. No extensions required.

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

The repository — a git repository — is the boundary. It constitutes the subject reality as a distinct entity with its own identity, history, and integrity. Within the boundary, data is structured but not ontological — the folder tree and context notes define functional scope.

## Subject Realities

There is no data world sitting somewhere as a single system. The data world is a logical totality — the sum of everything across the fabric. What actually exists is always mycelium fabric expressed as reality bubbles.

Each bubble is a scoped, working implementation. The whole emerges from partial couplings between bubbles — shared reality is produced by interaction, not discovered behind it.

## Immutability as Base Layer

Immutability is the default. Two immutable patterns operate at the base:

- **Atomic immutable records** — a complete fact, arrives whole, stays whole.
- **Data change records** — a fact about a change, what moved from what to what.

Both are simply records from the fabric's perspective. The distinction in meaning lives in the CDM context notes.

Mutable structures — tables, indexes, document libraries — are projections computed from the immutable base. They exist for practical work but are never the source of truth. They can be discarded and rebuilt from the immutable records.

This is a stronger commitment than event sourcing or lakehouse formats. Mycelium does not have an immutable component; it is an immutable foundation with mutable projections.

## Transaction Lifecycle

Data in progress is mutable and dirty. When a transaction closes, the same data, in the same structures, becomes immutable — a clean record in the fabric, referenceable by the whole mycelium.

Open state before consensus, settled state after. The same mutable structures serve as working space during a transaction and become permanent record at its close. The consensus mechanism is pluggable — a simple local commit or a full blockchain protocol.

## Public Deployment

Subject realities can be encapsulated in reinforced bubbles and floated into public hostile environments. The bubbles interact peer-to-peer. The underlying data remains in the trusted fabric. The bubble is a disposable projection — if compromised, the trusted fabric is unaffected.

Trust-model-agnostic: trusted by default, hardened at boundaries. Blockchain is an optional consensus mechanism at boundaries, not a structural dependency.
