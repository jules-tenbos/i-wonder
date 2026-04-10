---
title: "The Physical/Logical Pivot"
type: substantial
status: in-progress
destinations: engineering
---

# The Physical/Logical Pivot

Substantial submission. The discovery that carrier/meaning is physical/logical — and that this distinction, already native to AVRO, opens the architecture to natural language as a first-class data medium. This document describes the pivot, the mechanism, and the implications for AVRO and git.

---

## The Discovery

The AVRO design scope identified a governing principle: carrier/meaning separation. The data schema carries content. The schema name resolves meaning. This was framed as an observation about how AVRO namespaces work.

The discovery is that this separation is deeper than namespaces. It is the physical/logical axis of the entire architecture — and it maps directly onto the three-pillar structure:

- **Mycelium** — the physical. Strings, bytes, records, contexts. The carrier.
- **Splectrum** — the logical. Namespaces, meaning languages, concept schemas. What it means.
- **HAICC** — the activation. The cognitive capability that resolves logical against physical. What makes meaning operational.

Three fabrics, one act. Every data interaction involves all three simultaneously. The physical data exists in mycelium. The logical type declares what meaning language it belongs to. HAICC provides the cognition that can resolve one into the other.

Without HAICC, the logical layer is inert — an annotation doing nothing. HAICC is what activates the logical. This is the precise sense in which the three pillars are aspects of the same thing, not independent systems.

## AVRO as Double Core

AVRO was already constitutive to mycelium — alongside git, the full substrate. But it was constitutive as plumbing: serialisation, schema contracts, RPC boundaries, protocol definitions.

The pivot reveals AVRO as constitutive in a second sense: as the language of meaning expression. AVRO does not just carry data structures. It expresses meaning structures. The logical type mechanism, the namespace hierarchy, the conformance model — these are meaning machinery, not just engineering machinery.

AVRO is double core:

- **Engineering core** — serialisation, schema evolution, RPC, protocol definition. The infrastructure.
- **Meaning core** — logical types as meaning language identifiers, namespaces as language identity, conformance as conceptual extractability. The semantics.

Both were always there. The meaning core was latent in AVRO's own design — logical types, namespaces, reader/writer resolution. The pivot discovers it, not invents it.

## The Mechanism — Natural Language Logical Types

### Logical Types as Language Identifiers

AVRO logical types annotate primitive types with interpretation instructions. A `date` is an `int` with a logical type saying "interpret me as days since epoch." The primitive carries the data. The logical type declares the meaning.

The extension: a natural language field is a `string` with a logical type whose fully qualified name identifies the meaning language the text is expressed in.

```json
{
  "type": "string",
  "logicalType": "splectrum.heidegger"
}
```

This is not a description of text format. It is a declaration of which language game the content is playing. `splectrum.heidegger` says this text is in Heideggerian language. `splectrum.pragmatist` says Rorty territory. `app.legal.uk` says UK legal language. `splectrum.natural` is the base — uncommitted natural language with no declared language commitment.

Each logical type namespace is a language with equal standing (P4). None is privileged. Each has its own vocabulary of extractable concepts.

### Concept Lists as Language Vocabulary

The logical type carries the full vocabulary of the language — the concepts that are extractable from content in this language:

```json
{
  "type": "string",
  "logicalType": "splectrum.heidegger",
  "concepts": ["being", "dasein", "thrownness", "clearing",
               "readiness-to-hand", "present-at-hand", "das-man"]
}
```

The concept list declares competence — everything the language makes available. This is what this text *can* yield. The concept list is carried as logical type metadata, using AVRO's native mechanism for additional properties on logical types (as `decimal` carries `precision` and `scale`).

### Concept Explanations as Relational Structure

A concept is not just a name. It is a relational structure expressed in other concepts. `Dasein` is not an atom — it is "being that is aware of its own being, thrown into a world it didn't choose, always already in relation." The explanation uses concepts like `being`, `awareness`, `thrownness`, `world`, `relation`.

The concept declaration has two levels:

- **The concept name** — `dasein`. The identity within its language.
- **The concept explanation** — a relational structure composed of other concepts. The internal wiring that makes the concept what it is.

