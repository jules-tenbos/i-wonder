---
title: Subject Reality — Just Another Git Repo
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# Subject Reality — Just Another Git Repo
Labels: mycelium, engineering, Splectrum

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More on mycelium in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium area of the reference library</a>.</small>

---
<small>Photo: credit / Unsplash</small>

---

# Notes

## Storyline

### 1. Opening — just a git repo
- A subject reality in Splectrum engineering is a git repository
- That sounds ordinary. It's not — because of what falls out when you take it seriously
- Git provides the temporal axis: historicity, identity, integrity, the hard boundary, decentralised exchange

### 2. What git gives for free
- Clone — spawn a new subject reality, complete with full history
- Branch — diversify within a reality without losing the original
- Merge — reconcile divergent realities after the fact. Conflicts as how decentralised realities deal with divergence
- Fork — a new subject emerges from an existing one, carries its history
- No central authority needed for any of them
- These aren't metaphors mapped onto git. They are git operations read through the framework

### 3. Self-contained and operational from birth
- Mycelium embedded within gives the referential structure — cross-referencing, entity-world relations, process capabilities woven into data state
- A clone is straight away operational. Different reality but same experience input streams. No setup, no configuration
- The referential structure and embedded process capabilities travel with the clone
- At the point of clone: same input streams, same experience. Divergence comes later — through use, through different encounters
- Closer to cell division than anything else — identical at the split, divergent through life

### 4. The boundary as identity
- The git repository is the boundary. Constitutes the subject reality as a distinct entity
- Identity, history, integrity — all from the repository itself
- WYSIWYG: what you see is what there is. No hidden data, no hidden process

### 5. A living subject, not an archive
- Git's conventional philosophy: never lose anything. Append-only, content-addressable, complete audit trail
- A living subject reality needs more than that — it needs to forget
- Attention determines memory resolution — what the subject attends to gets detailed treatment, background fades
- Memory consolidates over time — recent history granular, older history progressively consolidated, eventually only the significant shape
- Forgetting is architecturally real — not failure but design. The reality stays navigable and alive
- Git provides mechanisms for both: the immutable store preserves, history rewriting and garbage collection allow forgetting

### 6. The same capability, different lenses
- A single git capability serves multiple levels simultaneously
- Staging area: plumbing mechanism, gathering point for management, threshold of commitment at cognitive level
- Squash: history rewriting operation, consolidation act, act of forgetting
- Clone: object exchange, management operation, birth of a new subject
- The checkpoint and the commit. The dirty-to-settled transition and the staging area. The memory gradient and history rewriting
- These pairings may not be analogy — they may be the same thing seen from two directions

### 7. Git's limits and where mycelium bridges
- Git is snapshot-based — commit, store, done. No concept of continuous flow
- For streaming data, high-frequency state changes, high-volume operational data — git is ill suited
- But git isn't asked to be a database. It's asked to be a container for a fabric
- Git holds the structure, references, embedded process, historicity. Remote sources hold the heavy data
- The fabric describes what's there, where it is, how it relates. The data itself can live elsewhere
- Scene is local, resources can be anywhere

### 8. Close
- Just a git repo. But when you take that seriously — self-contained subjects, living memory, decentralised exchange, reality operations that are already git operations
- The goal was not to add git to mycelium but to discover how much of the architecture's temporal life was already git

---

## Notes from submission

### The argument

A subject reality in motion has dynamic, historicity, and needs a strong containing wrapper — a hard boundary. Git gives us historicity out of the box and natural repo functionality — a solid container to hold a mycelium-woven subject reality, especially during the initial creational phases.

Git is inherently decentralised — every clone is a full copy, no central server required. And it's portable — a repo is a self-contained unit you can move anywhere. These properties make it a natural fit for a subject reality container in a decentralised setting.

### Mycelium embedded within

Git gives the container and the operations. Mycelium embedded within gives the referential structure — bidirectional cross-referencing, entity-world relations, process capabilities woven into the data state. Git holds it. Mycelium makes it alive.

The data embedding of the referential side and the processing side means that a clone is straight away operational. Different reality but same experience input streams. No setup, no configuration — the reality is self-contained. The referential structure and embedded process capabilities travel with the clone.

At the point of clone: same input streams, same experience. The divergence comes later — through use, through different encounters, through the evolutionary process. Different data state changes trigger different processes, different convergence patterns emerge. The two realities drift apart naturally. Closer to cell division than anything else — identical at the split, divergent through life.

