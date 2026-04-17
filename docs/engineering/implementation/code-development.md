[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Implementation](./) > Code Implementation

# Code Implementation — Way of Working

How the Splectrum codebase is structured, what it depends on, and how it reaches the peer. A portable, self-contained codebase targeting the Bare runtime.

---

## Principle

The code that runs is code you control. No external authority in the supply chain. No runtime dependency resolution. No registry as intermediary.

This follows from node self-containment — what you compose in is what exists. The dependency policy is the same principle applied to the supply chain.

---

## Runtime

Bare only. All code targets the Bare runtime from Holepunch. No Node.js, no dual-runtime compatibility layers. Bare is a modular JavaScript runtime with no standard library — everything is composed in explicitly.

Module names are always direct: `bare-fs`, `bare-net`, `bare-path`, `bare-crypto`, `bare-buffer`. Never aliased to Node names. There is no global `Buffer`, no global `process`, no global `TextEncoder`. If you need it, require it. The architecture of absence applied to the runtime itself.

---

## Three Repositories

Each with its own purpose and its own git identity.

### spl — The Runtime

The Splectrum runtime expressed as code. One repo, namespace structure inside following the three pillars.

```
spl/
  bin/                  — entry point scripts
  docs/                 — policy, schema, reference
  lib/                  — all dependencies
    avsc/               — AVRO type system (subtree)
    avsc-rpc/           — AVRO RPC layer (subtree)
    git/                — git operations (subtree)
    rpc-server/         — server lifecycle (subtree)
    bare-*/             — platform deps (gitignored)
  _test/                — test framework (subtree)
  _schema/              — local schema registry
  _client/              — default client identity
  mycelium/             — data fabric, xpath, protocols
  splectrum/            — language layer (when ready)
  haicc/                — cognition layer (when ready)
  package.json          — minimal: name, version, description
```

Internal structure follows the namespace. When a node warrants its own repo, it is lifted out. The structure supports this because of node self-containment.

### bare-for-pear — Constitutive Forks

Barified forks of external code that Splectrum depends on constitutively.

| Repo | Purpose | Upstream |
|------|---------|----------|
| avsc | AVRO type system, serialization | mtth/avsc |
| avsc-rpc | AVRO RPC protocol layer | extracted from mtth/avsc v5 |
| git | Git operations, subtree management | original |
| rpc-server | Server lifecycle, command IPC | original |

These are proper open-source repos with their own history and PRs. Day-to-day development happens in spl (where they are vendored as subtrees under `lib/`). Changes are pushed back to bare-for-pear as PRs.

### The Test Framework

Test framework as a separate repo, attached to spl via subtree at `_test/`. Full-chain tests — every test spawns the CLI, sends a real RPC request, and verifies the response. No mocking.

The test framework has its own client identity that travels with it. Suites are organized by module so they can travel with their module on extraction.

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

Dependencies that are the platform. Maintained by Holepunch. You build on them, you don't own them. Populated into `lib/` by `bin/setup` and gitignored — not committed to the repo.

| Dependency | Purpose |
|-----------|---------|
| bare-fs | Filesystem |
| bare-path | Path operations |
| bare-net | TCP networking |
| bare-crypto | Crypto primitives |
| bare-buffer | Buffer API |
| bare-events | Event emitter |
| bare-stream | Stream primitives |
| bare-os | OS operations |
| bare-subprocess | Process spawning |

**Policy:**
- Populated by `bin/setup` — pinned to specific versions in the setup script
- Gitignored — not committed to the repo
- If a platform module needs modification, fork to bare-for-pear — it becomes constitutive
- The boundary is permeable — constitutive when you change it, platform when upstream catches up

---

## Module Resolution

A symlink `node_modules → lib/` lets Bare's module resolver find all dependencies by their bare names. One mechanism, one structure.

```
node_modules → lib/
  avsc/           (constitutive, committed)
  avsc-rpc/       (constitutive, committed)
  bare-fs/        (platform, gitignored)
  bare-net/       (platform, gitignored)
  ...
```

Application code uses direct requires: `require('bare-fs')`, `require('bare-net')`. Constitutive deps use relative paths to reach siblings within `lib/`.

No import maps. No path aliases. No bundler configuration. The symlink is the resolution.

---

## Supply Chain

**No npm registry for code.** npm is used in `bin/setup` solely because native addon prebuilds (compiled C/C++ for each OS) are published to npm but not to GitHub repos. This is being eliminated — building native addons from source locally removes npm from the chain entirely.

**No runtime dependency resolution.** All code is resolved at development time. What's in `lib/` is what runs.

**No transitive trust.** Constitutive dependencies are barified — their dependency trees are audited and controlled. Platform dependencies are trusted at the source level.

**No lock files as security.** Lock files pin versions but fetch from the registry. Versions are pinned in `bin/setup`. The source tree is the lock.

---

## Entry Points

All execution starts from `bin/` scripts:

```bash
bin/spl-server    # start the RPC server
bin/spl           # CLI client
bin/spl-test      # run test suites
bin/setup         # populate platform deps after clone
```

Each script resolves the repo root and calls `exec bare <path>` to hand off to the runtime. No Node.js involved at any point.

---

## Code Conventions

**CommonJS modules.** `require()` / `module.exports`. Bare supports both CJS and ESM but the codebase uses CJS for consistency with the dependency ecosystem.

**Buffer is explicit.** Import from `bare-buffer`. There is no global Buffer on Bare.

**Process is explicit.** There is no global `process` on Bare. Use `bare-os` for cwd, `Bare.exit()` for exit.

**TextEncoder/TextDecoder.** Not global on Bare. Polyfilled in constitutive deps where needed.

**No standard library assumptions.** If it's not composed in, it doesn't exist. The architecture of absence applied to code.

---

## Version Management

**Constitutive:** versioned by commit in bare-for-pear. The subtree in spl reflects whatever was last pulled. bare-for-pear retains the full history.

**Platform:** versioned in `bin/setup`. Update the version and rerun.

### When a Platform Dependency Needs a Fix

1. Fork to bare-for-pear
2. Fix the issue
3. PR upstream if appropriate
4. Reference as constitutive (now under `lib/`, committed)
5. If upstream merges the fix, revert to platform (gitignored, setup-managed)

---

## Agent Workflow

One agent, one repo. The AI agent has full physical autonomy — structure, code, environments, testing, deployment. Direction and design come from collaborative interaction.

### After Cloning

```bash
bin/setup     # populates lib/ with platform deps
              # creates node_modules → lib/ symlink
```

### Running

```bash
bin/spl-server    # start the RPC server
bin/spl           # run the CLI client
```

### Making Changes

Work directly in the source tree. All code is local, all deps are in `lib/`. No build step, no transpiler, no bundler during development.

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
