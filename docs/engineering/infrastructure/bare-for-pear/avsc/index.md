[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > [bare-for-pear](/engineering/infrastructure/bare-for-pear/) > avsc

# avsc — Avro Type System

Reference for avsc — a complete pure JavaScript
implementation of the Apache Avro specification,
forked and adapted for the [Bare](/engineering/infrastructure/bare/) runtime.

---

## What avsc Is

avsc is a complete implementation of the
[Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/)
in pure JavaScript. Types, serialization, schema
evolution, container files, IDL parsing — the full
specification surface in a single library.

Forked from [mtth/avsc](https://github.com/mtth/avsc)
and barified for the Bare runtime.

**Source:** [github.com/bare-for-pear/avsc](https://github.com/bare-for-pear/avsc)
**Upstream:** [github.com/mtth/avsc](https://github.com/mtth/avsc)

## What the Fork Changes

The fork replaces Node.js built-in modules with Bare
equivalents. The Avro API is unchanged.

| Concern | Upstream | Fork |
|---------|----------|------|
| Crypto | `crypto` | `bare-crypto` |
| Filesystem | `fs` | `bare-fs` |
| Path | `path` | `bare-path` |
| Streams | `stream` | `bare-stream` |

Additional adaptations:

- **TextEncoder/TextDecoder polyfill** — Bare's
  text-decoder uses a streaming API. avsc expects the
  WHATWG standard `.decode()` and `.encodeInto()`.
  The polyfill bridges this.
- **Buffer/Uint8Array bridging** — conditional
  handling where Bare's buffer semantics differ from
  Node's global Buffer.
- **Bare-only targeting** — the upstream dual-runtime
  support (Node.js + browser) is removed. One runtime,
  no conditional resolution.

The public API surface is identical to upstream. All
[upstream documentation](https://github.com/mtth/avsc/wiki)
applies.

## Reference Pages

- [Type System](types) — schema definition,
  primitives, complex types, logical types, type
  inference, schema evolution
- [Serialization](serialization) — encoding,
  decoding, the Tap buffer, schema fingerprints
- [Container Files](containers) — block
  encoding/decoding streams, file headers, codecs
- [Schema Parsing](schemas) — JSON schemas,
  IDL protocols, import resolution
- [Barification](barification) — what was changed
  from upstream, platform dependencies, polyfills

## Library Reference

The library's own reference site:
[bare-for-pear.github.io/avsc](https://bare-for-pear.github.io/avsc/)
— plain API documentation without architectural
context.
