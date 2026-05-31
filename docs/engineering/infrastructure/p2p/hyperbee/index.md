---
layout: default
lastmod: 2026-05-31
title: "Hyperbee"
description: "Hyperbee is an append-only B-tree on a single Hypercore — sorted key-value storage with range queries, atomic batches, sub-databases, and diff streams."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > Hyperbee

# Hyperbee

Hyperbee is an **append-only B-tree** — a sorted key/value store running on a **single Hypercore**. It gives sorted iteration, range queries, atomic batches, and history/diff streams, plus cheap sub-namespaces. It is the index and metadata layer of the family: **Hyperdrive uses a Hyperbee** for its file metadata, and it is the common materialised-view type for **Autobase**.

---

## Core API

See the [README](https://github.com/holepunchto/hyperbee) for exhaustive detail.

### Create

```js
const db = new Hyperbee(core, [options])
```

`core` is a Hypercore. `options` includes `keyEncoding` and `valueEncoding` (`'binary'` | `'utf-8'` | `'ascii'` | `'json'` | an abstract-encoding; default binary).

```js
const db = new Hyperbee(core, { keyEncoding: 'utf-8', valueEncoding: 'json' })
await db.put('a', { hello: 'world' })
const { value } = await db.get('a')
```

### Read & write

- `await db.put(key, [value], [opts])` / `await db.del(key, [opts])`.
- `const node = await db.get(key)` — `{ seq, key, value }`, or `null`.
- `await db.peek([range], [opts])` — first entry in a range.

### Streams

- `db.createReadStream([range], [opts])` — `gt` / `gte` / `lt` / `lte`, `limit`, `reverse`.
- `db.createHistoryStream([opts])` — every put/del in insertion order.
- `db.createDiffStream(otherVersion, [opts])` — changes between two versions.

### Sub-databases, versions, batches

- `const sub = db.sub('prefix', [opts])` — a namespaced sub-database.
- `db.checkout(version)` / `db.snapshot()` — read-only view at a version / at the current `db.version`.
- `db.version` — a monotonically increasing modification counter.
- `const batch = db.batch()` … `await batch.flush()` — atomic multi-op.
- `await db.getAndWatch(key)` / `db.watch([range])` — reactive watchers.

---

## Gotchas

**`sub()` is byte-prefix namespacing, not isolation.** Sibling sub-DBs share the one underlying core and the one `version` counter, and a `createDiffStream` reflects changes across all of them. Good for organising keys; not an access-control boundary.

**`db.version` is Hyperbee's own counter**, and it is the point-in-time handle you pass to `checkout()` / `createDiffStream()`. Don't conflate it with the underlying core's `length`.

**Long-lived read streams hold a checkout implicitly**, which pins storage — close them when done.

---

## Version

`hyperbee@2` — a stable API (the family's storage churn is in the Hypercore backend beneath it, not in Hyperbee's surface). Check the npm registry before pinning.

## Sources
- Docs: [docs.pears.com/building-blocks/hyperbee](https://docs.pears.com/building-blocks/hyperbee)
- Repo: [github.com/holepunchto/hyperbee](https://github.com/holepunchto/hyperbee) (README = the authoritative API reference)
- npm: `hyperbee`
