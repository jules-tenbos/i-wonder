# Mycelium Protocol — Draft

Combined draft: ref lib page done (docs/engineering/mycelium/protocol.md), post notes below.

---

## Post notes

### Title options
- The Meaning of Get
- Protocol — Where Carrier Meets Meaning

### What makes this a post

Protocol is where the carrier/meaning split becomes operational. Every operation in the fabric — get, put, remove — is a generic carrier. The protocol gives it meaning. This is the Splectrum pattern (reading the same thing through different schemas) applied to operations themselves.

### Key angles for narrative

- **Generic operations, specific meaning** — get, put, remove mean nothing on their own. "Get in the context of datauri" retrieves opaque data nodes. "Get in the context of metadata" retrieves interpreted metadata. Same word, different reality. The protocol is the reader schema for operations.

- **One envelope** — every protocol invocation produces one message in the same shape. Invocation and response use the same envelope. One AVRO record. The envelope carries the meaning context (protocol namespace, logical type) alongside the carrier (opaque value).

- **Resolution as discovery** — protocols live in fabric metadata. Resolution walks the ancestor axis. What you can do depends on where you stand. No protocol in scope, no capability. Architecture of absence at the operational level.

- **Execution modes as metadata** — sync, queue, dry-run. Not caller arguments. The node decides how it wants to be executed. A child can override its parent. The fabric shapes execution, not the caller.

- **Debug without code change** — add debug metadata to a context node. Every invocation below wraps in debug. Remove it, normal execution resumes. No restart, no configuration. Structure is behaviour applied to debugging.

### Connects to

- Fabric — protocols are defined in fabric metadata, discovered during traversal
- XPath — protocol resolution uses the ancestor axis (functional resolution)
- AVRO — the envelope is an AVRO record, "readable as" applies to protocol invocation
- Process — execution environment dispatches resolved protocols
