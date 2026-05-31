---
layout: default
lastmod: 2026-05-31
title: "The P2P security model"
description: "What the Holepunch stack protects, what it leaves observable, and what it explicitly does not do — transport, content, metadata, and anonymity."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > The P2P security model

# The P2P security model

A faithful account of what the stack protects, what it leaves observable, and what it explicitly does *not* do. The honest summary: **transport encryption is strong and automatic; content-at-rest and network-metadata privacy are opt-in or limited; anonymity is not provided.** Built on the [key model](/engineering/infrastructure/p2p/key-model/).

---

## Two encryption layers

Don't conflate them.

**Transport (always on).** Every HyperDHT/Hyperswarm connection is end-to-end Noise-encrypted by default ([secret-stream](https://github.com/holepunchto/hyperswarm-secret-stream) — Noise XX, Ed25519, libsodium secretstream). You cannot turn it off; there is no plaintext connection mode.

**Block encryption (opt-in, off by default).** Hypercore content is encrypted at the block level *only* if you set an encryption key (`core.padding` is 0 otherwise). Unencrypted cores are readable by anyone who replicates them and holds the public key — content confidentiality from replicators is **not** automatic.

---

## Identity & access

Identity is an Ed25519 keypair, which is also the connectable address (you `connect(publicKey)` / `listen(keyPair)`). The discovery key (a hash of the public key) is what is advertised; the public key is not revealed to a peer until it proves it already knows it. (See the [key model](/engineering/infrastructure/p2p/key-model/).)

---

## What an observer can see

A party watching the DHT can collect announcers' **IP:port** and correlate activity by the **32-byte topic / discovery-key** hash (opaque, but a stable identifier anyone who knows the topic can use).

*Nuance:* addresses are not published to a freely-queryable public set; a peer reveals itself on a relayed Noise request, so it leaks its IP less often than a classic DHT would. Frame it as "discoverable to those who know the topic and the relay nodes involved," not "the whole swarm is enumerable by anyone."

---

## Traffic-analysis surface

Even with transport encryption, **block sizes** (padded only when block encryption is on), **timing**, and **connection metadata** remain observable. *This is architectural inference — upstream publishes no traffic-analysis statement either way.*

---

## Mitigations

**Private DHT / custom bootstrap** — run your own bootstrap nodes to limit who participates. Supported via the `bootstrap` option on [HyperDHT](/engineering/infrastructure/p2p/hyperdht/).

**Block encryption** — for content confidentiality + size padding.

*Our suggestion, not upstream guidance:* a VPN or overlay network as an additional layer. Holepunch explicitly leaves anonymity overlays to user-land.

---

## Known limitations

State these plainly — they are limitations, not features.

**No built-in anonymity / onion routing.** Upstream treats Tor/overlays as out of scope ("user land"), focused on throughput and stability.

**Privacy is an acknowledged open area, not a solved one.** [hyperdht #2](https://github.com/holepunchto/hyperdht/issues/2) ("secure and privacy preserving DHT") has been open since 2018; [#50](https://github.com/holepunchto/hyperdht/issues/50) was closed in 2021 with an explanation but no privacy feature shipped.

**No published formal threat model.** None exists in the docs or repos.

**No forward-secrecy or formal-verification claims.** Upstream does not claim either; even if Noise XX may provide forward secrecy as a property, it is not claimed.

---

## "Blind" infrastructure

Relays, seeders, and [blind-peers](https://github.com/holepunchto/blind-peering) operate on discovery keys and already-encrypted traffic, so they do not see content — the relayed bytes are the E2E-encrypted secret-stream, and blind-peers replicate Hypercore blocks by discovery key without the capability key.

*This is architectural inference, not a verbatim upstream guarantee.* The [blind-relay](https://github.com/holepunchto/blind-relay) and blind-peering READMEs describe the TURN-like relaying/availability role but do not state "cannot read content." Do not quote it as a guarantee.

---

## Key custody

*Our operational note — upstream docs do not give custody guidance.*

Identity and access are the keypair; lose it and you lose the ability to write or control the core. Treat the primary key (and Corestore's primary key, which derives all named cores) as the thing to back up.

## Sources
- Repo: [github.com/holepunchto/hyperdht](https://github.com/holepunchto/hyperdht) (README on `main`; issues [#2](https://github.com/holepunchto/hyperdht/issues/2) open, [#50](https://github.com/holepunchto/hyperdht/issues/50) closed)
- Repo: [github.com/holepunchto/hypercore](https://github.com/holepunchto/hypercore) (README — block `encryption`, `core.padding`)
- Repo: [github.com/holepunchto/hyperswarm-secret-stream](https://github.com/holepunchto/hyperswarm-secret-stream) (README — Noise/secretstream)
- Repo: [github.com/holepunchto/blind-relay](https://github.com/holepunchto/blind-relay) and [github.com/holepunchto/blind-peering](https://github.com/holepunchto/blind-peering) (the "blind" roles)
- npm: `hyperdht`, `hypercore`, `@hyperswarm/secret-stream`
