# What the Fabric Knows About Itself
Labels: mycelium, engineering, Splectrum
Blogger-ID: 1785391282506449814

<img src="https://plus.unsplash.com/premium_photo-1661590817216-b07e76427726?q=80&w=350&h=230&auto=format&fit=crop" alt="What the Fabric Knows About Itself" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

An empty repository knows nothing about its own content. No mutability metadata, no guarantees — the honest default. Whatever you put in, whatever you change, whatever you lose — the fabric has no opinion. This is the dirty regime. Not a flaw, not a starting point on the way to something better. It is the architecture of absence: what you don't declare doesn't exist as a guarantee. Control is built, not given.

The mutability protocol — `mycelium.mutability` — is interrogative. It reads what the fabric knows about its own content at a given location. The answer is one of three regimes, and each says something fundamentally different about self-knowledge. **Immutable** — the fabric knows everything. The record arrived whole and stays whole. The content *is* the fact. No change possible, no coordination needed, replicate freely. Complete self-knowledge. **Mutable** — the fabric knows the history. Every change arrives as an immutable data change record through a queue. The queue is the truth, the current state is derived. The fabric knows its own past. **Dirty** — the fabric knows nothing about change. The current state is all there is. No rebuild guarantee, no audit trail.

These are not lifecycle stages. They are paradigms — distinct commitments about what the fabric knows about itself. An area of the tree declared immutable is sealed. An area declared mutable is controlled. An area with no declaration stays dirty. The subject shapes its own reliability landscape by placing mutability metadata in its contexts. Nearest ancestor wins, discovered through traversal. Some areas sealed, some controlled, some deliberately left open. The landscape is locally determined — the subject declares its own commitments.

The mutable mechanism is where it gets interesting. A mutable resource is a living surface derived from a sealed queue. Data change records — themselves immutable records in the fabric — are written through the normal data access protocols. The queue is the permanent record. The surface is the convenience. The dependency is one-directional: discard the surface and the queue doesn't notice. The queue vanishes and the surface is orphaned. This asymmetry is the safety guarantee.

And because the surface is always derivable, expendability is a first-class property. Rebuild is not emergency recovery. Schema evolution? Rebuild. New projection against the same history? Rebuild. Corruption? Rebuild. Truth never lives in the derived state. Nothing is lost when a projection is destroyed, because the projection was never the truth.

The transition from dirty to immutable is a one-way creation act — a snapshot, a commitment. What happened in the dirty regime before that moment is gone. There is no memory to carry forward. Not a conversion — a birth. And the reverse does not exist. You can declare an area immutable. You cannot undeclare it. The sealing is permanent.

The fabric itself has no opinion about change. The landscape is the sum of declarations — cautious or adventurous, sealed or open. The mutability protocols read whatever the subject has declared about itself. Where there is a declaration, there is a guarantee. Where there is silence, there is dirt. And that is exactly as it should be.

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@gettyimages">gettyimages</a> / Unsplash</small>
