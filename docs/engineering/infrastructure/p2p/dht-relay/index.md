---
layout: default
lastmod: 2026-05-31
title: "dht-relay"
description: "dht-relay bridges the Hyperswarm DHT protocol over TCP or WebSocket so clients without UDP (e.g. browsers) can participate in the swarm. Experimental."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > dht-relay

# dht-relay

> **Experimental — do not use in production.** The README carries a verbatim warning: "This project is still experimental. Do not use it in production." It is sub-1.0. Treat accordingly.

dht-relay bridges the **Hyperswarm DHT protocol itself** over framed streams (TCP or WebSocket), so clients **without UDP** — e.g. browsers — can participate in the swarm at all. It is the structural **opposite of [blind-relay](/engineering/infrastructure/p2p/blind-relay/)**: dht-relay relays *the DHT protocol* (so you can reach the DHT without UDP); blind-relay relays *peer UDX streams* (a NAT/hole-punch fallback). Different jobs — don't conflate them.

---

## Core API

See the [README](https://github.com/holepunchto/hyperswarm-dht-relay) for exhaustive detail.

**Relaying side** (a node with a real UDP DHT): `relay(new DHT(), stream)`.

**Relayed side** (the client, over the framed stream): `const dht = new DHT(stream)` — then use it like a normal [HyperDHT](/engineering/infrastructure/p2p/hyperdht/) node.

**Transports:** TCP (uses secret-stream for framing + encryption) and WebSocket (native framing/encryption).

**CLI:** `dht-relay [--port 49443] [--host 0.0.0.0] [--cert] [--key] [--behind-proxy]`.

---

## Gotchas

**npm is well behind the repo.** `npm i @hyperswarm/dht-relay` installs **`0.4.3` (Oct 2023)**, while the repo has commits into late 2025 — so the *published* package is 2023-era code, even though the project is not dead. Pin knowingly; don't assume `latest` reflects current development.

**Not browser-only.** The WebSocket transport makes browsers the natural client, but the README positions it as "for everyone," not browser-only.

**Name trap.** Repo `holepunchto/hyperswarm-dht-relay`, package `@hyperswarm/dht-relay` — they don't match.

---

## Version

`@hyperswarm/dht-relay@0.4` — **experimental, sub-1.0**; npm `latest` is `0.4.3` (2023), the repo is newer. Check the npm registry and the repo before relying on it.

## Sources
- Repo: [github.com/holepunchto/hyperswarm-dht-relay](https://github.com/holepunchto/hyperswarm-dht-relay) (README = the authoritative reference; thorough — protocol + TCP/WS examples + CLI)
- npm: `@hyperswarm/dht-relay`
