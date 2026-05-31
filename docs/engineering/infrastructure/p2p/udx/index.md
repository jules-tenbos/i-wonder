---
layout: default
lastmod: 2026-05-31
title: "UDX"
description: "UDX is the bottom transport layer — reliable, multiplexed, congestion-controlled streams over raw UDP, with no handshake and no encryption by design."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > UDX

# UDX

UDX is the **bottom transport layer**: reliable, multiplexed, congestion-controlled streams over raw UDP — with **no handshake and no encryption**, by design. It is pure transport for peer-to-peer use; everything above rides on it. Encryption is added by [secret-stream](/engineering/infrastructure/p2p/secret-stream/) / [HyperDHT](/engineering/infrastructure/p2p/hyperdht/), not here. Packaged as a native addon (`libudx`) with a JS API.

---

## Core API

See the [README](https://github.com/holepunchto/udx-native) for exhaustive detail.

### Create

- `const udx = new UDX()`.

### Sockets

- `const socket = udx.createSocket([opts])`.
- `socket.bind([port], [host])`.
- `await socket.send(buffer, port, [host])`.
- `socket.on('message', (msg, from) => { ... })`.

### Streams

- `const stream = udx.createStream(id, [opts])` — `opts` include `firewall`, **`framed`**, `seq`.
- `stream.connect(socket, remoteId, port, [host])`.
- `await stream.changeRemote(remoteId, port, [host])` — migrate the path (mobility / NAT rebinding).
- `stream.relayTo(destination)` — relay path (the relay-fallback case).
- Events: `connect`, `data`, `end`, `close`, `remote-changed`, `mtu-exceeded`.
- Telemetry: `stream.mtu`, `stream.rtt`, `stream.cwnd`, `stream.inflight`.

### Utilities

- `udx.networkInterfaces()` / `udx.watchNetworkInterfaces(cb)` / `await udx.lookup(host)`.

---

## Gotchas

> **Version / dist-tag trap — read before you install.** `npm i udx-native` installs **`latest` = 1.19.2 — the *older* line**. The active development line is published under **`next` (1.20.x)**, and the repo README documents *that* newer API (`changeRemote`, `relayTo`, `framed`) — so the README and a default install **mismatch**. There is no caveat upstream. **Pin `@next` or an exact version**, and re-check `npm view udx-native dist-tags`.

**No encryption at this layer.** Confidentiality is entirely the job of the layers above (secret-stream / HyperDHT). Don't send anything sensitive over a raw UDX stream.

**`framed: true` makes a stream message-boundary-preserving** — that is what lets [protomux](/engineering/infrastructure/p2p/protomux/) run over UDX without an extra length-prefix layer.

**Native build.** It is a native addon, so it needs the platform prebuild — relevant when targeting Bare/Pear.

---

## Version

`udx-native` — `latest` is **1.19.2** (the older line); the current line is `next` (**1.20.x**). Use `@next` or pin exactly, and check the npm registry. See the dist-tag gotcha above.

## Sources
- Repo: [github.com/holepunchto/udx-native](https://github.com/holepunchto/udx-native) (README on `main` = the authoritative reference)
- npm: `udx-native` (check `dist-tags` — `latest` ≠ the active line)
