---
title: "Mycelium AVRO — Scope Update"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium AVRO — Scope Update

Update to the AVRO Design Scope document. Captures architectural discoveries from the AVRO suitability investigation that refine, extend, or reframe areas in the existing scope. These updates do not contradict the original scope — they deepen it.

---

## Updates to Governing Principles

### New Principle: Carrier/Meaning Separation

The investigation surfaced a structural distinction that should be elevated to a governing principle alongside "Relational, Not Representational" and "Simplification by Discovery."

**The data schema is the carrier language. The schema name resolves the meaning language.**

The data schema — fields, types, structural shape — carries content without committing to what it means. Any process that can read the shape can read the data. The schema's fully qualified name — the namespace path — places that structure into a meaning context. The namespace declares which language game is being played.

This is not an analogy. It is architecturally active:

- Multiple conformance is not a theoretical property but multiple readings through different meaning languages — same carrier, different namespace, different result.
- AVRO's nominal gate (name check before structural resolution) enforces language commitment, which is language hygiene — not rigidity.
- The carrier/meaning separation means AVRO's namespace mechanism already performs what a separate language identification system would have to be built to do. Splectrum's language hygiene lives natively inside AVRO's own structure.

**Design test:** every mechanism should be evaluated against this separation. If a mechanism conflates carrier and meaning, it is misplaced.

### Extension to "Simplification by Discovery"

The carrier/meaning discovery is itself an instance of simplification by discovery. The namespace was always present in AVRO. The carrier/meaning distinction was always present in the architecture. They are the same thing read through the Splectrum lens. Nothing was added. Something was discovered.

This reinforces the existing principle and provides a concrete example for implementers.

## Updates to Design Areas

### Area 8: Namespacing — Elevated Priority

The original scope lists namespacing as area 8 of 10, with the note "how AVRO's native namespace mechanism serves mycelium's architectural needs." The investigation shows this area is more foundational than its position suggests.

**Namespace as organisational architecture.** The tree structure of namespace names encodes protocol operations under specific meaning languages. `splectrum.relation.compare` is an operation that lives inside a meaning language. `haicc.persona.readiness.evaluate` — different language, different operation, same mechanical pattern. The namespace tree is simultaneously:

- The catalogue of available languages.
- The catalogue of operations within each language.
- The routing structure for invocation.

**Dynamic composition.** Namespace paths are not predefined entries in a hierarchy. They are assembled from segments that exist independently as facts in the fabric. Carrier segment, meaning domain segment, operation segment — composed at the point of use. The act of composing the namespace is the act of creating a specific language application (P0 — the boundary is the creation).

The combinatorial space is open. Paths that nobody composes don't exist — architecture of absence at the namespace level. A novel namespace composition might work. You don't know until you try. The trying is a schema conformance check, not a system redesign. This is where ambiguity is generative (P4).

**Recommendation:** namespacing should be treated as area 2 or 3 in the design sequence, not area 8. The carrier/meaning separation and dynamic composition model inform every subsequent design area.

### Area 5: Protocol Library Registration — Extended

The original scope describes protocol libraries placing their operation schemas in fabric metadata as facts. The investigation extends this with the namespace tree model.

**Protocol operations are located inside the languages they belong to.** There is no flat registry of operations. Each protocol library owns its namespace branch. Operations within that branch are reachable through the namespace path. Querying "what operations does Splectrum's relational language offer" is a traversal of the namespace tree.

**Language composition without collision.** Two languages can define an operation with the same local name — `compare`, `validate`, `transform` — and they never conflict because the namespace path disambiguates. The local name is the operation. The path is the language context. Together they are a unique address. This is P4 expressed as namespace architecture.

### Area 6: Process Invocation — Extended

The original scope describes how a complete input footprint becomes an AVRO message that triggers a transformation. The investigation adds two discoveries.

**Interpretation as invocation.** Reading data through a meaning language is not a passive check — it is an active process with the same shape as every other process: input data state, schema contract, output data state. Reading data as a financial record is an RPC call through the financial namespace. Reading the same data as a Splectrum relational structure is an RPC call through the Splectrum namespace. Schema discovery, process invocation, and data interpretation collapse into one pattern: namespace identifies the language, data schema specifies the carrier contract, RPC enforces the boundary and performs the transformation.

