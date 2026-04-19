# Reference Library Rewrite

Working list of pages in `docs/` that need review or rework. Walked top-down from the topnav and home page; detail added as we go.

## The three axes of the site

- **Topnav (About / HAICC / P2P)** — the **personal** axis. Jules's voice, the person behind the project.
- **Homepage boxes (seed + five areas)** — the **informational** axis. Structured reference library, narrator voice.
- **Posts (blog)** — the **conversational** axis. Thinking in motion, voice by persona.

Each axis is a legitimate path in. They reinforce each other through deliberate cross-links, but each has its own register and purpose.

## The shape of the library

Five main sections under home, each with a defined remit:

- **Language** — all language material, formal or otherwise. Category theory, formal languages, natural language, notation, language about language. The mechanics and properties of relation.
- **Reality** — the consequences of the seed for how we experience and know reality. SPLectrum's own philosophical and scientific work: metaphysics, epistemology, ontology — plus ethics, arts, anywhere the seed lands. First-person territory.
- **Positioning** — other people's work on reality. Where the seed sits among existing philosophical and scientific trajectories. Third-person territory. The counterpart to Reality: Reality is what SPLectrum says; Positioning is who else said something structurally adjacent.
- **Engineering** — how SPLectrum builds. Clear as-is; ongoing rework on AVRO/git/Kafka.
- **Vocabulary** — one vocabulary per language game. Today a single page of SPLectrum terms, but the direction is substantive: each language game gets its concepts documented explicitly. This is part of the language work — making concepts explicit so games can be studied, compared, and kept free of implicit drift. First-class area even while thin.

This framing informs the rework of each area index and the placement of pages that cross boundaries.

## Execution order

1. **Seed split** — trim `seed.md`; land the engineering view in `docs/engineering/seed.md`; add pointers to category-theory and discovery.
2. **Topnav P2P rework** — personal-voice rework with Holepunch + Midnight/Cardano.
3. **Language area rework** — new sub-pages, rewrite index.
4. **Reality area rework** — scope when we get there.
5. **Positioning review pass.**
6. **Engineering rework** — its own track, after everything else.
7. **Topnav deep-linking pass** — final cross-link cleanup from topnav into the reshaped library.

## Topnav pages

The topnav (About / HAICC / P2P) is intentionally different from the homepage boxes. It's the personal take on the project — Jules's voice, outside the structured library. Two legitimate paths in: topnav for people who want the person first, boxes for people who know what they're looking for. The topnav pages can be strengthened by making their links *into* the structured library more deliberate.

### P2P — `docs/p2p.md`

**Status:** needs rework.

**Current state:** SPLectrum-voice, philosophical framing ("not a technology choice. It is the structure of experience"). Covers Holepunch (Bare, Pear) and links into `/engineering/bare/` and `/engineering/mycelium/`. No blockchain content.

**Rework:**

- **Voice** — shift from SPLectrum/abstract to personal voice. This is a topnav page, so it should read as Jules speaking about what matters in the P2P space, not as the seed pronouncing.
- **Content to cover:**
  - P2P as a space — what's actually there, why it matters to the project
  - Holepunch stack — Bare (runtime), Pear (apps), the distributed primitives
  - Blockchain layer — Midnight, Cardano. Where they fit, why these two, how they relate to (or differ from) the Holepunch line
- **Structure question** — one page covering both Holepunch and blockchain, or a short landing page linking out to sub-pages? Sub-pages don't exist yet for Midnight / Cardano.
- **Cross-links** — existing `/engineering/bare/` is reference material; the topnav page should point in, not duplicate.

**Open questions for Jules:**
- Is the Holepunch / blockchain pairing on one page, or should P2P become an index linking to `/p2p/holepunch/` and `/p2p/blockchain/` (or similar)?
- Midnight and Cardano — what's the angle? (privacy/ZK, governance, something else?)
- Is there sub-page content already in drafts or submissions, or do we write from scratch?

## Area pages

### Seed — `docs/seed.md`

**Status:** needs trimming + split.

**Current state:** One long page holding the philosophical framework (P0–P5), an engineering translation (table + three fabrics), mathematical convergence (category theory / Yoneda), and creation and discovery. The last two sections largely duplicate content already in `docs/language/category-theory.md` and `docs/reality/discovery.md`.

**Split:**

