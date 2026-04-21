[Home](/) > [Engineering](/engineering/) > [SPLectrum](/engineering/splectrum/) > [Mycelium](/engineering/splectrum/mycelium/) > AVRO Design Scope

# Mycelium AVRO — Design Scope

AVRO is constitutive to mycelium alongside git. Git provides the subject reality boundary. AVRO provides the language of articulation. Together with the fabric primitives, that is the full substrate.

AVRO is load-bearing across every layer of mycelium. The core API, schema contracts, protocol registration, service routing, record interpretation, and boundary interfaces all depend on it. The AVRO design is where the architecture meets specification — and where simplification happens. Approaching it with intelligence against the established architecture reveals mechanisms that appear distinct but are actually one thing expressed through schemas in fabric metadata. The goal is not to add AVRO to mycelium but to discover how much of mycelium is already AVRO.

---

## Governing Principles

### Relational, Not Representational

AVRO's conventional usage relies on a schema registry — a central authority that assigns identity to data. A record *is* type X because the registry says so. This is representational. It fixes identity and creates a mediating authority.

Mycelium's AVRO design takes the opposite stance. The relational nature of the architecture should emanate from the design, not be implemented by it. The design does not manage relation — it creates the conditions where relation naturally occurs.

AVRO's schema compatibility feature — writer schema versus reader schema resolution — already supports this natively. A reader schema does not ask "is this record type X." It asks "can this record be read as X." The same record may conform to multiple reader schemas simultaneously. Each reader brings its own lens. No schema is the true identity of the record. Conformance is discovered at the point of contact, not assigned by an authority.

This means: no registry in the conventional sense. Schemas live in fabric metadata as facts — present or absent. A process declares what it needs through its reader schema. The data either conforms or it doesn't. No mechanism mediates. Structure is behavior.

Every design decision should be tested against: does this implement relation, or does it let relation emerge? If a mechanism is needed to make things relational, the design is wrong.

### Simplification by Discovery

Mycelium Process introduced the concept of "glasses" — injected interpretation that allows XPath to resolve into record internals. On closer examination, injection is not needed as a distinct mechanism.

Schemas are present in fabric metadata. Context metadata cascades during traversal. When XPath resolves a path, the traversal already accumulates metadata — including any schemas in scope. The resolution logic discovers applicable schemas naturally, the same way it discovers mutability rules and other behavioural metadata.

Record interpretation is not a separate concern. It is a consequence of schemas being present in the metadata along the path. No schema present, no internal visibility — architecture of absence. No injection verb, no glasses mechanism. Just: schemas are facts in the fabric, and traversal finds them.

The AVRO design should apply this simplification throughout. Every proposed mechanism should be tested against: is this already expressed by schemas living in context metadata?

### Carrier/Meaning Separation

The data schema and the schema name serve fundamentally different roles.

**The data schema is the carrier language. The schema name resolves the meaning language.**

The data schema — fields, types, structural shape — carries content without committing to what it means. Any process that can read the shape can read the data. The schema's fully qualified name — the namespace path — places that structure into a meaning context. The namespace declares which language game is being played.

This is architecturally active:

- Multiple conformance is not a theoretical property but multiple readings through different meaning languages — same carrier, different namespace, different result.
- AVRO's nominal gate (name check before structural resolution) enforces language commitment — language hygiene, not rigidity.
- The carrier/meaning separation means AVRO's namespace mechanism already performs what a separate language identification system would have to be built to do. SPLectrum's language hygiene lives natively inside AVRO's own structure.

**Design test:** every mechanism should be evaluated against this separation. If a mechanism conflates carrier and meaning, it is misplaced.

The carrier/meaning discovery is itself an instance of simplification by discovery. The namespace was always present in AVRO. The carrier/meaning distinction was always present in the architecture. They are the same thing read through the SPLectrum lens. Nothing was added. Something was discovered.

## Type System and Resolution

### Physical and Logical Types

Physical types carry data structure — the data schema says what's there. Logical types declare functional capability — what can be done with it. The physical carries. The logical activates. AVRO carries both dimensions simultaneously on the same type definition. A single schema identifier IS both concept (physical structure) and protocol operation (logical capability). Not two separate things — one definition with two dimensions, both always present.

