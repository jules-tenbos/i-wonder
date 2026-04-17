# Ref Lib Submission — avsc + avsc-rpc

Two module reference sections for engineering/.
avsc: 6 pages. avsc-rpc: 7 pages.

Also update engineering/index.md Technology References
to include these two entries:

- [avsc](avsc/) — Avro type system, serialization, schema evolution (bare-for-pear fork)
- [avsc-rpc](avsc-rpc/) — Avro RPC protocol, service definition, transports (bare-for-pear fork)

===================================================================

=== FILE: engineering/avsc/barification.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc](./) > Barification

# avsc Barification

What was changed from the upstream mtth/avsc to run on
Bare, and why.

---

## Approach

Bare ships with no standard library. Node.js built-ins
like `fs`, `crypto`, `stream`, and `path` do not exist.
Their Bare equivalents — `bare-fs`, `bare-crypto`,
`bare-stream`, `bare-path` — provide the same
functionality through separately installed modules.

The fork replaces all Node.js requires with their Bare
equivalents directly. No conditional imports, no
runtime detection, no compatibility layers. The code
targets one runtime.

## Module Replacements

### platform.js

```javascript
// upstream
let crypto = require('crypto')

// fork
let crypto = require('bare-crypto')
```

Provides `getHash(str, algorithm)` — used for schema
fingerprints (MD5) and protocol handshake hashes.

### files.js

```javascript
// upstream
let fs = require('fs')
let path = require('path')

// fork
let fs = require('bare-fs')
let path = require('bare-path')
```

Provides import hooks for IDL file resolution —
reading `.avdl`, `.avsc`, and `.avpr` files from the
filesystem.

### index.js

```javascript
// upstream
let fs = require('fs')

// fork
let fs = require('bare-fs')
```

The main entry point uses filesystem access for
container file convenience functions
(`createFileDecoder`, `createFileEncoder`,
`extractFileHeader`).

### containers.js

```javascript
// upstream
let stream = require('stream')

// fork
let stream = require('bare-stream')
```

Block and raw encoder/decoder streams for Avro
container file I/O.

## TextEncoder/TextDecoder Polyfill

**File:** `lib/encoding.js`

Bare's `text-decoder` module provides a streaming API
(`push`/`write`/`end`). avsc expects the WHATWG
standard API — `TextDecoder.decode(buf)` and
`TextEncoder.encodeInto(str, buf)`.

The polyfill provides WHATWG-compliant implementations
with full UTF-8 support (1–4 byte sequences, surrogate
pair handling). It installs on `globalThis` only if the
standard API is absent.

Auto-loaded via `require('./encoding')` in `utils.js`.

## Buffer Handling

`utils.js` contains conditional logic that checks for
`Buffer` availability:

```javascript
if (typeof Buffer === 'function') {
  // Use Buffer methods
} else {
  // Fall back to Uint8Array operations
}
```

On Bare, `Buffer` is available when `bare-buffer` is
required but is not a global. The conditional handling
ensures avsc works whether Buffer is present or not.

## Package.json

Upstream avsc v6 had a conditional imports field:

```json
{
  "imports": {
    "fs": { "bare": "bare-fs", "default": "fs" },
    "crypto": { "bare": "bare-crypto", "default": "crypto" }
  }
}
```

The fork strips this to:

```json
{
  "name": "avsc",
  "main": "lib/index.js"
}
```

No conditional resolution. Direct requires to bare-*
modules throughout. One runtime, one code path.

## Platform Dependencies

Required at runtime, installed by `bin/setup`:

| Module | Version | Purpose |
|--------|---------|---------|
| bare-crypto | 4.7.0 | Schema fingerprints, protocol hashes |
| bare-fs | 4.7.0 | Container file I/O, IDL imports |
| bare-path | 3.0.0 | IDL import path resolution |
| bare-stream | 2.13.0 | Container encoding/decoding streams |

These are platform dependencies — not committed to the
repository, populated by the setup script into `lib/`.
The `node_modules → lib/` symlink makes them
resolvable by name.

See [Code Implementation](../implementation/code-development)
for the full dependency management model.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc/containers.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc](./) > Container Files

# avsc Container Files

Avro container files — self-describing binary files
that embed the writer schema with the data. The
container is how data travels with its own carrier
description.

---

## What Containers Are

An Avro container file (also called Object Container
File or OCF) bundles:

1. A **header** — magic bytes, writer schema, sync
   marker, optional codec
2. **Data blocks** — sequences of records encoded with
   the writer schema

The writer schema travels with the data. Any reader
with a compatible reader schema can decode the
contents. No external registry needed.

This is AVRO's native answer to the question: how does
data describe itself? The container embeds the carrier
description. The reader brings the meaning lens.

## Reading

```javascript
const avro = require('avsc')

avro.createFileDecoder('./data.avro')
  .on('metadata', (type) => {
    // type is the writer's schema — what the data is
  })
  .on('data', (val) => {
    // val is a decoded record
  })
```

With a reader schema (schema evolution):

```javascript
const readerType = avro.Type.forSchema({ ... })

avro.createFileDecoder('./data.avro', { readerType })
  .on('data', (val) => {
    // val decoded through reader's lens
  })
```

## Writing

```javascript
const schema = {
  type: 'record',
  name: 'Entry',
  fields: [
    { name: 'key', type: 'string' },
    { name: 'value', type: 'bytes' }
  ]
}

const encoder = avro.createFileEncoder('./out.avro', schema)
encoder.write({ key: '/path', value: Buffer.from('data') })
encoder.write({ key: '/other', value: Buffer.from('more') })
encoder.end()
```

## Header Extraction

