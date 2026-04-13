# One Identifier, Many Dimensions — Draft

Combined draft: ref lib page done (docs/engineering/namespace.md), post notes below.

---

## Post notes

### Title options
- One Identifier, Many Dimensions
- The Name Is the Thing

### What makes this a post

A single identifier carries an AVRO namespace, a git repo, a logical type, a protocol, a fabric path. Not mapped to each — readable-as each. The "readable as" principle applied to identity itself.

### Key angles for narrative

- **Readable-as, not mapped-to** — The identifier doesn't point to five different things. It IS one thing with five dimensions, each realised when read through the right schema. Same pattern as everywhere in Splectrum — multiple readings of the same reality.

- **Two primitives** — Dot and underscore. That's the whole grammar. Dot separates namespace segments, underscore opens metadata subtrees. Simple enough to fit in a sentence, powerful enough to structure an entire framework. AVRO identifiers are underscore-free (namespace dimension only).

- **The backbone** — `spl.*` as framework top-level, with real structure emerging: fabric, fabric.layers, xpath (with data protocols like datauri and data), avro and git as constitutive technologies, process with execution environment. The backbone is not rigid — other top-level nodes can exist. The tree grows from the leaves.

- **Identifier mapping** — use an identifier sufficient for the context, no more. The excess is hidden in addressing logic. Mapping is decentralised, multi-pass, operating at all scopes (fabric relative to cwd, AVRO relative to subject reality, remote references). All referencing beyond local scope is hidden — same as code behind the RPC server. The execution context carries the mapping state.

- **Carrier, not meaning** — the identifier is opaque until read through a schema. Don't impose interpretation at the carrier level (no namespace/key separation). The reader determines what each dimension means.

- **Versioning without versions** — version is metadata, not name. Advisory to the resolution algorithm, not a gate. When something diverges beyond "readable as", it's a new namespace node — a new concept, not a version increment.

- **Metadata as ambiguity** — metadata is always contextual, always potentially different at every node. Same identifier, same version set, different metadata, different resolution behaviour. No fixed rules — what the metadata says where you are.

### What the namespace is not

- Not a package manager — no dependency resolution, no version ranges
- Not a registry — no central authority, ownership by repo endpoint
- Not a hierarchy of inheritance — children don't inherit from parents
- Not prescribed structure — no repo template, no required files, no identity files (the name is the identity)
- Not rigid — other top-level nodes besides `spl` can exist, internal mapping allows local naming
- Not a carrier of meaning — no namespace/key separation imposed at identifier level

### Connects to

- Mycelium Data Fabric post — fabric is where the namespace lives structurally
- AVRO design scope — "readable as" is the AVRO mechanism that makes multiple dimensions work
- XPath — addressing, traversal, data protocols under the namespace
- Process/execution — execution context carries mapping state, spl.mycelium.process.execute
