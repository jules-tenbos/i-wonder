---
title: AVRO — The Language of Articulation
series: mycelium
category: engineering
persona: Splectrum
status: draft
---

# AVRO — The Language of Articulation
Labels: mycelium, engineering, Splectrum

<img src="https://images.unsplash.com/photo-1705484229341-4f7f7519b718?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="AVRO — The Language of Articulation" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

I went into the [AVRO](https://avro.apache.org/) investigation expecting to confirm a technology choice. Mycelium needs two external dependencies — git for the boundary, AVRO for articulation — and I wanted to verify that AVRO could carry the weight. What I found was more interesting than suitability. The investigation kept revealing things that were already there, in AVRO's own design, waiting to be read differently.

Most people know AVRO through [Kafka](https://kafka.apache.org/) — serialization, schema registry, data exchange. Solid technology, widely adopted. But that isn't why mycelium needs it. Mycelium needs AVRO because it natively does something harder: it maps process to fully qualified schema. A reader schema meets the data and either fits or doesn't — discovered at the point of contact, not assigned by an authority. That's the relationship between record and process expressed as a single mechanism. Schema for what's inside a record, conformance for who can read it, protocol definitions for what operations are available. Three aspects of one thing.

The first discovery came from looking at how AVRO handles names.

A data schema — the fields, the types, the structural shape — carries content without committing to what it means. Any process that can read the shape can read the data. But the schema *name* — the fully qualified namespace path — does something else. It says which language game is being played. Two schemas could be structurally identical, same fields, same types. But `mycelium.imaging.ImageSpec` says: this is how imaging talks about it. `splectrum.relation.ImageSpec` says: this is how the relational language talks about it. Same carrier, different meaning.

I sat with that for a while. Same bytes, readable through different named schemas, each placing the reading in a different meaning context. The data doesn't change. The language does. And AVRO's nominal gate — where resolution starts with a name check before it even looks at structure — turns out to be doing exactly the right thing. It's not blocking access. It's enforcing commitment. You don't drift into the wrong reading just because the fields happen to match. You name your way in.

I didn't put this there. The namespace was always present in AVRO. The separation between what carries content and what gives it meaning was always present in the architecture. They turned out to be the same thing. Nothing added, something found.

The second discovery was about [RPC](https://avro.apache.org/docs/++version++/specification/#protocol-declaration). The industry has moved to [gRPC](https://grpc.io/) — streaming, HTTP/2. But mycelium doesn't stream. It propagates data state. The RPC need is surgical: schema-routed invocation at specific moments. And the reason for choosing AVRO RPC isn't transport — it's what happens at the boundary.

Two processes communicating through RPC can only see each other through the schema contract. No shared objects, no leaking internals, no hidden state. Even running in the same process on the same machine, the boundary holds. You don't prevent entanglement by policing it. You prevent it by making the schema boundary the only channel — there's nowhere for entanglement to form.

That has a consequence I hadn't anticipated. The process management layer sees namespace, schema, invocation, result. That's all it sees. It doesn't know what happened inside. It doesn't know *who* did it. Human behind the boundary, AI behind the boundary — same contract, same report. The boundary makes the distinction invisible. Not by hiding it, but by genuinely not caring.

Then a third thing surfaced — a pattern repeating at three levels. The fabric maps a key to opaque bytes and doesn't interpret content. The process layer maps input schema to output schema and doesn't interpret the transformation. The execution behind the RPC boundary is invisible to everything above it. Three levels, each one ignorant of what's on the other side. Each level stays minimal and universal precisely *because* it doesn't know. That ignorance isn't a limitation. It's what makes each level free to be itself.

The namespace turned out to be alive in a way I hadn't expected. It isn't a fixed hierarchy — it's composed. `splectrum.relation.compare` is assembled from segments that exist independently as facts in the fabric. Carrier, meaning domain, operation — put together at the point of use. The composition is the creation. Before someone composes that specific path, the operation in that specific language context doesn't exist. And paths nobody composes? They don't exist either. The space is open. A novel composition might work — you don't know until you try, and the trying is a conformance check, not a redesign.

The implementation runs on [avsc](https://github.com/mtth/avsc) — pure JavaScript, full Avro specification, single library. Protocol, server, handler, client, message. In-memory, no infrastructure. What you don't need, you don't import. The gap between architecture and working code is zero.

Two dependencies. Git for boundary, AVRO for articulation. Together with the fabric primitives, that's the full substrate. And the things I found along the way — the carrier/meaning separation, the boundary as enforced ignorance, the three-level pattern, the living namespace — none of them were designed in. They were there, in AVRO's own structure, visible once you looked with the right questions.

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
- AVRO as serialization is rock solid across the industry. Kafka made it the standard for schema-driven data exchange. Wide language support
- AVRO RPC is a different story. The industry moved to gRPC — HTTP/2, streaming. But mycelium's primary interaction mode is data state propagation, not streaming. The RPC need is surgical: schema-routed invocation at specific moments
- What the industry doesn't need — transport pluggability for local-first deployment — is exactly what mycelium does need
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
