---
layout: default
lastmod: 2026-06-05
title: "bare-for-pear"
description: "Modules built for the Bare runtime: community forks barified, git infrastructure, and a minimal P2P git engine."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > bare-for-pear

# bare-for-pear

Modules built for the [Bare](/engineering/infrastructure/bare/) runtime — a mix
of community forks (Node.js assumptions stripped, Bare's minimal API surface
honoured), git infrastructure, and a minimal P2P git engine. Published under
the [bare-for-pear](https://github.com/bare-for-pear) GitHub organisation.

## Modules

- [avsc](avsc/) — Avro type system, serialization, schema evolution. Fork of
  mtth/avsc, barified.
- [avsc-rpc](avsc-rpc/) — Avro RPC protocol, service definition, transports.
  Extracted from avsc v5, barified.
- [git](git/) — git CLI wrapper, subtree management, two-reality model.
  Original module.
- [rpc-server](rpc-server/) — server lifecycle, PID management, file-based
  command IPC. Original module.
- [isomorphic-git](isomorphic-git/) — full isomorphic-git with a Hyperdrive fs
  adapter. Standard git on bare-fs or P2P storage. Fork of isomorphic-git.
- [p2p-git](p2p-git/) — minimal git engine for embedding. isomorphic-git
  stripped to plumbing — object operations, index, refs, merge. No porcelain,
  no network, no packfiles, no working tree.
