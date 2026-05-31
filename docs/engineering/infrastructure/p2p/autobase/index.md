---
layout: default
lastmod: 2026-05-31
title: "Autobase"
description: "Autobase is the Hypercore family's multi-writer primitive — linearises independent input logs into one deterministic, eventually-consistent view."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [P2P building blocks](/engineering/infrastructure/p2p/) > Autobase

# Autobase

Autobase is the family's **multi-writer** primitive. Several writers each append to their own Hypercore; Autobase **linearises** those independent input logs into one deterministic, eventually-consistent **view** — an event-sourcing model. You define how the view is built and updated (the `open` and `apply` functions); the view itself is materialised as Hypercore-backed structures (commonly a [Hyperbee](/engineering/infrastructure/p2p/hyperbee/)). Built over a [Corestore](/engineering/infrastructure/p2p/corestore/).

---

## Core API

See the [README](https://github.com/holepunchto/autobase) for exhaustive detail.

### Create

```js
const base = new Autobase(store, bootstrap, options)
```

`store` is a Corestore; `bootstrap` is the key of the bootstrap writer (or `null` to create one). Key options: `open`, `apply`, `valueEncoding`, `ackInterval`, `optimistic`, `fastForward`.

### The open / apply pattern

This is the mental model.

- `open(store)` — build and return the view object(s).
- `async apply(nodes, view, host)` — apply the linearised `nodes` to the `view`. **Writer management lives here:** call `host.addWriter(key)` / `host.removeWriter(key)` inside `apply`, not as standalone calls.

### Read & write

- `await base.append(value, [opts])` — append to this writer.
- `await base.update()` — fetch and re-linearise.
- `base.view` — the current deterministic view.
- `base.replicate(isInitiator, [opts])`.

### Ordering state

- `base.signedLength` — the prefix whose ordering is **permanently fixed** (a quorum of indexers has signed it).
- `base.length` — the system core length (whole-autobase progress).

---

## Gotchas

**`apply`/`open` must be deterministic and side-effect-free.** Autobase *reorders* messages as new data arrives — it undoes and reapplies entries internally to converge. Any nondeterminism or external side effect inside `apply` corrupts the view, and corrupts it *differently on each peer*.

**`signedLength` vs `length`.** Only at or below `signedLength` is ordering immutable; above it, entries can still be reordered. Anything you surface as "final" or act on irreversibly must be at or below `signedLength` — optimistic reads above it can flip.

**Fast-forward resets the view.** With `fastForward`, a peer can jump straight to a quorum-signed state instead of replaying — fast catch-up, but local view state may be discarded and rebuilt. Design consumers to tolerate the view resetting under them.

**Optimistic mode** requires you to self-verify writes inside `apply` (reject unauthorised entries yourself).

---

## Version & maturity

`autobase@7`. This is the **fastest-moving member of the family** — the linearisation, quorum/`signedLength`, and fast-forward semantics are still evolving and the upstream docs are lighter here than for the rest. Production multi-writer behaviour (exactly when `signedLength` advances, how fast-forward rebuilds, optimistic-mode rules) is best validated by our own POC work — a specific-purpose subpage will follow from that. Treat this page as the orientation; pin the version and check the registry before depending.

## Sources
- Docs: [docs.pears.com/building-blocks/autobase](https://docs.pears.com/building-blocks/autobase)
- Repo: [github.com/holepunchto/autobase](https://github.com/holepunchto/autobase) (README = the authoritative reference; strong on concepts/warnings, lighter on full signatures)
- npm: `autobase`
