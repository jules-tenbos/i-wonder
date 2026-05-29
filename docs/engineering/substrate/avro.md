---
layout: default
lastmod: 2026-05-29
title: "AVRO"
---

[Home](/) > [Engineering](/engineering/) > [Substrate](/engineering/substrate/) > AVRO

# AVRO

AVRO is the committed language of structure — it articulates the shape of data. It is one of the four committed substrate languages: structure (AVRO), historicity ([Git](/engineering/substrate/git/)), addressing (XPath/URI), and mobility ([Kafka](/engineering/substrate/kafka/)). For AVRO on its own terms — schemas, encodings, the resolution rules, the type system, the ecosystem — see the [AVRO subject](/positioning/subjects/a/avro/); this page is the commitment and the role it plays.

## Conformance is discovered, not declared

AVRO reads a record by asking whether it can be read as a given type — the writer's schema reconciled with the reader's at the point of contact — not by an authority assigning it an identity. There is no schema registry: schemas are facts present in the fabric. Versioning follows — the question is whether a reader exists that can read the data, a discovery rather than a policy. This is what makes AVRO the right structure language for a relational, decentralised architecture with no hidden state and no central controller.

## Carrier and meaning are separate

The data schema is the carrier: it carries structure without committing to what the structure means. The namespace places that structure into a meaning context. AVRO's nominal gate — the name check before structural resolution — enforces the language commitment natively: the same bytes read under different names are different readings, not one datum reinterpreted.

## Physical and logical types — structure and capability on one identifier

A physical type carries data structure; a logical type declares functional capability. AVRO carries both on the same definition, so the structure language carries the shape of data together with the operations defined over it.