The explanation is itself language — a record with a logical type. It could be:

- Natural language with logical type `splectrum.natural` — a paragraph describing what the concept means
- A formal expression with logical type `splectrum.formal.logic` — a predicate structure
- An explanation in its own language — dasein explained in Heideggerian terms
- An explanation in a different meaning language — dasein explained in pragmatist terms
- Multiple of these simultaneously — different records, same concept, different languages

Each explanation is subject to the same "can I read it as" mechanism. The recursion is deliberate — concepts explain themselves in terms of other concepts, and each explanation is a transformation surface. The ground floor is `splectrum.natural` — uncommitted natural language with no further concept structure declared.

A concept is therefore not a definition but a nexus of transformations between languages. `Dasein` is the set of all its explanations across all meaning languages — and that set is open, growable. A new language enters the system, someone writes a new explanation of dasein in that language, the concept gets richer. P5 — complexity grows in expression, not in power.

Cross-language explanations are natural. A Heidegger-language explanation of a Hegel concept is a valid record — if the mapping is possible. Whether it is possible is itself a conformance question. The AI tries, the process report records what transferred and what didn't. The explanation exists with its conformance profile attached. And the friction points where the mapping doesn't work cleanly are where the two languages genuinely differ — that's not failure, that's P4 making itself visible.

The concept vocabulary of a language is not a flat list — it is a sub-fabric. Concepts as contexts, explanations as records within them, each with its own logical type. Discoverable during traversal. Architecture of absence — no explanation present, the concept is just a name. Explanations present, the concept has relational depth.

### Reader Footprints as Extraction Specs

A reader comes with a footprint — a subset of concepts it needs:

```json
{
  "concepts": ["dasein", "thrownness"]
}
```

The conformance question becomes: is the reader's footprint a subset of what the language can yield from this text? This separates competence (the full vocabulary) from performance (what's needed now).

### "Can I Read It As" — Unified Conformance

AVRO's existing conformance question — "can this be read as" — operates across three zones:

- **Formal zone:** can this record's fields be read through my reader schema? Structural compatibility. Deterministic.
- **Natural-to-structured zone:** can these concepts be extracted from this text? Conceptual extractability. Cognitive. Binary at the contract level.
- **Language-to-language zone:** can this text in language A be read as language B? Gradient conformance. A text declared as `splectrum.natural` queried against `splectrum.heidegger` may yield a partial match — some Heidegger concepts are present, others are not. The conformance answer is a profile, not a yes/no.

Same question across all three zones. Different resolution. In the formal zone, AVRO's native resolution handles it. In the natural zones, the resolution routes to an AI capability registered for the logical type's namespace. The AI behind the RPC boundary does the interpretive work.

The language-to-language conformance check does not require the text to use the target language's vocabulary. It requires the text to exhibit the *relational patterns* that the target language's concepts describe. A text about a person confronting the fact that they exist in circumstances they never chose — that's `dasein` in explanatory language, without the word ever appearing. The concept explanation is the matching template. The AI recognises the constituent concept pattern.

The reader schema *is* the extraction spec. Field names are concept names. Types are expected shapes. `firstname: string` means "I need the concept *firstname* as text." The schema doesn't describe a format — it describes an intent.

AVRO's existing reader schema behaviour maps directly:

- Missing fields with defaults → concept not found, default applied
- Extra fields → additional concepts in text, ignored by this reader
- Type promotion → concept extracted in a compatible shape

The conformance answer is binary at the contract level — conforms or doesn't. But the process behind the RPC boundary is doing fuzzy extraction and making a commitment. The process report carries provenance — what was interpreted, with what confidence, what was ambiguous.

### The Concepts Schema

The concepts property on a logical type points to a standard AVRO record schema by fully qualified name:

```json
{
  "type": "string",
  "logicalType": "splectrum.natural",
  "concepts": "app.contacts.PersonName"
}
```

The `PersonName` schema is defined normally in its own namespace:

```json
{
  "type": "record",
  "name": "PersonName",
  "namespace": "app.contacts",
  "fields": [
    {"name": "firstname", "type": "string"},
    {"name": "lastname", "type": "string"}
  ]
}
```

