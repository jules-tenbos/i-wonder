# Multilanguage site — Spanish, French, and beyond

Working notes for a future roadmap track. A multilanguage version of splectrum.world, starting with Spanish, then French, more as they come. Not a near-term build; the architectural sketch is captured here so it's ready when the time comes. Closely tied to the vocabulary-as-method work in `speaking-the-language-of.md` — each language version is a new language game, and the vocabulary translation is where the structural thinking lives.

## The vision

Translated versions of the site — content, vocabulary, navigation — per target language. English as source; other languages derived. Evolving toward AI-automated translation with the right glossary/vocabulary assistance, with human review in the loop until the automation is trusted.

Itself a SPLectrum exercise: the project applying its own method (one vocabulary per language game) to its own presentation across natural languages.

## Structural choice

**Subfolder per language:** `/es/`, `/fr/`, etc. under splectrum.world. One repo, one site, parallel page trees, single DNS, single sitemap registry.

Considered and deferred:

- **Subdomain per language** (`es.splectrum.world`). More isolation but more infrastructure.
- **jekyll-polyglot plugin.** Cleanest Jekyll solution but requires custom build (GitHub Actions), not vanilla GitHub Pages. Not needed now.

Subfolder works on vanilla GitHub Pages, keeps the site unified, preserves cross-links.

## Sitemap as translation registry

One unified sitemap across all languages, with hreflang annotations declaring translation relationships. Example:

```xml
<url>
  <loc>https://splectrum.world/seed/</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://splectrum.world/seed/" />
  <xhtml:link rel="alternate" hreflang="es" href="https://splectrum.world/es/seed/" />
</url>
```

Search engines treat these as translations of the same content — cleaner SEO signal than isolated per-language sitemaps.

The sitemap becomes more than an SEO artefact: it's the **authoritative record of what translations exist**. The script reads/writes it. The site can read a mirror (`docs/_data/translations.yml`) for UI-level queries — language switcher, "available in" badges.

## Script-owned translation workflow

All orchestration logic lives in a script (GitHub Action or similar), not in Jekyll Liquid:

- **Source of truth**: English content in `docs/_posts/`, `docs/seed/`, etc.
- **Script responsibilities**:
  - Decide what gets translated per language (all / selection / skip).
  - Run translation (AI-assisted → AI-automated) with the vocabulary glossary as constraint.
  - Produce translated pages under `docs/es/`, `docs/fr/`, etc.
  - Update the sitemap registry with hreflang annotations.
  - Emit `docs/_data/translations.yml` mirror for Jekyll UI access.
- **Jekyll**: renders whatever it finds. No orchestration in Liquid.

Fits alongside the existing daily-rebuild GitHub Action. Translation runs on source changes; human review pass flagged by diff.

## Advisory stubs for missing translations

Every URL exists somewhere reasonable. If a page isn't yet translated to Spanish, the script generates a stub at `/es/path/` with:

- Advisory in the target language: *"Esta página aún no está traducida. Versión en inglés abajo"* or similar.
- Full English content inline below the advisory.
- Canonical tag pointing to the English version (SEO signal — not duplicate content).

When a real translation arrives, the stub is replaced. No broken links across language versions; reader always lands somewhere useful. The advisory is the signpost — *this isn't in your language yet; here's what's available*. Fits the signpost-the-road-ahead principle.

## The vocabulary angle (the SPLectrum lens)

This is where multilanguage is *interesting*, not just operational. Each translated site is a new language game. `/vocabulary/splectrum-es/`, `/vocabulary/splectrum-fr/`, etc. become first-class artefacts. Three categories of terms:

- **Universal philosophical** — being, language, subject — have standard translations (Ser, Lenguaje, Sujeto).
- **SPLectrum-coined** — Mycelium, fabric, HAICC — decisions needed: keep English, or translate? Different languages may answer differently.
- **Cross-language baggage** — différance, Sein, śūnyatā — often stay untranslated with gloss.

Per-language vocabulary pages, declared bridges between them. Exactly the context-shift challenge from `speaking-the-language-of.md`, now at the inter-language level. Category theory (functors, natural transformations) has formal language for this — connects to `language-games-category-theory.md`.

Label translations follow the same pattern: the script maintains a label-mapping registry. Some labels translate; some stay as-is (project-native terms like "SPLectrum" or "mycelium"). Registry lives alongside the translation data.

## Evolution toward AI automation

Three stages, not a single choice:

1. **Manual + AI-assisted now.** Draft with AI, native-speaker review. Build the glossary as it goes.
2. **Scripted AI translation.** GitHub Action runs on changed pages, constrained by the vocabulary glossary. Human review pass per language.
3. **Fully automated.** The vocabulary file *is* the constraint; translation triggered on source change; review flagged by diff only.

Each stage needs the previous stage's glossary to be solid. The vocabulary discipline being set up now is what makes later stages tractable.

## Post potential

Candidate angle: *"Speaking the language of, literally"* or *"One site, many languages, one method"*. Key beats:

- The "speaking the language of" discipline (from the vocabulary-as-method submission) applied at the inter-language level.
- Each language version as a new language game with its own vocabulary.
- Script-owned orchestration, sitemap as registry, advisory stubs.
- Category theory angle for formal bridges between language vocabularies.

Probably SPLectrum persona — the project applying its own method to its own presentation.

## Related work

- `submissions/speaking-the-language-of.md` — vocabulary-as-method (foundation for this).
- `submissions/language-games-category-theory.md` — formal language for context shifts / translations between language games.