1. **Keep on `seed.md`** — intro, P0–P5, "What SPLectrum is". Trim the "this page presents the seed twice" framing since the engineering view is moving out. Keep it focused: the six principles and the meta-language claim.
2. **Move engineering view → engineering** — the philosophy/engineering translation table and the three-fabrics section (Mycelium, SPLectrum, HAICC). Probable home: new `docs/engineering/seed.md` (or fold into `top-level-design.md` — to decide). Link from the trimmed seed page and from `engineering/index.md`.
3. **Mathematical convergence → language** — already covered in `docs/language/category-theory.md` (§ "Convergence with the Seed"). Drop the section from `seed.md`; add a short inline pointer near P5 ("see [Category Theory](language/category-theory) for the mathematical convergence").
4. **Creation and discovery → reality** — already covered in `docs/reality/discovery.md` (§ "Creation conforms to discovery"). Drop from `seed.md`; add a short inline pointer ("see [Discovery](reality/discovery)").

**Open questions for Jules:**
- Engineering view: separate page (`engineering/seed.md`) or merge into `engineering/top-level-design.md`?
- Keep the translation table on the engineering page as-is, or rethink given the AVRO/git/Kafka framing?

### Language area — `docs/language/`

**Status:** needs restructuring. Source: `submissions/language-area-rework.md` (2026-04-19, since folded in and deleted).

**Current state:** `index.md` reads half as a post, half as an index — argues a position rather than describing the area. Only one sub-page (`category-theory.md`). The "Let's Talk Software Languages" blog post links to `/language/` because there's no dedicated page yet.

**Rework:**

1. **Rewrite `index.md`** — narrator / ref lib voice. Describe the area and link to sub-pages; move the argument (ground dimension, personal/shared, the pattern) into body sub-pages or distribute across reality/positioning where it fits. Keep it as an index.
2. **New `natural-languages.md`** — human language, ambiguity, context, language games. Saussure territory.
3. **New `formal-languages.md`** — mathematical, logical, type theory, formal systems.
4. **New `software-languages.md`** — taxonomy (assembly, imperative, functional, declarative, logic, markup, query, scripting, domain-specific), relation to formal language theory, where SPLectrum's engineering sits. Redirect the "Let's Talk Software Languages" post link here once it exists.
5. **Keep `category-theory.md`** — already works.

**Research needed:**
- Taxonomy of software languages and how it maps onto formal language theory (regular / context-free / context-sensitive / recursively enumerable). Is there a structural classification that lines up with SPLectrum's framework?

**Dependencies:**
- Semiotics research (`submissions/semiotics.md`) intersects: Saussure → natural-languages, Peirce generalises beyond, may need accommodation in the area shape.
- Natural/formal/software split affects where vocabulary work lands (each game documented under its own language category).

### Reality area — `docs/reality/`

**Status:** needs rework. Details deferred — to discuss when the work begins.

**Context:** Reality is SPLectrum's first-person axis — consequences of the seed for metaphysics, epistemology, ontology, ethics, arts. Large territory. Worth scoping properly when the time comes rather than pre-committing to a shape.

**Known touchpoint:** Seed split lands "creation and discovery" as a pointer to `docs/reality/discovery.md` (already exists). No conflict with the future rework.

### Positioning area — `docs/positioning/`

**Status:** review only. Already restructured into core views and views on the boundary (2026-04).

**Scope:** read each page for voice consistency, link health, and alignment with the three-axes framing. No structural changes expected.

### Engineering area — `docs/engineering/`

**Status:** deferred — tackled on its own track after the other areas land.

**Why deferred:** the area is in active flux (AVRO schema rethink, three committed languages — AVRO/git/Kafka). Reworking while the thinking is still moving would waste effort. Letting the other areas settle first also means their inbound links into engineering are deliberate by the time engineering's own rework begins.

**Pre-touch:** the seed split lands the engineering view (translation table + three fabrics) into engineering before the area's own rework — probable home `docs/engineering/seed.md`. The later engineering rework absorbs this.

## Final pass — topnav deep-linking

**When:** after the content rewrite across seed + five areas is done.

**Why:** once the informational axis is reshaped, the personal axis (topnav) needs its links refreshed so it points deliberately into the new structure. A reader arriving via About / HAICC / P2P should be able to step naturally into the reference material at the right places.

**Scope:**

- Review each topnav page (About, HAICC, P2P) for links into the ref lib.
- For each mention of a concept that now has a dedicated ref lib page, add or strengthen the link.
- Make the direction explicit: personal framing first, then "if you want the structured version, it's here".
- Check that the destinations exist, use correct paths, and land on the page that actually matches the framing the topnav page uses.
- Keep voice unchanged — topnav stays personal. Only the cross-links into the informational axis change.
