---
layout: default
lastmod: 2026-05-31
title: "protomux"
description: "protomux multiplexes several message-oriented protocols over one stream — channels, messages, compact-encoding, cork/uncork batching."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > protomux

# protomux

protomux **multiplexes several message-oriented protocols over one stream** — it is how a single peer connection carries, say, Hypercore replication *and* an app protocol at once without separate sockets. It sits on top of an already-established (encrypted) connection and needs a **framed, message-preserving** stream underneath (a [UDX](/engineering/infrastructure/p2p/udx/) stream with `framed: true`, or a byte stream you have length-prefixed). Message encoding is done with **compact-encoding**, not JSON/AVRO.

---

## Core API

See the [README](https://github.com/holepunchto/protomux) for exhaustive detail.

- `const mux = new Protomux(stream, [opts])` — `stream` must be framed/message-preserving.
- `Protomux.from(stream | muxer)` — wrap a stream or reuse an existing muxer.
- `const channel = mux.createChannel({ protocol, id, handshake, unique, onopen, onclose, ondestroy })` — **returns `null`** if the channel should not open (duplicate, or remotely closed).
- `const message = channel.addMessage({ encoding, onmessage })`; `message.send(data)`.
- `channel.open([handshake])` / `channel.close()`.
- `mux.cork()` / `mux.uncork()` and `channel.cork()` / `channel.uncork()` — batch frames.

---

## Gotchas

**Needs a framed / message-preserving stream.** Message boundaries must be intact — with UDX use `framed: true`; over a raw byte stream you must length-prefix first.

**`createChannel` can return `null`** (duplicate, or the remote already closed it) — always null-check before using the channel.

**Encodings are compact-encoding (`c.*`), not JSON or AVRO.** Relevant for any cross-encoding boundary on our side, where the wire format is AVRO — there is a mapping to account for.

**`cork` / `uncork` batch frames** at both the muxer and channel level — easy to forget, and it costs throughput if you don't use it for bursts.

---

## Version

`protomux@3` — a single `latest` dist-tag, but actively moving. Check the npm registry before pinning. Pairs with the `compact-encoding` helper.

## Sources
- Docs: [docs.pears.com/helpers/protomux](https://docs.pears.com/helpers/protomux)
- Repo: [github.com/holepunchto/protomux](https://github.com/holepunchto/protomux) (README = the authoritative reference)
- npm: `protomux`