Synchronous header reading without streaming the
entire file:

```javascript
const header = avro.extractFileHeader('./data.avro')
// header.meta['avro.schema'] — parsed writer schema
// header.meta['avro.codec'] — compression codec
// header.sync — 16-byte sync marker
```

## Stream Classes

The underlying stream implementations, available for
custom pipelines:

```javascript
const { BlockDecoder, BlockEncoder,
        RawDecoder, RawEncoder } = avro.streams
```

| Class | Direction | Description |
|-------|-----------|-------------|
| `BlockDecoder` | Read | Decodes container-format input |
| `BlockEncoder` | Write | Encodes records into container blocks |
| `RawDecoder` | Read | Decodes raw Avro binary (no container framing) |
| `RawEncoder` | Write | Encodes records as raw Avro binary |

Block streams handle the container format — header,
sync markers, block boundaries. Raw streams handle
bare record sequences — no container overhead.

All stream classes use `bare-stream` Duplex in the
fork.

## Container Structure

```
[magic: 4 bytes "Obj\x01"]
[header: avro record]
  meta: map<string, bytes>
    "avro.schema": writer schema as JSON
    "avro.codec": "null" | "deflate" | "snappy"
  sync: 16 bytes (random marker)
[block]*
  count: long (number of records)
  size: long (byte size of encoded records)
  data: bytes (encoded records, possibly compressed)
  sync: 16 bytes (must match header)
```

The sync marker detects corruption and enables random
access — seek to any sync marker and start reading
blocks from there.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc/index.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > avsc

# avsc — Avro Type System

Reference for avsc — the pure JavaScript Avro
implementation that provides mycelium's type system,
serialization, and schema resolution.

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

## Why avsc Is Constitutive

avsc is not a utility dependency. It is the language
through which mycelium articulates data.

Every message in the fabric is an Avro record. Every
schema contract between processes is expressed in Avro
types. Every protocol operation is defined through Avro
schema definitions. The type system is not a
serialization choice — it is the carrier language
itself.

This makes avsc constitutive. The architecture depends
on it the way it depends on git — not as a tool but as
a substrate. Changes to avsc are changes to the
language the system speaks. It is forked, maintained
locally, and treated as Splectrum code.

See [AVRO Design Scope](../mycelium/avro-design-scope)
for the full architectural role of Avro in mycelium.

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
— plain API documentation without the architectural
context.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc/schemas.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc](./) > Schema Parsing

# avsc Schema Parsing

Schema definition formats — JSON schemas and Avro IDL
— and how avsc parses them into Type instances.

---

## JSON Schemas

The primary schema format. A JSON object that
describes an Avro type.

```javascript
const avro = require('avsc')

// Parse from JSON text
const type = avro.readSchema(`{
  "type": "record",
  "name": "spl.mycelium.Message",
  "fields": [
    { "name": "key", "type": "string" },
    { "name": "value", "type": "bytes" }
  ]
}`)
```

`readSchema` parses JSON text into schema attributes.
`Type.forSchema` takes schema attributes (a JavaScript
object) and returns a Type instance.

## Avro IDL

Avro's Interface Definition Language — a more readable
format for defining protocols with multiple types and
messages.

```
@namespace("spl.mycelium")
protocol Mycelium {

  record Message {
    long offset = 0;
    long timestamp;
    string key;
    bytes value;
    Headers headers;
  }

  record Headers {
    Record record;
    array<ContextEntry> context;
  }
}
```

### Parsing IDL

```javascript
// Async — resolves imports from filesystem
avro.assembleProtocol('./protocol.avdl', (err, attrs) => {
  // attrs is the protocol definition
  // attrs.types contains all defined types
  // attrs.messages contains all defined messages
})
```

```javascript
// Parse protocol from schema object (not IDL)
const attrs = avro.readProtocol(protocolObj)
```

### IDL Import Resolution

IDL files can import other IDL files. avsc resolves
imports from the filesystem using `bare-fs` and
`bare-path` in the fork.

```
// In an .avdl file:
import idl "common-types.avdl";
import schema "external-type.avsc";
import protocol "other-protocol.avpr";
```

The `files.js` module provides synchronous and
asynchronous import hooks that resolve paths relative
to the importing file.

## Protocols

A protocol defines a named scope containing types and
messages. In Avro's model, a protocol is what avsc-rpc
uses to create services.

```javascript
const protocol = {
  protocol: 'ExecutionService',
  namespace: 'spl.mycelium.process.execute',
  types: [
    // Record, enum, fixed type definitions
  ],
  messages: {
    exec: {
      request: [{ name: 'message', type: 'Message' }],
      response: 'Message'
    }
  }
}
```

The protocol is the bridge between avsc (types) and
avsc-rpc (services). avsc parses and resolves the
types. avsc-rpc takes the protocol and creates a
service with client/server channels.

## Namespaces

Avro namespaces are dot-separated paths that qualify
type names. In mycelium, the namespace is not just
organisational — it is architecturally constitutive.
The namespace identifies the meaning language.

```javascript
// Fully qualified
'spl.mycelium.Message'

// Namespace inherited from enclosing record
{
  namespace: 'spl.mycelium',
  name: 'Message'    // resolves to spl.mycelium.Message
}
```

avsc resolves namespaces following Avro specification
rules — inner types inherit the namespace of their
enclosing type unless explicitly overridden.

See [AVRO Design Scope](../mycelium/avro-design-scope)
— section 8, Namespacing — for how this serves the
architecture.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc/serialization.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc](./) > Serialization

# avsc Serialization

Avro binary encoding as implemented in avsc. Compact,
self-describing where needed, and deterministic.

---

## Binary Encoding

