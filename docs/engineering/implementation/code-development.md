[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Implementation](./) > Code Development

# Code Development — Way of Working

How the Splectrum codebase is structured, what it depends on, and how it reaches the peer. A portable, self-contained codebase with no registry in the supply chain.

---

## Principle

The code that runs is code you control. No external authority in the supply chain. No runtime dependency resolution. No registry as intermediary.

This follows from node self-containment — what you compose in is what exists. The dependency policy is the same principle applied to the supply chain.

---

## Three Repositories

Each with its own purpose and its own git identity.

### spl — The Runtime

The Splectrum runtime expressed as code. One repo, namespace structure inside following the three pillars.

```
spl/
  CLAUDE.md
  lib/                  — constitutive dependencies
    avsc/               — AVRO type system (subtree)
    avsc-rpc/           — AVRO RPC layer (subtree)
  mycelium/             — data fabric, xpath, protocols
  splectrum/            — language layer (when ready)
  haicc/                — cognition layer (when ready)
```

Internal structure follows the namespace. When a node warrants its own repo, it is lifted out. The structure supports this because of node self-containment.

### bare-for-pear — Constitutive Forks

Barified forks of external code that Splectrum depends on constitutively.

| Repo | Purpose | Upstream |
|------|---------|----------|
| avsc | AVRO type system, serialization | mtth/avsc |
| avsc-rpc | AVRO RPC protocol layer | extracted from mtth/avsc v5 |

These are proper open-source repos with their own history and PRs. Day-to-day development happens in spl (where they are vendored as subtrees under `lib/`). Changes are pushed back to bare-for-pear as PRs.

### in-wonder — The Reference Library

Documentation, design, personas. The conversation about the engineering — kept separate from the engineering itself.

---

## Dependencies

### Constitutive

Dependencies that are part of the architecture. Forked, barified, maintained locally. As much Splectrum code as any other module. Vendored into spl under `lib/` as git subtrees from bare-for-pear.

**Policy:**
- Forked from upstream, barified, maintained locally
- Vendored via git subtree
- Changes pushed back to bare-for-pear as PRs
- Upstream changes pulled deliberately, reviewed
- Full ownership — free to diverge when the architecture requires it

### Platform

Dependencies that are the platform. Maintained by Holepunch. You build on them, you don't own them. Referenced directly from Holepunch's GitHub repos, pinned to specific release tags.

| Dependency | Purpose | Source |
|-----------|---------|--------|
| bare-fs | Filesystem | holepunchto/bare-fs |
| bare-path | Path operations | holepunchto/bare-path |
| bare-net | TCP networking | holepunchto/bare-net |
| bare-node-runtime | Node.js compat layer | holepunchto/bare-node-runtime |
| bare-process | Process API | holepunchto/bare-process |
| bare-buffer | Buffer API | holepunchto/bare-buffer |
| bare-crypto | Crypto primitives | holepunchto/bare-crypto |

**Reference format:** `github:holepunchto/bare-fs#v4.7.0`

**Policy:**
- Source from GitHub, not the npm registry
- Pinned to release tags — updates are deliberate
- If a platform module needs modification, fork to bare-for-pear — it becomes constitutive
- The boundary is permeable — constitutive when you change it, platform when upstream catches up

---

## Supply Chain

**No registry.** The npm registry is a publication intermediary. Compromised credentials, build-time injection, typosquatting — risks that exist because there is an intermediary. Skipped entirely.

**Source references only.** Constitutive deps via `file:` pointing to the vendored subtree. Platform deps via `github:` with tag pins. The source is the package.

**No transitive trust.** Constitutive dependencies are barified — their dependency trees are audited and controlled. Platform dependencies are trusted at the source level.

**No runtime dependency resolution.** All code is resolved at development time and bundled for distribution. The receiving peer runs exactly what was built.

---

## Version Management

**Constitutive:** versioned by commit in bare-for-pear. The subtree in spl reflects whatever was last pulled. bare-for-pear retains the full history.

**Platform:** versioned by git tag. The `github:` reference pins to a specific release. Update by changing the tag, testing, committing.

### When a Platform Dependency Needs a Fix

1. Fork to bare-for-pear
2. Fix the issue
3. PR upstream if appropriate
4. Reference as constitutive (now under `lib/`)
5. If upstream merges the fix, revert to `github:` reference at the new tag

---

## Agent Workflow

One agent, one repo. The AI agent has full physical autonomy — structure, code, environments, testing, deployment. Direction and design come from collaborative interaction.

### Constitutive Dependency Changes

1. Make the change in `spl/lib/avsc`
2. Test in context — the change is immediately available
3. Push the subtree changes back:
   ```
   git subtree push --prefix=lib/avsc bare-for-pear-avsc main
   ```
4. Open a PR on bare-for-pear/avsc

### Pulling Upstream Changes

```
git subtree pull --prefix=lib/avsc bare-for-pear-avsc main --squash
```

The `--squash` keeps spl's history clean. bare-for-pear retains the full history.

---

## Distribution

`bare-bundle` resolves all dependencies from the source tree and produces a single artifact. Pear distributes it P2P.

```
source tree → bare-bundle → pear → peer
```

No registry at any point. The code that runs on the peer is the code in the source tree.

---

## Not Yet in Scope

- **Namespace-to-repo mapping** — when nodes become their own repos
- **Multi-agent development** — multiple agents across or within repos
- **Release and versioning** — tagging, release cuts, Pear distribution management
- **CI/CD** — automated testing, build pipelines, deployment

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
