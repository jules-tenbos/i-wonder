---
layout: default
lastmod: 2026-05-31
title: "blind-peering"
description: "blind-peering is the client side of availability — registers your Hypercores and Autobases with always-on blind mirrors that replicate in your absence."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > blind-peering

# blind-peering

blind-peering is the **peer-side client** for keeping your data available when you are offline: it registers your Hypercores and Autobases (via RPC) with always-on **"blind peers" (mirrors)** that replicate and serve them in your absence. It is the *requester* side — you supply the mirror keys; it does not run a mirror itself. Built with a [Corestore](/engineering/infrastructure/p2p/corestore/) + [HyperDHT](/engineering/infrastructure/p2p/hyperdht/). It is the availability/pinning path — a sibling to [seeders](/engineering/infrastructure/p2p/seeders/) (which uses an authorised seeder swarm instead of blind-peer RPC).

---

## Core API

See the [README](https://github.com/holepunchto/blind-peering) for exhaustive detail.

- `const bp = new BlindPeering(dht, store, { keys, suspended, wakeup })` — `keys` is the list of blind-peer (mirror) keys.
- `await bp.addCore(core, [opts])` / `bp.addCoreBackground(core, [opts])` — register a core (the `Background` form is fire-and-forget).
- `await bp.addAutobase(base, [opts])` / `bp.addAutobaseBackground(base, [opts])`.
- `await bp.suspend()` / `await bp.resume()` / `await bp.close()`.

Mirror selection is by **XOR distance** to a `target` key (`opts.target` lets you pin / load-balance). It interplays with a Wakeup object — `addAutobase` defaults its target to the autobase's `wakeupCapability.key`.

---

## Gotchas

**It is the requester side, not the mirror.** You provide the blind-peer keys (the always-on hosts); this module talks to them, it does not host data for others.

**The "blind" property (mirrors hold replicable data without the capability to read it) is architectural inference, not a documented guarantee** — it follows from cores being replicated by discovery key (and block-encryptable), but the README does not state it. (See the [security model](/engineering/infrastructure/p2p/security-model/).)

**v2 is recent** (the 2.x line landed early 2026) — check for v1→v2 API changes if you are following older material.

---

## Version

`blind-peering@2` (active, current). Package name matches the repo — no trap. Check the npm registry before pinning.

## Sources
- Repo: [github.com/holepunchto/blind-peering](https://github.com/holepunchto/blind-peering) (README = the authoritative reference; thin — constructor + methods)
- npm: `blind-peering`
