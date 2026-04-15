---
title: "Code Development — Way of Working"
type: substantial
status: new
destinations: engineering
---

# Code Development — Way of Working

How Splectrum code is developed, structured, and
distributed. A starting point — expected to evolve
as the engineering develops.

---

## Principle

A subject reality is self-contained. The code that
runs is code you control. No external authority in
the supply chain. No runtime dependency resolution.
No registry as intermediary.

This follows from node self-containment (lift and
shift), the architecture of absence (what you don't
compose in doesn't exist), and P2P distribution via
Pear (the bundle IS the application).

Code development is AI-autonomous at the physical
level — structure, code, environments, testing,
deployment. It is interactive and collaborative at
the logical level — scope, meaning, design,
direction. One agent, one repo.

---

## Three Repositories

Three homes, three purposes. Each is a subject
reality with its own identity.

### spl — The Splectrum Runtime

The codebase. The Splectrum runtime expressed as
code. One repo, namespace structure inside following
the three pillars.

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

Internal structure follows the namespace. When a
node's life warrants its own repo, it is lifted out.
The structure supports this because of node
self-containment.

This is the agent's home. One agent, one repo, one
context. The agent sees everything it needs to work.

### bare-for-pear — Constitutive Forks

Barified forks of external code that Splectrum
depends on constitutively. Infrastructure.

| Repo | Purpose | Upstream |
|------|---------|----------|
| avsc | AVRO type system, serialization | mtth/avsc |
| avsc-rpc | AVRO RPC protocol layer | (extracted from mtth/avsc v5) |

These repos have their own git identity, their own
history, their own PRs. They are proper open-source
repos, not dumps from a monorepo.

Day-to-day development happens in the spl repo
(where they are vendored as subtrees). Changes are
pushed back to bare-for-pear as PRs.

### in-wonder — The Reference Library

The shared knowledge surface. Documentation, design,
personas. Published at jules-tenbos.github.io/
in-wonder/. Engineering specs, philosophical
grounding, technology references, persona
definitions.

Not code. Not runtime. The conversation about the
engineering — kept separate from the engineering
itself.

---

## Dependency Categories

### Constitutive

Dependencies that are part of the architecture.
Splectrum forks, maintains, and evolves them. They
are as much Splectrum code as any other module.

Constitutive dependencies are vendored into the spl
repo under `lib/` as git subtrees from
bare-for-pear.

**Reference format:**
```json
{ "avsc": "file:lib/avsc" }
```

**Policy:**
- Forked from upstream, barified, maintained locally
- Vendored in spl via git subtree
- Changes pushed back to bare-for-pear as PRs
- Upstream changes pulled deliberately, reviewed
- Full ownership — free to diverge when the
  architecture requires it

### Platform

Dependencies that ARE the platform. Maintained by
Holepunch. Same relationship as a program to its
runtime — you build on them, you don't own them.

Referenced directly from Holepunch's GitHub repos,
pinned to specific release tags. Not vendored.

| Dependency | Purpose | Source |
|-----------|---------|--------|
| bare-fs | Filesystem | holepunchto/bare-fs |
| bare-path | Path operations | holepunchto/bare-path |
| bare-net | TCP networking | holepunchto/bare-net |
| bare-node-runtime | Node.js compat layer | holepunchto/bare-node-runtime |
| bare-process | Process API | holepunchto/bare-process |
| bare-buffer | Buffer API | holepunchto/bare-buffer |
| bare-crypto | Crypto primitives | holepunchto/bare-crypto |

**Reference format:**
```json
{ "bare-fs": "github:holepunchto/bare-fs#v4.7.0" }
```

**Policy:**
- Source from GitHub, not the npm registry
- Pinned to release tags — updates are deliberate
- If a platform module needs modification, fork to
  bare-for-pear — it becomes constitutive
- The boundary is permeable — constitutive when you
  change it, platform when upstream catches up

---

## Supply Chain

**No npm registry.** The npm registry is a
publication intermediary. Compromised credentials,
build-time injection, typosquatting — risks that
exist because there is an intermediary. We skip it.

**Source references only.** Constitutive deps via
`file:` (vendored subtree). Platform deps via
`github:` (Holepunch's repos, tag-pinned). The
source IS the package.

**No transitive trust.** Constitutive dependencies
are barified — their dependency trees are audited
and controlled. Platform dependencies are trusted
at the source level.

**No lock files as security.** Lock files pin
versions but fetch from the registry. We pin at the
source (git tags) and fetch from the source (GitHub
repos). The source IS the lock.

**No runtime dependency resolution.** All code is
resolved at development time and bundled for
distribution. Pear distributes the complete bundle
P2P. The receiving peer runs exactly what was built.

---

## Version Management

**Constitutive:** versioned by commit in the
bare-for-pear repos. The subtree in spl reflects
whatever was last pulled. The bare-for-pear repo
retains the full history.

**Platform:** versioned by git tag. The `github:`
reference pins to a specific release. Update by
changing the tag in package.json and testing.

---

## Agent Development Workflow

The AI agent works in the spl repo. One agent, one
repo, one CLAUDE.md. The agent has full physical
autonomy — structure, code, testing. Direction and
design come from collaborative interaction.

### Normal Development

The agent works in spl. All runtime code and
vendored dependencies are in the repo. Changes are
committed to spl.

### Constitutive Dependency Changes

When the agent needs to change a vendored
dependency (e.g. lib/avsc):

1. Make the change in spl/lib/avsc
2. Test in context — the change is immediately
   available to all code in spl
3. When solid, push the subtree changes back:
   ```
   git subtree push --prefix=lib/avsc \
     bare-for-pear-avsc main
   ```
4. Open a PR on bare-for-pear/avsc
5. The bare-for-pear repo receives a clean commit
   history for the dependency changes

### Pulling Upstream Changes

When bare-for-pear/avsc has changes (e.g. from an
upstream pull):

```
git subtree pull --prefix=lib/avsc \
  bare-for-pear-avsc main --squash
```

The `--squash` keeps spl's history clean. The
bare-for-pear repo retains the full history.

### Platform Dependency Updates

1. Check Holepunch's repo for new releases
2. Update the tag in package.json
3. Install (fetches from GitHub, not npm)
4. Test on Bare
5. Commit the package.json change

### When a Platform Dependency Needs a Fix

If a bare-* module has a bug or incompatibility:

1. Fork to bare-for-pear organisation
2. Fix the issue
3. PR upstream if appropriate
4. Reference changes from file: (now constitutive)
5. If upstream merges the fix, revert to github:
   reference at the new tag

The boundary between platform and constitutive is
permeable. A dependency moves from platform to
constitutive when you need to change it. It can
move back when upstream catches up.

---

## Distribution

`bare-bundle` resolves all dependencies from the
source tree and produces a single artifact. Pear
distributes this artifact P2P.

```
source tree → bare-bundle → pear → peer
```

No registry at any point. The code that runs on the
peer is the code in the source tree.

---

## spl5 Transition

spl5 is the prototyping iteration. It proved the
core chain: message shape, RPC server, fabric
operations.

In spl5, constitutive dependencies are cloned
locally under `bare-for-pear/` and referenced via
`file:` paths. `npm install` is a development
convenience — it resolves the graph locally,
fetching from GitHub, not npm. The resulting
`node_modules` is a local cache, not a distribution
artifact.

```
~/bare-for-pear/
  avsc/              — constitutive, forked
  avsc-rpc/          — constitutive, owned

~/splectrum/spl5/
  projects/02-avro-rpc-server/
    package.json     — file: and github: refs
```

When the spl repo is established:

- Runtime code migrates from spl5 to spl
- Constitutive deps move from file: references to
  vendored subtrees under lib/
- Design docs are already in the reference library
- spl5 remains as the archive — the record of how
  the prototyping was done

---

## Rationale

This is not paranoia. It is architectural
consistency.

Splectrum's self-containment principle says: what
you compose in is what exists. The dependency
policy is the same principle applied to the supply
chain. The code you run is the code you chose. No
surprises from intermediaries, no implicit trust in
registries, no runtime resolution from external
sources.

The Pear distribution model already requires this
for the final artifact. This policy extends the
same discipline to the development process.

---

## What This Does Not Cover

**Namespace-to-repo mapping.** When nodes in the
namespace tree become their own repos — the criteria
and the mechanism. This is a future concern. For now,
one repo.

**Multi-agent development.** One agent, one repo is
the starting point. Multiple agents across repos, or
multiple agents in one repo, is a future concern.

**Release and versioning.** How spl versions are
tagged, how releases are cut, how Pear distribution
is managed. To be defined when distribution is in
scope.

**CI/CD.** Automated testing, build pipelines,
deployment automation. To be defined when the
development workflow is established.
