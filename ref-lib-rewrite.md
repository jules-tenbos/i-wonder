# Reference Library Rewrite

Working list of pages in `docs/` that need review or rework. Walked top-down from the topnav and home page; detail added as we go.

## The three axes of the site

- **Topnav (About / HAICC / P2P)** — the **personal** axis. Jules's voice, the person behind the project.
- **Homepage boxes (seed + five areas)** — the **informational** axis. Structured reference library, narrator voice.
- **Posts (blog)** — the **conversational** axis. Thinking in motion, voice by persona.

Each axis is a legitimate path in. They reinforce each other through deliberate cross-links, but each has its own register and purpose.

## The shape of the library

Six areas under home, each with a defined remit:

- **Seed** — the foundational principles themselves, plus their incarnations in different vocabularies (philosophical, engineering, category-theoretic, creation-and-discovery). Each incarnation is a principles-level translation, not a full domain treatment — depth lives in the relevant area.
- **Language** — all language material, formal or otherwise. Category theory, formal languages, natural language, notation, language about language. The mechanics and properties of relation.
- **Reality** — the consequences of the seed for how we experience and know reality. SPLectrum's own philosophical and scientific work: metaphysics, epistemology, ontology — plus ethics, arts, anywhere the seed lands. First-person territory.
- **Positioning** — other people's work on reality. Where the seed sits among existing philosophical and scientific trajectories. Third-person territory. The counterpart to Reality: Reality is what SPLectrum says; Positioning is who else said something structurally adjacent.
- **Engineering** — how SPLectrum builds. Clear as-is; ongoing rework on AVRO/git/Kafka.
- **Vocabulary** — one vocabulary per language game. Today a single page of SPLectrum terms, but the direction is substantive: each language game gets its concepts documented explicitly. This is part of the language work — making concepts explicit so games can be studied, compared, and kept free of implicit drift. First-class area even while thin.

This framing informs the rework of each area index and the placement of pages that cross boundaries.

## Execution order

1. **Seed area rework** — bare principles on `/seed/`; rework each incarnation (philosophical, engineering, category-theory, discovery) one at a time. Mechanical split already done.
2. **Topnav P2P rework** — personal-voice rework with Holepunch + Midnight/Cardano.
3. **Positioning review pass.**
4. **Reality area rework** — scope when we get there.
5. **Language area rework** — new sub-pages, rewrite index.
6. **Engineering rework** — its own track.
7. **Vocabulary** — consolidate / grow toward one vocabulary per language game.
8. **Topnav deep-linking pass** — final cross-link cleanup from topnav into the reshaped library.

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

### Seed area — `docs/seed/`

**Status:** split complete; per-incarnation rework pending.

**Structure:** the seed is now an area with an index of bare principles and four incarnation pages — each a principles-level translation, not a full treatment of the domain.

- `docs/seed/index.md` — bare P0–P5, "What SPLectrum is", links to incarnations.
- `docs/seed/philosophical.md` — philosophical vocabulary (being, world, subject); convergences with Heidegger, Wittgenstein, Saussure, Merleau-Ponty, Husserl, Rorty.
- `docs/seed/engineering.md` — translation table (being→entity, world→data world, subject→POV entity); three fabrics (Mycelium, SPLectrum, HAICC).
- `docs/seed/category-theory.md` — P0+P1 as categorical territory; Yoneda as P2. Deeper treatment lives on `/language/category-theory`.
- `docs/seed/discovery.md` — P5 + P2 combined into creation-as-discovery. Deeper treatment lives on `/reality/discovery`.

**Rework — one incarnation at a time.** Each needs:
- Voice and framing consistent with the "foundation incarnation" role: enough to make the reading clear, not the full domain.
- Explicit link out to the area that develops the domain in depth.
- Cross-links from the relevant area index back to the seed incarnation.

**Deep links.** `/seed/philosophical` links to `/positioning/being-as-tension` for P0. Other principle-themed positioning pages don't exist yet; that's post-rework research (see below).

