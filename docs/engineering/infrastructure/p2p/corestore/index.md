---
layout: default
lastmod: 2026-05-31
title: "Corestore"
description: "Corestore is a factory and manager for many Hypercores — deterministic derivation, namespacing, pooled sessions, and single-stream replication."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > Corestore

# Corestore

Corestore is a **factory and manager for many Hypercores**. It derives cores deterministically from a **primary key + a name**, namespaces them, pools sessions, and replicates all of them over a **single replication stream**. It is the storage and identity root the higher structures sit on — both Hyperdrive and Autobase take a Corestore.

---

## Core API

See the [README](https://github.com/holepunchto/corestore) for exhaustive detail.

### Create

```js
const store = new Corestore(storage, [options])
```

`storage` is a directory path or a `hypercore-storage` instance. `options` includes `primaryKey`.

```js
const store = new Corestore('./storage')
const main = store.namespace('app-a').get({ name: 'main' })
await main.ready()
```

### Get cores

- `store.get({ name, ...opts })` — a core **derived from the primary key + name**; writable.
- `store.get(key)` — an external core by its public **key**; read-only replica.

### Namespacing

- `store.namespace(name)` — a namespaced session; the **same `name` under different namespaces yields different cores**; chainable.

### Replication, sessions, lifecycle

- `store.replicate(isInitiatorOrStream, [opts])` — one stream replicates **every** core the store owns.
- `store.session([opts])` — a new session sharing the storage and cache.
- `store.list([namespace])` — a stream of the cores' discovery keys.
- `await store.ready()` / `await store.close()`.

---

## Gotchas

**One Corestore per app; namespace within it.** `namespace('app-a').get({name:'main'})` and `namespace('app-b').get({name:'main'})` are *different* cores. This is the intended multi-tenant pattern — don't spin up multiple Corestores per app.

**Name vs key are different access modes.** `{name}` derives a **writable** core from the primary key; a raw `key` gives a **read-only** replica. Lose the primary key and you cannot reproduce the name-derived writable cores — treat it as the thing to back up.

**One replication stream for everything.** `store.replicate()` carries all owned cores at once; you don't replicate cores individually.

---

## Version

> **`npm i corestore` installs v7, not the newest major.** The `latest` dist-tag is deliberately kept on Corestore 7 (`7.10.0`) "to avoid too much disruption," with v11 to become `latest` "in a few weeks." A v11 exists but is not `latest` yet. **Pin deliberately and re-check `npm view corestore dist-tags` before depending.** (Corestore 7 onward is RocksDB-backed, matching Hypercore's `hypercore-storage` line.)

## Sources
- Docs: [docs.pears.com/how-tos/work-with-many-hypercores-using-corestore](https://docs.pears.com/how-tos/work-with-many-hypercores-using-corestore)
- Repo: [github.com/holepunchto/corestore](https://github.com/holepunchto/corestore) (README is authoritative and unusually candid about the migration/dist-tag state)
- npm: `corestore`
