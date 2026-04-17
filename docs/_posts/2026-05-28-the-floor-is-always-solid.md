---
layout: post
title: "The Floor Is Always Solid"
date: 2026-05-28
labels: [mycelium, engineering, Splectrum]
blogger_id: 6469900294167461780
---
<img src="https://plus.unsplash.com/premium_photo-1685082608788-b531fd972c64?q=80&w=350&h=230&auto=format&fit=crop" alt="The Floor Is Always Solid" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

The mycelium fabric has a base layer — raw records and contexts, opaque bytes, no interpretation. It is the physical reality of the data. Everything above it is articulation: data layers that stack on top, each adding a specific kind of visibility. The base does not prescribe what those layers are. It provides the stacking mechanism. What gets stacked is defined by the protocol libraries that create them.

A projection layer reads immutable records and maintains a table. An index layer tracks a mutable structure and keeps a lookup current. A process state layer holds the working state of an active computation. All of these are instances of the same layering mechanism. The fabric provides the infrastructure — layer declaration in context metadata, discovery during traversal, synchronisation between layers. The specific layer types are defined by whoever needs them. The fabric grows in capability without changing the base.

Each layer declares its own read mode — how data in that layer is accessed. Direct read of settled state, changelog-aware read that includes change history, schema-interpreted read where content is resolved through discovered schemas. The read mode is a per-layer property, not a per-access choice. The subject reality defines its layers and their read modes as part of what it is. Two subjects looking at the same underlying data through different layer stacks see different realities. This is P2 — the way a subject experiences reality — expressed in the data access architecture.

When layers derive from the same underlying data, they need to stay current. A projection layer reading immutable records, an index tracking a mutable structure — each declares its synchronisation mode: immediate, batched, or on-demand. The mechanism is the same as the trigger model in the process layer. A derived layer is a process that watches its source and maintains its output. The fabric provides the infrastructure for declaring and discovering these relationships. No orchestration. The data state is the relay.

This is also how subjects interact. Data state propagation is the default mode. A process produces output visible as a data state change. Another process observes the change and acts. No messages pass between them. Decoupled, reactive, no direct communication needed. Replication follows the same pattern — the git-constituted boundary means every subject reality is a complete, self-contained unit that can be cloned, moved, and synchronised. Replication mode, like synchronisation mode, is per-layer metadata.

And underneath all of it — safe mode. Physical-layer-only access. Raw bytes, no schema discovery, no interpretation, no process activation, no layering. Records as opaque bytes, contexts as structure, nothing more. Whatever the layers above do, however they are configured, the raw physical layer is reachable. If a layer is corrupted, misconfigured, or simply not needed, safe mode bypasses it entirely. The floor is always solid.

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@alexshuperart">alexshuperart</a> / Unsplash</small>
