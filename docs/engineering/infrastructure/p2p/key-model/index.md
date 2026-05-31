---
layout: default
lastmod: 2026-05-31
title: "The key model"
description: "Three distinct keys with distinct powers — public key (identity + address), discovery key (find peers), encryption key (content confidentiality)."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > The key model

# The key model

The whole stack names and secures data with **three distinct keys, each with distinct powers** — and the separation between them is the foundation of its privacy model: you can let peers *find* a core without giving them the ability to *read* it, and you can let infrastructure *store and serve* a core without it being able to *decrypt* the contents.

---

## The three keys

| Key | Derived from | Grants | What sharing it reveals |
|---|---|---|---|
| **Keypair / public key** (Ed25519) | random, or a seed | identity + the **connectable address** (`connect(publicKey)` / `listen(keyPair)`); verification of the log's signatures | the capability to verify — and to *read*, unless block encryption is on |
| **Discovery key** (BLAKE2b hash of the public key) | the public key (one-way) | find / announce peers on the DHT | network *presence* (who is in a swarm), but **not** the capability key or content |
| **Encryption key** (optional, separate) | independent | decrypt block contents (when block encryption is enabled) | content confidentiality |

**Public key = identity = address.** At the DHT you connect to a public key, not an IP — so cryptographic identity and network address are the same object. The public key also verifies the append-only log's signatures.

**Discovery key** is a one-way hash of the public key. You announce and look up peers under it, so the DHT layer learns the *discovery* key (and your IP/port) but never the public (capability) key. Holding the discovery key lets you find peers — it does **not** let you verify or decrypt.

**Encryption key** is separate again: with block encryption enabled, holding the public or discovery key still does not grant content decryption.

---

## What the split buys

Because announcement uses the one-way discovery key, the DHT (and anyone watching it) sees the discovery key + IP/port — **not** the capability key or the content. This is exactly what makes "blind" infrastructure possible: relays, seeders, and blind-peers operate on discovery keys and ciphertext, never on capability keys or plaintext. It is the strongest, most assertable privacy property in the stack. (See the [security model](/engineering/infrastructure/p2p/security-model/) for the full picture and its limits.)

---

## Gotchas / honest limits

**Block encryption is opt-in and separate.** Without it, a holder of the public key can read the content — confidentiality-at-rest/from-replicators is *not* automatic.

**The discovery key still reveals presence.** It does not leak the capability key, but it is a stable, correlatable identifier — an observer near it in the DHT keyspace can see who is announcing/looking up a given topic. (Not anonymity — see the [security model](/engineering/infrastructure/p2p/security-model/).)

## Sources
- Repo: [github.com/holepunchto/hypercore-crypto](https://github.com/holepunchto/hypercore-crypto) (README = the authoritative reference for `keyPair`, `discoveryKey`, sign/verify, namespacing)
- Draws on: [github.com/holepunchto/hypercore](https://github.com/holepunchto/hypercore) and [github.com/holepunchto/hyperdht](https://github.com/holepunchto/hyperdht) READMEs (public-key-as-address; the discovery-key property)
- npm: `hypercore-crypto`
