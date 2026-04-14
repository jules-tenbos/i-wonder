---
title: Three Languages
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# Three Languages
Labels: mycelium, engineering, Splectrum

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@photographer">Name</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Mycelium is not a language
- Mycelium is where three languages meet — AVRO, git, Kafka
- Each addresses one orthogonal concern: structure, historicity, mobility
- None overlaps. None is mycelium.

### 2. Commitments, not discoveries
- The capability requirements are necessary — self-describing shape, history with forgetting, streaming with context
- The choice of which language fulfils each is Splectrum's commitment
- P4 — equal standing in potential. Another framework could commit differently.
- Each language has its own grammar that mycelium conforms to rather than invents

### 3. The Kafka record — five structural requirements
- Identity (key), context carriage (headers), arrival order (offset), historicity (timestamp), self-description (headers about headers)
- These are what data leaving the tree needs to travel self-sufficiently
- Kafka fulfils all five — that's what makes it the right commitment

### 4. Data at rest, data in motion
- Data in the tree speaks tree language — position, hierarchy, context through ancestry
- Data in a Kafka record speaks Kafka — context carried explicitly in headers
- The mutable protocol sits at the boundary: where motion becomes rest

### 5. Memory and forgetting in transit
- Extraction doesn't impose fidelity requirements on context carriage
- Headers can carry full provenance, partial, or none
- Architecture of absence — carry what you choose

### 6. Protocol operations are data in motion
- A get, put, or delete is a Kafka record
- The logical type names the operation (intent). Headers carry arguments. Value starts empty, fills with result.
- The mutable protocol's apply is a Kafka record arriving from a queue
- The streaming language doesn't distinguish "data transfer" from "operation" — both are records with context
- noop is the zero case: explicitly untransformed

### 7. The logical type spectrum
- Interpretation (retrospective) — the logical type tells you which language to read it in
- Transformation (encoding) — the logical type names the mapping between raw and meaningful
- Intent (prospective) — the logical type names what should happen
- All three are natural Kafka records. The envelope doesn't care whether content is contemplative or imperative.

### 8. Fractal indifference
- A subject reality can be the value payload of a Kafka record
- That subject reality contains Kafka records in its own queues
- Records contain realities contain records. No privileged level.
- Replication, migration, cloning — all natural Kafka expressions

---

## Relationship to Two Moves post

Two Moves is the **grammar** — how the identifier tree works, dot and underscore, the message shape, dispatch. Inward-facing: how the system is built.

Three Languages is the **commitment** — why these three languages, what they each bring, what it means that data changes mode. Outward-facing: how the system relates to its world.

Two Moves shows that a protocol operation is a nested Kafka record with headers.record.logicalType as dispatch. Three Languages explains *why* it's a Kafka record — because a protocol operation is data in motion.

### What stays in Two Moves
- The identifier grammar (dot/underscore)
- Property bags, namespace resolution, defined vs applied
- The message onion shape — headers/value nesting
- Physical schema assigns, logical type activates
- Self-description as incremental

### What stays in Three Languages
- The three committed languages framework
- Kafka record as necessary form for mobility
- Protocol operations as data in motion
- The logical type spectrum (interpretation/transformation/intent)
- Fractal indifference
- Memory and forgetting in transit

---

## Reference page

Created: docs/engineering/mycelium/kafka-design-scope.md

Updated:
- docs/engineering/mycelium/index.md — three-language framing, kafka entry
- docs/engineering/mycelium/message.md — Kafka link

---

## Vocabulary updates

- **Committed language** — a language that mycelium conforms to rather than invents. AVRO for structure, git for historicity, Kafka for mobility. A commitment, not a discovery of necessity.

---

## Open threads (not for this post)

- Logical types as Kafka records — activation contexts as data in motion. Thread from Two Moves session.
- Header self-description format
- Logical type namespace structure
- Data change record format as Kafka record with mutation conventions

---

## Tasks on scheduling

- [ ] Update docs/vocabulary.md with new terms
- [ ] Final review of kafka-design-scope.md
- [ ] Image selection
- [ ] Create clean post file in published/
- [ ] Schedule on Blogger
- [ ] Delete draft
- [ ] Delete submission
- [ ] Commit and push
