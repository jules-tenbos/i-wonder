---
title: "Mycelium — Structure Is Behavior"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium — Structure Is Behavior

Substantial submission. How mycelium works: behavioural principles, context layer, POV, references, interaction modes, addressing. Connects to the decentralised process models draft.

---

## Behavioral Principles

**Structure is behavior.** No flags, no configuration. A context with a bin has soft delete. A flat context skips interior traversal. What you build is how it behaves. What you don't build doesn't exist as a possibility. This is an architecture of absence — desirable properties emerge from what is not present rather than from what is policed.

**Nearest distance.** Definitions reside closest to their realization. Inner overrides outer.

**Data-triggered processing.** Data state drives progression. Presence/absence determines what happens next. Stateless steps, data as checkpoint.

## Context Layer

The context layer sits between the logical interface and the data:

**Traversal** — walk the path from root to target. At each segment, check for context definitions (metadata). Merge into accumulator. Nearest distance wins — inner context overrides outer.

**Flat contexts** — a context marked flat treats its interior as content, not sub-contexts. Traversal hops over physical structure to the resource directly.

**Metadata-driven behavior** — mutability, changelog mode, and enforcement are driven by metadata accumulated during traversal. No flags, no configuration. Structure is behavior.

## Point of View

The working directory sets the point of view (POV). POV determines what you can see and how you identify it.

**Resources** are relative to POV. You can only see what is in front of you. Paths go forward, never backward above POV.

**Functionality** — protocol operations — is root-relative. Regardless of where you stand, all registered operations are available.

The subject never touches the data world directly. It only knows the interface — how it interacts with the data world through its protocols from its POV.

## References

When a resource is behind POV but access is required, cascading references bring it into view. A reference creates a local identity for a remote resource.

References are read-only. Modification uses copy-on-write to the local context. Read wide, write local.

The graph of references defines the reachable set from any POV. No reference, no access — structure determines visibility, not permissions.

## Interaction Modes

**Default mode:** data state propagation. Subjects react to state changes in the fabric. Decoupled, reactive, no direct communication needed.

**Conversational mode:** direct protocols between subjects. A CDM-level process concern, not a fabric concern.

The mycelium is a propagation medium operating in a trusted environment. Boundary gating — trust decisions about what crosses between contexts — is handled by higher-level process.

## Addressing

Addressing is solved by ownership. The subject reality that creates data owns it, identified by the repo's unique endpoint. Cross-references from other realities trace back to the originating identifier. Fully decentralised, no central registry.

Within a subject, XPath-style addressing navigates contexts, accesses records, and reaches metadata through one uniform scheme.
