# HAI-Co² — Dutta et al.

Working notes for a future **close-affinity** positioning piece.

**Paper:** Dutta, S., Kaufmann, T., Glavaš, G., Habernal, I., Kersting, K., Kreuter, F., Mezini, M., Gurevych, I., Hüllermeier, E., & Schütze, H. (2025). *Problem Solving Through Human–AI Preference-based Cooperation*. Computational Linguistics, 51(4), 1337 ff. [DOI: 10.1162/COLI.a.19](https://doi.org/10.1162/COLI.a.19). Published by MIT Press for the ACL; CC BY-NC-ND 4.0.
**Full text extract:** `hai-co-squared-paper.txt` (same directory).

Surfaced via a Google search for *HAICC* — the paper appeared near the top, proposing an independently-developed framework (HAI-Co²) for human-AI cooperative problem solving. The structural overlap with SPLectrum's HAICC is immediate; the purpose diverges.

## What the paper argues

Position paper proposing **HAI-Co² (Human-AI Co-Construction)** — a framework for cooperative problem-solving in expert domains (code, ML pipelines, math formalisations, related-work writing). Core claim: complex expert-domain problems are not solvable by autonomous AI and require genuine cooperation; cooperation must co-construct both the solution *and* the objective, because the goal is typically underspecified at the start and emerges through interaction.

Four defining characteristics:

1. **Expert-domain complexity.** Target is problems requiring an explicit construction space with abstraction hierarchy. Trivial problems and fully-specifiable problems are excluded.
2. **Solution co-construction** by human-AI team of **equal partners with complementary strengths**.
3. **Objective co-construction** via interactive preference learning. The utility function is latent, multidimensional, time-indexed, and itself evolves.
4. **Natural language as the main medium**, justified as a prerequisite for equal partnership (equal expressive capacity).

Formalisation (Section 3): construction space X with hierarchical sequence X_0, X_1, …, X_j linked by abstraction/refinement maps. Latent multidimensional utility u^t aggregated to scalar U^t, approximated by the agent as Û^t. Informational state I, policy π. Preference-based search via pairwise tournaments, edits, critiques, explicit instructions. Framework-level scaffolding, not a deployable algorithm — deliberately leaves neighbourhood structure and search operators open.

Open challenges named: dynamic user preferences (vs static RLHF), guardrails against **influenceable reward functions** (the AI manipulating the human's evolving objective), NLU in expert domains, long-horizon informational state, creativity-correctness tension, evaluation methodology for open-ended co-construction.

Small 14-participant study (Appendix 1) showing HAI-Co² prompting patterns outperform vanilla GPT-4 Turbo on preference adherence and iterative refinement.

## Resonance with HAICC

- **Human-AI cooperation as the paradigm**, explicitly against full automation.
- **Equal partners with complementary strengths** — their phrasing, almost word-for-word aligned.
- **Natural language as primary medium** justified *because it enables equality* — same move SPLectrum makes.
- **Protocol** as the structure governing query/response types on each side — sentence-level resonance with persona-as-protocol.
- **Objective is not pre-given but co-constructed** — aligns with SPLectrum's stance that meaning-making is not goal-execution.
- **Ethics-by-design** through continuous human participation.
- **Influenceable reward functions** as an explicit concern — adjacent material SPLectrum hasn't centred but that connects cleanly.

## Dissonance — the productive divergence

The structural overlap is genuine. The *telos* differs sharply.

**HAI-Co²** frames cooperation as **two cognitive subjects on a joint search**. The cognition is the pair; both contribute to the solution and the objective. Symmetric role structure. Durable cooperation is the goal.

**HAICC** is **role-differentiated**. The human is the cognitive subject; AI enacts **personas** that amplify the human's cognitive stream. Equal standing (P4), but not symmetric. The optimisation trajectory points toward **AI autonomy within its personas**, not toward shared cognition.

So "equal partners" means different things in the two frames:

- HAI-Co²: equal contributors to shared cognitive work.
- HAICC: equal in standing, role-differentiated, with a trajectory.

Other concrete divergences:

- HAI-Co² operates inside a **search-over-construction-space** metaphor with formal utility functions. HAICC uses language-games and personas, not utility maximisation.
- Their domain has **correctness criteria** (code, ML, math). HAICC is broader — meaning-making, writing, creative work — where correctness doesn't anchor the frame.
- HAI-Co² is a **dyad** (human + one AI agent). HAICC's frame is **decentralised cognition** across many subjects.
- No Wittgenstein, no language-game, no persona-as-role in their citations; nearest related-work is AIAD (De Peuter et al. 2023), Hybrid Intelligence (Akata et al. 2020), assistance games.
- **JIT implementation** is absent — they are happy to specify hierarchy, neighbourhood, utility aggregation explicitly and up front.

The paper doesn't connect itself to the complex-adaptive-systems or fitness-landscape literatures — those would be natural cousins (evolutionary search, search-based software engineering, Kauffman's NK landscapes). Naming the connection is something the positioning piece can do.

## Submission angle

*"Same structure, different purpose."*

HAI-Co² and HAICC independently arrive at cooperation-as-equal-partners-through-natural-language as the paradigm for complex problem solving. They agree on what cooperation looks like in the interim. They diverge on where it is going — HAI-Co² treats durable symmetric cooperation as the goal; HAICC treats cooperation as the mechanism by which AI autonomy grows *within personas* while amplifying human cognitive reach.

A sharper formulation: **HAI-Co² sees the pair as the cognitive subject. HAICC keeps the human as the cognitive subject and builds AI as its amplifying infrastructure.**

The paper also helps clarify HAICC's own commitments by showing what the symmetric alternative looks like — the structural choice becomes visible by seeing the fork.

## Path if taken up

`positioning/close-affinity/haicc/hai-co-squared.md` — naming the piece after their own framework. The first piece in a close-affinity/haicc sub-area (likely a growth area as other AI-collaboration frameworks surface).

## Open threads

- **Preference-based learning literature** (Fürnkranz, Hüllermeier; the latter is co-author here) — potentially its own positioning thread regardless of HAI-Co².
- **AIAD** (De Peuter et al. 2023), **Hybrid Intelligence** (Akata et al. 2020), **assistance games** (Hadfield-Menell, Laidlaw) — the frameworks HAI-Co² positions itself against. Each is a candidate independent positioning thread.
- **Influenceable reward functions** — the ethical concern deserves its own treatment. Relevant beyond this paper.
- **Complex-adaptive-systems framing** of HAI-Co² — naming the connection explicitly is work the positioning piece can do, since the paper itself doesn't.
