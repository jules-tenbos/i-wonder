---
title: The Meaning of Get
series: mycelium
category: engineering
persona: SPLectrum
status: storyline
---

# The Meaning of Get
Labels: mycelium, engineering, SPLectrum

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/blog/label/mycelium). More in the <a href="/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@photographer">Name</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. The operator is just a word
- Get, put, delete — generic names, no inherent meaning
- The word is the carrier. It carries nothing until placed in context.
- An operator without a protocol is a verb without a language

### 2. The protocol is the language game
- The protocol is the meaning context that gives the operator its specific meaning
- "Get, in the context of datauri" — one game. "Get, in the context of metadata" — a different game entirely.
- Same carrier, different meaning. The carrier/meaning split expressed at the operational level.

### 3. The protocol name as tree structure
- The protocol name is a path through the namespace tree — each segment narrows the language game
- `spl.splectrum.natural.philosophical.heidegger` — framework, domain, natural language, philosophical sub-domain, specific thinker
- The tree structure IS the categorisation. What makes sense as a protocol path? The segments that tell you which game you're in.
- Not a flat registry of protocol names. A tree where each level adds specificity.

### 4. Operators as actors — defined and chosen
- Defined operators are the moves the protocol declares — constitutive, dot-navigated
- Without them, it is a different protocol. They ARE the protocol expressed as actions.
- The protocol chooses its own words. `heidegger.concepts` — returns the specific concepts of that philosophical language. `xpath.data.uri.get` — retrieves opaque data nodes.
- Different protocols, different operators, different vocabulary. The operator name is meaningful within the protocol's own language game.

### 5. Base meanings, flavoured by context
- Get retrieves. Put places. Delete removes. These are base meanings — the minimum the word carries.
- The protocol flavours them. "Get" in datauri returns opaque bytes. "Get" in schema-aware data returns AVRO-interpreted content. Same base meaning, different operational reality.
- The base meaning is universal. The flavour is local. The protocol determines the flavour.

### 6. The base interface — applied operators
- Applied operators are inherited — available on every protocol and every operator node
- `_help` — returns info about the node. What is this protocol? What operators does it define?
- `_is` — returns type characterisation. What kind of thing is this?
- These are visitors from outside, underscore-navigated, schema-namespaced. Not part of what makes the node what it is.
- Any logical type — protocol or operator — responds to the base interface. Self-description is built into the architecture.

### 7. Resolution as discovery
- Protocols live in fabric metadata, resolved on the ancestor axis — nearest wins
- What you can do depends on where you stand
- No protocol in scope, no capability — architecture of absence at the operational level
- The same operator resolves to different protocols at different positions in the tree

### 8. The fabric shapes execution
- Execution mode (sync, queue, dry-run) is metadata in the context, not a caller argument
- Debug wrapping is metadata — add it, every invocation below wraps in debug. Remove it, normal resumes.
- The node decides how its operators execute. Structure is behaviour applied to the protocol/operator binary.

### 9. Close — protocol as reader schema for operations
- The protocol is to the operator what the reader schema is to the data
- Same data, different reader schema, different reading. Same operator, different protocol, different meaning.
- The architecture doesn't distinguish these two patterns — both are readings through a meaning context

## Connects to
- Two Moves — defined vs applied from the grammar perspective
- Three Languages — committed languages as meaning contexts at the technology level
- AVRO post — carrier/meaning separation, "readable as" mechanism
- Data in Motion — the message carries the protocol/operator pair as a Kafka record
- XPath post — six protocols, each giving get/put/delete different operational meaning
- One Identifier — the namespace tree that protocol names navigate

---

## Tasks on scheduling

- [ ] Image selection
- [ ] Write narrative
- [ ] Schedule on Blogger
- [ ] Delete draft
