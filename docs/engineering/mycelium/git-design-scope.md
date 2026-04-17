[Home](/) > [Engineering](../) > [Mycelium](./) > Git Design Scope

# Mycelium Git — Design Scope

Git is constitutive to mycelium alongside AVRO. AVRO provides the language of articulation. Git provides the temporal axis — historicity, identity, integrity, the hard boundary, and the decentralised exchange between realities. Together with the fabric primitives, that is the full substrate.

Git provides capabilities that are drawn on across the architecture — at the fabric level, the management level, the cognitive level, the peer-to-peer level. The same capability may serve different needs at different levels, each level accessing it through its own language. The goal is not to add Git to mycelium but to discover how much of the architecture's temporal life is already Git.

---

## Governing Principles

### Open Capability Mapping

Git's capabilities are not assigned to levels. They are available. Each level of the architecture brings its own needs and its own language to Git's capability set, and finds its own use.

A single capability may serve multiple levels simultaneously. The staging area is a Git mechanism at the plumbing level, a gathering point at the management level, and a threshold of commitment at the cognitive level. Squash is a history rewriting operation, a consolidation act, and an act of forgetting. Clone is an object exchange, a management operation, and the birth of a new subject reality.

The design proceeds by laying Git's capabilities open and mapping them against needs at every level — without predetermining where a capability is allowed to land. What appears to be separate concerns at different levels may turn out to be one Git capability accessed through different lenses.

Every design decision should be tested against: are we limiting a capability to one level when it could serve more? Are we building mechanism where Git already provides one?

### The Living Subject

The subject reality operates on cognitive principles — attention, memory, forgetting, conscious engagement, subconscious routine. Git's temporal capabilities must be evaluated against how well they serve a subject reality that is alive in this sense.

Git's conventional philosophy is to never lose anything — the append-only DAG, content-addressable integrity, the complete audit trail. A living subject reality needs the opposite capability alongside preservation: it needs to forget. Selective memory, progressive consolidation, detail fading over time, only the significant shape surviving.

Git provides mechanisms for both. The immutable object store preserves. History rewriting, squashing, shallow boundaries, and garbage collection allow forgetting. The design must use both — not as a tension to be resolved but as complementary aspects of a living memory.

The cognitive model from HAICC informs how Git's capabilities are read at the higher levels:

- **Attention determines memory resolution.** What the subject is consciously engaged with gets detailed treatment. Background activity gets minimal treatment. The resolution is not uniform — it follows the attention gradient.
- **Memory consolidates over time.** Recent history is granular. Older history is progressively consolidated. Eventually only the significant shape remains.
- **Forgetting is architecturally real.** Not a failure of retention but a design feature. The subject reality stays navigable and alive rather than becoming an archive.

Every design decision should be tested against: does this serve a living subject or an archive?

### Simplification by Discovery

Approached with intelligence against the established architecture, mechanisms that appear distinct may turn out to be one thing expressed through Git's capabilities at different levels.

The checkpoint and the commit. The dirty-to-settled transition and the staging area. The memory gradient and history rewriting. Selective recall and path-filtered log. Peer-to-peer exchange and push/fetch. Reality spawning and clone. These pairings may be more than analogy — they may be the same thing seen from two directions.

The design should actively look for these collapses. Every proposed mechanism should be tested against: is this already a Git capability used at the appropriate level?

---

## Git Capabilities

What Git gives us, presented as capabilities available to all levels.

### The Object Model

Four object types, all content-addressable and immutable once written:

**Blob** — opaque content identified by SHA-1 hash of content plus type header. Same content always produces the same hash.

**Tree** — a named collection of blobs and sub-trees. A directory snapshot at a point in time.

**Commit** — wraps a tree with parent links, timestamp, author, and message. Captures full tree state, not a diff. Parent links create a directed acyclic graph.

**Tag** — a named pointer to any object, optionally annotated with its own message, author, and timestamp.

Everything identified by hash. Once written, immutable. The object store is append-only at the physical level.

### The Index