Avro uses a compact binary format. No field names in
the output, no type tags on primitives. The schema
is the codec — encoder and decoder must agree on the
schema to communicate.

This is the carrier principle made physical. The
binary stream carries content. The schema — present
elsewhere — provides meaning.

```javascript
const type = avro.Type.forSchema({
  type: 'record',
  name: 'Entry',
  fields: [
    { name: 'key', type: 'string' },
    { name: 'value', type: 'bytes' }
  ]
})

const buf = type.toBuffer({ key: '/path', value: Buffer.from('data') })
// buf is compact binary — no field names, no framing

const val = type.fromBuffer(buf)
// val is { key: '/path', value: <Buffer 64 61 74 61> }
```

## The Tap

avsc's internal binary reader/writer. A cursor over a
byte buffer that reads and writes Avro primitives in
sequence.

The Tap is not public API in the conventional sense,
but it is the mechanism behind all encoding and
decoding. Understanding it clarifies how Avro binary
works.

```javascript
const { Tap } = require('avsc/lib/utils')

const buf = new Uint8Array(1024)
const tap = new Tap(buf)

// Write
tap.writeLong(42)
tap.writeString('hello')

// Read
tap.pos = 0
tap.readLong()    // 42
tap.readString()  // 'hello'
```

Integers use zigzag varint encoding — small values
take fewer bytes. Strings and bytes are length-prefixed
with a varint.

## Schema Fingerprints

Every schema has a deterministic fingerprint — a hash
of its canonical JSON representation. Used for schema
identification without transmitting the full schema.

```javascript
const fp = type.fingerprint('md5')
// 16-byte Buffer — the schema's identity
```

In mycelium, schema fingerprints are used in the RPC
handshake — client and server compare fingerprints to
determine if they share a protocol.

The `platform.js` module provides `getHash()` using
`bare-crypto` for MD5 computation.

## Encoding Characteristics

| Aspect | Detail |
|--------|--------|
| Null | 0 bytes |
| Boolean | 1 byte |
| Int/Long | 1–10 bytes (zigzag varint) |
| Float | 4 bytes (IEEE 754) |
| Double | 8 bytes (IEEE 754) |
| Bytes | varint length + raw bytes |
| String | varint length + UTF-8 bytes |
| Record | concatenated field encodings |
| Array | blocks of [count, items...], terminated by 0 |
| Map | blocks of [count, [key, value]...], terminated by 0 |
| Union | varint branch index + branch encoding |
| Enum | varint symbol index |
| Fixed | raw bytes (size from schema) |

No framing, no delimiters, no padding. The encoding
is fully determined by the schema. Two records of the
same type concatenated in a buffer are distinguishable
only because the schema says where one ends and the
next begins.

## JSON Encoding

avsc also supports JSON encoding for debugging and
interop:

```javascript
const jsonStr = JSON.stringify(type.toJSON(val))
const val = type.fromJSON(JSON.parse(jsonStr))
```

JSON encoding includes type tags for unions and uses
string representations for bytes. Larger than binary
but human-readable.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc/types.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc](./) > Type System

# avsc Type System

The Avro type system as implemented in avsc. This is
the carrier language — the structural vocabulary
through which mycelium articulates data.

---

## Type.forSchema

The primary entry point. Takes an Avro schema
definition and returns a Type instance that can
encode, decode, validate, and compare values.

```javascript
const avro = require('avsc')

const type = avro.Type.forSchema({
  type: 'record',
  name: 'spl.mycelium.Message',
  fields: [
    { name: 'offset', type: 'long', default: 0 },
    { name: 'timestamp', type: 'long' },
    { name: 'key', type: 'string' },
    { name: 'value', type: 'bytes', default: '' },
    { name: 'headers', type: 'Headers' }
  ]
})
```

### Options

| Option | Description |
|--------|-------------|
| `logicalTypes` | Map of logical type names to implementations |
| `namespace` | Default namespace for unqualified names |
| `noAnonymousTypes` | Require all types to be named |
| `registry` | Shared type registry for cross-schema references |
| `typeHook` | Intercept type creation |
| `wrapUnions` | Union representation strategy |

## Type.forValue

Infers a schema from a JavaScript value. Useful for
quick prototyping — the inferred type can encode any
structurally compatible value.

```javascript
const type = avro.Type.forValue({
  key: '/blog/submissions',
  value: Buffer.from('hello')
})
```

## Primitive Types

| Avro Type | JavaScript Type | Size |
|-----------|----------------|------|
| `null` | `null` | 0 bytes |
| `boolean` | `boolean` | 1 byte |
| `int` | `number` | 1–5 bytes (varint) |
| `long` | `number` | 1–10 bytes (varint) |
| `float` | `number` | 4 bytes |
| `double` | `number` | 8 bytes |
| `bytes` | `Buffer` | variable |
| `string` | `string` | variable |

All primitives use Avro's binary encoding — varints
for integers, IEEE 754 for floats, length-prefixed for
bytes and strings.

## Complex Types

### Record

Named type with ordered fields. The fundamental
structure in mycelium — every message, every schema
contract, every protocol definition is a record.

```javascript
{
  type: 'record',
  name: 'spl.mycelium.operator.Record',
  fields: [
    { name: 'schema', type: 'string' },
    { name: 'args', type: ['null', 'bytes'], default: null }
  ]
}
```

Fields support defaults, ordering hints, and
documentation. Field order determines binary layout.

### Enum

Named type with a fixed set of symbols.

```javascript
{
  type: 'enum',
  name: 'Mode',
  symbols: ['SYNC', 'ASYNC', 'FIRE_AND_FORGET']
}
```

