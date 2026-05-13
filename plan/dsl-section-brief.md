# DSL section — implementation brief

Task: build an eight-page cluster under `/positioning/subjects/d/domain-specific-languages/` covering Domain-Specific Languages as a subject. Reference material, independent treatment, written to serve both human searchers and AI search snippet extraction.

## Why this matters

DSL is a frequently searched term. The current single page at this URL does two jobs in one slot (subject-reference and SPLectrum-positioning) and the searcher-facing material out there is thin in a specific way: Wikipedia and Fowler's site dominate, both software-only, and academic literature mostly consists of papers building specific DSLs rather than treatments of DSL-as-a-general-phenomenon. The cluster fills that gap with broad coverage plus enough depth for initial understanding, deep-linking out for specialist depth.

The SPLectrum-internal take on DSLs lives separately on the `/language/` axis (to be specified later). This brief is for the positioning/reference cluster only.

## Cluster structure

Eight pages. Existing single page at the landing URL is replaced.

1. `/positioning/subjects/d/domain-specific-languages/` — **landing page**
2. `/positioning/subjects/d/domain-specific-languages/history/`
3. `/positioning/subjects/d/domain-specific-languages/classification-axes/`
4. `/positioning/subjects/d/domain-specific-languages/internal-dsls/`
5. `/positioning/subjects/d/domain-specific-languages/external-dsls/`
6. `/positioning/subjects/d/domain-specific-languages/language-workbenches/`
7. `/positioning/subjects/d/domain-specific-languages/design-considerations/`
8. `/positioning/subjects/d/domain-specific-languages/the-pattern-beyond-software/`

## Voice & editorial conventions

These apply across every page in the cluster. They follow the rules in `positioning-voice.md`, `editorial-stance.md`, and `post-vs-ref-lib.md`.

**Independent treatment.** Present DSLs and the surrounding material on their own terms. The reader does not need to know SPLectrum exists to use these pages.

**No P-tags. No SPLectrum vocabulary in the body.** No P0, P1, P4, etc. No "seed", no "interrelational pluralism", no "subject reality". If something can only be said by reaching for SPLectrum vocabulary, it does not belong on these pages — it belongs on the future `/language/dsl/` page.

**No claiming verbs.** No "matters to SPLectrum because", no "this is what SPLectrum means by", no closing gestures pointing at the project's engineering direction. The pages stand on their own.

**No personifying.** "It follows that", "this suggests", "the principle is" rather than "DSLs say", "the pattern demands".

**Setting examples, not imposing.** Where the page summarises or characterises (e.g., a brief account of internal vs external), use humble framings: "Fowler's distinction is...", "a common way to classify...", "one approach...". Avoid "the way" or "the definition".

**Stand back when the content speaks.** Don't write trailing commentary paragraphs that tell the reader how to read the page. If a list of examples does its job, no closing summary is needed.

**Deep-linking strategy.** Each section orients the reader and points outward. The page gives enough depth for initial understanding; specialist depth lives at the link target. External links go to authoritative sources (original papers, canonical books, official documentation). Internal links cross-reference sister pages in the cluster and existing site pages where relevant (Wittgenstein, Merleau-Ponty, software languages, category theory).

**AI snippet readiness.** Every page leads with a clean definitional paragraph. No hedging at the top, no buried lede. Key facts in scannable form where appropriate. The landing page especially is written so the opening paragraph is the paragraph an AI search assistant pulls verbatim.

## Per-page specification

### 1. Landing page

Purpose: a self-contained answer good enough for AI search blurb extraction, and a hub that funnels a human searcher to the right sub-page.

Sections:

- **Opening paragraph** (snippet-worthy). Definition of a DSL, contrast with general-purpose languages, two or three canonical examples (SQL, regex, CSS). Roughly 80–120 words.
- **Key characteristics** (scannable list of 5–7 items). Examples: limited expressiveness focused on a domain; vocabulary and operators carry domain meaning; often declarative; usually not Turing-complete; two main implementation styles (internal and external); distinct from general-purpose languages.
- **A short overview** (three paragraphs). One paragraph on brief history (Iverson, Fowler, the lineage in compressed form). One paragraph on the internal/external distinction. One paragraph on the cross-domain observation (the pattern of purpose-built vocabularies recurring in mathematics, music, chemistry, philosophy). Each paragraph self-contained, complete enough that a reader who stops here has a real answer.
- **Examples gallery**. The curated list, one line each: SQL, regex, CSS, HTML, Make, LaTeX, APL, musical notation, chemical formulas (SMILES), mathematical notation. No deep treatment.
- **Explore further**. The cluster map — each of the seven sub-pages named with a one-sentence summary of what it covers.
- **Sources**. Compact list: Fowler 2010, Mernik/Heering/Sloane 2005, Voelter 2013, Iverson 1980.

