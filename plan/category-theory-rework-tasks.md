# Category Theory Rework — Task List

## Done

- [x] Blog post series — 5 posts created (June 1, 8, 16, 24, 28), category-theory label and series
- [x] Seed page `/seed/category-theory` — rewritten (narrower scope: P0+P1 as input, CT generates the rest)
- [x] Blog-entries include — extracted loop into `_includes/blog-entries.html`, series list centralised
- [x] Category-theory label page created, added to label index under Series

## Blocked on sections rework (9-box homepage restructuring)

These tasks depend on the Language / Vocabulary / Tools sections being restructured per the 9-box homepage discussion. The restructuring introduces `a-z / concepts / types` shape across all three sections, renames Math Tools → Tools, and moves existing pages into the new structure.

- [ ] **Tools section** — create `/tools/` landing, `/tools/a-z/c/category-theory/` entry (tool-aspect: what CT does when held as a tool for relational analysis). Currently `/math-tools/index.md` is a one-line stub that needs to become the Tools landing.
- [ ] **Language section CT page** — move `/language/category-theory/` to `/language/a-z/c/category-theory/` (language-aspect: CT as a language with its own grammar). Refocus content on the approach: float principle, meaning patterns, how CT is used to reason about languages. Current page has old Yoneda/convergence/relational-power content.
- [ ] **Language section restructure** — move existing `/language/natural-languages/`, `/language/formal-languages/`, `/language/software-languages/` into `/language/types/`. Create `/language/concepts/what-is-a-language/` (grammar criterion from 9-box discussion). Move `/language/what-is-a-language/` there.
- [ ] **Vocabulary section CT entry** — create `/vocabulary/a-z/c/category-theory/` (vocabulary-aspect: CT's specific vocabulary — morphism, functor, natural transformation, etc.).
- [ ] **Cross-links** — category theory entries in all three A-Zs cross-link to each other and to the seed page and positioning subject page.

## Independent of sections rework

- [ ] **Positioning subject page** `/positioning/subjects/c/category-theory` — update: expand higher categories section, reframe "where category theory stops" (CT captures the carrier of meaning patterns, not meaning itself), add foldback as structural insight. Draft proposes targeted updates, not full rewrite.
- [ ] **Seed index description** — currently "Mathematical convergence and its impact" — undersells the rewritten page. Update to reflect the structural claim.
- [ ] **Post images** — Posts 2–5 (Wrapper, Is Like Is, Meaning Patterns Travel, Friction) have IMAGE_TBD. Post 1 has Annie Spratt image. Decide: one shared image (series identity) or five different.
- [ ] **Post 1 pending-link on seed page** — seed page currently has no link to the blog series (removed in rewrite). Consider whether to add one at the bottom.
- [ ] **Open questions from rework doc** — Post 3 title ("Is Like, Is" vs "Same Restaurant" vs other). Post 1 word count (760, could trim). Image strategy.
- [ ] **Prior art section** — removed from seed page in the narrower rewrite. Lambek, DisCoCat, Institutions material can land on the Tools CT entry or the Language CT entry when those sections exist.
- [ ] **Wrapper, convergence, meaning patterns, epistemic asymmetry** — removed from seed page. These are covered by the blog posts. May also land on ref-lib pages (Tools concepts, Language concepts) when sections exist.

## Deferred (later in the programme)

- [ ] **Companion posts** — "Meaning Patterns Travel" thought post variant (separate from the series post), "RQM as test case" positioning piece, "Token/type and signifier/signified as the same meaning pattern" vocabulary entry.
- [ ] **Submissions file** `submissions/language-games-category-theory.md` — CT applied to SPLectrum's own language registers. May become a Tools concept page or a blog post when the Tools section exists.
- [ ] **Draft cleanup** — `drafts/seed-and-category-theory.md` and `drafts/seed-and-category-theory-notes.md` can be removed once all material has landed.