The schema does double duty. In the formal zone it is a data structure. In the natural zone it is a concept extraction spec. Same schema, different conformance resolution. This is multiple conformance operating on the schema itself.

The schema lives in fabric metadata as a fact, discovered during traversal. No registry.

### Concept Mapping Between Languages

The concept lists make languages comparable. Heidegger declares `[dasein, thrownness, clearing, ...]`. Rorty declares `[conversation, solidarity, contingency, ...]`. The mapping question: can `dasein` be read as `conversation`?

This is the same "can I read it as" pattern, one level up. Not extracting structured data from natural text, but extracting one meaning language's concepts from another's. The transformation is itself a morphism — input concept in one language, output concept in another, AI behind the boundary doing the interpretive work, process report carrying what was preserved and what was lost.

This is P4 as operational machinery. Equal standing means languages can be mapped — with explicit awareness of what translates and what doesn't. The concept lists make the mapping surface visible. The graph of concept mappings between logical types *is* the Splectrum language fabric as a concrete engineering thing.

### Meaning Loss

Every transformation between languages loses something. Meaning loss is not a bug — it is a first-class datum. The process report doesn't just say "here's what I extracted." It says "here's what didn't survive."

Every cross-language mapping could carry three things:

- **What transferred** — concepts that mapped with confidence
- **What transformed** — concepts that mapped but changed shape, partial conformance
- **What was lost** — concepts that have no landing zone in the target language

Meaning loss is asymmetric. Heidegger reading Hegel loses different things than Hegel reading Heidegger. The loss profile in each direction is different data. The pair of profiles together tells you how two languages relate — what they share, where they diverge, and what each sees that the other cannot.

Meaning loss also accumulates across transformation chains. A concept explanation in language A transformed into language B, then into language C, may lose explanatory power at each step. The individual steps may each be valid, but the accumulated loss may hollow out what made the explanation an explanation of *that concept*. A round-trip conformance check — taking the end-of-chain result back to the original language — is the empirical test for whether a transformation chain preserves explanatory meaning.

The meaning loss profile could carry information about what a language is structurally unable to say about another language's concepts. As the concept web grows — more explanations, more transformation attempts — the meaning loss landscape becomes richer. Patterns emerge: which languages lose the least between each other, which are fundamentally incommensurable on specific concepts.

This feeds back into language selection. When HAICC needs to choose which meaning language to think in about a problem, the meaning loss profiles inform which language will capture the most with the least loss for a particular conceptual territory.

None of this is imposed. The meaning loss profile is a possibility — a structure that exists if someone builds it into the fabric. Architecture of absence. A transformation that doesn't record meaning loss simply doesn't. No enforcement.

## The Activation Layer — HAICC

The only extension needed beyond native AVRO is implementation: when the resolution logic encounters a natural logical type, it routes to an AI capability instead of a deterministic converter.

This is an implementation behind the RPC boundary. The boundary contract remains AVRO — message in, message out. The concepts schema defines the output shape. The process report carries provenance.

HAICC's complexity gradient applies directly. The same logical type, same concepts schema, same RPC boundary — but behind it:

- A simple extractor for highly structured natural text
- An AI agent for genuinely ambiguous content
- A human for edge cases that need judgment

The caller doesn't know. The schema contract is identical. The process report tells you what happened. Three levels of opacity from the AVRO design scope — fabric sees opaque bytes, process management sees input/output schemas, execution is invisible behind the boundary.

## XPath — One Mechanism, Three Depths

### The Three-Layer Extension

The fabric's addressing mechanism — XPath-style path expressions — extends progressively through three layers. Each layer is discovered during traversal, not declared in advance. The path walks, accumulates metadata, and the resolution logic adapts.

**Layer one — opaque bytes.** XPath reaches a record. Key to opaque bytes. The base fabric. No schema, no interpretation. You get what's there.

**Layer two — structured data.** A schema is discovered in context metadata during traversal. XPath extends past the record boundary into structured internals. The same path expression continues through AVRO's reader schema resolution. Already established in the fabric design.

