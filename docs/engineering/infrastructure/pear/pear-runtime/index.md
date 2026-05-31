---
layout: default
lastmod: 2026-05-31
title: "pear-runtime"
description: "pear-runtime embeds Pear's P2P runtime as a library — Bare workers and OTA updates without the pear CLI. Experimental / MVP, API will change."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [Pear](/engineering/infrastructure/pear/) > pear-runtime

# pear-runtime

`pear-runtime` lets a host app **embed Pear's P2P runtime as a library** — running Bare workers and taking P2P OTA updates — instead of shelling out to the `pear` CLI. It is the replacement for the embedded-runtime capability that `pear run` provided (which is being removed; see the [Pear](/engineering/infrastructure/pear/) overview). It builds on [Bare](/engineering/infrastructure/bare/) and uses Corestore / Hyperswarm / [Hyperdrive](/engineering/infrastructure/p2p/hyperdrive/) underneath.

> **Experimental / MVP.** Self-described as "most definitely will change" despite a `1.x` npm version. Pin a version and treat the API as moving.

---

## Core API

See the [README](https://github.com/holepunchto/pear-runtime) for exhaustive detail.

- `const pear = new PearRuntime(opts)` — required `opts`: `dir` (data storage), `upgrade` (the Pear link), `name`; optional `version`, custom store/swarm.
- `await pear.ready()` — init complete.
- `pear.run(path, args, opts)` — launch a Bare worker (a duplex stream).
- `pear.storage` — the recommended app-data location.
- `await pear.close()` — graceful shutdown (incl. OTA cleanup).

---

## OTA updates

Updates ride on a separate **`pear-runtime-updater`** module. The release→update workflow is CLI-driven: `pear touch` allocates a Pear link (stored in `package.json`'s `upgrade`), `pear stage` + seed publishes a version, and running instances pick it up.

Driving this loop for our own deployment — and embedding in a headless/terminal app with no Electron UI — is an open POC question; a specific-purpose subpage will follow. This page stays at orientation level.

---

## Gotcha — two runtime surfaces

There is the raw `PearRuntime` class (above) and a separate `pear-electron` `Runtime().start({ bridge })` path used for Electron UIs. Which one a headless app should use is a POC question — don't present one as the universal answer.

## Sources
- Repo: [github.com/holepunchto/pear-runtime](https://github.com/holepunchto/pear-runtime)
- npm: `pear-runtime` (experimental; pin a version) · updater: `pear-runtime-updater`
- Context: [Pear Evolution](https://pears.com/news/pear-evolution/)
