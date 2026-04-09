---
title: "AVRO as Process Management Core — Post Notes"
type: post-notes
status: draft
destinations: blog
---

# AVRO as Process Management Core — Post Notes

Notes for a post on AVRO — specifically the avsc pure JavaScript library — as the core component of the Splectrum engineering process management layer. These notes capture the findings and discoveries from a structured investigation into AVRO's suitability.

---

## The Core Claim

AVRO is suitable as the process management layer's core component because it provides process-as-fully-qualified-schema-mapping natively. It is not being adopted for serialization convenience. It is constitutive — alongside git, the second external technology that is architecturally load-bearing. Git provides the subject reality boundary. AVRO provides the language of articulation. Together with the fabric primitives, that is the full substrate.

## Eight Points

### 1. AVRO's Three Roles in Mycelium

AVRO serves three distinct roles, all through a single technology:

- **Record internal structure** — the schema that defines what is inside a record. The basis for schema discovery during traversal.
- **Schema conformance** — the relationship between record and process. Not an agreement but a discovered compatibility. A process brings a reader schema; the data conforms or it doesn't.
- **Protocol definitions and RPC** — the operational interface. Process invocation, service routing, boundary interfaces. Every protocol operation defined as AVRO schema, invoked through AVRO RPC.

These are not three separate uses bolted together. They are three aspects of one thing: AVRO as the language through which the subject reality articulates itself. Without AVRO, the subject reality exists (git provides that) but cannot speak.

### 2. Carrier/Meaning Separation

A discovery from the investigation: the data schema and the schema name serve fundamentally different roles.

**The data schema** — the fields, the types, the structural shape — is the carrier language. It carries content without committing to what it means. Any process that can read the shape can read the data. This is what makes the fabric universal at the structural level.

**The schema name** — the fully qualified namespace — places that structure into a meaning context. The namespace says which language game is being played. `mycelium.imaging.ImageSpec` and `splectrum.relation.ImageSpec` could be structurally identical — same fields, same types. But the namespace declares: this is how imaging talks about it, this is how Splectrum's relational language talks about it. The name is the language commitment.

This maps directly onto multiple conformance (P4). The same record, same bytes, same carrier — readable through different named schemas, each placing the reading in a different meaning context. The data doesn't change. The meaning language does.

AVRO's nominal gate — where schema resolution starts with a name check — is doing the right thing here. It's not blocking conformance. It's enforcing language commitment. You don't accidentally read imaging data through a financial schema just because the fields happen to match. You name your way into a meaning context. That is language hygiene, not rigidity.

### 3. RPC as Process Boundary Enforcement

The reason for adopting AVRO RPC is not transport. It is process separation.

Two processes that communicate through AVRO RPC can only see each other through the schema contract. No shared objects, no classpath leakage, no hidden state coupling. Even if they run in the same process on the same machine, the RPC boundary guarantees that the only thing passing between them is a schema-conformant message.

This is architecture of absence applied to process coupling. You don't prevent hidden dependencies by policing them. You prevent them by making the RPC schema boundary the only channel. There is no structure in which hidden dependencies can form.

The process management layer sees all invocations identically. It does not know whether an RPC call is "interpreting a record" or "running a business transformation" or "checking readiness." It sees namespace, schema, invocation, result. Opaque at the management level. Meaningful at the language level. This is what makes the HAICC work division — human or AI behind the boundary — invisible to process management.

Transport pluggability is a consequence of this design, not the motivation. The same schema contract holds whether the transport is in-memory, TCP, HTTP, or direct function call. The transport adapts to the deployment context. The schema boundary is invariant.

### 4. Dynamic Namespace Composition

The namespace hierarchy is not a fixed taxonomy. It is dynamically composed.

`english.philosophy.do-an-analysis` — the namespace path is assembled from segments that each exist independently in the fabric as facts. A carrier segment. A meaning domain segment. An operation segment. They are composed at the point of use, not predefined as a complete path.

This is P0 operating at the namespace level. The boundary — the specific composed path — is the creation. Before composition, the operation in that specific language context doesn't exist as a distinct thing. The act of composing the namespace is the act of creating that specific language application.

The combinatorial space is open. You don't need to enumerate every possible path. You need the segments. The paths that actually get composed are the paths that actual use demands. Paths that nobody composes don't exist — architecture of absence at the namespace level.

Protocol operations are encoded under specific meaning languages through the tree structure. `splectrum.relation.compare` is an operation that lives inside a meaning language. `haicc.persona.readiness.evaluate` — different language, different operation, same mechanical pattern. The tree is simultaneously the catalogue of available languages, the catalogue of operations within each language, and the routing structure for invocation.