A mutable staging buffer between working state and the object store. Selective staging — choose what goes into the next commit. Multiple additions before a single commit. The only mutable structure in the core model.

### The DAG

Commits form a directed acyclic graph through parent references. Zero parents (root), one (normal), or multiple (merge). Encodes causal history — what came from what, not just temporal sequence.

### Refs

Named pointers to objects. Branches advance with new commits. Tags stay put. HEAD points to the current ref. Lightweight — just files containing a hash. Movable, deletable, creatable at near-zero cost.

### Branching

Creating a branch creates a new ref. No data copied. Work proceeds independently. Timelines diverge from a common ancestor.

### Merging

Three-way merge using the common ancestor. Merge commits record convergence with multiple parents. Conflicts surface for resolution. Fast-forward when one timeline is strictly ahead.

### Worktrees

Multiple working directories linked to the same repository, each with its own branch checked out. Shared object store, shared refs, independent working state and index.

### History Traversal

DAG walking with composable filters:

- **By path** — commits affecting a specific part of the tree.
- **By date range** — temporal windowing.
- **By author** — who made the change.
- **By message content** — grep through commit messages.
- **By code change** — pickaxe: when a specific string appeared or disappeared.
- **History simplification** — prune branches irrelevant to a path's story.
- **Graph display** — DAG structure visible: branches, merges, parallel lines.
- **Custom formatting** — control exactly what fields appear per entry.

### Diffing

Between any two commits, trees, working state versus index, index versus last commit. Content-level line-by-line diffs. Stat summaries per path.

### History Rewriting

**Interactive rebase** — pick, reword, squash, fixup, drop, reorder across a commit range.

**Squash** — collapse multiple commits into one. Detail gone, consolidated state remains.

**Fixup** — squash discarding the message.

**Drop** — remove a commit from the timeline.

**Amend** — modify the most recent commit.

**filter-repo** — rewrite entire history: remove paths, rename, transform across all commits.

**Cherry-pick** — copy a single commit to another timeline.

### Shallow Operations

**--depth N** — only the last N commits.

**--shallow-since=DATE** — truncate at a date boundary.

**--shallow-exclude=REF** — exclude a specific ancestry line.

**Deepening** — incrementally add more history.

**Unshallow** — restore full history from a remote.

Graft points tracked in `.git/shallow`.

### Replace

Swap one object for another transparently. All operations see the replacement. Stored as refs, pushable and fetchable. Original can be garbage-collected after replacement.

### Notes

Arbitrary text attached to any object without changing its hash. Multiple namespaces. Stored as independent object tree. Viewable in log, editable, removable. Not pushed by default — explicit configuration required.

### Hooks

Scripts triggered at defined points: pre-commit, post-commit, pre-push, post-merge, pre-rebase, and others. Can validate, transform, reject, or trigger side effects.

### Garbage Collection

Packing and pruning. Unreferenced objects pruned after configurable grace period. `git gc --prune=now` for immediate cleanup. Pack files use delta encoding. Physical deletion — the data is gone.

### Reflog

Local record of every ref movement. Survives rewriting operations. Configurable expiry. Recovery buffer.

### Decentralised Exchange

Every clone is complete. No central server required. Push and fetch exchange objects peer to peer. Multiple remotes supported.

---

## Needs Across Levels

What the architecture needs, at each level, from temporal infrastructure. These needs are mapped against Git's capabilities in the design areas that follow.

### Fabric Level

- A hard boundary constituting the subject reality as a distinct entity.
- Immutability of committed state — settled facts that stay settled.
- The tree structure of the fabric captured and versioned.
- Opaque content storage — the fabric does not interpret, Git does not interpret.

### Management Level

- Checkpointing — consolidating fabric activity into remembered timesteps.
- Checkpoint granularity responsive to activity load.
- The staging area as a gathering point before commitment.
- Consolidation of older history — multiple timesteps collapsed into broader strokes.
- Pruning and forgetting — physical removal of detail that has been consolidated.
- Process annotation — attaching metadata to checkpoints without altering them.
- The management layer's own state maintained as data in the fabric.
- A complementary high-frequency mechanism for activity-pace change that rolls up into Git checkpoints.

