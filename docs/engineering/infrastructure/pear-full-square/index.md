---
layout: default
lastmod: 2026-06-05
title: "pear-full-square"
description: "P2P application code built on the Bare + Holepunch stack — production modules and proof-of-concept work."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > pear-full-square

# pear-full-square

P2P application code built on the Bare + Holepunch stack. A mix of
proof-of-concept work and production modules. Published under the
[pear-full-square](https://github.com/pear-full-square) GitHub organisation.

## Modules

- [hyperdrive-fuse](hyperdrive-fuse/) — read-only FUSE mount for Hyperdrive
  v11. Mount a P2P drive as a local filesystem. The swarm as a drive.
- [mycelium](mycelium/) — the Mycelium data fabric base layer. CRUD and XPath
  navigation over git objects, with a Kafka record dispatch boundary.

## POC work

- [p2p-docker-dev](https://github.com/pear-full-square/p2p-docker-dev) —
  containerised P2P dev cluster. Phases 0–6 exploring Hyperswarm, RPC,
  pub/sub, managed code, reactive dataflow. The proving ground for the
  building blocks.