### 5. Three Levels of Opacity

The architecture exhibits the same structural pattern at three levels:

**Fabric level** — a record is key mapped to opaque bytes. The fabric moves it, stores it, makes it available. It does not interpret content. Schemas discovered during traversal are what make content visible.

**Process management level** — a process is input schema mapped to output schema. The management layer triggers it, monitors state, records reports. It does not interpret the transformation. The RPC boundary enforces this.

**Execution level** — what actually runs behind the RPC boundary is invisible to everything above it. A human step, an AI transformation, a local function, a remote service. Same input schema, same output schema, same process report. The boundary prevents the management layer from seeing the difference.

Three levels of enforced ignorance. Each level stays minimal and universal precisely because it does not know what is on the other side of its boundary.

### 6. avsc as Implementation Choice

avsc is a pure JavaScript implementation of the full Avro specification. Not a partial port — it covers serialization, schema evolution, protocol definition, RPC, IDL support, and container file handling.

Key properties for the architecture:

- **Transport-agnostic RPC** — in-memory, TCP, HTTP. Handler code is not coupled to transport. The same service definition works across all transports.
- **Handler dispatch** — `server.onMessage(name, handler)`. Simple map registration. O(1) lookup. Scales to any number of registered handlers.
- **Middleware chain** — wrapped request/response with `next()`. Process reports, tracing, and auditing can live here.
- **One-way messages** — fire-and-forget. Maps to data state propagation.
- **Browser-capable** — ships browser distributions. Full at ~51kB, protocols at ~34kB, types-only at ~20kB.
- **Schema handshake** — stateful connections exchange schemas once, subsequent calls skip the handshake. Efficient for persistent connections within a subject reality.

### 7. Bare Ready

avsc gives the primitive right now. Define a protocol. Create a server. Register a handler. Create a client. Call the message. In-memory transport, no infrastructure, no build pipeline, no dependencies beyond the library itself.

The namespace composition model, the footprint watcher pattern, the trigger model — all of these can be prototyped against avsc's actual RPC layer immediately. The architecture meets implementation with zero gap.

No framework to configure, no server infrastructure to deploy, no schema registry to stand up. The library is the capability. `npm install avsc`. You are building.

### 8. Minimal Code Surface — Library on Need

avsc is one library. It provides serialization, schema evolution, protocol definition, RPC with transport pluggability, and middleware in a single dependency. No framework. No ecosystem of modules imported for potential use.

The "on need" principle is architecture of absence applied to the dependency graph. You don't import streaming because you might need streaming. You don't import HTTP/2 because some future deployment might cross a network boundary. When you need TCP, you require `net` — a Node.js built-in. When you need HTTP, you require `http` — another built-in. avsc plugs into whatever transport is present. The transport is a dependency of the deployment context, not the library.

Contrast with the gRPC path: protobuf compiler, generated code, HTTP/2 dependency, specific server infrastructure, language-specific runtime libraries, build toolchain integration. All potential — capability waiting for a use case.

What you don't import doesn't exist as a dependency. The code surface is exactly what the current use case demands. Growth happens by adding what is needed when it is needed — spawn not design.

## Enterprise Landscape Context

AVRO as serialization is rock solid across the industry. The Kafka ecosystem has made it the standard for schema-driven data exchange. Wide language support across JVM, Python, C/C++/C#, PHP, Ruby, Rust, JavaScript.

AVRO RPC is a different story. The industry has largely moved to gRPC for the RPC layer — driven by HTTP/2 streaming requirements. But mycelium's primary interaction mode is data state propagation, not streaming. The RPC need is surgical: schema-routed invocation at specific moments.

AVRO RPC's native design — transport-independent framing, pluggable transport, schema handshake — fits the mycelium use pattern more precisely than gRPC. What the industry doesn't need (transport pluggability for local-first deployment) is exactly what Splectrum engineering does need.

The library (avsc) is solid enough to embrace as a constitutive dependency. If extension or maintenance becomes necessary, the pure JavaScript implementation is accessible and modifiable.

## Remaining Investigation Points

These are confidence builders, not blockers:

- **Dynamic handler registration at runtime** — can `server.onMessage()` be called after the server is already listening? The API surface suggests yes.
- **Schema conformance checking without RPC invocation** — using avsc's Type system to test "can this buffer be read as X" cheaply, for footprint watcher readiness tests.
- **Multiple services on one transport** — a single connection serving multiple protocol definitions, for subjects exposing many namespace branches.
- **Middleware flexibility** — whether the chain intercepts before or after schema validation.

---

*These notes capture the state of investigation. The post should crystallise the argument without losing the discoveries.*