**Three levels of opacity.** The process management layer is agnostic to transformation internals, the same way the fabric base layer is agnostic to record content. This parallel is structurally exact:

- Fabric: key mapped to opaque bytes. The fabric does not interpret content.
- Process management: input schema mapped to output schema. The management layer does not interpret the transformation.
- Execution: what runs behind the RPC boundary is invisible. Human, AI, local, remote — same schema contract, same process report.

This three-level opacity should be explicitly documented as a design property in the process invocation area.

## New Design Area: RPC as Constitutive Dependency

The existing scope treats AVRO RPC as part of design areas 2 (core API) and 6 (process invocation). The investigation reveals RPC deserves recognition as a concern in its own right — not as a transport mechanism but as the process boundary enforcement mechanism.

**RPC for separation, not communication.** The primary purpose of AVRO RPC in the architecture is to enforce the schema boundary between processes. Two processes communicating through RPC can only see each other through the schema contract. No shared objects, no classpath leakage, no hidden state. Even in local in-memory execution, the RPC boundary guarantees that only schema-conformant messages pass.

**Process management opacity.** Because RPC enforces the boundary, the process management layer can be agnostic to execution internals. It sees: was the input complete, was the transformation invoked, did the output land. What happened inside is not its concern. This is what makes the HAICC work division — human or AI behind the boundary — invisible to process management.

**Transport as deployment concern.** Transport pluggability is a consequence, not the motivation. The same schema contract holds whether the transport is in-memory (local subject reality operations), TCP (cross-boundary within trusted environment), or HTTP (public-facing bubble). The transport adapts to context. The boundary is invariant.

**Relationship to "no dependency hell."** The architecture's claim that there are no transitive dependencies between processes is mechanically enforced by RPC. Without RPC, process separation is a convention. With RPC, it is a physical fact.

## New Design Area: Implementation Platform

The investigation identified avsc — the pure JavaScript AVRO implementation — as the implementation platform.

**Why avsc.** Full Avro specification coverage in pure JavaScript. Serialization, schema evolution, protocol definition, RPC with transport pluggability (in-memory, TCP, HTTP), middleware chain, IDL support, browser-capable distributions. Single library, ~51kB full distribution. No framework dependencies.

**Why JavaScript.** Minimal code surface. Library on need rather than potential. Transport dependencies are Node.js built-ins (`net`, `http`). No build toolchain for the core layer. Dynamic language aligns with AVRO's design philosophy — code generation not required.

**Transport pluggability in avsc.** Handler code is transport-agnostic. The same service definition works across in-memory (for local testing and subject-internal operations), TCP (for inter-process communication), and HTTP (for boundary interfaces). Stateful transports avoid repeated handshakes. Stateless transports work for one-shot invocations.

**Bare ready.** The library provides the complete primitive immediately. Protocol definition, server creation, handler registration, client creation, message invocation — all available without infrastructure. Prototyping against the real mechanism from day one.

**Extensibility posture.** avsc is solid enough to embrace as a constitutive dependency. If extension or maintenance becomes necessary, the pure JavaScript implementation is accessible and modifiable. Own it architecturally regardless of authorship.

## Investigation Items for Detailed Design

These emerged from the investigation as points requiring verification during detailed design:

1. **Dynamic handler registration** — verify that `server.onMessage()` can be called at runtime after the server is listening. Required for dynamic namespace composition.
2. **Schema conformance without invocation** — verify that avsc's Type system supports cheap "can this be read as X" tests without going through RPC. Required for efficient footprint watcher readiness checks.
3. **One-way message maturity** — verify clean implementation in avsc. Required for fire-and-forget data state propagation.
4. **Multiple services on one transport** — verify that a single connection can serve multiple protocol definitions. Required for subjects exposing many namespace branches.
5. **Middleware interception point** — verify whether the middleware chain intercepts before or after schema validation. Determines where process reports and auditing attach.

---

*This update extends the AVRO Design Scope with discoveries from the suitability investigation. It does not replace the original scope — it deepens it. The original design areas and sequence recommendations should be re-evaluated in light of the elevated priority of namespacing and the new design areas identified here.*