### Array

Ordered collection of a single item type.

```javascript
{ type: 'array', items: 'string' }
```

### Map

Key-value pairs. Keys are always strings. Values are
a single type.

```javascript
{ type: 'map', values: 'bytes' }
```

### Union

One of several types. Represented as a JSON array.

```javascript
['null', 'string', 'bytes']
```

Avro unions carry a type index — the decoder knows
which branch was encoded. This is what makes the
`['null', 'bytes']` pattern work for optional fields
without ambiguity.

### Fixed

Fixed-size byte array.

```javascript
{ type: 'fixed', name: 'Hash', size: 16 }
```

## Logical Types

Logical types attach semantic meaning to a physical
type. The physical type carries the data. The logical
type declares what it means.

```javascript
class TimestampType extends avro.types.LogicalType {
  _fromValue (val) { return new Date(val) }
  _toValue (date) { return +date }
  _resolve (type) {
    if (avro.Type.isType(type, 'long')) {
      return this._fromValue
    }
  }
}

const type = avro.Type.forSchema({
  type: 'long',
  logicalType: 'timestamp'
}, { logicalTypes: { timestamp: TimestampType } })
```

This is the carrier/meaning separation at the type
level. The `long` carries. The `timestamp` means.
Same binary representation, different interpretation
depending on which logical type is in scope.

## Schema Evolution

Avro's native schema resolution — writer schema versus
reader schema — is the mechanism behind mycelium's
relational type system. A reader does not ask "is this
type X." It asks "can this record be read as X."

```javascript
const writerType = avro.Type.forSchema({
  type: 'record',
  name: 'Event',
  fields: [
    { name: 'id', type: 'long' },
    { name: 'name', type: 'string' }
  ]
})

const readerType = avro.Type.forSchema({
  type: 'record',
  name: 'Event',
  fields: [
    { name: 'id', type: 'long' },
    { name: 'name', type: 'string' },
    { name: 'source', type: 'string', default: 'unknown' }
  ]
})

// Reader can read writer's data — new field gets default
const resolver = readerType.createResolver(writerType)
const val = readerType.fromBuffer(buf, resolver)
```

Resolution rules:

- **Reader adds a field with default** — compatible.
  The default fills in.
- **Writer has extra fields** — compatible. Reader
  ignores them.
- **Type promotion** — int to long, float to double.
  Compatible.
- **Name mismatch** — incompatible. The nominal gate
  enforces language commitment.

This is not versioning machinery. It is discovery at
the point of contact.

## Type Methods

Every Type instance provides:

| Method | Description |
|--------|-------------|
| `toBuffer(val)` | Encode value to binary |
| `fromBuffer(buf, resolver?, noCheck?)` | Decode binary to value |
| `isValid(val)` | Check value conforms |
| `compare(val1, val2)` | Sort-order comparison |
| `compareBuffers(buf1, buf2)` | Binary-level comparison |
| `clone(val, opts?)` | Deep copy with optional coercion |
| `createResolver(writerType)` | Schema evolution resolver |
| `schema(opts?)` | Return the JSON schema |
| `fingerprint(algorithm?)` | Schema hash |
| `random()` | Generate random conforming value |

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/barification.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Barification

# avsc-rpc Barification

What was changed from the upstream avsc v5 services
code to run as a standalone module on Bare.

---

## Two Operations

avsc-rpc required two distinct adaptations:

1. **Extraction** — separating the RPC layer from
   the avsc monolith into a standalone module
2. **Barification** — replacing Node.js dependencies
   with Bare equivalents

Both happened together. The result is a standalone
module that depends on avsc as a peer for types and
utils, and on Bare platform modules for runtime
primitives.

## Extraction from avsc

The upstream `services.js` lived inside avsc and
imported its siblings with relative paths:

```javascript
// upstream (inside avsc)
let types = require('./types')
let utils = require('./utils')
let platform = require('./platform')
```

The fork imports from the avsc sibling:

```javascript
// fork (standalone)
let types = require('../avsc/lib/types')
let utils = require('../avsc/lib/utils')
let avscPlatform = require('../avsc/lib/platform')
```

This works because both libraries sit under `lib/`
in the spl codebase. The relative path resolves at
the filesystem level — no package manager involved.

## Stream Adaptation

The most significant change. Upstream used Node.js
`stream.Transform`. The fork uses streamx.Transform.

### API Differences

| Concern | Node stream.Transform | streamx.Transform |
|---------|----------------------|-------------------|
| Constructor | `{ readableObjectMode: true }` | `{ ... }` |
| Transform | `_transform(buf, encoding, cb)` | `_transform(buf, cb)` |
| Unpipe | `.unpipe()` available | Not available |
| Error on close | Emits error | Suppressed |

### Affected Classes

Four internal stream classes were changed:

- `FrameDecoder` — standard Avro frame decoder
- `FrameEncoder` — standard Avro frame encoder
- `NettyDecoder` — Netty-compatible frame decoder
- `NettyEncoder` — Netty-compatible frame encoder

All extend `streamx.Transform` instead of
`stream.Transform`.

### Error Handling

Node streams emit errors on unexpected close. streamx
does not. The fork adds `decoder.on('error', () => {})`
to suppress expected errors when connections close
during frame decoding. This is not error swallowing —
channel-level error handling still operates.

## The v5/v6 Bridge

avsc-rpc was written against avsc v5. The fork pairs
it with avsc v6 (the barified fork). The compatibility
module (`compat.js`) bridges the differences.

### Hash Results

avsc v6's `platform.getHash()` returns Uint8Array.
The services code calls `.toString('binary')` and
`.readInt16BE()` on hash results — methods that exist
on Buffer but not Uint8Array.

