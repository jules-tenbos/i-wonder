[In Wonder - The World of Splectrum](../) > [Engineering](./) > Top Level Design

# Splectrum Engineering — Top Level Design

The bridge between the Splectrum philosophical framework and its engineering. This document introduces the three pillars and the design commitments that govern all engineering below this level.

---

## From Philosophy to Engineering

Splectrum's six seed principles (P0–P5) describe properties shared by all languages. The engineering does not implement these principles — it is these principles expressed in another language. The relationship is relational, not representational. Neither side governs the other. The quality gate is low friction at the boundary.

If the seed holds, the engineering that grows from it should look like how reality works.

## The Three Pillars

P0 — being implies language — yields three inseparable aspects. These become the three pillars of the engineering: state, meaning, and cognition. Three fabrics, not three layers. Aspects of the same thing.

### Mycelium — Where Things Exist

The data fabric. The substrate. Structure, records, contexts, metadata, traversal. Everything encoded as information. The subject never touches the data world directly — only through the mycelium interface.

Mycelium is decentralised at the data level. No central database, no single source of truth. Subject realities within git repositories. What actually exists is always mycelium fabric expressed as subject realities. The totality of data is only a logical totality — the sum of everything across the fabric.

Mycelium hosts both languages (splectrum) and process (HAICC) as facts in its metadata. It is the stable ground — minimal, universal, unchanged when the layers above evolve.

Constitutive dependencies: git (identity, history, boundary) and AVRO (schema, conformance, protocol, interface).

### Splectrum — What Languages Are Available and How They Relate

The language fabric. Meaning. Splectrum supplies the languages — protocol libraries, schemas, meaning structures. A fabric in its own right, not glue between the other two.

The relational structure that governs how decentralised data and decentralised cognition interact without needing a central authority. P4 — equal standing — expressed as architecture.

P1–P5 as engineering:

- P1 (relational) → protocols as language games, interaction through surfaces
- P2 (medium of experience) → subject as POV entity, persona as interaction role
- P3 (sharing knowledge) → visibility as sharing, convergence as objectivity
- P4 (equal standing) → no hierarchy between languages, orchestration within not across
- P5 (growing complexity) → web not tree, spawn not design, complexity through diversification

Natural language as the carrier language. AI makes this operational. Ambiguity at the fringes is generative — where new meaning enters.

### HAICC — How Process Flows Through Those Languages

The cognition fabric. Human-AI Creative Collaboration. How process flows through languages while maintaining genuine human partnership.

The persona is the operational unit. It declares required capabilities. These are tested against available capabilities — human and AI. The conformance determines work division. Optimisation direction: toward AI autonomy. The human retains what AI capability does not yet cover.

Conscious is what is in focus — the work at hand. Subconscious is what supports it — the additional activity needed to achieve the conscious task. AI and human are present in both layers. The persona is the continuous identity across both.

Plasticity is the ability to learn. A capability starts conscious — attended, deliberate. Through practice it moves subconscious — running without attention. The movement IS learning. Learning is architecturally native because the conscious/subconscious design makes it so. The design is compatible with learning by construction.

The subconscious operating pattern is evolutionary: scan, diversify, evolve. Process capabilities dormant in the fabric, woken by data state change. What works reinforces, what doesn't fades. No orchestration — the data state is the relay. The appearance of orchestration is emergent.

HAICC is decentralised at the cognition level. Human and AI agents as collaborative peers, no central controller.

## How the Pillars Weave

The three pillars are not independent systems. They meet at defined boundary points:

**Mycelium–Splectrum.** Protocol libraries place their schemas as facts in mycelium metadata. Splectrum defines the languages. Mycelium hosts them. Schema discovery during traversal is the mechanism — schemas present in context metadata, accumulated naturally as the path is walked. No registry, no injection — facts in the fabric.

**Mycelium–HAICC.** The process layer sits in the fabric alongside the projection layer. Process definitions, watcher expressions, readiness schemas — all live in mycelium context metadata. The trigger model operates on the fabric: data footprint observation, watcher expressions as get paths, accumulation and readiness as data state facts. HAICC's process flow uses mycelium's substrate.

**Splectrum–HAICC.** Splectrum supplies the languages. HAICC supplies the process flow through them. Protocol libraries (splectrum) define what operations exist. The process layer (HAICC) determines when and how they fire. The persona (HAICC) uses protocols (splectrum) in service of its role. The persona is the why; the protocols are the how.

**All three together.** A process is triggered by data state change (mycelium), its inputs conform to a schema (splectrum), the persona engages with the ready state (HAICC). The three pillars are simultaneously present in every act.

## Design Commitments

The design commitments govern all engineering below this level. They are the philosophical framework in engineering language. Each design must conform to them. The quality test is low friction with the framework.

The full set of commitments is maintained in [Design Commitments](design-commitments). They include:

- Three-pillar unity — aspects of the same thing, not independent systems
- Decentralisation is constitutive — P4 all the way through
- Context and language are mutually constitutive — inseparable design units
- Designing creates reality — reality is the dynamic of the data state of being
- Natural language as carrier — splectrum supplies, HAICC flows, AI enables
- Ambiguity is generative — openness at the fringes
- The honesty criterion — relational, low friction, conformance not perfection
- Boundary is structurally real — the boundary expresses the differentiation
- Recursive self-similarity — same patterns at every level
- Complexity grows in expression, not in power — web not tree
- The subject experiences reality only through the local data fabric
- Visibility is sharing — no separate mechanism
- Splectrum supplies languages, HAICC supplies process flow
- Persona-driven role assignment with optimisation toward AI autonomy
- Conscious and subconscious with plasticity — learning is architecturally native
- Evolutionary process model — the subconscious operating pattern

## Document Map

### This Level

| Document | What it covers |
|----------|---------------|
| **[This document](top-level-design)** | Bridge between philosophy and engineering. Introduces pillars and commitments |
| **[Design Commitments](design-commitments)** | The constraints. Philosophical structure as engineering law |
| **[Process Models](process-models)** | HAICC: the decentralised evolutionary pattern and its neuroscience grounding |

### Mycelium Design

| Document | What it covers |
|----------|---------------|
| **[Mycelium Fabric](mycelium/)** | The static architecture. Records, contexts, metadata, traversal, the boundary |
| **Mycelium Process** | The dynamic layers. Trigger model, process layer, core API, protocol libraries |

### Open

| Area | Status |
|------|--------|
| **Splectrum engineering design** | Early stage. Protocol libraries defined in mycelium process. Language fabric design not yet articulated as its own document |
| **HAICC design** | Early stage, ahead of splectrum. Persona mechanism, conscious/subconscious, plasticity, and evolutionary model established. Detailed design not yet articulated |

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