### Cognitive Level

- Memory shaped by attention — what the subject attends to is remembered in detail.
- Subconscious activity getting minimal memory — background processes fade quickly.
- Selective recall — "what happened to me" answered from the subject's perspective, scoped by context, time, or concern.
- Forgetting as a living function — the reality stays navigable, not archival.
- Plasticity — memory profile shifting as capabilities move from conscious to subconscious.
- The timeline as narrative, not log — the subject's remembered experience, not a complete record.

### Peer-to-Peer Level

- Decentralised exchange — no central server, subject to subject.
- Complete self-containment — a reality is fully operational independently.
- Selective sharing — what travels and what stays local is a design choice.
- Reality spawning — clone as the birth of a new subject, complete with history and embedded process.
- Shallow exchange — sharing recent configuration without full history.
- Divergence and reconciliation — realities that have diverged can merge.
- Portability — a subject reality can be moved anywhere, intact.

---

## Design Areas

### 1. The Checkpoint

The commit as timestep. How fabric activity becomes remembered time.

- How the management layer creates checkpoints. What constitutes a timestep boundary — load-responsive, context-sensitive.
- The staging area as gathering point. Selective staging — shaping what enters the checkpoint.
- The commit message as narrative. Structured for later querying and consolidation.
- Checkpoint granularity tuned by context — busy areas checkpoint frequently, stable areas rarely.
- At the cognitive level: what the subject chose to commit is what it remembers. The checkpoint is an act of attention as much as an act of recording.

### 2. The Memory Gradient

History is not preserved uniformly. The subject reality has short-term memory, long-term memory, and forgetting.

- **Short-term** — recent commits, full detail, close to the present.
- **Consolidation** — sequences squashed into broader timesteps. Detail released, shape retained.
- **Long-term** — distant history reduced to significant milestones.
- **Forgetting** — garbage collection removing orphaned objects after consolidation. Physical deletion.
- How consolidation is driven — a management concern responding to data state.
- At the cognitive level: the same gradient that living subjects experience. Remember what mattered, release the rest.
- The reflog as temporary safety buffer during consolidation, not permanent memory.

### 3. The Attention-Memory Relationship

The HAICC conscious/subconscious architecture shapes how Git's capabilities are used at the cognitive level.

- Contexts under conscious attention: high-resolution checkpointing, detailed messages, rich notes.
- Contexts running subconsciously: low-resolution checkpointing, summary messages, minimal annotation.
- The attention signal as data state — persona engagement visible as footprints in the fabric.
- Plasticity: as capability moves conscious to subconscious, memory profile shifts.
- At the management level: the management layer reads the attention signal and adjusts checkpoint behaviour accordingly.

### 4. The High-Frequency Complement

Where Git's snapshot-based model doesn't reach — high-frequency, high-volume activity.

- What the complement needs: fast append, lightweight capture, minimal overhead.
- The boundary: activity accumulates in the high-frequency layer, rolls up into Git checkpoints.
- Summarisation during rollup — how activity detail is condensed for the commit message or notes.
- Pruning in the high-frequency layer — aggressive, attention-shaped.
- Candidate mechanisms: append-only log, ring buffer, journaling structure. Embeddable without external dependencies.
- At the management level: the complement is the management layer's operational memory. Git is the consolidated memory.

### 5. Selective Recall

"What happened to me" — the subject's ability to query its own past.

- Path-based filtering as context-scoped memory.
- History simplification as narrative — the essential story, not every merge.
- Date-range filtering as temporal windowing.
- Commit messages and notes as the queryable narrative layer.
- The memory gradient's effect on recall — recent history is detailed, distant history is consolidated.
- At the fabric level: path expressions resolving against history.
- At the cognitive level: the persona's experience of its own past.

### 6. Notes as Annotation Layer

Post-hoc metadata attached without altering the checkpoint.

- Process summaries, attention state, consolidation records — as different note namespaces.
- Notes as the link between operational detail and committed history.
- Note lifecycle — creation, consolidation, pruning alongside the commits they annotate.
- Whether notes travel during exchange or remain local — a design choice per namespace.
- At the management level: process documentation.
- At the cognitive level: the subject's annotations on its own memories.

