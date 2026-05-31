---
layout: default
lastmod: 2026-05-31
title: "P2P building blocks"
description: "The Hypercore storage family plus the networking, crypto, and availability primitives of the Holepunch peer-to-peer stack, usable on their own."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > P2P building blocks

# P2P building blocks

The distributed-data and networking primitives at the heart of the stack — the Hypercore family for storage, plus the networking, crypto, and availability layers built around it. These are usable directly, on their own: many projects depend on them without ever touching Pear.

## Storage
- [Hypercore](hypercore/) — append-only, secure log; the core primitive.
- [Hyperbee](hyperbee/) — B-tree key-value store on a Hypercore.
- [Hyperdrive](hyperdrive/) — file system over Hypercores.
- [Corestore](corestore/) — manages many Hypercores under one backend.
- [Autobase](autobase/) — multi-writer log built from many Hypercores.
- [Hyperblobs](hyperblobs/) — blob storage on a Hypercore.

## Networking & transport
- [HyperDHT](hyperdht/) — the distributed hash table peers find each other through.
- [Hyperswarm](hyperswarm/) — topic-based peer discovery and connection.
- [UDX](udx/) — fast UDP-based transport.
- [secret-stream](secret-stream/) — end-to-end encrypted Noise streams.
- [protomux](protomux/) — multiplexed protocol channels over one stream.

## Crypto & security
- [The key model](key-model/) — keypairs, discovery keys, and encryption keys.
- [The P2P security model](security-model/) — how trust and encryption work across the stack.

## Availability & relays
- [blind-peering](blind-peering/) — peers that replicate without reading content.
- [seeders](seeders/) — always-on availability for cores.
- [blind-relay](blind-relay/) — relays connections without seeing payloads.
- [dht-relay](dht-relay/) — reach the DHT from environments that can't speak it directly.

## Sources
- Docs: [docs.pears.com/building-blocks](https://docs.pears.com/building-blocks/)
- Repo: [github.com/holepunchto](https://github.com/holepunchto/)