```javascript
function wrapGetHash (originalGetHash) {
  return function getHash (str, algorithm) {
    let arr = originalGetHash(str, algorithm)
    return Buffer.from(arr.buffer, arr.byteOffset, arr.length)
  }
}
```

### Removed Utilities

avsc v6 removed several utility functions that
services code still references:

| Function | Purpose | Shim |
|----------|---------|------|
| `newBuffer(size)` | Allocate buffer | `Buffer.alloc(size)` |
| `bufferFrom(data, enc)` | Create buffer from data | `Buffer.from(data, enc)` |
| `addDeprecatedGetters` | Attach deprecated properties | No-op |
| `debuglog` | Debug logger factory | Returns no-op |
| `deprecate` | Mark function deprecated | Identity (returns fn) |

### process.nextTick

Bare does not provide a global `process`. The services
code uses `process.nextTick` for deferred execution.

```javascript
function ensureProcess () {
  if (typeof process === 'undefined') {
    globalThis.process = { nextTick: queueMicrotask }
  } else if (!process.nextTick) {
    process.nextTick = queueMicrotask
  }
}
```

Called once at module load.

## Module Dependencies

### From avsc (peer, constitutive)

- `types` — Avro type system, schema resolution
- `utils` — buffer operations, Tap, helpers
- `platform` — hash computation

### From Bare (platform)

| Module | Purpose |
|--------|---------|
| bare-buffer | Buffer API for hash wrapping, message framing |
| bare-events | EventEmitter for Service, Client, Server |
| bare-stream | Stream base classes |
| streamx | Transform streams for frame encoding/decoding |

## Module Structure

```
services.js   — 2470 lines. Service, Client, Server,
                channels (stateful/stateless, client/server),
                message framing, handshake, multiplexing,
                middleware chain, protocol negotiation.

compat.js     — 55 lines. v5/v6 bridge: hash wrapping,
                removed utils, process.nextTick polyfill,
                debug/deprecation no-ops.
```

One large module — same structure as upstream. The
extraction preserved the original file organisation.
Internal classes (channels, adapters, registries) are
not factored out because the upstream kept them
together and the coupling is deliberate — channels
depend intimately on the handshake and framing logic.

