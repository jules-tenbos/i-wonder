---
title: AVRO — The Language of Articulation
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# AVRO — The Language of Articulation
Labels: mycelium, engineering, Splectrum

<img src="https://images.unsplash.com/photo-1705484229341-4f7f7519b718?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="AVRO — The Language of Articulation" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More on AVRO in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/avro-design-scope">AVRO design scope in the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@markuswinkler">Markus Winkler</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Opening — two constitutive dependencies
- Mycelium has two external technologies that are architecturally load-bearing. Everything else is fabric primitives
- Git provides the boundary — identity, history, integrity. The subject reality exists because the repo exists
- AVRO provides articulation — schema, conformance, protocol, interface. Without it, the subject reality exists but cannot speak
- This post is about the second dependency. What AVRO does in mycelium, and what was discovered when the architecture met the specification

### 2. Not serialization — articulation
- AVRO's reputation in the industry is serialization. Kafka made it the standard for schema-driven data exchange
- Mycelium does not adopt AVRO for serialization convenience. It adopts it because process-as-fully-qualified-schema-mapping is native to AVRO
- Three roles through a single technology: record internal structure (what is inside a record), schema conformance (the relationship between record and process), protocol definitions and RPC (the operational interface)
- These are not three separate uses bolted together. Three aspects of one thing: AVRO as the language through which the subject reality articulates itself

### 3. Carrier and meaning
- A discovery from investigation, not a design decision
- The data schema — fields, types, structural shape — is the carrier language. Carries content without committing to what it means
- The schema name — the fully qualified namespace — is the meaning language. Declares which language game is being played
- Same bytes, same carrier, readable through different named schemas, each placing the reading in a different meaning context. The data doesn't change. The meaning language does
- This maps directly onto multiple conformance (P4)
- AVRO's nominal gate — name check before structural resolution — is doing language hygiene, not blocking conformance
- Nothing was added. Something was discovered. The namespace was always there. The carrier/meaning distinction was always there. They are the same thing read through the Splectrum lens

### 4. RPC as boundary, not transport
- The industry moved to gRPC for RPC. Streaming, HTTP/2. Mycelium's need is different — surgical schema-routed invocation, not streaming
- The reason for adopting AVRO RPC is not transport. It is process separation
- Two processes through RPC can only see each other through the schema contract. No shared objects, no classpath leakage, no hidden state. Even in the same process on the same machine
- Architecture of absence applied to process coupling. You don't prevent hidden dependencies by policing them. You prevent them by making the RPC boundary the only channel
- This is what makes the HAICC work division invisible to process management. Human or AI behind the boundary — same schema contract, same process report
- Transport pluggability is a consequence, not the motivation

### 5. Three levels of opacity
- The same structural pattern at three levels
- Fabric: key mapped to opaque bytes. Does not interpret content
- Process management: input schema mapped to output schema. Does not interpret the transformation
- Execution: what runs behind the RPC boundary is invisible. Human, AI, local, remote — same contract
- Three levels of enforced ignorance. Each level stays minimal and universal precisely because it does not know what is on the other side

### 6. Namespace as living architecture
- Not a fixed taxonomy. Dynamically composed
- Segments exist independently as facts in the fabric. Composed at the point of use
- The act of composing is the act of creating a specific language application — P0 at the namespace level
- The tree is simultaneously: catalogue of available languages, catalogue of operations within each language, routing structure for invocation
- Paths that nobody composes don't exist. Architecture of absence at the namespace level

### 7. Bare ready
- avsc — pure JavaScript, full Avro specification. Single library, ~51kB. No framework dependencies
- Define a protocol, create a server, register a handler, create a client, call the message. In-memory, no infrastructure
- Library on need — architecture of absence applied to the dependency graph. What you don't import doesn't exist as a dependency
- The architecture meets implementation with zero gap. Prototyping against the real mechanism from day one

### 8. Close
- Two external dependencies: git for boundary, AVRO for articulation. Together with the fabric primitives, that is the full substrate
- The discoveries — carrier/meaning, RPC as boundary, three-level opacity, dynamic namespace — were not designed. They were found when the architecture met the specification
- Simplification by discovery. The goal was not to add AVRO to mycelium but to discover how much of mycelium was already AVRO

---

## Reference page — docs/engineering/mycelium/avro-design-scope.md

Already created from the merged submission. Review and update on scheduling if needed.

---

## Vocabulary updates

Review and update `docs/vocabulary.md` entries for:
- **AVRO** — not currently defined. Constitutive dependency: schema, conformance, protocol, interface
- **Carrier/meaning separation** — not currently defined
- **avsc** — not currently defined. Implementation platform

---

## Tasks on scheduling

- [ ] Review/update docs/engineering/mycelium/avro-design-scope.md
- [ ] Update docs/vocabulary.md
- [ ] Image selection
- [ ] Schedule on Blogger
- [ ] Delete draft
- [ ] Delete submissions (avro-process-management-post-notes.md, mycelium-avro-scope.md, mycelium-avro-scope-update.md)
