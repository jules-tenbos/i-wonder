---
layout: post
title: "The Physical/Logical Pivot"
date: 2026-06-02
labels: [mycelium, engineering, SPLectrum]
status: Mandatory review
---
<img src="https://plus.unsplash.com/premium_photo-1683133924436-a7afbdf8cd25?q=80&w=350&h=230&auto=format&fit=crop" alt="The Physical/Logical Pivot" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

There is a principle that keeps showing up. Not one we designed — one we found. The physical does not have to be the target. It has to be readable as the target. A schema does not have to match another schema. It has to be readable as that schema. A carrier does not have to be the meaning. It has to be readable as bearing that meaning. "Readable as" — not "is." That is the pivot between physical and logical, and it operates everywhere.

The fabric is woven from namespace trees. Every language that participates in the fabric gets its own namespace tree — its own way of organising identity, its own structure for naming what it knows. The three languages committed so far — AVRO, git, Kafka — are three such trees. But the principle is not limited to three. It extends to any language. Each tree is a namespace structure for a different concern, and the fabric is what holds them together.

Data at rest lives in the fabric tree. A navigable structure of dot-paths and nodes, with property bags at each level. Identity here is positional — where something sits in the tree determines what it is called and how it is reached. Git provides the history dimension: every state of the tree has a past, and that past is navigable. The tree is the landscape of data at rest — stable, addressable, structured.

Schema at rest is AVRO's domain. An AVRO schema assigns namespace to field names — that is its single role. Everything else follows from it. The schema defines what the data is at a given point in the tree: which fields, which types, which constraints. These are the fruits hanging from the fabric tree. You navigate the tree to find your location. The schema at that location tells you what you are looking at. Physical schemas, attached to the namespace structure at the points where conformance matters.

Data in motion is where Kafka and the protocol namespace enter. Streaming carries data between locations, between trees, between contexts. The Kafka record is the carrier — a container with headers, key, and value, moving through the fabric. The protocol and operator namespace organises what happens with that data: which operations, which record types, which dispatch. How schema travels with the data in motion is still taking shape — the design is open. What is clear is that motion has its own namespace tree, its own way of organising identity, distinct from rest.

The pivot between these trees is always the same principle. Can this data, structured by one tree, be read as what another tree expects? Schema resolution in AVRO is precisely this: reader schema asks whether the writer schema is readable as what the reader needs. The same test applies between the data tree and the schema tree, between rest and motion, between any two namespace structures. One principle, everywhere. Not a mapping table — a structural relationship between languages.

Where the pivot loses something, languages genuinely differ. Every transformation between languages — every "readable as" — has a loss profile. Some information does not survive the crossing. That is not failure. It is equal standing making itself visible. P4 — languages have equal standing in potential. That equal standing means no language is a superset of another. Each has its own territory, its own namespace tree, its own way of carving reality. The loss at the pivot is where that difference becomes concrete. And because languages are evolutionary — P5 — new trees will grow, new pivots will form, new loss profiles will emerge. The fabric does not need to anticipate them. It only needs the principle: readable as.

The fabric weaves namespace trees for different purposes. The pivot between them is one principle. The languages are finding each other.

<small>This post is part of the [mycelium series](/blog/label/mycelium). More in the <a href="/engineering/splectrum/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@gettyimages">Getty Images</a> / Unsplash</small>
