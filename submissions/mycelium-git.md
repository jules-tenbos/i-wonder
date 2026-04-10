---
title: "Mycelium Git"
type: substantial
status: new
destinations: engineering, post
---

# Mycelium Git

The git API layer in mycelium. The git design scope ref lib page was written before several discoveries matured. This submission collects material for updating the ref lib page and producing a detailed post.

A key design question: how to approach the API. Git capabilities are low-level — plumbing. Mycelium needs to expose them at the right level for the fabric. This suggests at least two layers: a thin wrapper around git operations (isomorphic-git), and a higher-level API that speaks in mycelium terms — checkpoints, memory, reality operations, quiescence — rather than git terms. The higher level translates architectural intent into git operations. The wrapper ensures the fabric never touches git directly. How these two layers relate, where the boundary sits, and what the higher-level vocabulary looks like are open design questions.

An alternative direction: a standalone git API stack rather than a mycelium-embedded git integration. The layers are independent regardless — that's not the issue. The question is logical structure. Git provides the subject reality boundary, and the subject reality is the unit that all three fabrics operate within. Does git sit inside the mycelium pillar as one of its internals, or below all three as a substrate service? If git is substrate, the logical structure would be: git holds the container, mycelium/splectrum/HAICC are fabrics within it. If git is mycelium-internal, the other pillars access git capabilities indirectly through mycelium. The architectural placement shapes how we think about the design. There is a lot to say for embedded: it is consistent with how AVRO is positioned — both are constitutive dependencies of mycelium, not standalone services. The fabric holds everything. Git embedded means the temporal axis is a property of the data fabric itself, not an external service. The subject reality is a git repo with mycelium woven in — not a mycelium system with git bolted on. The other pillars don't need their own git access — they operate within the subject reality that mycelium already provides. And the reasoning extends further: mycelium handles both the static and dynamic aspects of visible data state. Git serves both — the static (committed state, immutable records) and the dynamic (branching, merging, memory gradient, reality operations). Git belongs where both aspects live.

---

## 1. The subject owns its historicity

The mycelium data fabric post introduced this: the subject reality controls what gets remembered and how. Not an external system applying checkpoints. This needs working through in the git design scope.

- **Gitignore as memory choice** — operational data backed up separately, git for configuration and structural state. The subject decides what enters history and what doesn't.
- **Layered setup** — referenced read-only base providing initial configuration, local overlay for overrides. Read wide, write local. How does this interact with git's mechanisms?
- **Checkpoint as attention** — the subject decides when to commit, shaping its own memory. Not clock-driven, not event-driven — attention-driven.
- How does this change the framing of the memory gradient and attention-memory relationship already in the design scope?

## 2. Quiescence and portability

New material from the mycelium data fabric post. Not yet in the git design scope.

- **Quiescence** — subject reality going completely dormant, moved anywhere, reactivated where it left off. Everything embedded.
- **Hot standby** — clone tracking the active reality, ready to take over. What git mechanisms serve this? Shallow clones? Fetch intervals?
- **Peer-to-peer exchange** — subjects moving between environments. The p2p design area in the scope touches this but not from the portability angle.
- **Disaster recovery** — the repo as recovery unit. Self-contained by design. What does this mean for backup strategy?
- **Deployment as clone** — spawning production instances as reality operations.
- What engineering patterns emerge from treating git operations as reality operations concretely?

## 3. Narrative commits — from the physical/logical pivot

The pivot submission introduced narrative commits. This is substantial new material for the git design scope.

- **Commit message as primary record** — the meaning, not the diff. The human commits meaning, the system derives structure.
- **Multiple reader schemas on a commit message** — extracting process state, editorial judgment, rewrite details, physical operations from the same natural language text.
- **Narrative history** — consolidation as AI reading ten narrative commits and producing one that captures what mattered. Forgetting as editorial.
- **History rewriting as re-understanding** — the same events narrated from where the subject stands now.
- **Selective recall as conversation** — "what happened to submissions last month?" against natural language history.
- How does this reshape the memory gradient? The checkpoint design area? The selective recall design area?

## 4. The logical/physical framing applied to git

The new design commitment: the design lives in the logical space. How does this apply to git specifically?

- Git capabilities are physical. The design scope maps them to architectural needs at multiple levels. But the mapping is logical — which physical capabilities serve which logical needs.
- The living subject principle is a logical design. Git's mechanisms (squash, gc, shallow) are physical implementations of that design. Not all need to be implemented — JIT.
- Does this change how the design areas should be framed?

## 5. Self-auditing process execution

Mentioned in earlier discussion — the idea of a full self-auditing process execution flow using git.

- Every process execution leaves a narrative commit trail
- The trail is queryable through reader schemas
- The subject can audit its own process history
- What does this look like concretely? What git mechanisms serve it?
- Connection to the process report from the AVRO design scope

## 6. The high-frequency complement — revisited

Design area 4 in the current scope. Still open. But now with context from:

- Operational data gitignored (from mycelium fabric post) — the high-frequency layer IS the operational data
- The boundary between git (structural memory) and the high-frequency layer (operational memory) is the gitignore boundary
- Rollup from high-frequency to git checkpoint is the consolidation step
- Does the narrative commit change what rollup looks like?

## 7. Reality operations as concrete engineering patterns

The design scope lists clone, branch, merge, fork as reality operations. The mycelium fabric post adds quiescence, hot standby, disaster recovery. Can we map these to concrete engineering patterns?

- **Clone** → deployment, subject spawning, hot standby creation
- **Branch** → A/B testing, experimental diversification, parallel exploration
- **Merge** → reconciliation after offline operation, conflict as discovery
- **Shallow clone** → partial exchange, configuration-only deployment
- **Fork** → new subject emergence from existing, carrying history
- **Worktree** → simultaneous points of view within one reality

What's the relationship between these patterns and traditional deployment/operations patterns?

---

*Material for discussion. Expected outputs: updated git design scope ref lib page, potentially a detailed git post.*
