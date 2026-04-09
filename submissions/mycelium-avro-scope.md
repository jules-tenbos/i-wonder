---
title: "Mycelium AVRO — Design Scope"
type: substantial
status: in-progress
destinations: engineering
---

# Mycelium AVRO — Design Scope

Substantial submission. Scoping document for the AVRO integration design — what it must address and the simplification opportunities identified. AVRO is constitutive to mycelium alongside git. This document captures the design surface while the architectural decisions from Mycelium Fabric and Mycelium Process are fresh.

---

## Why This Matters

AVRO is load-bearing across every layer of mycelium. The core API, schema contracts, protocol registration, service routing, record interpretation, and boundary interfaces all depend on it. Without a formal AVRO design, implementers will make divergent assumptions. The AVRO design is where the architecture meets specification.

More importantly, the AVRO design is where simplification happens. Approaching it with intelligence against the established architecture will reveal mechanisms that appear distinct but are actually one thing expressed through schemas in fabric metadata. The goal is not to add AVRO to mycelium but to discover how much of mycelium is already AVRO.

## Governing Principles

### Relational, Not Representational

AVRO's conventional usage relies on a schema registry — a central authority that assigns identity to data. A record *is* type X because the registry says so. This is representational. It fixes identity and creates a mediating authority.

Mycelium's AVRO design takes the opposite stance. The relational nature of the architecture should emanate from the design, not be implemented by it. The design does not manage relation — it creates the conditions where relation naturally occurs.

AVRO's schema compatibility feature — writer schema versus reader schema resolution — already supports this natively. A reader schema does not ask "is this record type X." It asks "can this record be read as X." The same record may conform to multiple reader schemas simultaneously. Each reader brings its own lens. No schema is the true identity of the record. Conformance is discovered at the point of contact, not assigned by an authority.

This means: no registry in the conventional sense. Schemas live in fabric metadata as facts — present or absent. A process declares what it needs through its reader schema. The data either conforms or it doesn't. No mechanism mediates. Structure is behavior.

Every design decision in this document should be tested against: does this implement relation, or does it let relation emerge? If a mechanism is needed to make things relational, the design is wrong.

### Simplification by Discovery

Mycelium Process introduced the concept of "glasses" — injected interpretation that allows XPath to resolve into record internals. On closer examination, injection is not needed as a distinct mechanism.

Schemas are present in fabric metadata. Context metadata cascades during traversal. When XPath resolves a path, the traversal already accumulates metadata — including any schemas in scope. The resolution logic discovers applicable schemas naturally, the same way it discovers mutability rules and other behavioural metadata.

Record interpretation is not a separate concern. It is a consequence of schemas being present in the metadata along the path. No schema present, no internal visibility — architecture of absence. No injection verb, no glasses mechanism. Just: schemas are facts in the fabric, and traversal finds them.

The AVRO design should apply this simplification throughout. Every proposed mechanism should be tested against: is this already expressed by schemas living in context metadata?

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
- Namespace conventions — how AVRO namespaces map to protocol library identity. Mycelium core, Splectrum, HAICC, application protocols each in their own namespace.
- Operation schemas — how each protocol operation is defined as an AVRO RPC method with input and output types.
- Schema discovery — how a subject or process encounters what protocol operations are available through traversal.
- Evolution — how protocol libraries evolve their schemas using AVRO's native compatibility rules.

### 6. Process Invocation

How a complete input footprint becomes an AVRO message that triggers a transformation.

- The mapping from a data state (set of immutable records in a context) to an AVRO input message.
- How RPC binding is configured on the input message schema — the schema determines routing.
- The contract between the fabric's process layer and the service executing the transformation.
- Input and output schema contracts for transformations — formal definition.
- How the process report is schematised — its AVRO definition as part of the output.
- Local versus remote execution — same schema, different binding. How the configuration works.

### 7. AVRO Containers

When and how AVRO containers are used as record content.

- A container carrying a branch — how put handles this. Does the fabric expand it or store it as a single record?
- A container as self-describing content — the writer schema travels with the data.
- The relationship between the container's embedded writer schema and reader schemas discovered in context metadata. AVRO's native resolution applies.
- Implications for get — does get return raw container bytes or structured content when a reader schema is in scope?

### 8. Namespacing

How AVRO's native namespace mechanism serves mycelium's architectural needs.

- The namespace hierarchy — mycelium core, protocol libraries, application schemas.
- How namespaces map to the protocol library structure in metadata.
- Cross-namespace references — how a process in one namespace consumes records defined in another.
- Namespace governance — who owns what, how conflicts are prevented.

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

## Design Approach

The AVRO design should proceed by working from the inside out — start with schemas in fabric metadata (area 1), because every other area depends on how this is resolved. Then the core API (area 2), because the substrate must be solid. Then record structure and schema contracts (areas 3-4), because these are what process depends on. Then protocol registration and process invocation (areas 5-6), because these are the dynamic layers. Finally containers, namespacing, boundary interfaces, and compound operations (areas 7-10).

At each step, apply both governing principles. The relational test: does this implement relation, or does it let relation emerge? The simplification test: is this a new mechanism, or is it already expressed by schemas in context metadata?