**Layer three — meaning.** A natural logical type is discovered during traversal. XPath extends into meaning. The same path expression now carries conformance thresholds against concept vocabularies. The resolution routes to AI capability behind the RPC boundary.

One addressing language, progressively deeper reach, determined entirely by what schemas and logical types are present in the metadata along the path. Architecture of absence at every layer — no schema, no structural access. No logical type, no meaning access. What's present determines what's possible.

The caller doesn't know which layer resolved. The return shape is the same — key-value pairs. What's in the value depends on what the traversal discovered and what the reader footprint requested. The XPath expression is the same at every depth. The fabric gets smarter as you add schemas and logical types to context metadata, not as you add machinery.

### Fuzzy Conformance and Gradient Queries

At layer three, conformance is not binary. A text declared as `splectrum.natural` queried against `splectrum.heidegger` may yield a gradient — 3 of 7 concepts extractable with confidence, the rest absent or loosely resonant. The conformance answer is a profile, not a yes/no.

This introduces threshold-based filtering into the path expression. A watcher or query can express: select all records where language conformance to `splectrum.heidegger` is at least 0.5. Records passing the threshold are in the result set. Records below are invisible to this query.

The pattern is identical to the formal zone — a get path with a reader schema filters out records that don't conform. The difference: structural conformance is binary and instant; language conformance is fuzzy and cognitive. Same mechanism, different resolution cost.

The conformance profile itself becomes data — a projection maintained in the fabric, the same way mutable structures are projections from immutable records. The cognitive cost of evaluating language conformance is paid once. Subsequent queries hit the cached profile. The projection layer maintains it as new content arrives.

A conformance profile attached to a record is itself a data state change. Watchers can observe conformance profiles — triggering when the language landscape of a context shifts. The fabric becomes aware of what languages its own content speaks.

## Git Enters the Picture

### The Narrative Commit

Git's commit message has always been a second-class annotation on the real thing — the diff. The physical/logical pivot inverts this.

The natural language commit message *is* the primary record. The structured changes are what you extract from it. The human commits meaning. The system derives structure.

A commit message as natural language text with a logical type and concepts list:

"Received submission 'Mycelium and Memory' from Jules. Evaluated — strong alignment with current editorial direction, the connection between forgetting and architecture of absence is novel. Accepted. Rewritten as draft: tightened the opening, restructured section three around the memory gradient, kept the original voice. Original submission removed."

This is simultaneously a commit, a process report, an auditable record, and queryable history. One natural language act doing what were previously separate concerns.

Multiple reader schemas extract different views:

- `{submission, status, action}` → the formal process state
- `{editorial_judgment, reasoning}` → the evaluation rationale
- `{changes_made, structural, stylistic}` → the rewrite details
- `{files_created, files_deleted}` → the physical operations

Same text, multiple conformance. Each reader gets what it needs.

### Narrative History

The git design scope's memory gradient now has a medium. Consolidation is not squashing diffs into a combined diff. It is an AI reading ten narrative commits and producing one narrative that captures what mattered. The forgetting is editorial. The living subject remembers its own story, not its own diffs.

History rewriting becomes re-understanding. The same events, narrated from where the subject stands now. The original commits are immutable records. The consolidated narrative is a new immutable record at a different resolution. Both exist. The subject chooses which resolution to recall at.

Selective recall becomes natural language query against natural language history. "What happened to the submissions process last month?" is a conversation with your own past, not a log filter.

The attention-memory relationship gets real: conscious activity produces rich narrative commits. Subconscious activity produces minimal ones. During consolidation, rich narratives survive in shape while minimal ones dissolve into summary. Exactly how human memory works.

### Git Unchanged

Git doesn't change. The commit message field has no length limit, no format constraint. It is already opaque text. Slotting a logical type onto it is a metadata decision in the fabric, not a git modification.

What changes is weight. The message carries the meaning. The tree snapshot carries the physical result. The diff is derivable. The narrative is not.

Checkpoint granularity becomes narrative rhythm — when has enough happened to warrant a meaningful commit? An editorial judgment, attention-shaped, not clock-shaped.

## Relationship to Existing Search Technology

