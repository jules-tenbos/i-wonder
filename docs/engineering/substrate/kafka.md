---
layout: default
lastmod: 2026-05-29
title: "Kafka"
---

[Home](/) > [Engineering](/engineering/) > [Substrate](/engineering/substrate/) > Kafka

# Kafka

Kafka is the committed language of mobility — the envelope for data in motion. It is one of the four committed substrate languages — structure ([AVRO](/engineering/substrate/avro/)), historicity ([Git](/engineering/substrate/git/)), addressing ([XPath/URI](/engineering/substrate/addressing/)), mobility (Kafka) — each a grammar the architecture conforms to rather than invents. The commitment here is specifically to Kafka's record — its envelope for data leaving the tree — not to its topic/partition/broker machinery, which is Kafka's own. For Kafka the system — the log, partitions, the cluster, the ecosystem — see the [Kafka subject](/positioning/subjects/k/kafka/); this page is the commitment and the role it plays.

## The record is the mobility envelope

A record carries what a datum needs to leave the tree and travel self-sufficiently: a key (identity, addressable outside the tree), a value (the payload, opaque to the envelope), headers (the context ancestry used to give it, now carried explicitly), an offset (order of arrival — always a fact, whether or not order matters to the content), and a timestamp (the moment of extraction, itself a datum). Identity, context, arrival order, time, self-description — the structural requirements for data in motion.

## Data at rest, data in motion

In the tree, data is at rest: its context comes from position and ancestry, with no motion envelope. Extracted into a record, it is in motion: the context ancestry gave it now travels explicitly in the headers. The record is the form data takes when it leaves the tree to move.

## Indifferent to scale

The record doesn't know whether its value is four bytes or an entire subject reality; the grammar is the same at every magnitude. So replicating, migrating, or cloning a whole reality between nodes needs no special protocol — a reality travelling is a record, and records can contain realities that contain records.

## Atomic

A record is a self-contained extracted datum; it carries no structural cross-references. Relationships live in the tree; if linkage must travel, it goes in the headers by deliberate choice. The relational structure stays at rest; the extraction moves.