See [Code Implementation](../implementation/code-development)
for the full dependency management and subtree
workflow. See the
[API Reference](https://github.com/bare-for-pear/avsc-rpc/blob/main/doc/api.md)
for the complete method and option documentation.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/client-server.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Client and Server

# avsc-rpc Client and Server

Creating RPC endpoints, registering handlers, and
making calls.

---

## Server

A server binds handlers to protocol messages. Each
handler receives a typed request and returns a typed
response through the schema contract.

```javascript
const server = service.createServer()
```

### Registering Handlers

Handler method names are generated from message names
with capitalised first letter:

```javascript
// For message 'exec':
server.onExec((message, cb) => {
  // message is the decoded request (typed by schema)
  // cb(err, response) — response typed by schema
  cb(null, responseMessage)
})
```

To suppress capitalisation:

```javascript
const server = service.createServer({ noCapitalize: true })
server.on_exec((message, cb) => { ... })
```

### Default Handler

Catch-all for unmapped messages:

```javascript
const server = service.createServer({
  defaultHandler (wreq, wres, next) {
    wres.error = 'not implemented'
    next()
  }
})
```

### Server Options

| Option | Default | Description |
|--------|---------|-------------|
| `silent` | `false` | Suppress error logging |
| `strictTypes` | `false` | Strict error type coercion |
| `defaultHandler` | — | Handler for unmapped messages |
| `noCapitalize` | `false` | Preserve message name casing |
| `remoteProtocols` | — | Pre-populate protocol cache |

## Client

A client emits typed messages to a remote server.
Methods are generated from the protocol's message
definitions.

```javascript
const client = service.createClient()
```

### Making Calls

Generated methods match message names:

```javascript
// For message 'exec':
client.exec(message, (err, response) => {
  // err is typed by the error schema
  // response is typed by the response schema
})
```

With options:

```javascript
client.exec(message, { timeout: 5000 }, (err, response) => {
  ...
})
```

### Lower-Level Call

```javascript
client.emitMessage('exec', request, opts, (err, response) => {
  ...
})
```

### Client Options

| Option | Default | Description |
|--------|---------|-------------|
| `server` | — | In-memory server (auto-connects) |
| `transport` | — | Transport stream (auto-creates channel) |
| `buffering` | `false` | Buffer calls before channel ready |
| `timeout` | `10000` | Message timeout in ms |
| `strictTypes` | `false` | Strict error type coercion |
| `channelPolicy` | — | Custom channel selection |
| `remoteProtocols` | — | Pre-populate protocol cache |

## In-Memory Connection

The simplest pattern — client and server in the same
process, no serialization overhead:

```javascript
const server = service.createServer()
server.onExec((message, cb) => {
  cb(null, response)
})

const client = service.createClient({ server })
client.exec(message, (err, res) => { ... })
```

This is the pattern used for testing and for
subject-internal operations where processes
communicate within the same runtime. The RPC boundary
is still enforced — messages are validated against the
schema contract. Only the transport is eliminated.

## Channel Lifecycle

Both client and server expose channel management:

```javascript
// Create a channel on a transport
client.createChannel(transport, opts)
server.createChannel(transport, opts)

// List active channels
client.activeChannels()
server.activeChannels()

// Destroy all channels
client.destroyChannels()
```

Channels are created per-transport. A client may have
multiple channels to different servers. A server may
serve multiple clients simultaneously.

### Events

**Client channels:**
- `'handshake'` — protocol negotiation complete
- `'outgoingCall'` — message sent
- `'eot'` — end of transmission
- `'error'` — channel error

**Server channels:**
- `'handshake'` — protocol negotiation complete
- `'incomingCall'` — message received
- `'eot'` — end of transmission
- `'error'` — channel error

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/index.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > avsc-rpc

# avsc-rpc — Avro RPC Protocol

Reference for avsc-rpc — the Avro RPC protocol layer
that provides mycelium's process boundary enforcement.

---

## What avsc-rpc Is

avsc-rpc is the Avro RPC/IPC implementation extracted
from avsc v5 and maintained as a standalone library for
the Bare runtime. Service definition, client/server
creation, transport channels, middleware, and protocol
negotiation.

The RPC layer was removed from avsc in v6
([PR #428](https://github.com/mtth/avsc/pull/428)).
This module preserves and maintains it independently.

**Source:** [github.com/bare-for-pear/avsc-rpc](https://github.com/bare-for-pear/avsc-rpc)
**Extracted from:** commit `dd82783` of mtth/avsc

## Why avsc-rpc Is Constitutive

RPC is not a communication mechanism in mycelium. It is
the process boundary enforcement mechanism.

Two processes communicating through RPC can only see
each other through the schema contract. No shared
objects, no classpath leakage, no hidden state. Even
in local in-memory execution, the RPC boundary
guarantees that only schema-conformant messages pass.
This is what makes the architecture's claim —
no transitive dependencies between processes — a
physical fact rather than a convention.

Transport pluggability is a consequence, not the
motivation. The same schema contract holds whether the
transport is in-memory, TCP, or HTTP. The transport
adapts to context. The boundary is invariant.

This makes avsc-rpc constitutive alongside avsc itself.
Together they provide the complete Avro primitive:
types and serialization from avsc, protocol and
boundary from avsc-rpc.

See [AVRO Design Scope](../mycelium/avro-design-scope)
— section 11, RPC as Constitutive Dependency — for the
full architectural role.

## What the Fork Changes

The extraction adapted the code for standalone use on
Bare:

| Concern | Upstream (avsc v5) | Fork |
|---------|--------------------|------|
| Streams | `stream.Transform` | `streamx.Transform` |
| Buffer | `buffer` | `bare-buffer` |
| Events | `events` | `bare-events` |
| Streams | `stream` | `bare-stream` |

Additional adaptations:

- **streamx transport** — all frame encoder/decoder
  classes use streamx.Transform. Two-parameter
  `_transform(buf, cb)` — no encoding argument.
- **v5/v6 compatibility bridge** (`compat.js`) —
  avsc-rpc was written against avsc v5. The fork pairs
  it with avsc v6. The bridge handles hash result
  types (Uint8Array to Buffer), restored utility
  functions, and `process.nextTick` polyfill via
  `queueMicrotask`.
- **Peer dependency on avsc** — types and utils are
  imported directly from the avsc sibling. Both
  libraries live together under `lib/`.

## Reference Pages

- [Service Definition](services) — protocols,
  messages, Service.forProtocol, type resolution
- [Client and Server](client-server) — creating
  clients and servers, handler registration, options
- [Transports](transports) — in-memory, TCP,
  HTTP, channel lifecycle, stateful vs stateless
- [Middleware](middleware) — request/response
  chain, use patterns
- [Wire Protocol](wire-protocol) — handshake,
  framing, Netty compatibility, protocol negotiation
- [Barification](barification) — streamx
  adaptation, v5/v6 bridge, platform dependencies

## Library Reference

The library's own reference site:
[bare-for-pear.github.io/avsc-rpc](https://bare-for-pear.github.io/avsc-rpc/)
— complete API documentation including full method
signatures, all options, and wire format details.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/middleware.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Middleware

# avsc-rpc Middleware

Request and response interception on both client and
server. The mechanism for cross-cutting concerns —
tracing, logging, authentication, context propagation.

---

## Model

Middleware functions are registered with `.use()` and
execute in order for each message. They receive the
writable request, writable response, and a `next`
callback to continue the chain.

The chain is bidirectional — middleware can act on
the outgoing request and on the incoming response.

```
client middleware → transport → server middleware → handler
                                                      ↓
client middleware ← transport ← server middleware ← response
```

## Client Middleware

Intercepts outgoing calls and incoming responses:

```javascript
client.use((wreq, wres, next) => {
  // Before: outgoing request
  console.log('calling:', wreq.header.method)

  next(null, (err, prev) => {
    // After: incoming response
    console.log('response received')
    prev(err)
  })
})
```

### wreq (Writable Request)

| Property | Description |
|----------|-------------|
| `wreq.header` | Message header (method name, etc.) |
| `wreq.request` | The typed request object |

### wres (Writable Response)

| Property | Description |
|----------|-------------|
| `wres.response` | The typed response (after handler) |
| `wres.error` | Error value (after handler) |

## Server Middleware

Intercepts incoming calls before the handler:

```javascript
server.use((wreq, wres, next) => {
  // Before handler
  const start = Date.now()

  next(null, (err, prev) => {
    // After handler
    console.log('handled in', Date.now() - start, 'ms')
    prev(err)
  })
})
```

## Chaining

Multiple middleware functions execute in registration
order:

```javascript
server.use(
  tracing,
  authentication,
  logging
)

// Or individually:
server.use(tracing)
server.use(authentication)
server.use(logging)
```

## Use in Mycelium

Middleware is the natural point for context metadata
propagation. The mycelium message shape includes a
context array — key-value pairs that accumulate
through the processing pipeline. Middleware can:

- **Inject context** — add entries to the context
  on the way in (tracing IDs, timestamps, caller
  identity)
- **Read context** — inspect accumulated context
  for routing or authorisation decisions
- **Enrich context** — add entries on the way out
  (execution metadata, timing, handler identity)

The middleware chain and the message context array
serve the same purpose at different levels — the
chain is the runtime mechanism, the context is the
data trail.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/services.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Service Definition

# avsc-rpc Service Definition

How protocols become services — the bridge from schema
to executable boundary.

---

## Service.forProtocol

The primary entry point. Takes an Avro protocol and
returns a Service instance that can create clients and
servers.

```javascript
const { Service } = require('avsc-rpc')

const service = Service.forProtocol({
  protocol: 'ExecutionService',
  namespace: 'spl.mycelium.process.execute',
  messages: {
    exec: {
      request: [{ name: 'message', type: 'Message' }],
      response: 'Message'
    }
  },
  types: [
    // Type definitions used by messages
  ]
})
```

The protocol defines the contract. The service
enforces it. Every message that crosses the boundary
is validated against the protocol's type definitions.

### Options

| Option | Description |
|--------|-------------|
| `strictTypes` | Strict error type coercion |

## Protocol Structure

A protocol is an Avro protocol definition — types and
messages scoped under a name and namespace.

```javascript
{
  protocol: 'Name',           // service name
  namespace: 'spl.mycelium',  // Avro namespace
  types: [ ... ],             // shared type definitions
  messages: {
    methodName: {
      request: [ ... ],       // argument fields
      response: 'TypeName',   // return type
      errors: [ ... ],        // error types (optional)
      'one-way': false        // fire-and-forget (optional)
    }
  }
}
```

## Messages

Each message in the protocol becomes a typed RPC
method. The Message class holds the Avro types for
request, response, and errors.

```javascript
const msg = service.message('exec')
msg.name          // 'exec'
msg.requestType   // Avro RecordType for request args
msg.responseType  // Avro Type for response
msg.errorType     // Avro UnionType for errors
msg.oneWay        // boolean
```

## Service Methods

| Method | Description |
|--------|-------------|
| `Service.forProtocol(ptcl, opts)` | Create service from protocol |
| `Service.compatible(client, server)` | Check protocol compatibility |
| `Service.isService(any)` | Type check |
| `service.createClient(opts)` | Create RPC client |
| `service.createServer(opts)` | Create RPC server |
| `service.message(name)` | Get message by name |
| `service.type(name)` | Get type by name |
| `service.hash` | Protocol fingerprint |
| `service.name` | Qualified service name |
| `service.protocol` | Protocol schema object |
| `service.types` | Frozen array of types |
| `service.messages` | Frozen array of messages |

## Protocol Hash

The service hash is the MD5 fingerprint of the
protocol's canonical representation. Used during the
RPC handshake — client and server compare hashes to
determine if they share a protocol before exchanging
messages.

```javascript
service.hash  // Buffer — 16-byte MD5
```

If hashes match, the handshake succeeds immediately.
If not, the server sends its protocol to the client
for resolution. This is Avro's native protocol
negotiation — no external registry.

## Compatibility Check

```javascript
Service.compatible(clientService, serverService)
// true if client's protocol can communicate with server's
```

Uses Avro's type resolution rules — the same
mechanism as schema evolution. A client with fewer
message types can communicate with a richer server.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/transports.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Transports

# avsc-rpc Transports

How RPC messages move between client and server. The
transport is a deployment concern — the schema contract
is invariant.

---

## Transport Model

avsc-rpc separates the protocol boundary (schema
contract, handshake, message encoding) from the
transport (how bytes move). Handler code is
transport-agnostic. The same service definition works
across all transports.

Two categories:

- **Stateful** — persistent connection, single
  handshake, multiplexed messages. TCP, in-memory.
- **Stateless** — handshake per request, one
  message per connection. HTTP.

## In-Memory

Direct object passing between client and server in
the same process. No serialization, no framing.

```javascript
const client = service.createClient({ server })
```

Or explicitly:

```javascript
const client = service.createClient()
client.createChannel(server.createChannel, {
  objectMode: true
})
```

Used for testing and subject-internal communication.
The RPC boundary is enforced — schema validation
happens — but there is no wire encoding.

## TCP (Stateful)

Persistent connection with a single handshake and
multiplexed messages. The natural transport for
inter-process communication.

```javascript
const net = require('bare-net')

// Server
const tcpServer = net.createServer((socket) => {
  server.createChannel(socket)
})
tcpServer.listen(8090)

// Client
const socket = net.connect(8090)
client.createChannel(socket)
```

The socket is both readable and writable — avsc-rpc
uses it as a duplex transport. Messages are
multiplexed with ID headers so responses match
requests.

### Reconnection

TCP channels do not auto-reconnect. When a connection
drops, the channel emits `'eot'` and is destroyed.
Create a new channel on a new socket.

```javascript
function connect () {
  const socket = net.connect(8090)
  const channel = client.createChannel(socket)
  channel.on('eot', () => {
    // Reconnect after delay
    setTimeout(connect, 1000)
  })
}
```

## HTTP (Stateless)

Request-response pattern. Each message is a complete
interaction — handshake, request, response.

```javascript
client.createChannel((cb) => {
  // cb(err, readable) when response arrives
  const req = http.request(opts, (res) => cb(null, res))
  cb(null, req)  // return writable for request
})
```

The factory function is called for each message.
Suitable for HTTP servers, serverless functions, or
any request-response protocol.

## Channel Options

| Option | Default | Description |
|--------|---------|-------------|
| `objectMode` | `false` | `true`: object passing. `false`: binary framing |
| `noPing` | `false` | Skip initial handshake ping |
| `timeout` | `10000` | Per-channel timeout in ms |
| `endWritable` | `true` | End writable after stateless request |
| `scope` | — | Message ID scoping |
| `serverHash` | — | Pre-populate protocol adapter |

### objectMode

When `true`, messages pass as JavaScript objects —
no serialization. Used for in-memory transports.

When `false` (default), messages are serialized using
Avro binary encoding with wire framing. Two framing
formats are available (see
[Wire Protocol](wire-protocol.md)):

- **Standard** (FrameEncoder/FrameDecoder) — Avro
  specification framing
- **Netty** (NettyEncoder/NettyDecoder) — Java
  Netty-compatible framing, used by default for
  stateful binary channels

## Transport Summary

| Transport | Type | Framing | Multiplexing | Use Case |
|-----------|------|---------|--------------|----------|
| In-memory | Stateful | None (objects) | Yes | Testing, IPC |
| TCP | Stateful | Netty | Yes | Inter-process |
| HTTP | Stateless | Frame | No | Request-response |
| Custom | Either | Configurable | Configurable | Special protocols |

## Custom Transports

Any duplex stream (or pair of readable/writable
streams) can serve as a transport:

```javascript
// Duplex stream
client.createChannel(duplexStream)

// Separate readable/writable
client.createChannel({
  readable: inputStream,
  writable: outputStream
})
```

The transport only needs to deliver bytes reliably.
avsc-rpc handles framing, handshake, multiplexing,
and timeout.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*


=== FILE: engineering/avsc-rpc/wire-protocol.md ===

[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [avsc-rpc](./) > Wire Protocol

# avsc-rpc Wire Protocol

Handshake, framing, and protocol negotiation — how
bytes are structured on the wire.

---

## Handshake

Every new connection (stateful) or every message
(stateless) begins with a handshake. The handshake
determines whether client and server share a protocol.

### Handshake Request

```
{
  clientHash: bytes(16),     — MD5 of client protocol
  clientProtocol: null|string, — full protocol (if needed)
  serverHash: bytes(16),     — expected server protocol hash
  meta: null|map<bytes>      — optional metadata
}
```

### Handshake Response

```
{
  match: enum { BOTH, CLIENT, NONE },
  serverProtocol: null|string, — full protocol (if mismatch)
  serverHash: null|bytes(16),  — server's actual hash
  meta: null|map<bytes>        — optional metadata
}
```

### Resolution

- **BOTH** — client and server protocols match.
  Proceed directly.
- **CLIENT** — server recognises client's protocol
  but client doesn't know server's. Server sends its
  protocol. Client caches it.
- **NONE** — neither recognises the other. Both
  protocols exchanged. Both cache.

After resolution, client and server create an
Adapter — a resolver that maps between the two
protocol versions using Avro's type resolution.
Subsequent messages use the adapter.

This is schema evolution applied to the protocol
level. A client with an older protocol version can
communicate with a newer server if the types are
compatible.

## Framing

Two framing formats are available for binary
transports:

### Standard Frame Encoding

Avro specification framing. Messages are split into
frames, each prefixed with its byte length.

```
[frameLength: 4 bytes, big-endian] [payload: N bytes]
[frameLength: 4 bytes, big-endian] [payload: N bytes]
...
[0x00 0x00 0x00 0x00]  — zero-length frame terminates
```

Used by `FrameEncoder` and `FrameDecoder`.

### Netty Encoding

Java Netty-compatible framing. Default for stateful
binary channels. Interoperates with JVM Avro RPC
implementations.

```
[messageID: 4 bytes] [frameCount: 4 bytes]
[frameLength: 4 bytes] [payload: N bytes]
[frameLength: 4 bytes] [payload: N bytes]
...
```

The message ID enables multiplexing — responses are
matched to requests by ID. Used by `NettyEncoder` and
`NettyDecoder`.

### Stream Classes

All four are streamx.Transform instances:

```javascript
const { streams } = require('avsc-rpc')

// Standard
const enc = new streams.FrameEncoder()
const dec = new streams.FrameDecoder()

// Netty
const enc = new streams.NettyEncoder()
const dec = new streams.NettyDecoder()
```

## Message Wire Format

A single RPC message on the wire:

### Request

```
[handshake request (first message only, stateful)]
[message metadata: map<bytes>]
[method name: string]
[request body: Avro-encoded by message.requestType]
```

### Response

```
[handshake response (first message only, stateful)]
[message metadata: map<bytes>]
[boolean: is-error flag]
[body: Avro-encoded by message.responseType or errorType]
```

The metadata map in each message is distinct from the
handshake metadata. It carries per-message context —
the wire-level equivalent of mycelium's context
entries.

## Multiplexing

Stateful channels multiplex messages over a single
connection using message IDs (4-byte prefix in Netty
encoding). Multiple concurrent requests share one TCP
socket.

The Registry class tracks pending callbacks by ID.
When a response arrives, the ID matches it to the
original request's callback.

```javascript
// Internal — not normally used directly
const registry = new Registry()
const id = registry.add(callback)
// ... later ...
registry.get(id)(err, response)
```

## Protocol Discovery

Discover a remote server's protocol without knowing
it in advance:

```javascript
const { discoverProtocol } = require('avsc-rpc')

discoverProtocol(transport, (err, protocol) => {
  // protocol is the server's Avro protocol definition
  const service = Service.forProtocol(protocol)
  const client = service.createClient()
  client.createChannel(transport)
})
```

Sends a handshake with an intentionally wrong hash.
The server responds with its full protocol. The
client now knows what the server speaks.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*