The semantic search landscape — vector databases, knowledge graphs, embedding models — was built before AI cognition was available as an infrastructure component. These technologies approximate meaning through mathematics because there was no cognition available to actually interpret it.

**Vector/embedding search** (Pinecone, Weaviate, FAISS) converts text into high-dimensional vectors and measures similarity by geometric proximity. Powerful but opaque — you get a similarity score but no visibility into *why* things are similar. There is no concept vocabulary, no declared language, no extraction spec. It is a statistical proxy for understanding.

**Knowledge graphs and ontologies** (RDF, OWL) encode meaning explicitly as structured concept networks with defined relationships. Powerful for reasoning but rigid — the ontology must be designed up front, and querying requires knowing the structure. Concepts are pre-mapped, not discovered at the point of contact.

The natural logical type mechanism is post-AI search. It assumes cognition is available behind the RPC boundary. The schema declares the language. The concept list declares the vocabulary. The reader footprint declares what's needed. An AI capability — not a vector distance calculation — resolves the conformance. This is a fundamentally different question: not proximity in a space but conformance to a declared vocabulary.

What neither existing approach does: declare a meaning language on the data itself, carry a concept vocabulary with the data as extractable competence, allow a reader to bring a subset footprint and get structured extraction, support gradient conformance, or unify structural and conceptual conformance in one mechanism.

However, existing search technology is not obsolete — it is repositioned. AI can pre-generate the search landscape as subconscious background activity. Conformance profiles are cached as projections. Vector indexes can operate on an AI-generated landscape where the vectors represent actually understood concepts rather than statistical approximations. Knowledge graphs can encode actually discovered relationships rather than hand-coded ontology.

The architecture of this is clean: HAICC generates the landscape as subconscious process. Splectrum declares the languages. Mycelium hosts the projections. Existing search technology becomes an implementation choice within the projection layer — efficient query mechanisms operating on cognitively generated data.

The two modes from the process design apply directly: lightweight — new content arrives, conformance profile generated, projections updated, real-time and incremental. Heavyweight — re-evaluate an entire context against a new meaning language, same mechanism at broader scope.

## What This Means for the Architecture

### Three Pillars Tightened

The physical/logical/cognitive framing is more precise than the previous formulation:

- Mycelium is not just "where things exist." It is the physical layer — carrier, substrate, bytes and structure.
- Splectrum is not just "what languages are available." It is the logical layer — meaning languages, concept vocabularies, the mapping surface between them.
- HAICC is not just "how process flows." It is the activation layer — the cognition that makes logical types operational, that resolves meaning from carrier, that bridges physical and logical.

The three are simultaneously present in every act. The natural language extraction case makes this vivid and concrete.

### No New Patterns

The physical/logical pivot introduces no new architectural patterns. Everything uses existing machinery:

- Logical types — native AVRO
- Metadata properties on logical types — native AVRO
- Namespaced schemas — native AVRO
- Reader/writer conformance — native AVRO
- Resolution routing through RPC — established in the process design
- Schema discovery during traversal — established in the fabric design
- Commit messages — native git

The only implementation extension: routing natural logical type conformance to AI capability behind the RPC boundary.

### AVRO Double Core in the Design

The AVRO design scope needs revision to reflect this. The carrier/meaning governing principle becomes the physical/logical principle. The "interpretation as invocation" concept in design area 6 now has concrete machinery — the natural logical type. A new design area is warranted for natural logical types as a first-class concern.

The broader narrative across the engineering documents — top-level design, design commitments, mycelium process — needs the physical/logical reframing threaded through.

### The Splectrum Engineering Opening

This gives Splectrum as engineering something concrete to design. The language fabric is the graph of logical type namespaces, their concept vocabularies, and the mappings between them. Protocol libraries supply the AI capabilities that activate each namespace. The concept mapping between languages is an operational concern, not a theoretical one.

Splectrum engineering design — previously flagged as "early stage, not yet articulated" — now has a clear entry point through the natural logical type mechanism.

---

*This document captures discoveries from a working conversation. The mechanism is clean but the design details — concept declaration format, reader footprint expression, resolution routing, cross-language mapping structures — are open for detailed design work.*