"Put it there" — put is an operation (logical type). "What is put?" — put is data (physical type). Same AVRO identifier, both dimensions coexist. Self-description is built in: every operation is both invokable and queryable.

### Type Resolution on Axes

Physical types resolve within data scope — forward-looking from process POV into self and descendants. Logical types resolve on the ancestor axis — from process POV up to subject reality root. The carrier/meaning split expressed as axis selection.

A logical type is discovered on the ancestor axis. What it produces is a physical schema that lands in the data scope.

### Protocol and Concept

Protocol is the meaning context for operations. Concept is the meaning context for data schemas. Both under mycelium — `spl.mycelium.protocol` and `spl.mycelium.concept`. Same carrier/meaning pattern, same "readable as" mechanism. Protocol flavours generic operations (get, put, remove). Concept flavours generic data structures (table, record, list). A table in natural language, a table in prehistoric times, in Victorian times — different schema flavours, all readable as a natural language table.

### Versioning as Resolution

Versioning is metadata, not name. Traditional rigid compatibility modes are replaced. Compatibility becomes: does a functional implementation exist that can read this data? Not a policy — a discovery.

Resolution modes:
- **Latest** — highest version, input must conform to latest schema.
- **Adaptive** — highest version whose reader schema can read the provided input. The data determines which implementation handles it.

Header metadata annotates the handler identified — full traceability.

Degradation as two-stage resolution:
1. **Same logical type** — is there a version that can read this input?
2. **Alternative logical type** — if not, which alternative logical type handles this? Exception processing of any kind.

Compatibility extended to states of deficiency. Exception handling becomes orthogonal — just more logical types available for resolution. No try-catch chains. Scalable and easy to set up.

Explicit version request tests only that version. Failure goes to exception mode — no fallback chain. Max version as context metadata constrains the adaptive range without hiding what's available.

## Design Areas

### 1. Schemas in Fabric Metadata

How AVRO schemas live in context metadata. This is the foundational question — everything else follows from it.

- How schemas are placed in context metadata — as facts, not as registrations. Present or absent.
- How schema presence cascades — inner context overrides outer, consistent with all other metadata behaviour.
- How traversal accumulates schema information during path resolution — discovery, not lookup.
- How the absence of a schema naturally limits visibility — opaque bytes when no schema is in scope, structured access when a schema is present.
- Schema discovery — how a process or subject encounters what schemas are available at a given path, without querying a registry.
- Multiple schemas in scope — how different schemas present at the same path enable different views of the same data.

### 2. The Core API as AVRO RPC

The three substrate operations — get, put, remove — expressed as AVRO RPC schemas.

- The RPC schema for each operation — input message, output message.
- How the XPath expression is represented in the AVRO message.
- How opaque content is carried in get responses and put requests.
- How the uniform return shape — [{key, value}, ...] — is expressed as an AVRO schema.
- How flat addressing and query expressions are handled uniformly in the same schema.

### 3. Record Internal Structure

How AVRO schemas enable XPath to extend past the record boundary.

- How a schema discovered during traversal is used as a reader schema against record content.
- How XPath resolution transitions from fabric navigation to record-internal navigation using the discovered schema — the reader asks "does this conform", not "is this type X."
- How AVRO containers — which embed their writer schema with the data — relate to schemas present in metadata. Writer schema travels with the record. Reader schema is discovered in context. AVRO's native resolution handles the mapping.
- Content handling — how the fabric treats AVRO-encoded content at the substrate level (opaque bytes) versus at the schema-aware level (structured access).
- Multiple conformance — how the same record may be readable through different reader schemas discovered in different contexts, producing different structured views of the same data.

### 4. Schema Contracts

The conformance relationship between record and process — the core mechanism that enables process decoupling and prevents dependency hell.

- How a process declares its reader schema — what it needs from its input records. The reader schema is the process's lens, not the record's identity.
- How a process declares its writer schema — what it produces. The writer schema travels with the output data.
- How the footprint watcher uses reader schema conformance to verify completeness — "can these records be read as my input type" rather than "are these records of my input type."
- Schema evolution — how reader and writer schemas evolve independently. A broader reader schema can consume records that a narrower one could not, without data migration.
- AVRO compatibility rules as the native mechanism — forward compatibility, backward compatibility, full compatibility. No custom versioning machinery needed.

