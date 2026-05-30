---
layout: default
lastmod: 2026-05-29
title: "Git"
description: "Git is the committed substrate language of historicity, recording time as a content-addressed DAG of commits for decentralised, verifiable exchange."
---

[Home](/) > [Engineering](/engineering/) > [Substrate](/engineering/substrate/) > Git

# Git

Git is the committed language of historicity — it gives the architecture its sense of time. It is one of the four committed substrate languages: structure ([AVRO](/engineering/substrate/avro/)), historicity (Git), addressing ([XPath/URI](/engineering/substrate/addressing/)), and mobility ([Kafka](/engineering/substrate/kafka/)). For Git on its own terms — the object model, refs and branching, the distributed model, the ecosystem — see the [Git subject](/positioning/subjects/g/git/); this page is the commitment and the role it plays.

## Time as causality, not sequence

Git records history as a directed acyclic graph of commits: each state names the states it came from. Time in the architecture is this lineage — what derived from what — not a clock-ordered list. Branching and merging are first-class, so divergence and reconvergence are part of the record, not anomalies in it.

## Integrity and identity by content-addressing

Every object is named by the hash of its content, and a commit's identity includes the whole history behind it. A state cannot be altered without changing its name; integrity and identity are intrinsic to the model, not conferred by an authority — the historicity counterpart to AVRO's content-addressing of structure.

## Decentralised exchange

Every repository is complete — its full history, operational on its own — and exchange between repositories is peer-to-peer, with no privileged central copy. This is what makes Git the right historicity language for a decentralised architecture with no central controller: realities can diverge, work independently, and reconverge, each carrying and able to verify its own history. It also gives a hard, content-addressed boundary around a state-with-history — the clean edge between one reality and another.
