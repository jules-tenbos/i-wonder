---
title: "SPLectrum Engineering"
labels: [seed, engineering, SPLectrum]
status: review needed
---
<img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="SPLectrum engineering" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

In this post I am going to take a rather unusual step: use the SPLectrum philosophical framework as a first-principles approach to engineering. This post won't go very deep — it will peel off the first layer. You will notice that that on its own already has far-reaching consequences.

Before we go there, a few words on why this approach.<br/>
The SPLectrum seed principles talk about properties shared by all languages, what they have in common. The language scope is wide — that's why the framing is firmly philosophical.<br/>
SPLectrum engineering has an analytical side and an applied side. It deals with language as the way we think and live, and through engineering it aims to build that understanding into AI-collaborative solutions.<br/>
I am convinced that we are on the brink of another revolution akin to the industrial revolution. I call it the Decentralised Cognition Revolution — the rise of autonomous, person-extending AI tooling and the expansion of our cognition through the penetrative capacities of AI.

Let's do the round of the principles to peel off that layer.

***P0 — Being implies language***<br/>
I interpret this very much in the Heidegger way — *being is always already disclosed in the world* — and the Fichte way — *being comes into existence through the act of differentiation*. There is an entity in interaction with the world that surrounds it. This gives us three components: the **entity**, the **world**, and the relational between them, **language**.

***P1 — Language is relational***<br/>
Language as the relational medium that expresses the interaction — the self communicating with the other.

***P2 — Language is the medium through which a subject experiences reality***<br/>
With those three components in hand, we identify the entity with **subject** — the reference point for the relational — and the totality of interaction as **reality**. Real to the subject is what flows through the relational (no hidden stuff). Experience is reality as specific to the subject's reference point.

***P3 — Language is where subjects share knowledge about reality***<br/>
Knowledge is informational bits of reality. Through language interaction, subjects create units of sameness across their separate realities — shared reality, what we feel we have in common. Shared reality is never equal to any subject's experienced reality. It is consensus reality.<br/>
And here it gets interesting: consensus reality has sameness across all participating subjects. It is the effective reality of the group — and the group, through that consensus, becomes a separate entity. A being in its own right.

***P4 — Languages are inter-relational and have equal standing in potential***<br/>
Languages relate in many ways — as versions of each other, as compositions, as decompositions — but none ranks above another. Binary has the full computational power; Python has the clarity; natural language has the ambiguity. Equal standing in potential means no language is inherently superior. The hierarchy we impose is practical, not structural.

***P5 — Together they form a web of growing complexity***<br/>
Think of it as the entropy law of the relational: interaction increases the complexity of interrelation. This is driven by **historicity**. More languages, more connections, more ways of expressing what was always there. The web grows through use — not by adding power, but by adding articulation.

The bold terms are those I want to carry forward into the engineering. The next question is: what design pattern is a good candidate to express the structures described above, and at the same time create a human-AI friendly collaboration environment? The structure I am going to propose came about organically, prototyped in the spl repositories. The principles of the seed actually materialised when my philosophical endeavours joined up with the software engineering.

The design that follows lives in the logical space. It describes how a SPLectrum system must look — not how it must be physically built. Physical implementations are free to use whatever technology fits, as long as they are compatible with the logical design. Compatibility, not literal translation. Physical implementation is JIT — it goes only as far as capability requires. The logical design is complete; the physical emerges through use. This is not MVP with a roadmap, presuming a known target. It is materialisation through actual need.

I propose a three-pillar design: **mycelium — splectrum — HAICC**<br/>
***Mycelium*** — the data fabric, holding data entities and the data world they sit in.<br/>
***SPLectrum*** — the language fabric, supplying the protocols that act on data state. The pillar takes the project's name because language is the project's central concern.<br/>
***HAICC*** — the process fabric, where humans and AI collaborate as peers. **HAICC** stands for Human-AI Creative Collaboration.

***Mycelium*** is the fabric that expresses the world in data. Each data owner has a local tree of data nodes — their own data state. The fabric is what connects these local trees: references that address nodes across repositories, and data state propagation that carries change between owners. Decentralised at the data level: no central database, no single source of truth.

***SPLectrum*** is the language fabric. Protocols are software APIs with meaning constraint; operators are their methods; personas are compositions of protocols that take on roles. Protocols and personas are colocated as metadata with the data nodes they act on, in mycelium. P1 (relational): protocols as language games. P2 (medium of experience): meaning anchored to the data owner's point of view. P3 (sharing knowledge): visibility is sharing — no separate mechanism, what is visible is what is (potentially) shared. P4 (equal standing): no imposed hierarchy between protocols. P5 (growing complexity): complexity through diversification, not centralisation. Natural language as the carrier — AI makes this operational. Ambiguity at the fringes is generative — Derrida's insight applied to engineering.

***HAICC*** is the process fabric. Process definitions, watcher expressions, readiness schemas — colocated as metadata in mycelium. Processes trigger on data state change. Personas declare required capabilities; conformance against available human and AI capabilities determines the division of work. Conscious is what is in focus; subconscious is what supports it; through practice, capabilities move between the two — that movement is learning, architecturally native. The neuroscience grounding — Neural Darwinism, Global Workspace Theory, predictive processing — is not metaphor; it is structural correspondence in a different medium.

What has this first-principles approach yielded? A unified approach to the three main components of a SPLectrum system — state, meaning, and process — expressed as three fabrics. Mycelium as the data fabric: visible state, no hidden stuff. SPLectrum as the language fabric: structured meaning we can reason about. HAICC as the process fabric: triggers, flow, persona-driven work division.

Decentralisation is an upfront property, not an afterthought. Mycelium is decentralised at the data level. HAICC is decentralised at the process level — human and AI agents as collaborative peers, no central controller. SPLectrum as the language fabric is what makes both decentralisations coherent — equal standing all the way through. P4 expressed as architecture.

The relationship between this engineering and the seed is itself an instance of what the seed describes: two languages with equal standing, neither governing the other. The quality gate is low friction at the boundary — conformance, not perfection. You don't need an external judge; you feel the friction when it's there. A reader schema against data, a watcher expression against data state, the philosophy against the engineering — the same pattern, instances all the way down.

The aim is not to replace traditional solution design patterns. It is to sandwich a decentralised cognition layer in between — a SPLectrum-specific layer with its own vocabulary, sitting between the philosophical framework above and the traditional engineering patterns below. In subsequent posts I will go into more detail about each pillar — and the question that follows naturally: what do you build when you honour these constraints?

<small>This post is part of the [seed series](/blog/label/seed). More on SPLectrum engineering in the <a href="/engineering/">engineering area of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@christopher__burns">Christopher Burns</a> / Unsplash</small>
