[Home](/) > [Engineering](../) > [Mycelium](./) > Kafka Design Scope

# Mycelium Kafka — Design Scope

Kafka is constitutive to mycelium alongside AVRO and git. AVRO provides the language of structure. Git provides the language of historicity. Kafka provides the language of mobility. Mycelium is where the three meet — the fabric, the tree structure, the context model, the protocols. The relational space in which three equal-standing languages interoperate.

These are commitments, not discoveries of necessity. The necessity is at the level of what capabilities are needed — self-describing shape, history with forgetting, streaming with context. The choice of which language fulfils each is Splectrum's commitment. The fit between requirement and commitment is what makes it a good commitment, not what makes it a law. P4 — equal standing in potential.

Each language has its own grammar that mycelium conforms to rather than invents. Mycelium does not replace any of them. It does not wrap them in an abstraction that hides their nature. It speaks all three.

---

## The Kafka Record as Data in Context

A Kafka record is a data bucket in context. Its components:

- **Value** — the data payload. Opaque to the envelope. Could be four bytes or an entire subject reality.
- **Key** — unique identity. What makes this datum addressable outside the tree.
- **Headers** — contextual metadata. Dimensional space for carrying whatever history and interpretive context the extraction requires. The headers need a self-describing structure — headers about headers — so the envelope can describe itself.
- **Offset** — order of arrival. Always meaningful, because every arrival has an order. Whether order matters for the content is a different concern from the fact that arrival order is a fact.
- **Timestamp** — historicity. The moment of extraction is itself a datum.

These are the structural requirements for data leaving the tree and travelling self-sufficiently. Identity, context carriage, arrival order, historicity, self-description. That the Kafka record fulfils all five is why it is the right commitment for streaming data in Splectrum.

---

## Data at Rest, Data in Motion

Data in the tree is data at rest. It speaks tree language — position, hierarchy, context through ancestry. It does not carry a motion envelope.

Data extracted into a Kafka record is data in motion. It speaks Kafka's language. The tree provided context through ancestry. Once extracted, context must travel explicitly in headers.

The mutable protocol sits at the boundary between the two modes. Kafka records arrive — data in motion, enveloped, carrying context. The mutable protocol unpacks them, applies the change, maintains the living surface in the tree. The point where motion becomes rest.

The extraction into Kafka record form does not impose fidelity requirements on context carriage. Memory and forgetting — you carry what you choose. Headers can carry full provenance, partial provenance, or none. If origin coordinates are carried, the data can travel a long transformation chain and still find its way home. If not carried, it can't. The architecture makes both possible. No imposition.

---

## Logical Types and the Kafka Record

A logical type annotates a physical type with context. A Kafka record wraps a data payload with context. The same structural gesture at different scales.

The Kafka record's logical type declares the nature of the transformation that produced the value. Input arguments in the headers provide the dimensional context of how the value came about. The value carries the output. Every record is a process trace — carrying the story of its own making.

The zero case: `noop`. Data with no transformation story. The logical type exists but says "nothing happened here." Even raw data is explicitly marked as untransformed rather than ambiguously silent about its provenance.

### The Logical Type Spectrum

Logical types provide context across a range:

**Interpretation** — `splectrum.natural.heidegger` — pure reading context. The payload is what it is. The logical type tells you which language to read it in. Retrospective.

**Transformation** — `date`, `decimal` — encoding context. The payload is a physical type. The logical type names the mapping between raw form and meaningful form.

**Intent** — action types — the payload is something to be acted upon. The logical type names what should happen. Headers carry the arguments. Prospective.

All three are natural Kafka records. The envelope is indifferent to whether its content is contemplative or imperative. The distinction between event and command is a concern within particular language games, not a structural constraint on the record.

### Every Logical Type as Kafka Record

The isomorphism holds: every logical type declares a context that maps naturally onto the envelope structure of data in motion. The Kafka record is the necessary and sufficient form for data entering the streaming language.

`decimal` — value is bytes, headers carry precision and scale, logical type names the encoding transformation.

`date` — value is an int, logical type names the "days since epoch" interpretation.

Splectrum meaning languages — value is text, logical type names the language that produced it, headers carry concept vocabulary.

Action types — value carries the operation payload, logical type names the intent, headers carry arguments.

A bare physical type without any logical type — data that hasn't entered any language game — wouldn't be in the fabric, because being in the fabric already means being in context.

---

## Three Extraction Languages

Data can be extracted from the tree into any of the three committed languages. Streaming is not the only extraction mode.

**AVRO** — extraction as shaped response. A get query returns an AVRO container. Data described by its schema. No offset, no partition — not entering a stream.

**Git** — extraction as historical snapshot. A commit captures data as it was at a moment. Extraction into the language of versioning.

**Kafka** — extraction as streaming datum. Data in motion with its context. The full envelope.

Each extraction language provides its own necessary envelope. The logical type does different work in each — appropriate to that language. Same mechanism, three languages, three different jobs.

---

## Fractal Indifference

A subject reality as a whole can be the value payload of a Kafka record. Key identifies it. Headers carry whatever context matters — origin, purpose, state. Offset marks its arrival. And the subject reality contains Kafka records in its own queues.

The Kafka record is indifferent to this. It doesn't know if its value is four bytes or an entire world. The grammar doesn't scale differently at different magnitudes. The envelope is the envelope.

This gives subject reality replication, migration, and cloning a natural expression. A subject reality travelling between nodes is a Kafka record. No special protocol needed. The streaming language already handles it.

Records contain realities that contain records. Same pattern, no privileged level.

---

## Atomicity

A Kafka record is atomic. An extracted piece of data. It does not natively maintain relationships to other records — no structural cross-referencing. Linking between records is a metadata responsibility, not a structural one.

This is correct, not a limitation. You don't ask an extraction to maintain relationships. You extracted it *from* relationships. The relational structure lives in the tree. The extraction lives in the stream. If it needs to relate to other extractions, that's metadata someone chose to include in the headers. Architecture of absence — no linking, no relationship. Linking present, the relationship was deliberately carried.

---

## Topic and Partition

Kafka's topic and partition structure is Kafka's own organisational scheme — how Kafka manages its physical storage. This is Kafka's tree, not mycelium's. They are separate concerns. They might align, they might not. Mycelium's fabric tree structure is not mapped onto Kafka's topic/partition model.

---

## Open Areas

### Header Self-Description

The headers need a self-describing structure. A record that carries context but can't tell you how to read that context is incomplete. The format and conventions for header self-description need design.

### Logical Type Namespace Structure

The namespace hierarchy for logical types — `splectrum.natural.heidegger` as a path — needs formal definition. How namespaces are registered, how they compose, how they relate to concept vocabularies.

### Data Change Record Format

The mutable protocol applies data change records from Kafka queues but the data change record format is not yet defined. This intersects with the Kafka record structure — the data change record is a Kafka record with specific conventions for expressing mutations.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