**Next session — post cross-links.** Scan `docs/_posts/` for posts suitable to link from the seed incarnation pages. `/seed/original` already links to "And Then There Were Six". Candidates likely exist for `/seed/philosophical` (e.g. "SPLectrum from First Principles"), `/seed/engineering`, `/seed/category-theory` ("The Seed and Category Theory" post), `/seed/discovery` ("Creation and Discovery", "Diversified Discovery").

**Open questions for Jules:**
- Should the seed incarnations have a shared footer pattern pointing to "full treatment in [area]"?
- Does "What SPLectrum is" stay on `/seed/index` or get its own page eventually?

### Language area — `docs/language/`

**Parked from seed area:** the "SPLectrum as meta-language" framing (previously on `/seed/`) needs a home in the language area. The content:

> A meta-language: a language about languages. The claim is purely structural — language is relational, whatever its contents. Content varies by language; structure does not. The fabric is the relational structure all languages share. SPLectrum studies the fabric, not any particular cloth.

Possible landings: language index, a dedicated page, or distributed across the new sub-pages. To decide during the language rework.



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

(Depth work — new principle-themed positioning pages, cross-principle themes — is post-rework research; see "Post-rework research topics" below.)

### Engineering area — `docs/engineering/`

**Status:** deferred — tackled on its own track after the other areas land.

**Why deferred:** the area is in active flux (AVRO schema rethink, three committed languages — AVRO/git/Kafka). Reworking while the thinking is still moving would waste effort. Letting the other areas settle first also means their inbound links into engineering are deliberate by the time engineering's own rework begins.

**Note:** the engineering incarnation of the seed now lives under `docs/seed/engineering.md` (not under `docs/engineering/`). The engineering area can reference it for the foundational translation without owning it.

## Post-rework research topics

Topics that surfaced during the rework but need genuine research and conversation to develop properly. After the active rework is done, these move into `submissions/` to flow through the normal pipeline: submission → draft → blog conversation → eventual ref lib absorption.

- **Principle-themed positioning pages** — the big three (philosophical-trajectory, scientific-positioning, being-as-tension) funnel into Reality. P1–P5 could each grow their own positioning page as the material matures. Candidate thinkers per principle (rough map, not prescriptive):
  - **P1** — Wittgenstein, Saussure (briefly cited on `/seed/philosophical`); plus Peirce's triadic sign, structuralism.
  - **P2** — Merleau-Ponty, Husserl (cited); plus Heidegger's being-in-the-world, James's radical empiricism.
  - **P3** — Peirce, Habermas, Davidson, Rorty, Sellars/Brandom.
  - **P4** — looser convergences: Feyerabend, Lyotard, Goodman, Deleuze. Most SPLectrum-original of the relational principles.
  - **P5** — different lineage from the relational turn: Peirce (evolutionary realism), Whitehead, Bergson, Hegel, Popper/Kuhn/Lakatos, Teilhard.
- **P0–P5 potentiality/actuality theme** — active in `submissions/seed-discovery-research.md`. Cross-principle territory spanning P0 (full power) and P5 (expression); philosophical anchors Aristotle / Bergson / Deleuze.
- **`/seed/philosophical` updates** — as each new positioning page lands, add a "See …" pointer from the relevant P-section, matching the pattern `/seed/philosophical` already uses for P0 → being-as-tension.

## Final pass — topnav deep-linking

**When:** after the content rewrite across seed + five areas is done.

**Why:** once the informational axis is reshaped, the personal axis (topnav) needs its links refreshed so it points deliberately into the new structure. A reader arriving via About / HAICC / P2P should be able to step naturally into the reference material at the right places.

**Scope:**

- Review each topnav page (About, HAICC, P2P) for links into the ref lib.
- For each mention of a concept that now has a dedicated ref lib page, add or strengthen the link.
- Make the direction explicit: personal framing first, then "if you want the structured version, it's here".
- Check that the destinations exist, use correct paths, and land on the page that actually matches the framing the topnav page uses.
- Keep voice unchanged — topnav stays personal. Only the cross-links into the informational axis change.
