---
title: "Mutability Protocols and Serialization"
type: substantial
status: processed
destinations: engineering
---

# Mutability Protocols and Serialization

Two protocols governing the stability regime of content in the mycelium fabric. The **mutability** protocol is interrogative — it reads the regime. The **mutable** protocol is operational — it maintains living surfaces derived from immutable sources. Plus: the serialization model built into the data access protocols.

---

## The Three Regimes

The fabric primitive — key mapped to content — has no opinion about change. Mutability is not a property of the fabric. It is a paradigm declared through metadata, discovered during traversal, and enforced through protocol operators.

Three regimes exist:

**Immutable** — no change possible. The record arrived whole and stays whole. The record *is* the history. Complete self-knowledge. Replicate freely, cache anywhere, no coordination needed.

**Mutable** — controlled change. Every change arrives as an immutable data change record through a queue. The queue is the history. Full reconstruction possible. The mutable resource knows its own past through the queue.

**Dirty** — uncontrolled change possible. No record of the changes. The current state is all there is. No rebuild guarantee, no audit trail, no safe replication.

### Default: Dirty

When no mutability metadata is present on the ancestor axis, the regime is dirty. Architecture of absence — no declaration, no guarantee. Control is built, not given.

An empty repository is entirely dirty. As mutability metadata is placed in contexts, the reliability landscape takes shape. The subject shapes its own commitments.

### Not a Lifecycle

The three regimes are distinct paradigms, not stages. Each declares something fundamentally different about what the fabric knows about its own content:

- Immutable — the fabric knows everything. The content is the fact.
- Mutable — the fabric knows the history through the queue. The current state is derived.
- Dirty — the fabric knows nothing about change. The current state is all there is.

The transition from dirty to immutable is a one-way creation act — a snapshot, a commitment. What happened in the dirty regime before that moment is gone. There is no memory to carry forward.

---

## The Mutability Protocol

**Namespace:** `mycelium.mutability`

Interrogative. Reads mutability metadata through the metadata API, accumulates on the ancestor axis (nearest-ancestor-wins), and returns interpreted results. The mutability protocol reports the regime and its replication characteristics. It does not determine what operations are permitted — that is the concern of a write mode protocol.

### Operators

#### status

Returns the mutability regime at the resolved path.

- Walks the ancestor axis from process POV to subject reality root.
- Accumulates mutability declarations from context metadata.
- Nearest ancestor wins.
- No metadata found → dirty.

**Input:** resolution envelope.
**Output:** `immutable | mutable | dirty`

#### replication-mode

The replication characteristics of content at the resolved path, derived from the regime and any additional replication metadata in scope.

- Immutable → replicate freely, no synchronisation.
- Mutable → replicate with declared synchronisation mode (immediate, batched, on-demand).
- Dirty → snapshot only, no consistency guarantee.

**Input:** resolution envelope.
**Output:** replication profile — mode, synchronisation requirements, staleness tolerance.

---

## The Mutable Protocol

**Namespace:** `mycelium.mutable`

Operational. Owns the full lifecycle of mutable resources — living surfaces derived from immutable data change records in queues. The mutable protocol is the machinery between the sealed queue and the current-state surface.

A mutable resource never generates truth. It derives truth from its immutable source queue. The queue relationship is constitutive — the queue *is* the rebuild path.

The mutable protocol reads and writes through the existing data access protocols. It has no serialization concern of its own — serialization is handled by the data access level the operation passes through.

### The Mechanism

Immutable data change records land in a queue — sealed, permanent, ordered. The mutable protocol reads them and applies each change to maintain the current-state value at the key. What those bytes are — a single record, a table, an index — is behind the RPC boundary. The mutable protocol sees a key and its value.

The dependency is one-directional. Immutable records never depend on mutable state. Mutable state always depends on immutable records. The mutable resource could vanish and the queue wouldn't notice. The queue vanishes and the mutable resource is orphaned.

### Operators

#### create

Creates a mutable resource bound to an immutable source queue.

Establishes the constitutive relationship: this mutable resource derives from this queue. Sets the synchronisation mode (immediate, batched, on-demand). The resource is created empty — initial state is built through replay or through the first arriving data change records.

**Input:** resolution envelope — target path for the mutable resource, source queue path, synchronisation mode.
**Output:** confirmation envelope — the mutable resource exists, bound to its source.

#### apply

Applies one or more immutable data change records from the source queue to the mutable resource. This is the core operation — the machinery of controlled change.

The handler behind the RPC boundary interprets the data change record against the current state and updates the value. Each application is deterministic given the same starting state and the same change record.

**Input:** resolution envelope — data change records to apply.
**Output:** confirmation envelope — updated state, any application issues.

#### current

Returns the current state of the mutable resource. Routes through the data access protocols — uri level returns opaque bytes (default serialization), schema-aware level returns AVRO-serialized content.

**Input:** resolution envelope — path to the mutable resource.
**Output:** current state of the resource.

#### rebuild

Discards the current state and replays the entire source queue from the beginning. The expendability guarantee made operational — the mutable protocol can always reconstruct from sealed history.