### Point of view

The working directory sets the point of view (POV). POV determines what you can see and how you identify it. Resources are relative to POV — you can only see what is in front of you. Paths go forward, never backward above POV.

The subject never touches the data world directly. It only knows the interface — how it interacts with the data world through its protocols from its POV.

### References bring remote into view

When a resource is behind POV but access is required, cascading references bring it into view. A reference creates a local identity for a remote resource. References are read-only — modification uses copy-on-write to the local context. Read wide, write local.

The graph of references defines the reachable set from any POV. No reference, no access — structure determines visibility, not permissions.

### Git's limits and where mycelium bridges

Git is snapshot-based — commit, store, done. It has no concept of continuous flow. For intense streaming data, high-frequency state changes, or high-volume operational data, git is ill suited. It also lacks query capability, indexes, and real-time triggering.

But git isn't asked to be a database. It's asked to be a container for a fabric.

Git at the lowest level: file storage, structural container, historicity backbone. When structured access demand is high — queries, streaming, throughput — that lives at a higher context level in an appropriate repository structure, not in git itself.

The git repo holds the mycelium fabric scene — the referential structure, the cross-references, the embedded process definitions — but the actual data can be remote. The fabric describes what's there, where it is, how it relates. The data itself can live elsewhere. The scene is local, the resources can be anywhere. Mycelium's referential layer doesn't care where the data physically lives. It cares about the relations.

Worth noting: the industry is already feeling the need for git semantics on operational data. Dolt (a SQL database with fork, clone, branch, merge) and lakeFS (git-like version control for data lakes) are attempts in that direction.

### Sequencing note

This post should precede the peer-to-peer post — the reader needs to understand what a subject reality looks like concretely before the architecture between subject realities makes sense.

---

## Notes from git design scope

### The living subject principle

The subject reality operates on cognitive principles — attention, memory, forgetting, conscious engagement, subconscious routine. Git's temporal capabilities must be evaluated against how well they serve a subject reality that is alive in this sense.

Git's conventional philosophy is to never lose anything. A living subject reality needs the opposite capability alongside preservation: it needs to forget. Selective memory, progressive consolidation, detail fading over time, only the significant shape surviving.

Git provides mechanisms for both. The immutable object store preserves. History rewriting, squashing, shallow boundaries, and garbage collection allow forgetting. Not a tension to be resolved but complementary aspects of a living memory.

### Open capability mapping

Git's capabilities are not assigned to levels. They are available. Each level brings its own needs and language to Git's capability set.

A single capability may serve multiple levels simultaneously:
- Staging area: Git mechanism / gathering point / threshold of commitment
- Squash: history rewriting / consolidation / forgetting
- Clone: object exchange / management operation / birth of a new subject

### Simplification by discovery

The checkpoint and the commit. The dirty-to-settled transition and the staging area. The memory gradient and history rewriting. Selective recall and path-filtered log. Peer-to-peer exchange and push/fetch. Reality spawning and clone. These pairings may be the same thing seen from two directions.

### The memory gradient

- **Short-term** — recent commits, full detail, close to the present
- **Consolidation** — sequences squashed into broader timesteps. Detail released, shape retained
- **Long-term** — distant history reduced to significant milestones
- **Forgetting** — garbage collection removing orphaned objects. Physical deletion

### The attention-memory relationship

Contexts under conscious attention: high-resolution checkpointing, detailed messages, rich notes. Contexts running subconsciously: low-resolution checkpointing, summary messages, minimal annotation. As capability moves conscious to subconscious, memory profile shifts.

### The cognitive level needs

- Memory shaped by attention
- Subconscious activity getting minimal memory
- Selective recall — "what happened to me" from the subject's perspective
- Forgetting as a living function
- Plasticity — memory profile shifting
- The timeline as narrative, not log

### The high-frequency complement

Where Git's snapshot-based model doesn't reach. Activity accumulates in a high-frequency layer, rolls up into Git checkpoints. Candidate mechanisms: append-only log, ring buffer, journaling structure.

---

## Vocabulary updates

- **Subject reality** — review/update if entry exists

---

## Tasks on scheduling

- [ ] Image selection
- [ ] Schedule on Blogger
- [ ] Delete draft
- [ ] Delete submission (subject-reality-git-repo.md)
