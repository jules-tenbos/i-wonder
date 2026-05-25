---
layout: default
lastmod: 2026-05-25
title: "CAS — Methodologies"
description: "The methodologies of complex adaptive systems research — agent-based modeling, genetic algorithms, network analysis, generative simulation."
---

[Home](/) > [Positioning](/positioning/) > [Subjects](/positioning/subjects/) > [Complex Adaptive Systems](/positioning/subjects/c/complex-adaptive-systems/) > Methodologies

# Methodologies

CAS's methodological signature is bottom-up modeling rather than top-down derivation. Where classical approaches write equations for aggregate behaviour and solve for equilibria, CAS specifies the micro-level — agents, rules, interaction topology — and observes what the macro-level produces. The four methods below share this orientation.

---

## Agent-based modeling

The tradition's signature method. The modeler specifies agents, their internal rules, and the structure of their interactions; global behaviour is observed rather than derived. The epistemic stance is distinctive: model the micro, observe the macro, and treat the gap between them as the phenomenon to be explained.

Key models that shaped the tradition: [Thomas Schelling](/positioning/persons/s/schelling/)'s segregation model (1971) showed that mild individual preferences for similar neighbours produce stark macro-level segregation — a canonical demonstration that individual intentions do not predict aggregate outcomes. [Robert Axelrod](/positioning/persons/a/axelrod/)'s iterated prisoner's dilemma tournaments showed how cooperation can emerge and sustain itself among self-interested agents without central enforcement. Epstein and Axtell's Sugarscape (1996) modeled entire artificial societies — agents gathering resources, trading, migrating, reproducing — to study how wealth distributions, cultural boundaries, and conflict arise from simple behavioural rules. Holland's Echo system explored the dynamics of evolving ecological communities.

The tools landscape reflects the method's computational character. [NetLogo](https://en.wikipedia.org/wiki/NetLogo) is the standard teaching and prototyping environment. [Repast](https://en.wikipedia.org/wiki/Repast_(modeling_toolkit)), [MASON](https://en.wikipedia.org/wiki/MASON_(Java)), and [Mesa](https://en.wikipedia.org/wiki/Mesa_(agent-based_modeling)) (Python) serve larger-scale research models. The common pattern: define agents, define interaction rules, run, observe, vary parameters, compare.

---

## Genetic algorithms and evolutionary computation

Holland's original framework, developed from the 1960s at Michigan and formalised in *Adaptation in Natural and Artificial Systems* (1975). The mechanism: a population of candidate solutions, each represented as a string of symbols. Fitness is evaluated; fitter individuals are selected for reproduction. Crossover recombines parts of two parent strings into offspring. Mutation introduces random variation. Across generations, the population explores the solution space and converges toward high-fitness regions.

The schema theorem provides the theoretical account: short, low-order schemata (building blocks) of above-average fitness receive exponentially increasing representation in the population. The power of the genetic algorithm lies in implicit parallelism — many schemata are being tested simultaneously within each generation.

Genetic algorithms sit within a broader evolutionary computation landscape. Genetic programming (Koza) evolves programs rather than fixed-length strings. Evolution strategies (Rechenberg, Schwefel) emphasise real-valued parameters and self-adaptive mutation. All share the variation-and-selection mechanism; they differ in representation and operator design.

---

## Network analysis

Agents and their interactions treated as graph structures — nodes and edges. The graph-theoretic toolkit provides measures for connectivity, clustering, centrality, path length, and community structure. Three network types carry most of the CAS-relevant work.

Random networks ([Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s)–[Rényi](https://en.wikipedia.org/wiki/Alfr%C3%A9d_R%C3%A9nyi)) connect nodes with uniform probability. They serve as baselines — what network properties look like when there is no organising principle. Small-world networks ([Watts](https://en.wikipedia.org/wiki/Duncan_J._Watts) and [Strogatz](https://en.wikipedia.org/wiki/Steven_Strogatz), 1998) show that a few long-range links in an otherwise local network drastically reduce path lengths while preserving clustering — the "six degrees" phenomenon. Scale-free networks ([Barabási](/positioning/persons/b/barabasi/) and Albert, 1999) have degree distributions following a power law — most nodes have few connections, a few hubs have many. Preferential attachment generates the pattern: new nodes connect preferentially to already-well-connected nodes.

CAS's specific contribution to network analysis is the adaptive network — networks whose topology changes as agents interact. Links form, strengthen, weaken, and break in response to agents' strategies. The network is not a fixed scaffold on which dynamics play out; it coevolves with the dynamics.

---

## Computer simulation and the generative stance

CAS simulation is typically generative rather than predictive. The goal is to show how a pattern *can* arise from specified micro-level conditions — not to forecast what *will* happen in a specific case. Epstein's formulation: "If you didn't grow it, you didn't explain it." The generative sufficiency test: can the model produce the target macro-pattern from plausible micro-specifications?

This stance is sometimes criticised as unfalsifiable — if the model is not predicting, what would count as failure? The response from within the tradition: generative models are tested by whether they reproduce qualitative patterns (fat-tailed distributions, phase transitions, clustering) under robust parameter ranges, not by point predictions. Sensitivity analysis, parameter sweeps, and replication across platforms serve as the verification toolkit. The deeper claim is that for non-linear, path-dependent systems, point prediction is the wrong standard — the appropriate question is what class of outcomes the micro-level conditions can produce.

Validation remains an open problem. Agent-based models can be calibrated against empirical data, but the many-to-one mapping from micro-specifications to macro-patterns means multiple models can produce the same target pattern. The tradition generally treats this as a feature of the subject matter rather than a methodological defect — but the debate is live.
