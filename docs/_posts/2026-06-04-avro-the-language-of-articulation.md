---
layout: post
title: "AVRO — The Language of Articulation"
date: 2026-06-04
labels: [mycelium, engineering, SPLectrum]
blogger_id: 2428550605989625379
---
<img src="https://images.unsplash.com/photo-1705484229341-4f7f7519b718?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="AVRO — The Language of Articulation" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

I went into the [AVRO](https://avro.apache.org/) investigation expecting to confirm a technology choice. Mycelium operates at the intersection of three committed languages — AVRO for articulation, git for the boundary, Kafka for mobility — and I wanted to verify that AVRO could carry the weight. What I found was more interesting than suitability. The investigation kept revealing things that were already there, in AVRO's own design, waiting to be read differently.

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

Three committed languages. AVRO for articulation, git for boundary, Kafka for mobility. Together with the fabric primitives, that's the full substrate. And the things I found along the way — the carrier/meaning separation, the boundary as enforced ignorance, the three-level pattern, the living namespace — none of them were designed in. They were there, in AVRO's own structure, visible once you looked with the right questions.

<small>This post is part of the [mycelium series](/search/label/mycelium). More on AVRO in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/avro-design-scope">AVRO design scope in the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@markuswinkler">Markus Winkler</a> / Unsplash</small>
