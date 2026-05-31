---
layout: default
lastmod: 2026-05-31
title: "Hyperblobs"
description: "Hyperblobs is a blob store on a single Hypercore — chunks binary data across blocks, returns a positional id, and streams byte ranges sparsely."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > Hyperblobs

# Hyperblobs

Hyperblobs is a simple **blob store on a single Hypercore**. It chunks arbitrary binary data across the core's blocks and hands back a pointer — the **id** — that you store elsewhere to read the blob back. It is **Hyperdrive's content layer** (Hyperdrive's `getBlobs()` returns a Hyperblobs instance; the file metadata lives in a Hyperbee alongside it).

---

## Core API

See the [README](https://github.com/holepunchto/hyperblobs) for exhaustive detail.

- `const blobs = new Hyperblobs(core, [options])` — `options` includes `blockSize` (default **64 KB**), the chunking granularity.
- `const id = await blobs.put(blob, [opts])` — store a blob; returns the id.
- `const buf = await blobs.get(id, [opts])` — read a blob by its id.
- `blobs.createReadStream(id, [opts])` / `const ws = blobs.createWriteStream([opts])` — stream large blobs; after writing, the id is at `ws.id`.
- `await blobs.clear(id, [opts])` — remove a blob.

The **id** is `{ byteOffset, blockOffset, blockLength, byteLength }` — a positional locator within the core's blocks.

---

## Gotchas

**The id is a pointer, not a hash.** It locates the blob by *position* in the append-only core, so you must persist it yourself (Hyperdrive keeps it in each file entry's `value.blob`). Hyperblobs is not content-addressed.

**Append-only underneath.** `clear()` removes access but doesn't reclaim the log.

**`blockSize` (64 KB default) is the chunking granularity.** Large blobs span many blocks and replicate sparsely — you can stream a byte range without fetching the whole blob.

---

## Version

`hyperblobs@2` — a small, stable surface. Check the npm registry before pinning.

## Sources
- Docs: [docs.pears.com/building-blocks/hyperblobs](https://docs.pears.com/building-blocks/hyperblobs)
- Repo: [github.com/holepunchto/hyperblobs](https://github.com/holepunchto/hyperblobs) (README = the authoritative API reference)
- npm: `hyperblobs`
