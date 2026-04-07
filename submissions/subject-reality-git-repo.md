---
title: "Subject Reality — Just Another Git Repo"
type: post-topic
status: in-progress
destinations: engineering
---

# Subject Reality — Just Another Git Repo

Post topic submission. Engineering post.

---

## The argument

A subject reality in motion has dynamic, historicity, and needs a strong containing wrapper — a hard boundary. Git gives us historicity out of the box and natural repo functionality — a solid container to hold a mycelium-woven subject reality, especially during the initial creational phases.

Git is inherently decentralised — every clone is a full copy, no central server required. And it's portable — a repo is a self-contained unit you can move anywhere. These properties make it a natural fit for a subject reality container in a decentralised setting.

## Git operations as reality operations

Operations that come for free:

- **Clone** — spawn a new subject reality, complete with full history
- **Transpose** — move a reality to a different context, intact
- **Branch** — diversify within a reality without losing the original
- **Merge** — reconcile divergent realities after the fact
- **Fork** — a new subject emerges from an existing one, carries its history

No central authority needed for any of them. Reconciliation after the fact — merge conflicts — is exactly how decentralised realities deal with divergence. Not prevented, not orchestrated, resolved when the realities meet.

## Mycelium embedded within

Git gives the container and the operations. Mycelium embedded within gives the referential structure — bidirectional cross-referencing, entity-world relations, process capabilities woven into the data state. Git holds it. Mycelium makes it alive.

The data embedding of the referential side and the processing side means that a clone is straight away operational. Different reality but same experience input streams. No setup, no configuration — the reality is self-contained. The referential structure and embedded process capabilities travel with the clone.

At the point of clone: same input streams, same experience. The divergence comes later — through use, through different encounters, through the evolutionary process. Different data state changes trigger different processes, different convergence patterns emerge. The two realities drift apart naturally. Closer to cell division than anything else — identical at the split, divergent through life.

## The boundary as identity

The git repository is the boundary. It constitutes the subject reality as a distinct entity with its own identity, history, and integrity. Within the boundary, data is structured but not ontological — the folder tree and context notes define functional scope.

## Point of view

The working directory sets the point of view (POV). POV determines what you can see and how you identify it. Resources are relative to POV — you can only see what is in front of you. Paths go forward, never backward above POV.

The subject never touches the data world directly. It only knows the interface — how it interacts with the data world through its protocols from its POV.

## References bring remote into view

When a resource is behind POV but access is required, cascading references bring it into view. A reference creates a local identity for a remote resource. References are read-only — modification uses copy-on-write to the local context. Read wide, write local.

The graph of references defines the reachable set from any POV. No reference, no access — structure determines visibility, not permissions.

## Git's limits and where mycelium bridges

Git is snapshot-based — commit, store, done. It has no concept of continuous flow. For intense streaming data, high-frequency state changes, or high-volume operational data, git is ill suited. It also lacks query capability, indexes, and real-time triggering.

But git isn't asked to be a database. It's asked to be a container for a fabric.

Git at the lowest level: file storage, structural container, historicity backbone. When structured access demand is high — queries, streaming, throughput — that lives at a higher context level in an appropriate repository structure, not in git itself.

The git repo holds the mycelium fabric scene — the referential structure, the cross-references, the embedded process definitions — but the actual data can be remote. The fabric describes what's there, where it is, how it relates. The data itself can live elsewhere. The scene is local, the resources can be anywhere. Mycelium's referential layer doesn't care where the data physically lives. It cares about the relations.

This resolves the scalability question. Git holds the structure, the references, the embedded process definitions, the historicity. Remote sources hold the heavy data, the streaming feeds, the high-volume operational state. Mycelium bridges both.

Worth noting: the industry is already feeling the need for git semantics on operational data. Dolt (a SQL database with fork, clone, branch, merge) and lakeFS (git-like version control for data lakes) are attempts in that direction.

## Sequencing

This post would precede the peer-to-peer post — the reader needs to understand what a subject reality looks like concretely before the architecture between subject realities makes sense.
