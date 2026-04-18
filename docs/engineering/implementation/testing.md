[Home](/) > [Engineering](/engineering/) > [Implementation](/engineering/implementation/) > Testing

# Testing — Full Chain, No Mocking

How the spl runtime tests itself. The test framework exercises the same path as the user. If a test passes, the feature works. If it fails, it fails the way a user would experience it.

---

## The Principle

A mock test can pass while the real system fails. The mock captured your assumptions about the interface at the time you wrote the mock. If the interface changed, the mock didn't. Your test is green, your system is broken, and you don't know.

The test framework doesn't mock. Every protocol test spawns the spl CLI as a subprocess, sends a real RPC request to a running server, goes through real dispatch to a real handler, gets a real response, and verifies it. The full chain: CLI → RPC → server → dispatch → handler → response → extraction.

This is slower than mocking. A test suite that spawns 60+ subprocesses takes seconds, not milliseconds. The trade-off is worth it. You know the system works because you watched it work.

Infrastructure tests (lib/git, lib/rpc-server) test the module API directly via `require()`. These modules have no protocol layer above them that could mask failures. Direct testing is the authentic path.

---

## Test as Entity

The test framework is a separate repo attached to spl via subtree at `_test/`. It has its own identity — `_test/_client/context.txt` defines the test client vocabulary. The test client speaks test language, not xpath language, not git language.

This is the same multi-client identity system that serves all entities in the fabric. The test framework is an entity like any other. It has its own reality (the subtree), its own language (the client context), its own concerns. It happens to be an entity whose concern is verification.

The identity travels with the test repo. Attach it to any spl instance and the test vocabulary comes with it. No configuration in the host repo. The entity is self-contained.

---

## Organization for Extraction

Test suites are organized by module, not by test type or by whatever was convenient at the time of writing.

```
suites/
  lib/
    git.js            — travels with lib/git
    rpc-server.js     — travels with lib/rpc-server
  xpath/
    raw.uri.js        — travels with xpath protocols
    data.uri.js
    metadata.uri.js
    raw.js
  git/
    status.js         — travels with spl.mycelium.git
    subtree.js
```

When a module is extracted to its own repo, the tests in its directory go with it. No test archaeology required. No untangling test files that test three modules at once.

The runner supports prefix filtering. `spl-test lib` runs all infrastructure tests. `spl-test xpath` runs all protocol tests. `spl-test lib/rpc-server` runs one suite. The hierarchy serves both day-to-day development and module-scoped verification.

---

## The Harness

The test harness provides two things: CLI execution and fluent assertions.

`spl(streamType, key, value)` spawns the spl CLI with the `raw` modifier (full JSON response), parses the result, and returns it. `splFrom(cwd, ...)` does the same from a specific working directory — essential for testing the two-reality model.

`expect(response)` provides fluent assertions: `.hasValue()`, `.typeIs('leaf')`, `.hasError('not found')`, `.valueContains('text')`. Chain them. The first failure short-circuits and the message tells you what went wrong.

The harness is deliberately simple. No setup/teardown lifecycle. No before/after hooks. No parallel execution. No test isolation beyond what the filesystem provides. Each test is a function that returns `{ pass, message }`. The simplest mechanism that tells you if the system works.

---

## The Runner

The runner walks the suites directory recursively, loads each `.js` file as a suite, runs the tests, and reports. It checks for a running server before starting (PID file first, TCP fallback).

Report format is human-readable on stdout:

```
lib/git (19 tests)
  + exec runs git command
  + status returns branch and files
  - log with count
    expected <= 3 commits, got 10

66 tests, 65 passed, 1 failed
```

The `+` and `-` are enough. You don't need colours and progress bars to know what's broken.

---

## What's Tested

As of the current implementation:

- **lib/git** (19 tests) — exec, status, log, diff, subtrees, detectReality, remote
- **lib/rpc-server** (18 tests) — pid lifecycle, logging, command IPC, running server verification
- **xpath protocols** (18 tests) — raw/data/metadata URI visibility, schema-aware type resolution, into-file navigation
- **git protocols** (11 tests) — status, log, diff through the protocol chain, two-reality model, subtree operations

66 tests total. All passing.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