### 5. Protocol Library Registration

How protocol libraries place their operation schemas in fabric metadata.

- The convention — what a protocol library places into metadata to make its capabilities available. Facts in the fabric, not entries in a registry.
- Namespace conventions — how AVRO namespaces map to protocol library identity. Mycelium core, SPLectrum, HAICC, application protocols each in their own namespace.
- Operation schemas — how each protocol operation is defined as an AVRO RPC method with input and output types.
- Schema discovery — how a subject or process encounters what protocol operations are available through traversal.
- Evolution — how protocol libraries evolve their schemas using AVRO's native compatibility rules.

Protocol operations are located inside the languages they belong to. There is no flat registry of operations. Each protocol library owns its namespace branch. Operations within that branch are reachable through the namespace path. Querying "what operations does SPLectrum's relational language offer" is a traversal of the namespace tree.

Language composition without collision: two languages can define an operation with the same local name — `compare`, `validate`, `transform` — and they never conflict because the namespace path disambiguates. The local name is the operation. The path is the language context. Together they are a unique address.

### 6. Process Invocation

How a complete input footprint becomes an AVRO message that triggers a transformation.

- The mapping from a data state (set of immutable records in a context) to an AVRO input message.
- How RPC binding is configured on the input message schema — the schema determines routing.
- The contract between the fabric's process layer and the service executing the transformation.
- Input and output schema contracts for transformations — formal definition.
- How the process report is schematised — its AVRO definition as part of the output.
- Local versus remote execution — same schema, different binding. How the configuration works.

**Interpretation as invocation.** Reading data through a meaning language is not a passive check — it is an active process with the same shape as every other process: input data state, schema contract, output data state. Reading data as a financial record is an RPC call through the financial namespace. Reading the same data as a SPLectrum relational structure is an RPC call through the SPLectrum namespace. Schema discovery, process invocation, and data interpretation collapse into one pattern: namespace identifies the language, data schema specifies the carrier contract, RPC enforces the boundary and performs the transformation.

**Three levels of opacity.** The architecture exhibits the same structural pattern at three levels:

- Fabric: key mapped to opaque bytes. The fabric does not interpret content.
- Process management: input schema mapped to output schema. The management layer does not interpret the transformation.
- Execution: what runs behind the RPC boundary is invisible. Human, AI, local, remote — same schema contract, same process report.

Three levels of enforced ignorance. Each level stays minimal and universal precisely because it does not know what is on the other side of its boundary.

### 7. AVRO Containers

When and how AVRO containers are used as record content.

- A container carrying a branch — how put handles this. Does the fabric expand it or store it as a single record?
- A container as self-describing content — the writer schema travels with the data.
- The relationship between the container's embedded writer schema and reader schemas discovered in context metadata. AVRO's native resolution applies.
- Implications for get — does get return raw container bytes or structured content when a reader schema is in scope?

### 8. Namespacing

How AVRO's native namespace mechanism serves mycelium's architectural needs. The carrier/meaning separation elevates this area — the namespace is not just organisational but architecturally constitutive.

- The namespace hierarchy — mycelium core, protocol libraries, application schemas.
- How namespaces map to the protocol library structure in metadata.
- Cross-namespace references — how a process in one namespace consumes records defined in another.
- Namespace governance — who owns what, how conflicts are prevented.

**Namespace as organisational architecture.** The tree structure of namespace names encodes protocol operations under specific meaning languages. `splectrum.relation.compare` is an operation that lives inside a meaning language. `haicc.persona.readiness.evaluate` — different language, different operation, same mechanical pattern. The namespace tree is simultaneously:

- The catalogue of available languages.
- The catalogue of operations within each language.
- The routing structure for invocation.

**Dynamic composition.** Namespace paths are not predefined entries in a hierarchy. They are assembled from segments that exist independently as facts in the fabric. Carrier segment, meaning domain segment, operation segment — composed at the point of use. The act of composing the namespace is the act of creating a specific language application (P0 — the boundary is the creation).

The combinatorial space is open. Paths that nobody composes don't exist — architecture of absence at the namespace level. A novel namespace composition might work. You don't know until you try. The trying is a schema conformance check, not a system redesign.

### 9. Boundary Interfaces

How AVRO RPC defines the external surface of a subject reality.

