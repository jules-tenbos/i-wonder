# Speaking the language of — vocabulary as method

Working notes for a future post and associated ref-lib work. Triggered by a cold-review finding that load-bearing technical vocabulary on ref-lib pages isn't systematically defined or linked to `/vocabulary/`. What started as a score issue is really a methodological pointer: SPLectrum's own theory applied to the site.

## The cold-review finding

A newly-built quality rubric's ref-lib profile scored four mature pages on explicit vocabulary:

- `seed/original`: "Language", "relational", "subjects", "convergence" — load-bearing, undefined on page.
- `positioning/close-affinity/seed/the-turn-in-western-philosophy`: "relational turn", "outside view", "structural account".
- `positioning/close-affinity/seed/being-as-tension`: "tension", "differentiation", "complement", "logos", "différance", "śūnyatā".
- `engineering/splectrum/mycelium/index`: "fabric", "committed language", "three-fabric architecture", "subject reality", "defined vs applied".

Every page scored 2-3 out of 5 on the criterion. That isn't a bug in the rubric — it's a real and systemic site gap.

## Two kinds of load-bearing terms

The terms flagged split by venue of definition:

- **SPLectrum-internal** — fabric, subject reality, three-fabric architecture, namespace tree, barified, relational turn (as SPLectrum reads it), outside view. Belong in `/vocabulary/splectrum/`.
- **External / philosophical** — différance, śūnyatā, logos, hermeneutic. Belong to other traditions; belong linked to authoritative external sources (SEP, Britannica) where load-bearing on the page.

Both violate the same discipline — don't let load-bearing terms drift in undefined — but the venue of the definition differs.

## The reflexive insight

SPLectrum's own theory: each language game has its own vocabulary; speaking a game well means holding the vocabulary explicitly. The site is itself a set of language games — ref lib speaks the narrator's language, topnav speaks Jules's, blog speaks each persona's. Vocabulary discipline on the site is SPLectrum applied to itself.

The method, sharpened: *assign the language first, then write the page within it.* A ref-lib engineering page is spoken in the engineering vocabulary; a positioning page is spoken in the positioning register (with external terms linked out); a personal topnav page is spoken in the author's voice. The page is written in its language, and the vocabulary is the constraint that keeps it speaking that language coherently.

## The main challenge: vocabulary evolution across context shifts

Vocabularies don't sit flat. They evolve as context shifts — and most visibly as the reader drills from high-level design into specific detail.

Engineering example:

- **Top design level** — three pillars, fabric, metadata on data. High-level structural vocabulary.
- **HAICC pillar** — persona, plasticity, conscious/unconscious protocols, decentralised cognition. A more specific vocabulary.
- **Specific persona** — the vocabulary of that persona's context. splectrum-engineering-persona has its own terms distinct from splectrum-thinking-persona.

Moving between these levels means switching vocabularies. Terms from the top level may appear in detail pages but often in a narrower or differently-scoped sense; terms from the detail don't bubble up unchanged. What is the right structure for this?

Candidates:

- **Inheritance** — detail inherits parent vocabulary, can override.
- **Translation** — detail has its own, with declared bridges to the parent.
- **Layered** — each level has its own, relations between layers are separately specified.

Category theory likely has formal language for this (functors, natural transformations, refinements). That's a research thread, not a near-term decision — and it connects to the already-active submission on category theory applied to SPLectrum's language games.

## Work to be done

Ref-lib work, roughly prioritised:

1. **Audit** — walk the ref-lib pages, list load-bearing terms per page, classify as internal / external / already-in-vocabulary.
2. **Link-out pass** — for terms already in `/vocabulary/splectrum/`, link them on first substantive use in each ref-lib page.
3. **Grow vocabulary entries** — prioritise SPLectrum-internal terms used across the ref lib that aren't yet in vocabulary.
4. **External-reference pass** — on positioning and philosophy pages, ensure external technical terms have authoritative links.
5. **Articulate the context-shift principle** — eventually `/vocabulary/` needs a meta-page explaining how vocabularies evolve across zoom levels within the site.

## Post potential

A conversational post about vocabulary-as-method — the reflexive SPLectrum move. Title candidates: *"Speaking the language of"* or *"Every page has a language"*. Key beats:

- The cold-review finding (concrete).
- The two-venue distinction (internal vs external).
- The reflexive insight — SPLectrum applied to itself.
- The deeper challenge of vocabulary evolution across context shifts.
- The open category-theory angle (without over-claiming).

Persona: probably SPLectrum — the move is to speak from within the project about the project's own method.
