---
layout: default
lastmod: 2026-05-31
title: "Hyperdrive"
description: "Hyperdrive is a secure, realtime, distributed filesystem — Hyperbee for metadata, Hyperblobs for content, backed by a Corestore."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > Hyperdrive

# Hyperdrive

Hyperdrive is a secure, realtime, distributed **filesystem**. It is a **three-layer composition**: a [Hyperbee](/engineering/infrastructure/p2p/hyperbee/) holds the metadata (paths → entry records), a [Hyperblobs](/engineering/infrastructure/p2p/hyperblobs/) holds the file content, and both are backed by one [Corestore](/engineering/infrastructure/p2p/corestore/). Because metadata and content are *separate cores*, listing and content sync independently — which is what makes selective sync and versioned diffs cheap.

---

## Core API

See the [README](https://github.com/holepunchto/hyperdrive) for exhaustive detail.

### Create

```js
const drive = new Hyperdrive(store, [key])
```

`store` **must be a Corestore**; `key` loads an existing drive.

### Files

- `await drive.put(path, buffer, [opts])` — `opts`: `executable`, `metadata`.
- `await drive.get(path, [opts])` — content Buffer; **`null` for a missing file *or* a symlink**.
- `await drive.del(path)` / `await drive.exists(path)`.
- `await drive.entry(path, [opts])` — the metadata record: `{ seq, key, value: { executable, linkname, blob, metadata } }`.

### Listing

- `drive.list(folder, [opts])` — recursive entry stream.
- `drive.readdir(folder, [opts])` — immediate subpaths.

### Streams & batches

- `drive.createReadStream(path, [opts])` / `drive.createWriteStream(path, [opts])`.
- `drive.batch()` … `await batch.flush()`.

### Sync

- `await drive.update([opts])` / `drive.replicate(stream)` / `drive.findingPeers()`.
- `await drive.download(folder, [opts])` — prefetch content under a prefix.
- `await drive.mirror(out, [opts])` — efficient drive→drive copy.
- `drive.checkout(version)` — read-only snapshot at a version.

### Accessors

- `drive.version` — the current version.
- `drive.db` — the underlying Hyperbee.
- `drive.blobs` / `await drive.getBlobs()` — the underlying Hyperblobs.

---

## Gotchas

**Metadata and content are separate cores.** "I have the listing but not the bytes" is a normal, expected (sparse) state — and `update()` / `download()` behave differently for metadata vs content. Don't assume an entry means its content is local.

**`get()` returns `null` for symlinks too**, not just missing files — resolve via `entry()`'s `value.linkname`; don't treat `null` as "absent."

**`findingPeers()` is the classic footgun.** Call the function it returns once peer discovery has finished — skip it and `update()` can resolve against zero peers and report a stale version.

---

## Version

`hyperdrive@13` (current `latest` is the 13.x line). The storage migration reaches Hyperdrive through its Corestore; transitional `next`/`tmp` dist-tags exist, so use `latest` and check the npm registry before pinning.

## Sources
- Docs: [docs.pears.com/building-blocks/hyperdrive](https://docs.pears.com/building-blocks/hyperdrive)
- Repo: [github.com/holepunchto/hyperdrive](https://github.com/holepunchto/hyperdrive) (README = the authoritative API reference)
- npm: `hyperdrive`
