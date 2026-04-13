[In Wonder - The World of Splectrum](../../) > [Engineering](../) > [Mycelium](./) > Protocol

# Mycelium Protocol

Protocol is the meaning layer for operations in the fabric. A protocol provides the context that gives generic operations their specific meaning.

## Protocol as Meaning Context

Operations have generic names — get, put, remove. These names carry no inherent meaning on their own. The protocol is the context that gives them meaning. "Get, in the context of datauri" means something different from "get, in the context of metadata." Same carrier, different meaning. The protocol determines the flavour.

This is the carrier/meaning split expressed at the operational level. The operation name is the carrier. The protocol is the meaning. What an operation does is determined by the protocol context it operates within, not by the operation name itself.

## Protocol Operations

Protocol operations have base meanings — get retrieves, put places, remove takes away. These base meanings are flavoured by the protocol context. Each protocol gives its operations the specific meaning appropriate to what the protocol represents. The operation names stay generic. The protocol makes them specific.

## The Resolution Envelope

Every protocol invocation produces one message:

```
envelope {
  headers {
    namespace     — resolved protocol namespace
    logical-type  — as provided
    execution     — from context metadata (sync | queue | dry-run)
    debug         — from context metadata (present or absent)
    pov           — current working directory path
    trace         — traversal accumulation record
  }
  key   — current node path (XPath expression)
  value — data payload (opaque)
}
```

The envelope is an AVRO record. The handler receives it through a single operation: `resolve(envelope) → envelope`. The return envelope carries the result in the same shape. One message shape for invocation and response.

## Protocol Resolution

Protocols are defined in fabric metadata. Resolution walks the ancestor axis from the current position up to the subject reality root. Nearest ancestor wins.

No match on the full ancestor axis — nothing happens. No error, no fallback. Architecture of absence: no protocol in scope, no capability.

## Execution Modes

Execution mode is metadata in the context, not a caller argument:

- **sync** — resolve, execute, return result. Default when no execution mode metadata is present.
- **queue** — resolve, place envelope in the node's process queue, return acknowledgment.
- **dry-run** — resolve, report what would execute and against what data scope, return report. No state change.

A context can declare its default execution mode. A child context can override. The accumulated metadata determines which mode applies.

## Debug Wrapping

Debug is a context metadata fact. When present on the ancestor axis, execution wraps in the debug protocol found nearest on the path.

The debug protocol itself is resolved on the ancestor axis — it can be a simple trace logger at one level, a full step-through inspector at another. Remove the debug metadata, normal execution resumes. No code change, no restart.

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
