---
title: SPlectrum Software History
type: substantial
status: in-progress
---

# SPlectrum Software History — From Solo Struggle to Seed

The evolution of the SPlectrum software project through six iterations. Not a failure
story — an evolution story. Each iteration taught something the previous couldn't.

---

## The Pre-AI Era: spl and spl1

### spl — The Original Vision

Jules's first attempt to conceive SPlectrum, working alone. A modular execution
platform: data streaming, immutable Kafka-like records, plugin APIs, self-contained
packages. Everything addressed by URI (`spl/execute/next`, `tools/git/status`).

The architecture was thoughtful:
- Execution engine with pipeline management and TTL protection
- Immutable data layer with filesystem encoding of topic/primary key
- Complete package lifecycle (create → save → load → deploy → remove)
- Self-extracting archives for distribution

But the vision was enormous. P2P, blockchain applications, AI integration,
security-first deployment. One person, no AI. The struggle to conceive it
properly was real.

### spl1 — Restructuring

The enhanced iteration. Still pre-AI. Focus on restructuring:
- Federated monorepo design (single-concern folders → container-wrapped git repos)
- External install workflows
- Core API enhancements

Seven major epics planned (Repository Restructure, SPlectrum Engines, Core API
Enhancement, TDD Implementation, BARE Migration, New Functionality, AVRO Integration).
A PRINCE2 "just enough planning" approach.

Also explored Qubes OS integration for security-first development — isolation
by design, disposable testing, air-gapped operations. Ambitious, systematic,
and entirely Jules working alone.

**What the pre-AI iterations show:** Jules had the vision from the start.
Language was already central — APIs, DSLs, "using my own words." The
architecture was sound. What was missing was the capacity to build it.
One person can conceive a cathedral but not build one alone.

---

## First AI Period: spl2 (July 2025)

### The Launch

Jules came out of near-retirement, frustrated with AI hype. Chose Claude Code
for its "detached terminal chat mode" — think space, not implementation space.
Started the "Joint to the Hip" blog. Published "I Didn't Think I Would Go There."

Core philosophy established immediately:
- AI should run the executive branch with minimal oversight
- Jules's role: help, collaborate, figure it out together
- Goal: help AI become a better team member

### What spl2 Built

Thirteen projects. Fifty-plus system analysis. The three-pillar framework
crystallised for the first time:

1. **Mycelium** — the data layer (immutable lists, cascading references,
   polymorphic views, P2P ready)
2. **Splectrum** — the meaning layer (test-driven creation, quality gates
   from meaning, API crystallisation)
3. **HAICC** — the creative action layer (entity-neutral collaboration,
   maximum autonomy, dynamic boundary)

### The Critical Reframe

Fifteen analysis documents captured the learning. The pivotal one: `02_the_reframe.md`.

> Problem: spl2 built infrastructure FOR AI instead of letting AI build FROM meaning.
> Solution: start with meaning layer (intent, understanding, capability), let
> technology decisions fall out the bottom.

This is the moment the infrastructure-first approach died. Jules had been
building containers, CLI tools, module systems — technology decisions that
should have been AI's domain.

### The over-orchestration lesson

An early phase of over-orchestration created frustrations for both sides. What became apparent: AI likes a clean focus point but doesn't like too much of a straight jacket. After pushing for too much workflow, the approach was talked through collaboratively. The pattern: collaborate to create workflows that work for both. Scripts for the rigid stuff, freedom where needed.

Key observations:
- AI likes clear roleplay, not mixture
- Boundaries most effective when natural to the roleplay
- AI likes constraints of failing tests — "goes wild on making them succeed"
- TDD became a shared language between human vision and AI execution

These experiences contributed toward what would later become HAICC.

### Key Insights from spl2

**What survived:**
- The three-pillar framework (Mycelium / Splectrum / HAICC)
- Test-driven creation
- P2P sovereignty
- Entity-neutral collaboration (both human and AI are "agents" with shared limitations)
- The API principle (crystallised capability)

**What failed:**
- Container framework (over-engineering)
- Custom CLI (premature)
- Tool wrappers (wrong abstraction level)
- Infrastructure-first approach (built solutions before understanding problems)

