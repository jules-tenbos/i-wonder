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
- **Engineering** — how SPLectrum builds. Split into `splectrum/` (logical design: top-level design, three pillars Mycelium/SPLectrum/HAICC) and `technology/` (external platform: bare, bare-for-pear modules).
- **Vocabulary** — one vocabulary per language game. Structured as `vocabulary/splectrum/` with per-game pages (seed, engineering, HAICC). Room for other families to sit alongside SPLectrum.

This framing informs the rework of each area index and the placement of pages that cross boundaries.

## Execution status

1. **Engineering rework** — done. Three siblings: `splectrum/` (logical design, three pillars), `technology/` (bare + bare-for-pear), and earlier `implementation/` now removed (content is SPLectrum-specific and sits better as blog narrative).
2. **Vocabulary** — done. Per-game structure under `/vocabulary/splectrum/`, sourced from canonical seed pages.
3. **Topnav deep-linking pass** — pending. Final cross-link cleanup from topnav into the reshaped library.

## Post-rework research topics

Topics that surfaced during the rework but need genuine research and conversation to develop properly. After the active rework is done, these move into `submissions/` to flow through the normal pipeline: submission → draft → blog conversation → eventual ref lib absorption.

- **Principle-themed positioning pages** — the big three (philosophical-trajectory, scientific-positioning, being-as-tension) funnel into Reality. P1–P5 could each grow their own positioning page as the material matures. Candidate thinkers per principle (rough map, not prescriptive):
  - **P1** — Wittgenstein, Saussure (briefly cited on `/seed/philosophical`); plus Peirce's triadic sign, structuralism.
  - **P2** — Merleau-Ponty, Husserl (cited); plus Heidegger's being-in-the-world, James's radical empiricism.
  - **P3** — Peirce, Habermas, Davidson, Rorty, Sellars/Brandom.
  - **P4** — looser convergences: Feyerabend, Lyotard, Goodman, Deleuze. Most SPLectrum-original of the relational principles.
  - **P5** — different lineage from the relational turn: Peirce (evolutionary realism), Whitehead, Bergson, Hegel, Popper/Kuhn/Lakatos, Teilhard.
- **P0–P5 potentiality/actuality theme** — active in `submissions/seed-discovery-research.md`. Cross-principle territory spanning P0 (full power) and P5 (expression); philosophical anchors Aristotle / Bergson / Deleuze.
- **Category theory on SPLectrum's language games** — active in `submissions/language-games-category-theory.md`. Research programme: once language registers are documented explicitly (tone-of-voice, process, vocabularies), apply category theory to them as operational tool, not structural parallel. Produces relational insight across the project's own languages.
- **SPLectrum test framework as infrastructure module** — active in `submissions/spl-test-framework.md`. Full-chain no-mock testing principles; future modularisation into `technology/bare-for-pear/test-framework/` is on spl5's worklist.
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
