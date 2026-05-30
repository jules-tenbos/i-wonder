---
layout: default
lastmod: 2026-05-29
title: "Bare Platform Support"
description: "Bare platform support tiers with architectures and minimum versions, plus instructions for building from source and embedding via the C API."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [Bare Runtime](/engineering/infrastructure/bare/) > Platform Support

# Bare Platform Support

---

## Tier 1 — Prebuilds, CI-tested

Failures block CI. Prebuilt binaries provided via
npm.

| Platform | Architectures | Minimum Version |
|----------|--------------|-----------------|
| Linux | arm64, x64 | >= 5.15, glibc >= 2.35 |
| Android | arm, arm64, ia32, x64 | >= 10 |
| macOS | arm64, x64 | >= 12.0 |
| iOS | arm64, x64 (simulator) | >= 14.0 |
| Windows | arm64, x64 | >= 10 |

## Tier 2 — Known to work, no CI

Regressions possible between releases.

| Platform | Architectures | Minimum Version |
|----------|--------------|-----------------|
| Linux | arm64, x64 | >= 5.10, musl >= 1.2 |
| Linux | arm, ia32 | >= 5.10, musl >= 1.2 |
| Linux | riscv64 | >= 6.8, glibc >= 2.39 |
| Linux | riscv64 | >= 6.6, musl >= 1.2 |
| Linux | mips, mipsel | >= 5.10, musl >= 1.2 |

---

## Building from Source

```
npm i -g bare-make
npm i
bare-make generate
bare-make build
```

Output:
- `build/bin/bare(.exe)`
- `build/libbare.(a|lib)`
- `build/(lib)bare.(dylib|dll|lib)`

Compile options via `--define`:
- `BARE_ENGINE` — JS engine (default: libjs)
- `BARE_PREBUILDS` — enable prebuilds (default: ON)
- `BARE_MEMORY_LIMIT` — JS heap limit (default: 0,
  unlimited)

---

## Embedding (C API)

Bare is designed for embedding. Clean C API via
`bare.h`:

```c
#include <bare.h>
#include <uv.h>

bare_t *bare;
bare_setup(loop, platform, &env, argc, argv,
           options, &bare);
bare_load(bare, filename, source, &module);
bare_run(bare, UV_RUN_DEFAULT);

int exit_code;
bare_teardown(bare, UV_RUN_DEFAULT, &exit_code);
```

Mobile embedding examples:
- [github.com/holepunchto/bare-android](https://github.com/holepunchto/bare-android)
- [github.com/holepunchto/bare-ios](https://github.com/holepunchto/bare-ios)

---

**Source:** [github.com/holepunchto/bare](https://github.com/holepunchto/bare)