### 2. History page

Purpose: the lineage proper, in light narrative form with anchors. The piece the searcher can't find elsewhere.

Coverage (chronological, with light treatment per pivot — paragraph each, links out for depth):

- **1950s–60s — proto-DSLs.** FORTRAN (1957) for scientific computation; COBOL (1959) for business; APL (Iverson, conceived 1957, implemented 1966) for array mathematics. Each was domain-shaped but grew toward general purpose.
- **1970s — the declarative wave.** SQL (Codd 1970, Chamberlin/Boyce 1974), Make (Feldman 1976), Awk (Aho/Weinberger/Kernighan 1977), Sed, Lex/Yacc. The pattern of small focused languages around Unix becomes visible.
- **1979–80 — Iverson's Turing Award lecture.** Notation as a Tool of Thought. The first major argument that programming-language design is part of a wider history of notation, drawing on Lavoisier, Linnaeus, Boole.
- **1980s — Lisp and the seed of internal DSLs.** Lisp's macro system and homoiconicity make it natural to build small languages inside Lisp. This tradition feeds directly into the later internal-DSL renaissance.
- **1990s — markup and the web.** HTML, CSS, XML, and the XML-derivative family (XSLT, XPath, XQuery). DSLs become mainstream infrastructure.
- **2000s — internal DSL renaissance.** Ruby's expressiveness brings internal DSLs to wide attention (Rails, RSpec, Rake). Sergey Dmitriev coins "language-oriented programming". Fowler's Domain-Specific Languages (2010) consolidates the field.
- **2010s–present — workbenches and infrastructure.** JetBrains MPS, Eclipse Xtext, Spoofax mature. Terraform HCL, Kubernetes YAML, Gradle's Kotlin DSL — DSLs become standard for infrastructure-as-code.
- **The academic strand.** Mernik, Heering & Sloane's 2005 paper "When and How to Develop Domain-Specific Languages" gives the decision framework; van Deursen, Klint & Visser's 2000 annotated bibliography surveys the field; Voelter's DSL Engineering (2013) treats the workbench era.

### 3. Classification axes

Purpose: the taxonomy proper. All the ways DSLs can be classified, laid out cleanly. The page nobody else has.

Axes (one paragraph each, with a paired example to anchor each end):