### 7. Reality Operations

Clone, branch, merge, fork, push, fetch, worktrees — the operations that constitute reality-level acts.

- **Clone** — reality spawning. Complete, operational from the moment of clone.
- **Branch** — parallel exploration within one reality.
- **Merge** — reconciling divergent configurations. Conflict as the mechanism for reconciling divergent realities.
- **Fork** — new subject emergence carrying history.
- **Push/Fetch** — peer-to-peer exchange. What travels, what stays.
- **Worktrees** — simultaneous points of view within one reality.
- At the fabric level: structural operations on the repository.
- At the peer-to-peer level: the decentralised interaction between subject realities.
- At the cognitive level: conscious acts of the subject on its own reality.

### 8. The Object Model Mapping

How Git's object types relate to mycelium's primitives and how the content-addressable store serves the architecture.

- Blob and mycelium record content — both opaque at their level.
- Tree and mycelium context structure — named arrangement of content and sub-contexts.
- Commit as temporal wrapper — tree state plus causality and narrative.
- Tag as significant marker in the timeline.
- Content-addressable identity — same content, same hash. The immutability guarantee.
- Physical storage: loose objects, pack files, delta compression. Scalability characteristics.

### 9. The Management Layer Interface

How the management layer operates Git internally.

- Git plumbing used directly, not wrapped or abstracted.
- The operational vocabulary: staging, committing, log traversal, rebasing, garbage collection, notes.
- Triggered by data state — watcher expressions, not schedules or calls.
- Error handling and recovery.
- The management layer's own state as data in the fabric — visible, auditable.

### 10. Decentralisation and Exchange

Git's native decentralisation serving P4.

- Every subject reality complete and independent.
- Push/fetch as peer-to-peer exchange.
- Shallow operations for partial exchange — recent configuration without full history.
- Replace enabling consolidated history exchange.
- Multiple remotes — exchange relationships with many peers.
- The relationship between Git exchange and mycelium references — fetched content becomes local.

### 11. Implementation Platform

**isomorphic-git** — pure JavaScript Git implementation for Node.js and browser environments.

**Why isomorphic-git.** Pure JavaScript, no native dependencies. Programmatic API with individual functions for each operation. Full interoperability with canonical Git — standard `.git` format. Same runtime as avsc (AVRO). Tree-shakeable. Active community maintenance.

**Why JavaScript.** Consistent with avsc choice. Same runtime, same dependency philosophy. Management layer operates both AVRO and Git through JavaScript libraries in the same process. No polyglot substrate.

**Programmatic access.** Plumbing-level operations available as function calls. The management layer operates Git through the same programming model it uses for everything else.

**Interoperability.** Standard `.git` format means canonical Git tooling works alongside. Development and debugging use any Git client.

**Gaps to evaluate.** History rewriting coverage (interactive rebase, squash, filter-repo) and garbage collection within isomorphic-git. These serve the memory gradient — consolidation and forgetting. If insufficient, options include extending the library, supplementing with canonical Git operations, or implementing directly against the object store.

---

## Design Approach

The Git design should proceed from the capabilities outward to the needs, allowing the mapping to emerge rather than prescribing it.

Start with the checkpoint (area 1), because the commit as timestep is where Git most obviously meets the architecture. Then the memory gradient (area 2) and the attention-memory relationship (area 3), because these extend the temporal capabilities into the cognitive model. Then the high-frequency complement (area 4), because the boundary of Git's reach must be understood. Then selective recall (area 5) and notes (area 6), because these are how the capabilities serve the subject's experience of its own past. Then reality operations (area 7), the object model mapping (area 8), the management layer interface (area 9), and decentralisation (area 10). Implementation platform (area 11) informs the entire sequence.

At each step, apply the governing principles. The open mapping test: are we limiting a capability to one level when it could serve more? The living subject test: does this serve a living subject or an archive? The simplification test: is this already a Git capability used at the appropriate level?

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