- The relationship between internal protocol operations and the external boundary interface.
- How a subject reality declares what it exposes — which operations, which schemas.
- The security model intersection — how AVRO at the boundary relates to the trust perimeter.
- Subject-to-subject interaction — how two subject realities communicate through their respective AVRO RPC boundaries.

### 10. Compound Operations

How move and copy — compositions in mycelium's own process protocol library — are expressed.

- Their AVRO RPC schemas as process library operations.
- How they compose from the three substrate operations.
- Transaction wrapping — how atomicity is expressed in the schema.

### 11. RPC as Constitutive Dependency

AVRO RPC is not a transport mechanism but the process boundary enforcement mechanism.

**RPC for separation, not communication.** Two processes communicating through RPC can only see each other through the schema contract. No shared objects, no classpath leakage, no hidden state. Even in local in-memory execution, the RPC boundary guarantees that only schema-conformant messages pass.

**Process management opacity.** Because RPC enforces the boundary, the process management layer can be agnostic to execution internals. It sees: was the input complete, was the transformation invoked, did the output land. What happened inside is not its concern. This is what makes the HAICC work division — human or AI behind the boundary — invisible to process management.

**Transport as deployment concern.** Transport pluggability is a consequence, not the motivation. The same schema contract holds whether the transport is in-memory, TCP, or HTTP. The transport adapts to context. The boundary is invariant.

**No dependency hell.** The architecture's claim that there are no transitive dependencies between processes is mechanically enforced by RPC. Without RPC, process separation is a convention. With RPC, it is a physical fact.

### 12. Implementation Platform

**Enterprise landscape.** AVRO as serialization is rock solid across the industry. The Kafka ecosystem has made it the standard for schema-driven data exchange, with wide language support across JVM, Python, C/C++/C#, PHP, Ruby, Rust, JavaScript. AVRO RPC is a different story — the industry has largely moved to gRPC, driven by HTTP/2 streaming requirements. But mycelium's primary interaction mode is data state propagation, not streaming. The RPC need is surgical: schema-routed invocation at specific moments. AVRO RPC's native design — transport-independent framing, pluggable transport, schema handshake — fits the mycelium use pattern more precisely than gRPC. What the industry doesn't need (transport pluggability for local-first deployment) is exactly what mycelium does need.

avsc — the pure JavaScript AVRO implementation — is the implementation platform.

**Why avsc.** Full Avro specification coverage in pure JavaScript. Serialization, schema evolution, protocol definition, RPC with transport pluggability (in-memory, TCP, HTTP), middleware chain, IDL support, browser-capable distributions. Single library, ~51kB full distribution. No framework dependencies.

**Why JavaScript.** Minimal code surface. Library on need rather than potential. Transport dependencies are Node.js built-ins (`net`, `http`). No build toolchain for the core layer. Dynamic language aligns with AVRO's design philosophy — code generation not required.

**Transport pluggability.** Handler code is transport-agnostic. The same service definition works across in-memory (for local testing and subject-internal operations), TCP (for inter-process communication), and HTTP (for boundary interfaces). Stateful transports avoid repeated handshakes. Stateless transports work for one-shot invocations.

**Bare ready.** The library provides the complete primitive immediately. Protocol definition, server creation, handler registration, client creation, message invocation — all available without infrastructure. Prototyping against the real mechanism from day one.

**Extensibility posture.** avsc is solid enough to embrace as a constitutive dependency. If extension or maintenance becomes necessary, the pure JavaScript implementation is accessible and modifiable.

## Design Approach

The AVRO design should proceed from the inside out — start with schemas in fabric metadata (area 1), because every other area depends on how this is resolved. Then the core API (area 2), because the substrate must be solid. Then record structure and schema contracts (areas 3–4), because these are what process depends on. Then protocol registration and process invocation (areas 5–6), because these are the dynamic layers. Then containers, namespacing, boundary interfaces, and compound operations (areas 7–10). RPC as constitutive dependency (area 11) and implementation platform (area 12) inform the entire sequence.

At each step, apply all three governing principles. The relational test: does this implement relation, or does it let relation emerge? The simplification test: is this a new mechanism, or is it already expressed by schemas in context metadata? The carrier/meaning test: does this conflate carrier and meaning, or does it keep them separate?

