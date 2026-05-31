---
layout: default
lastmod: 2026-05-31
title: "HyperDHT"
description: "HyperDHT is the Kademlia DHT powering Holepunch networking — topic-based discovery, distributed UDP hole-punching, and Noise-encrypted connections by key."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > HyperDHT

# HyperDHT

HyperDHT is the **Kademlia DHT** that powers Holepunch networking: peer **discovery** by topic plus **distributed UDP hole-punching**, running its transport over [UDX](/engineering/infrastructure/p2p/udx/). The crucial idea: **you connect to an Ed25519 public key, not an IP address** — the DHT locates the peer and punches through. Connections it hands you are **already Noise-encrypted**. [Hyperswarm](/engineering/infrastructure/p2p/hyperswarm/) wraps HyperDHT with a friendlier topic/connection API; reach for HyperDHT directly when you want the lower-level control.

---

## Core API

See the [README](https://github.com/holepunchto/hyperdht) for exhaustive detail.

### Create + identity

- `const node = new DHT([options])` — `options`: `bootstrap`, `keyPair`, `seed`, `connectionKeepAlive`, `randomPunchInterval`.
- `const keyPair = DHT.keyPair([seed])` — `{ publicKey, secretKey }` (Ed25519).

### Server (accept connections)

- `const server = node.createServer([opts], [onconnection])`.
- `await server.listen(keyPair)` — the key pair **is** your connectable address.
- `server.on('connection', socket => { ... })` — `socket` is Noise-encrypted.
- `server.address()` → `{ host, port, publicKey }`.

### Client (dial)

- `const socket = node.connect(remotePublicKey, [opts])` — connect by key; the DHT does the locating + hole-punch.

### Discovery

- `node.lookup(topic)` — find announcers of a 32-byte topic (a stream).
- `node.announce(topic, keyPair, [relayAddresses])` / `node.unannounce(topic, keyPair)`.

### DHT records (BEP44-style)

- `await node.immutablePut(value)` → `{ hash }` / `await node.immutableGet(hash)`.
- `await node.mutablePut(keyPair, value)` / `await node.mutableGet(publicKey, [opts])`.

### Run your own bootstrap

- `DHT.bootstrapper(port, host, [opts])`.

---

## How it works

**Topic-based discovery.** A topic is a **32-byte buffer** (commonly a hash of an app name or a core's key). `announce` stores your connectable info under the topic in the DHT; `lookup` queries for announcers and you dial each. Many peers on one topic form a swarm.

**UDP hole-punching.** Peers rarely have public addresses, so a DHT node acts as a **rendezvous**: it observes each peer's external IP:port (its NAT mapping), then both peers fire UDP packets at each other simultaneously so each opens its own NAT mapping for the other's inbound packet. Works for cone NATs; **symmetric NAT defeats it** (the external port changes per destination) and the system **falls back to relaying**. The exact algorithm is not specified in the README — this page gives the model; the step-by-step and real-world success across NAT types is a future deep-dive subpage.

**Public vs private DHT.** By default a node joins the public network via Holepunch's bootstrap nodes (`node1/2/3.hyperdht.org:49737`). Pass `bootstrap: [...]` to point at your own, and run one with `DHT.bootstrapper(...)`. A **private DHT** suits closed/enterprise deployments, deterministic test environments, or not depending on third-party infra.

**Noise encryption.** Every connection is Noise-encrypted by default (pattern XX). Because the **Ed25519 key is both identity and address**, cryptographic identity and network address are the same object — you `connect(remotePublicKey)` and `listen(keyPair)`.

---

## Gotchas

**You connect to a key, not an address** — no IP/port in `connect()`; the DHT resolves and punches. Connections are Noise-encrypted by default — don't wrap them again.

**`remotePublicKey` isn't trustworthy until the connection opens.**

**Hole-punch is best-effort** — symmetric NAT fails over to relay; tune `randomPunchInterval` / `connectionKeepAlive` for mobile/aggressive NATs (defaults govern NAT-mapping survival).

---

## Version

`hyperdht@6` (single `latest` dist-tag — no trap here). Check the npm registry before pinning.

## Sources
- Docs: [docs.pears.com/building-blocks/hyperdht](https://docs.pears.com/building-blocks/hyperdht)
- Repo: [github.com/holepunchto/hyperdht](https://github.com/holepunchto/hyperdht) (README on `main` = the authoritative API reference)
- npm: `hyperdht`
