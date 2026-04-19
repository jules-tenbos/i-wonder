---
title: Language area rework
status: new
date: 2026-04-19
---

# Language Area — Rework

The language area of the ref lib needs restructuring. The current index page reads like a post, not a reference page.

---

## Issues

1. **docs/language/index.md is half post** — needs rewriting as a proper ref lib index in narrator voice. Should describe the area and link to sub-pages, not argue a position.

2. **Missing: natural and formal languages** — the language area has no page on the distinction between natural languages (human, ambiguous, contextual) and formal languages (mathematical, logical, programming). This is fundamental to SPLectrum's treatment of language — P4 (equal standing) applies across both, and the seed's definition of language extends well beyond linguistics.

3. **Missing: software/formal languages page** — the "Let's Talk Software Languages" blog post links to the language area top level. It should link to a dedicated page on software languages as a category of formal language. What are the types? How do they relate? Where does SPLectrum's engineering sit?

4. **Research needed: taxonomy of software languages** — similar to how formal languages are classified (regular, context-free, context-sensitive, recursively enumerable), software languages have their own taxonomy. Assembly, imperative, functional, declarative, logic, markup, query, scripting, domain-specific. How does this taxonomy relate to formal language theory? Is there a structural classification that maps onto SPLectrum's framework?

---

## Proposed structure

```
docs/language/
  index.md              — area index (rewrite: narrator, ref lib voice)
  category-theory.md    — exists, fine
  natural-languages.md  — new: human language, ambiguity, context, language games
  formal-languages.md   — new: mathematical, logical, type theory, formal systems
  software-languages.md — new: taxonomy, types, relation to formal languages
```

## Blog post link update

- "Let's Talk Software Languages" (2026-04-11) currently links to `/language/`. Should link to `/language/software-languages` once the page exists.

## Dependencies

- The semiotics research (submissions/semiotics.md) intersects here — Saussure is about natural language, Peirce generalises beyond it. The language area should accommodate both.
- Category theory page already handles the mathematical formalisation angle.
