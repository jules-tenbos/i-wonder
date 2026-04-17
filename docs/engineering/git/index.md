[In Wonder - The World of Splectrum](../../) > [Engineering](../) > Git

# Git — Operations Module

Git operations for the Bare runtime. Synchronous command execution, structured output parsing, subtree lifecycle management, and configurable hosted repo operations. One of the constitutive bare-for-pear modules.

Source: [bare-for-pear/git](https://github.com/bare-for-pear/git)

---

## Why a Git Module

Git is constitutive to mycelium — the temporal axis, the hard boundary, the decentralised exchange. The mycelium fabric needs to operate git programmatically, through protocol handlers that are thin wrappers around infrastructure.

The alternative was shelling out to git from every handler, parsing output ad hoc, hoping the subtree flags were right. A module makes the operations testable, the output structured, and the subtree workflow safe.

The module wraps the git CLI rather than reimplementing git internals. Git is the authority on git. The module adds structure on top: parsed status, typed log entries, validated subtree operations, reality detection.

---

## The Two-Reality Model

Position determines scope. When you invoke from the repo root, you get full repo scope. When you invoke from inside a registered subtree, operations scope to that subtree — its remote, its branch, its prefix.

The same command, different behaviour based on where you stand. The fabric resolves it, not the operator.

`detectReality()` compares the caller's local root against `.gittrees` entries. If the local root falls inside a registered subtree prefix, the operation enters subtree reality. Push becomes subtree push. Pull becomes subtree pull. Status scopes to the prefix.

This is the physical expression of subject reality at the git level. A subtree is a referenced repo with its own identity. When you're inside it, you're inside its reality.

---

## Subtree Management

Git subtree doesn't persist prefix-to-remote mappings anywhere. The operator must remember which prefix goes with which remote and branch. This is error-prone — one wrong flag and you're pushing to the wrong place.

`.gittrees` solves this. A committed flat file at repo root. Three columns: prefix, remote name, branch. Read by the module, validated before every subtree operation.

```
lib/avsc          bare-for-pear-avsc          main
lib/avsc-rpc      bare-for-pear-avsc-rpc      main
lib/git           bare-for-pear-git           main
lib/rpc-server    bare-for-pear-rpc-server    main
_test             spl-test                    main
```

The `subtrees.add()` function does the full workflow: add remote, fetch, add subtree, register in `.gittrees`. One call instead of four commands.

---

## Remote and Hosted Repo Operations

Remote management (add, list, remove, rename) is standard git. Hosted repo creation (creating the repo on GitHub or another platform) is adjacent — you almost always need both.

The module keeps them together with a configurable platform. GitHub is the default (uses the `gh` CLI). The platform is pluggable — add a `createRepo` and `repoUrl` function and switch.

The hosting platform is an implementation detail. The interface is: give me a name, I'll create the repo and give you the URL.

---

## Design Decisions

**Synchronous execution.** All operations use `spawnSync`. Git commands are fast and the protocol handlers are synchronous. The sync/async problem is solved once in the infrastructure layer, not in every handler.

**Structured output.** Status returns `{ branch, files }`, not a porcelain string. Log returns `[{ hash, author, timestamp, message }]`, not formatted text. The handler gets data, not text to parse.

**Thin handlers on top.** The mycelium protocol handlers (spl.mycelium.git.*) are ~20 lines each: read execution context, call the module, set response type header, return. All the git logic lives here. All the protocol logic lives there.

**Cache in subtrees.** The `.gittrees` file is loaded once and cached. This is correct for a request-handling process where `.gittrees` doesn't change during a request. The cache is invalidated on `register()`.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