**The void identified:** No persistent meaning layer exists. Session-based tools
(Claude Code), flat files, MCP (plumbing without meaning). What's needed: minimal
structure giving AI a persistent, navigable, growing meaning layer.

**Unique positioning found:** Surveyed 27 existing systems across 7 categories.
Nobody had: semantic compaction, replay + semantics + P2P, agent-neutral meaning
layer, self-validating knowledge, living knowledge.

### Sunset

spl2 was sunset February 8, 2026. "Superseded by advances in AI."

---

## Second AI Period: spl3 (November 2025)

### The Adaptation

AI had evolved significantly since July. Previous approaches no longer optimal.
spl3 took a fundamentally different approach: start with minimum primitive,
build real tools, evaluate, let the model evolve through use.

Mission: "Boot Mycelium from principles to working code."

### What spl3 Built

Nine projects, each with REQUIREMENTS.md and EVALUATION.md. An honest, iterative
build cycle: decide → build → evaluate → evolve.

**The primitive emerged:** Record (key → content) in Context (container). Not the
immutable lists the principles had prescribed. The practice discovered something
simpler and more productive — context-centric rather than log-centric.

**Two working tools:**
- Context-view: generates a self-describing project state
- Evaluator: natural language requirements → AI-powered evaluation → reports

**The evaluator was remarkable:** AI evaluating AI output. It found real
discrepancies. It worked. But there was a blind spot: self-evaluation within
the same session. The builder assessing its own work.

### The Architectural Divergence

This is the most important thing that happened in spl3. The principles (from spl2)
said: immutable lists as sole primitive, cascading references, polymorphic views.
The practice built: record/context with metadata-driven mutability, flat API,
context traversal.

Not a refinement. A divergence. And the divergence was productive.

spl3's analysis documents were brutally honest about this. "Positioning vs reality"
gap explicitly identified. Principles reconciliation showed what didn't work.
Capability inventory listed "claimed but absent."

### Key Insights from spl3

**What was proven:**
- Record/context primitive sufficient (no new primitives needed across 9 projects)
- Three-layer architecture works (logical / capability / physical) with swappable storage
- Flat API correct — one interface, no type hierarchy
- Data-triggered processing works (file presence drives state)
- Natural language requirements work as quality gates
- Entity-neutral collaboration demonstrated practically
- Maximum beneficial autonomy is practical

**Critical difference from spl2:** Technology decisions were fully delegated to AI.
AI decided context-centric over log-centric. AI chose flat API over type hierarchy.
The results were better.

**The spawn protocol emerged:** A pattern for handing off knowledge between
iterations — preserve analysis, extract seed, let the target make its own
structural decisions. Don't impose; inform.

---

## Continuation: spl4 (November 2025)

### Integration Iteration

spl4's job was clear from spl3's analysis: connect tools to API, add stored
metadata, build practical tooling.

### What spl4 Achieved

Eighteen projects. Eighty-nine tests. This was the proof of concept:

- **Protocol stack:** 37 operations across 13 protocols, uniform factory pattern
- **Eight implementation patterns (P1–P8):** Mechanically verifiable design rules
- **Cascading references:** Repository facet implemented with copy-on-write
- **Process standards formalised**
- **Self-hosting:** Tools built in spl4 helped build spl4
- **Git as substrate:** Version control as part of the system, not outside it

The protocol stack:
```
mc.xpath → mc.core → mc.raw → (mc.data, mc.meta, mc.proto)
```

mc.core: five primitives (list, read, create, update, del) — stable foundation.
Everything else derived.

### Key Insights from spl4

**Patterns compound autonomy.** As P1–P8 were established and proven,
human intervention decreased progressively. The patterns taught the system
how to build itself.

**Autonomy target clarified:**
- Physical (structure, code, environments, testing, deployment): fully AI autonomous
- Logical (scope, meaning, design, direction): collaborative — and this is a feature, not a limitation

**Lifecycle model changed:** Not per-iteration but per-concern. Different
parts of the system develop at different rates — like organs in a body.
POC → Pilot → Production applied independently.

**Memory bloats.** Carrying implementation detail forward between iterations
causes bloat. Memory should orient, not catalogue. This is why each new
iteration rebuilds memory rather than inheriting it.

