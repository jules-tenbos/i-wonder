---
layout: default
lastmod: 2026-06-06
title: "P2P Swarm and Bridgehead"
description: "The P2P swarm network and the bridgehead container that establishes a foothold on it — connectivity, replication, shared infrastructure."
sitemap: false
---

[Home](/) > [Engineering](/engineering/) > [SPL Platform](/engineering/spl/platform/) > P2P Swarm and Bridgehead

# P2P Swarm and Bridgehead

The swarm is the network reality — peers discovering, connecting, and replicating over a private DHT. The bridgehead is the container that establishes a foothold on the swarm: once it's up, participation follows.

**Bridgehead infrastructure** — everything inside the container that makes a node operational: DHT bootstrap, Hyperswarm connectivity, the HTTP API, the browser GUI, replication management.

**Swarm infrastructure** — shared structure exposed across the swarm: the Hyperdrive that carries code, manifests, and apps, mountable via FUSE for local visibility.

*Content expanding when the POCs are complete.*
