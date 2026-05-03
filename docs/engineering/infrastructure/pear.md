---
title: "Pear"
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > Pear

# Pear

Pear is Holepunch's peer-to-peer application platform. It provides the runtime and distribution layer for fully peer-to-peer applications — no servers, no app stores. Applications are discovered, distributed, and updated directly between peers.

**Source:** https://github.com/holepunchto/pear
**Docs:** https://docs.pear.sh

---

## What Pear Is

Pear is built on top of the [Bare](/engineering/infrastructure/bare/) runtime and the Holepunch stack. It adds application lifecycle management — staging, seeding, running — on top of Bare's minimal JavaScript runtime, and peer-to-peer networking on top of Holepunch's core libraries.

A Pear application is a directory with an `index.js` (or `index.html` for desktop GUI apps) and a `package.json`. Pear stages it into a Hypercore (an append-only log), producing a key. Anyone with the key can run the application directly from the swarm — no download, no install, no central server.

## Key Components

Pear uses the Holepunch stack for its peer-to-peer layer:

- **Hypercore** — append-only log. The storage primitive. Immutable, replicable, identified by a public key.
- **Hyperbee** — B-tree index on top of a Hypercore. Key-value storage with sorted iteration.
- **Hyperswarm** — peer discovery and connection. Topic-based: peers announce and look up topics (usually derived from a Hypercore key). Connections are end-to-end encrypted via the Noise protocol.
- **Hyperdrive** — file system on top of Hypercores. Used by Pear for application distribution.
- **Corestore** — manages multiple Hypercores. One storage backend, many cores.

## Application Types

- **Terminal apps** — run in the Bare runtime. No GUI. Headless services, CLI tools, daemons.
- **Desktop apps** — run in a Chromium-based webview backed by Bare. HTML/CSS/JS frontend with full access to the Bare runtime via `pear.api`.

## Identity

Identity in Pear is cryptographic. A Hypercore is identified by its public key (ed25519). Applications are identified by the key of the Hyperdrive they're staged to. There is no username, no account, no registry — just keys.

Peers connecting through Hyperswarm authenticate via the Noise protocol handshake. The connection is encrypted and the remote peer's identity is the public key used in the handshake.

## Application Lifecycle

1. **`pear stage`** — bundles the application into a Hyperdrive and produces a key.
2. **`pear seed`** — makes the application available on the swarm.
3. **`pear run pear://<key>`** — runs the application from the swarm. If not locally available, it's fetched from peers.

Updates propagate through the same mechanism: stage a new version, seed it, and peers running the application pick up the update.
