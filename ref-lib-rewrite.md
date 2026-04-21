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

1. **Engineering rework** — its own track.
2. **Vocabulary** — consolidate / grow toward one vocabulary per language game.
3. **Topnav deep-linking pass** — final cross-link cleanup from topnav into the reshaped library.

## Area pages

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
- **Category theory on SPLectrum's language games** — active in `submissions/language-games-category-theory.md`. Research programme: once language registers are documented explicitly (tone-of-voice, process, vocabularies), apply category theory to them as operational tool, not structural parallel. Produces relational insight across the project's own languages.
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