---

## Third AI Period: spl5 (February 2026 — Current)

### Another Reset

AI had evolved again. Another reset. But this time the learning was deeper.

Mission: Establish autonomous dev environments for protocols. Implement the
spawn protocol. Move from POC to Pilot.

### The Language-Centric Shift

This is where the software and the philosophy start to converge. spl5 reframes
the three pillars:

> Data (Mycelium) shaped by meaning (Splectrum) through creative action (HAICC).

The system is named Splectrum because **meaning is at the centre of everything.**
Not data platforms, not retrieval systems. A structured environment for working
with meaning.

### What spl5 Brings

**Spawn protocol formalised:** How one context seeds a new context. Critical
self-examination. Seed as information package, not template. Target makes own
structural decisions.

**Dev environment diversification:** From monolithic repo to autonomous,
self-sufficient repositories. Each concern develops at its own pace.

**Updated landscape (2026):** Context engineering now mainstream. Letta (MemGPT)
and Manus use agent-curated filesystem approaches. Splectrum's difference: formal
model, metadata as operational semantics, meaning as first-class concern.

**Refined operations:** Seven core operations (list, read, create, update, del,
move, copy). Cleaner than spl4's eight. Forty-one operations across fourteen
protocols total.

### The Philosophical Connection

spl5's framing makes the connection to the seed principle visible:

- **Record/context primitive:** Opaque — interpretation belongs to higher layers,
  where meaning lives
- **Metadata-driven behaviour:** Structure expresses intent
- **Natural language at logical level:** Requirements and quality gates in
  natural language
- **Point of view:** What you see depends on where you stand. Resources relative
  to position.
- **Cascading references:** Knowledge hierarchies controlled by AI — attention
  as a meaning concern
- **Focus over efficiency:** Tailoring context to task is a meaning concern,
  not an optimisation concern

These are not just software design decisions. They are the seed principle
expressed in code:
- Language is relational → the system's meaning emerges through interaction
- Languages are inter-relational → protocols compose, reference each other
- Together they form a web of growing complexity → the protocol stack grows
  through interaction density

---

## The Arc

| Iteration | Period | What it taught |
|-----------|--------|----------------|
| spl, spl1 | Pre-AI | The vision is real but too big for one person |
| spl2 | Jul 2025 | Don't build infrastructure first — start from meaning |
| spl3 | Nov 2025 | Let AI make technology decisions — practice beats theory |
| spl4 | Nov 2025 | Patterns compound autonomy — the system learns to build itself |
| spl5 | Feb 2026 | Meaning is central — data shaped by meaning through creative action |

The durability challenge remains. Each AI evolution forces adaptation. But the
direction — toward language, meaning, AI-friendly structure — has more staying
power than any specific implementation, precisely because it aligns with how
AI naturally works. And, not coincidentally, with the seed principle: language
is relational, and relation is how anything works.

---

## Material for Blog Posts

### The solo struggle
spl and spl1 — trying to build a cathedral alone. The vision was there. The
architecture was sound. Language was already central ("using my own words").
But one person cannot build what requires genuine collaboration. This is not
a story about inadequacy. It's a story about the nature of complex creation.

### The infrastructure trap
spl2 — the instinct to build infrastructure first. Containers, CLI tools,
module systems. Technology decisions that should have been the AI's domain.
The reframe: start from meaning, let technology fall out the bottom.

### The practice surprise
spl3 — what happens when you let AI make technology decisions. The planned
architecture (immutable lists, log-centric) gave way to something simpler
and better (record/context, context-centric). Theory said one thing;
practice said another. Practice was right.

### The compounding
spl4 — patterns that teach the system to build itself. Eighty-nine tests.
Self-hosting. The distinction between physical autonomy (AI's domain) and
logical collaboration (the feature, not the limitation).

### The convergence
spl5 — "meaning is at the centre of everything." The software and the
philosophy saying the same thing. Data shaped by meaning through creative
action. The seed principle expressed in code.

### The durability question
Six iterations. Three AI resets. How do you build something durable when your
partner keeps getting smarter? The answer emerging: build around language and
meaning, not around specific capabilities. The common layer that survives change.