- **Internal vs external** (Fowler's distinction). Internal: embedded in a host language. External: own grammar and parser. Example: jOOQ (internal, in Java) vs SQL (external).
- **Declarative vs imperative.** Declarative: state what the result should be. Imperative: state the steps. Example: SQL (declarative) vs Awk (imperative).
- **Notational vs executable.** Notational: a way of writing things down. Executable: a way of running things. Example: musical notation (notational) vs Make (executable). Iverson's lecture lives in this distinction.
- **User-facing vs technical.** User-facing: intended for domain experts who aren't programmers. Technical: intended for programmers working in a domain. Example: a business rules DSL (user-facing) vs ANTLR's grammar language (technical).
- **Standalone vs embedded.** A near-synonym for external vs internal, but worth noting separately because some embedded DSLs are heavyweight and some standalone DSLs are minimal.
- **Markup vs modelling vs programming.** Wikipedia's high-level split. Markup: HTML, XML. Modelling: UML, ER diagrams. Programming: SQL, regex. Each has its own implementation conventions.
- **Turing-complete vs not.** Most DSLs are deliberately not Turing-complete (SQL, regex, CSS) — domain focus benefits from giving up universality. Some are (PostScript, TeX). Worth flagging because non-Turing-completeness is often what makes a DSL safe to embed.

Close with a brief note that the axes are not orthogonal — a real DSL sits at a specific position across all of them, and the same DSL can be classified differently from different angles.

### 4. Internal DSLs

Purpose: full treatment of Fowler's internal approach.

Sections:

- **What an internal DSL is.** Definition. The host language gives the DSL its lexical structure; the DSL gets the host's tooling, parser, and ecosystem for free.
- **Techniques.** Method chaining and fluent interfaces; operator overloading; blocks and closures as composable units; monadic embedding (Haskell); meta-programming and macros (Lisp, Ruby, Scala). Brief description of each.
- **Trade-offs.** Inherits the host language's ecosystem (IDE support, debugger, packaging); but bounded by the host's syntactic surface. The DSL's grammar is the host's grammar with strategic choices about which features to use.
- **Examples** (with short code snippets where useful):
  - RSpec (Ruby) — test specification
  - ActiveRecord (Ruby) — database querying
  - jOOQ (Java/Kotlin) — type-safe SQL
  - Gradle Kotlin DSL — build configuration
  - sbt (Scala) — build configuration
  - Parsec / parser combinators (Haskell) — parsing
  - QuickCheck (Haskell) — property-based testing
- **Host languages well-suited to internal DSLs.** Ruby, Scala, Kotlin, Haskell, Clojure, Lisp. Why each: features that support DSL surface (blocks, infix operators, macros, type-class machinery).

### 5. External DSLs

Purpose: full treatment of Fowler's external approach.

Sections:

- **What an external DSL is.** Definition. Own grammar, own parser, no host language. Full syntactic freedom; full implementation responsibility.
- **The implementation pipeline.** Lexer → parser → AST → semantic model → execution (interpretation or code generation). One paragraph on each stage.
- **Parsing approaches.** Parser generators (ANTLR, Yacc/Bison, JavaCC); parser combinators (Parsec, FParsec); PEG parsers (PEG.js, tree-sitter); hand-written recursive descent.
- **Trade-offs.** Full freedom over syntax and semantics; substantial up-front investment; no ecosystem inheritance — tooling has to be built from scratch.
- **Examples** (brief, with link to the canonical reference for each):
  - SQL — relational querying (Codd, Chamberlin/Boyce)
  - Regular expressions — pattern matching (Friedl)
  - CSS — styling
  - Make — build dependencies (Feldman)
  - Awk — text processing
  - GraphQL — API querying
  - Terraform HCL — infrastructure as code
  - LaTeX — typesetting (Lamport, on TeX/Knuth)
- **Tooling.** ANTLR, Bison, tree-sitter, PEG.js — the modern ecosystem for building external DSLs.

### 6. Language workbenches

Purpose: the modern third path beyond the internal/external split. Genuinely under-covered in current materials.

Sections:

- **What a language workbench is.** Integrated environment for defining a DSL: grammar, type system, editor with syntax highlighting and code completion, transformation, generation. The workbench treats the DSL as a first-class artefact with its own IDE.
- **Projectional vs parser-based.** Most workbenches still use parsers; projectional workbenches (JetBrains MPS) edit the AST directly, no parsing involved. The trade-off: projectional editing allows non-textual syntax (tables, diagrams) but breaks plain-text tooling (diff, grep).
- **Key tools.**
  - JetBrains MPS — projectional, used for production DSLs (mbeddr for C, Realaxy for Java)
  - Eclipse Xtext — parser-based, integrates with Eclipse tooling
  - Spoofax — research-oriented, Stratego transformations
  - Rascal — meta-programming and source analysis
- **Why this is a distinct third path.** Workbenches make external DSL creation comparable in cost to internal DSLs, by industrialising the surrounding infrastructure. They also enable forms of language composition (multiple DSLs in one document) that neither pure internal nor pure external can match.
- **Trade-offs.** Heavy upfront investment in learning the workbench itself; powerful tooling once the language is defined; lock-in to the workbench's ecosystem.

### 7. Design considerations

Purpose: when to build a DSL, what the trade-offs are, what makes one good.

Sections:

- **When to build a DSL.** Mernik/Heering/Sloane's decision framework: when the domain has recurring problems, when a stable vocabulary already exists, when domain experts can usefully read or write code, when productivity gains justify the investment. Brief treatment of each criterion.
- **Costs.** Tooling investment; learning curve for users; ecosystem fragmentation (each DSL is its own world); maintenance and evolution; risk of language obsolescence.
- **Benefits.** Domain-level expressiveness; error checking at the domain level (a SQL syntax error is more useful than a Java compile error about a string); code that reads as domain description; possible audience expansion (domain experts can read the code).
- **Pitfalls.** Under-powered languages that hit limits and need escape hatches; languages that grow toward general-purpose without ever quite getting there; languages designed by programmers for programmers when domain experts were the intended audience; slow evolution.
- **Patterns.** Brief treatment of Fowler's main patterns: semantic model, symbol table, expression builder. Link out to his book for full coverage.
- **Evolution.** DSLs need to evolve as the domain evolves. Strategies: versioning, deprecation, parallel grammars. Pointer to Voelter on this.

### 8. The pattern beyond software

Purpose: the cross-domain treatment. The page nobody else has.

Sections:

- **Iverson's argument.** Open the section with Iverson's 1979 Turing Award lecture as anchor. Notation as a Tool of Thought makes the explicit case that programming languages sit in a long history of notation, alongside chemistry, botany, and mathematics. Quote sparingly; summarise the argument.
- **Lavoisier's chemical nomenclature.** Lavoisier's 1787 *Méthode de Nomenclature Chimique* replaced an inconsistent vocabulary of alchemical names with a systematic one (oxygen, hydrogen, sulphuric acid). The reform was both linguistic and conceptual — a purpose-built vocabulary for a domain that had outgrown its old names.
- **Linnaeus's binomial nomenclature.** The 1750s system that gives every organism a two-part name (genus + species). A DSL for biological taxonomy. The vocabulary made comparative biology possible.
- **Mathematical notation.** Cajori's *A History of Mathematical Notations* covers the long evolution from rhetorical algebra through symbolic algebra to modern notation. Leibniz's calculus notation versus Newton's: a famous case where the choice of notation shaped which research programme could be pursued. Link out to Cajori.
- **Musical notation.** A DSL for performance. The five-line staff, note values, dynamics markings, tempo indications — operators that carry meaning only within the practice of performance. Notation evolved alongside the music it served.
- **Chemical structure notation.** SMILES, InChI, IUPAC nomenclature — modern DSLs for molecular structure. Each makes different aspects of a molecule visible.
- **The philosophical strand.** Where a domain becomes well enough understood to need its own vocabulary, vocabularies grow. Heidegger built one for Being (*Dasein*, *Zuhandenheit*, *Geworfenheit*); Wittgenstein's later work runs on its own vocabulary (language games, forms of life, family resemblance); Merleau-Ponty coined *le corps propre*, *la chair*, the chiasm. Each is a purpose-built vocabulary for a domain that ordinary language could not address. Link to the relevant site pages.
- **The underlying pattern.** Close with a brief statement of what these all share: where ordinary language cannot say what needs saying, a purpose-built vocabulary develops. The formal treatment that software engineering brought to this pattern — explicit grammar, defined operators, parsable syntax — is one chapter in a much longer story.

## Cross-cutting

### Sources to link

Core references the agent should cite and link consistently:

- Fowler, M. (2010). *Domain-Specific Languages*. Addison-Wesley. Also: <https://martinfowler.com/dsl.html> and <https://martinfowler.com/bliki/DomainSpecificLanguage.html>
- Mernik, M., Heering, J., & Sloane, A. M. (2005). When and how to develop domain-specific languages. *ACM Computing Surveys*, 37(4), 316–344.
- van Deursen, A., Klint, P., & Visser, J. (2000). Domain-specific languages: An annotated bibliography. *ACM SIGPLAN Notices*, 35(6), 26–36.
- Voelter, M. (2013). *DSL Engineering*. Available at <http://dslbook.org/>
- Iverson, K. E. (1980). Notation as a tool of thought. *Communications of the ACM*, 23(8), 444–465. <https://www.jsoftware.com/papers/tot.htm>
- Wikipedia, *Domain-specific language*: <https://en.wikipedia.org/wiki/Domain-specific_language>
- Cajori, F. (1928–1929). *A History of Mathematical Notations*. Open Court.
- Ward, M. P. (1994). Language oriented programming. *Software — Concepts and Tools*, 15, 147–161.

### Internal cross-links

- Sister pages within the cluster — every page links to the landing page and to its closest cluster neighbours.
- Existing site pages to link from `the-pattern-beyond-software/`: `/positioning/persons/w/wittgenstein/`, `/positioning/persons/m/merleau-ponty/`, `/positioning/persons/h/heidegger/`, `/positioning/subjects/c/category-theory/`.
- Existing site page to link from the landing page where relevant: `/language/software-languages/`.

### Length guidance

- Landing page: ~800–1000 words. Dense, comprehensive enough to stand alone, organised for both AI extraction and human navigation.
- Sub-pages: ~1000–1500 words each. Substantial treatment, but not bloated. Each section earns its place.
- History page can run longer (~1500–2000) given the chronological span.
- The-pattern-beyond-software can run longer (~1500–2000) given the breadth of domains covered.

### Format conventions

- Markdown throughout.
- H1 for page title only. H2 for major sections. H3 sparingly, only where genuinely needed.
- Compact paragraphs. No long unbroken text.
- Sources at the end of each sub-page; landing page has a compact sources section.
- Code snippets only where they demonstrate something specific (internal DSL techniques benefit from one or two short snippets; external DSL examples mostly don't need them).

## Out of scope

What this cluster does **not** cover:

- SPLectrum's own view of DSLs. That belongs on the future `/language/dsl/` page, which will be specified separately. Do not pre-empt it.
- DSL implementation tutorials. The pages orient and link out; they do not teach how to build a DSL.
- Specific DSL deep-dives (a full SQL tutorial, a full regex reference). Examples are illustrative; depth lives at the linked sources.

## Editorial pass

After the agent drafts the cluster, the editorial pass will check:

- Voice rules followed: no P-tags, no SPLectrum vocabulary in body, independent treatment, no claiming verbs, no closing gestures pointing at the project.
- Opening paragraphs are clean and definitional (AI snippet readiness).
- Deep-linking strategy applied consistently (every section points outward where appropriate).
- Cross-links between cluster pages and to existing site pages.
- No drift toward Wikipedia-style flat coverage; the pages should feel like a structured tour, not an encyclopedia entry.
- No drift toward over-claiming or magisterial tone; the learning register applies (engaged but on equal standing with the material).