Not an emergency recovery path. A first-class operation. Rebuild may be triggered by schema evolution, corruption detection, or a new projection requirement against the same history.

**Input:** resolution envelope — path to the mutable resource, optional replay parameters (from a specific point, through a specific reader schema).
**Output:** confirmation envelope — rebuilt state, replay report.

#### discard

Destroys the mutable resource. The source queue is unaffected. The projection ceases to exist. Can be recreated at any time through `create` and `rebuild`.

**Input:** resolution envelope — path to the mutable resource.
**Output:** confirmation envelope — resource removed.

#### sync-status

Reports the synchronisation state of the mutable resource relative to its source queue. How far behind is the projection? Are there unapplied data change records?

**Input:** resolution envelope — path to the mutable resource.
**Output:** synchronisation profile — last applied record, queue head, lag, synchronisation mode.

---

## Relationship Between the Two Protocols

The mutability protocol declares the regime. The mutable protocol operates within one specific regime.

When `mycelium.mutability.status` returns `mutable`, it means the mutable protocol is operationally active at that location. When it returns `immutable`, the mutable protocol has no business there. When it returns `dirty`, neither protocol is operationally active — dirty is the absence of both sealing and controlled change.

The mutability protocol reads metadata. The mutable protocol reads immutable queues and writes mutable surfaces. They share no operational dependency — only the conceptual dependency that the mutable protocol presupposes a `mutable` regime declaration.

---

## Serialization in the Data Access Protocols

Serialization is not a separate protocol. It is built into the data access protocols as part of what get does when a key resolves to a subtree.

### The Principle

Requesting the value of a node returns the whole subtree — self plus descendants. When a subtree must travel as a single value, it is serialized into an AVRO container. AVRO is constitutive to mycelium — the container is the natural serialization envelope. The schema depth within the container is determined by the data access level.

### AVRO Containers as Uniform Envelope

AVRO is constitutive to mycelium — it is substrate, not optional infrastructure. The AVRO container is the uniform serialization envelope at both data access levels. Self-describing — the writer schema travels with the data. No separate hardwired format is needed.

The two levels differ not in serialization technology but in schema depth:

**URI level (datauri, metadatauri, rawuri)** — AVRO container with a structural schema. The schema describes tree shape — key, children, value as opaque bytes. Content inside values stays opaque. No schemas from context metadata are involved. Always available.

**Schema-aware level (data, metadata, raw)** — AVRO container with content-aware schemas discovered during traversal. The schema describes both tree shape and what is inside the values. Writer schema embedded in the output.

Same serialization mechanism. Same library. Same container format. Different schema depth. The distinction between opaque and interpreted access is a schema question, not a format question.

### Physical Storage Provides Content Serialization

Each physical means of resource storage — file system, database, in-memory structure — provides its own serialization of content into bytes that go inside the AVRO container as the value payload.

A file system knows how to pack its tree structure into bytes. An in-memory store knows how to serialize its own structures. A database knows how to dump its content. Each produces bytes. The AVRO container carries them.

The contract for a physical storage medium: you must be able to serialize your content into a form that fits inside an AVRO container. The container is uniform. The content serialization is storage-native. This is a required capability of any physical storage that participates in the fabric.

### Implications for XPath

The XPath addressing scheme navigates contexts and returns results. When a path expression resolves to a subtree, the result is always an AVRO container. The data access protocol determines the schema depth:

- Through a uri protocol → AVRO container with structural schema. Values as opaque bytes.
- Through a schema-aware protocol → AVRO container with content-aware schemas. Values interpreted.

The path expression itself does not change. What changes is the schema depth of the container that carries the result set.

### Implications for Put

The symmetry holds for put. Placing a subtree at a key:

- Through a uri protocol → the value is expected as an AVRO container with structural schema. The storage unpacks the tree structure and places it. Content stays opaque.
- Through a schema-aware protocol → the value is expected as an AVRO container with content-aware schema. Writer schema embedded, content validated against discovered reader schemas in scope.

### Implications for Replication

Serialization is upstream of replication. Content travels between subject realities as AVRO containers. The mutability protocol's `replication-mode` operator reports the regime. The schema depth of the container determines what the receiving end can interpret without additional schema discovery.

---

## Open Areas

### Write Mode Protocol

The mutability protocol reports the regime. What operations are permitted at a given location — whether a put is allowed, under what conditions — is a write mode concern. This is a separate protocol, not yet defined.

### Data Change Record Format

The mutable protocol applies data change records but does not define their format. The data change record is itself a schema concern — what operations on a subtree can be expressed (add child, update value, remove descendant) and how they are serialized. This needs its own design.

### Queue Protocol

The immutable queue that feeds the mutable protocol is referenced but not defined as a protocol. The queue may need its own protocol identity — ordering guarantees, delivery semantics, position tracking.

---

*This document defines the mutability and mutable protocols as a matched pair, and establishes AVRO containers as the uniform serialization envelope at both data access levels. The mutability protocol is interrogative — it reads the regime. The mutable protocol is operational — it maintains the living surface. Serialization is what get and put do when operating on subtrees — always through AVRO containers, with schema depth determined by the access level.*
