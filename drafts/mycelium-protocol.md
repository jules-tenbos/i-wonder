---
title: The Meaning of Get
series: mycelium
category: engineering
persona: Splectrum
status: storyline
---

# The Meaning of Get
Labels: mycelium, engineering, Splectrum

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@photographer">Name</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Generic operations, specific meaning
- Get, put, remove mean nothing on their own
- "Get in the context of datauri" retrieves opaque data nodes
- "Get in the context of metadata" retrieves interpreted metadata
- Same word, different reality. The protocol is the reader schema for operations.

### 2. One envelope
- Every protocol invocation produces one message in the same shape
- Invocation and response use the same envelope
- The envelope carries meaning context alongside the carrier

### 3. Resolution as discovery
- Protocols live in fabric metadata, resolved on the ancestor axis
- What you can do depends on where you stand
- No protocol in scope, no capability — architecture of absence at the operational level

### 4. Execution modes as metadata
- Sync, queue, dry-run — not caller arguments
- The node decides how it wants to be executed
- A child can override its parent — the fabric shapes execution, not the caller

### 5. Debug without code change
- Add debug metadata to a context node — every invocation below wraps in debug
- Remove it, normal execution resumes
- No restart, no configuration. Structure is behaviour applied to debugging.

## Connects to
- Fabric — protocols defined in metadata, discovered during traversal
- XPath — protocol resolution uses the ancestor axis
- AVRO — the envelope is an AVRO record, "readable as" applies to protocol invocation
- Process — execution environment dispatches resolved protocols

---

## Tasks on scheduling

- [ ] Image selection
- [ ] Write narrative
- [ ] Schedule on Blogger
- [ ] Delete draft
