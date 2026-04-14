---
title: Two Moves
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# Two Moves
Labels: mycelium, engineering, Splectrum

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@photographer">Name</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Two primitives
- The entire identifier grammar reduces to two structural primitives — dot and underscore
- That's the whole language for navigating and describing

### 2. Dot — tree navigation
- Dot walks the tree — positional namespace
- Each parent defines the child
- The path *is* the qualification

### 3. Underscore — property bag
- Underscore opens a property bag — lateral, not deeper
- The bag is *at* the node, not *below* it
- Schema-assigned namespace, not tree-positional

### 4. Physical schema assigns namespace
- The property bag's physical data schema assigns namespace to short names — that's the namespace switch
- Property names inside can form their own identifier tree with their own property bags
- Recursive — same grammar at every level
- The distinction between data and metadata is not structural — it is a schema distinction

### 5. Defined vs applied
- Defined operators (get, put, delete) — part of the protocol's identity, dot-navigated
- Applied operators (_is, _noop) — visitors from outside, underscore-navigated, schema-namespaced
- One test distinguishes them: does this operator exist because this node declares it, or because a schema brought it?

### 6. Tree in motion
- The tree sits still or it moves
- At rest it's storage — file, database, in-memory
- In motion it's a Kafka record — same structure, now with directionality
- Headers are the question. Value is the answer.

### 7. One code path
- Every message is an operator invocation
- Pure data transfer is noop — a real operator with args: null and a specific contract
- The RPC server has exactly one code path

### 8. Physical assigns, logical activates
- The message proves it three levels deep
- Outer schema gives headers its namespace. Headers schema gives record its namespace. Record schema gives logicalType its namespace.
- At the bottom: logicalType — a physically named property whose value is a logical type that activates an operation
- The AVRO type system is the grammar

### 9. Self-description is incremental
- The system works with short names — dirty with respect to self-knowledge
- Schemas add self-knowledge progressively
- Architecture of absence applied to self-awareness
- Full description needed for shared knowledge (P3), but insight is real without schemas (P2)

---

## Reference pages

Already created:
- docs/engineering/mycelium/identifier-grammar.md
- docs/engineering/mycelium/message.md

Updated:
- docs/engineering/mycelium/fabric.md — primitive and underscore sections
- docs/engineering/mycelium/xpath.md — protocol namespace hierarchy
- docs/engineering/mycelium/protocol.md — defined/applied, message reference

---

## Vocabulary updates

- **Identifier point** — a position in the identifier tree, addressed by its path. The key is the address. Everything a node has is properties in bags.
- **Property bag** — a context at an identifier point. Its physical data schema assigns namespace to the properties within it. Property names inside can form their own identifier tree — recursive.
- **Defined operator** — an operator that is part of a protocol's identity, dot-navigated in the tree. Without it, the protocol is a different protocol.
- **Applied operator** — an operator brought from outside via a schema, underscore-navigated in property bags. A visitor, not a constituent.

---

## Open threads (not for this post)

- Logical types may be Kafka records — activation contexts as data in motion. Not yet clear.
- Base interface operators (_is, _noop, others) need definition as a schema set.
- Data change record format still undefined.
- Queue protocol needs its own identity.

---

## Tasks on scheduling

- [ ] Update docs/vocabulary.md with new terms
- [ ] Final review of identifier-grammar.md and message.md
- [ ] Update sitemap (already done)
- [ ] Image selection
- [ ] Create clean post file in published/
- [ ] Schedule on Blogger
- [ ] Delete draft
- [ ] Delete submission
- [ ] Commit and push
