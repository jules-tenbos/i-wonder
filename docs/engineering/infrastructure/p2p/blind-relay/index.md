---
layout: default
lastmod: 2026-05-31
title: "blind-relay"
description: "blind-relay is a TURN-like fallback that forwards UDX stream messages between peers when direct hole-punching fails, without seeing the content."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > blind-relay

# blind-relay

blind-relay is the **TURN-like fallback** for peer connections that cannot be established directly — when hole-punching fails (e.g. symmetric NAT). A relay host accepts **pairing requests** from two peers and **forwards [UDX](/engineering/infrastructure/p2p/udx/) stream messages** between them over [protomux](/engineering/infrastructure/p2p/protomux/) channels. It carries *live peer traffic*; it does **not** store or pin data. Because the relayed bytes are the peers' already-encrypted UDX stream, the relay is "blind" to content. **Not to be confused with [dht-relay](/engineering/infrastructure/p2p/dht-relay/)** — that bridges the *DHT protocol* over TCP/WebSocket, a different job.

---

## How it works

See the [README](https://github.com/holepunchto/blind-relay) for specifics.

A relay host accepts `pair` requests; two peers that present matching pairing tokens get their UDX stream messages forwarded between them (TURN-style). `unpair` tears it down.

The README documents the **wire protocol** (the `pair` / `unpair` message fields), not a JS Server/Client API — treat it as the protocol reference; the integration surface is the relay role rather than a documented class.

---

## Gotchas

**The hole-punch-failure / symmetric-NAT use case is *implied*, not named.** The README frames it only as "similar to TURN" — it does not say "symmetric NAT" or "when hole-punching fails." That is the role, but it is our framing, not a README statement.

**"Blind = can't read content" is architectural inference**, not a documented guarantee — it follows from the relayed UDX stream being end-to-end encrypted, but the README does not state it. (See the [security model](/engineering/infrastructure/p2p/security-model/).)

**It relays streams, it does not store data** — distinct from [blind-peering](/engineering/infrastructure/p2p/blind-peering/) / [seeders](/engineering/infrastructure/p2p/seeders/) (availability) and from [dht-relay](/engineering/infrastructure/p2p/dht-relay/) (DHT bridging).

---

## Version

`blind-relay@1` (active, current — 1.x). Package name matches the repo — no trap. Check the npm registry before pinning.

## Sources
- Repo: [github.com/holepunchto/blind-relay](https://github.com/holepunchto/blind-relay) (README = the authoritative reference; documents the wire protocol, not a JS API)
- npm: `blind-relay`
