---
layout: default
lastmod: 2026-05-31
title: "seeders"
description: "seeders is the authorised-seeder availability tier — a swarm joined only with seed nodes named in a signed, spoof-proof mutable DHT record."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > seeders

# seeders

seeders is the **authorised-seeder** availability tier: a swarm you join only with seed nodes named in a **signed, spoof-proof list**. The list is a **signed mutable DHT record keyed by the first seed's public key**, so it cannot be forged and only its owner can update it; seeders advertise the seeded core's metadata (`length`, `fork`). It is the explicitly-authorised counterpart to [blind-peering](/engineering/infrastructure/p2p/blind-peering/)'s blind-mirror model — both keep data available, but seeders uses a curated, signed seed list rather than blind-peer RPC.

---

## Core API

See the [README](https://github.com/holepunchto/hyperswarm-seeders) for exhaustive detail.

- `const swarm = new Seeders(firstSeedPublicKey, [options])` — the first seed's public key keys the record.
- `swarm.on('connection', (conn) => { ... })`.
- `await swarm.join([record])` — the **owner** passes the seed-list record; non-owners join without it (read-only).
- `swarm.owner` — are you the record owner (i.e. hold the first-seed key)?

---

## Gotchas

**Ownership is key-bound.** Only the holder of the first-seed key can mutate the seed list; everyone else is a read-only joiner.

**Name trap.** Repo `holepunchto/hyperswarm-seeders` (branch `master`), package `@hyperswarm/seeders` — they don't match.

---

## Version

`@hyperswarm/seeders@1` — `latest` is 1.1.x, last published 2024; stable and functional, but not actively iterated. Check the npm registry before pinning.

## Sources
- Repo: [github.com/holepunchto/hyperswarm-seeders](https://github.com/holepunchto/hyperswarm-seeders) (README = the authoritative reference; branch `master`)
- npm: `@hyperswarm/seeders`
