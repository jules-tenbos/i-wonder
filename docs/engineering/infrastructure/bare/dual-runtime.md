---
layout: default
lastmod: 2026-05-29
title: "Dual-Runtime Config"
description: "How package.json configuration — the imports field plus bare-node-runtime — lets the same code run on both Bare and Node.js without conditional requires."
---

[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [Bare Runtime](/engineering/infrastructure/bare/) > Dual-Runtime Config

# Dual-Runtime Config

Writing code that runs on both Bare and Node.js
without conditional requires or runtime detection.

---

## Package.json Imports Field

The `"imports"` field in package.json maps module
specifiers conditionally by runtime:

```json
{
  "imports": {
    "fs": { "bare": "bare-fs", "default": "fs" },
    "net": { "bare": "bare-net", "default": "net" },
    "path": { "bare": "bare-path", "default": "path" }
  },
  "dependencies": {
    "bare-fs": "^4.7.0",
    "bare-net": "^2.3.1",
    "bare-path": "^3.0.0"
  }
}
```

Code writes `require('fs')` — the runtime resolves
to the correct module. The `"bare"` condition matches
when running in Bare. The `"default"` condition is
the fallback (Node.js).

Unlike Node.js, the `#` prefix on import keys is
not required in Bare — it is supported for
disambiguation but optional.

**Source:**
[github.com/holepunchto/bare-module](https://github.com/holepunchto/bare-module)

---

## Third-Party Node.js Packages

Node.js packages use built-in modules internally.
On Bare, their dependency tree needs remapping. The
`bare-node-runtime` package provides this:

```js
// Set up Node.js globals (Buffer, process, etc.)
require('bare-node-runtime/global')

// Load Node.js package with full import remapping
const pkg = require('some-node-package', {
  with: { imports: 'bare-node-runtime/imports' }
})
```

The `with: { imports }` mechanism applies the
complete Node.js-to-Bare module map to the entire
dependency tree of the required package. The
package and all its dependencies transparently get
Bare equivalents instead of Node.js built-ins.

**Source:**
[github.com/holepunchto/bare-node-runtime](https://github.com/holepunchto/bare-node-runtime)

---

## How It Works Together

For your own code: use `"imports"` in package.json.
Map only the modules you actually use.

For third-party packages: use `bare-node-runtime`
with the `with: { imports }` mechanism. This
handles the full Node.js built-in set.

Example combining both:

```json
{
  "imports": {
    "fs": { "bare": "bare-fs", "default": "fs" },
    "net": { "bare": "bare-net", "default": "net" },
    "path": { "bare": "bare-path", "default": "path" }
  },
  "dependencies": {
    "some-node-package": "^1.0.0",
    "bare-fs": "^4.7.0",
    "bare-net": "^2.3.1",
    "bare-path": "^3.0.0",
    "bare-node-runtime": "^1.2.0"
  }
}
```

```js
// In your code
if (typeof Bare !== 'undefined') {
  require('bare-node-runtime/global')
}
const avro = require('avsc', typeof Bare !== 'undefined'
  ? { with: { imports: 'bare-node-runtime/imports' } }
  : undefined
)
const fs = require('fs')   // resolved by imports field
const net = require('net')  // resolved by imports field
```

The runtime detection (`typeof Bare !== 'undefined'`)
is only needed at the boundary where third-party
packages are loaded. Your own application code stays
clean.

---

## Node.js Compatibility Map

Mapping maintained by bare-node-runtime.

### Supported

These modules are mapped and available — which is not
the same as full API parity. *Supported* means the
common subset is present, not that every Node.js API
matches (see [When remapping isn't
enough](#when-remapping-isnt-enough)).

assert, async_hooks, buffer, child_process,
console, crypto, dgram, diagnostics_channel, dns,
events, fs, http, https, inspector, module, net,
os, path, perf_hooks, process, punycode,
querystring, readline, repl, stream,
string_decoder, timers, tls, tty, url, util, v8,
vm, worker_threads, zlib.

### Unsupported

cluster, constants, domain, http2, sea, sqlite,
sys, test, trace_events, wasi.

---

## When remapping isn't enough

The imports map only remaps module *names*. When the
difference between Node.js and Bare is missing
capability rather than a different name, remapping
cannot close it. The cases below need real work, not a
mapping entry.

**Partial support.** A module being mapped does not
mean full API parity. For example, `crypto` →
`bare-crypto` covers hashing, HMAC, symmetric ciphers,
`randomBytes`, and `pbkdf2` — but not asymmetric
(public-key) crypto: no sign/verify, key-pair
generation, Diffie-Hellman, or X509, and no `scrypt`.
Code that reaches for an API outside the mapped subset
fails even though the module "is supported."

**Native addons.** Node.js N-API / node-gyp addons do
not work through the imports map at all — it routes
JavaScript specifiers, not compiled binaries. Packages
with native bindings must be rebuilt as Bare addons.
This is a hard blocker, not a remapping problem.

**Behavioral differences.** Even a mapped module can
behave differently. Bare's streams are `streamx`, not
Node.js streams; error shapes and event ordering are
not guaranteed identical. Code that depends on exact
Node.js behaviour can break despite a clean mapping.

When these bite, reimplementing for Bare beats
remapping. See
[bare-for-pear](/engineering/infrastructure/bare-for-pear/)
for first-hand examples of where the standard mechanism
breaks and what was done instead.

