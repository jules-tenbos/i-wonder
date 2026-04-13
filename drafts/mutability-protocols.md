# Mutability — Draft

Post draft. Source material in `submissions/mutability-protocols.md`. Ref lib pages: `docs/engineering/mycelium/mutability.md`, `docs/engineering/mycelium/mutable.md`. Serialization added to `docs/engineering/mycelium/xpath.md`.

---

## Post notes

### Title options
- What the Fabric Knows About Itself
- Three Regimes of Change
- Dirty Until Proven Otherwise

### Persona
Splectrum (engineering)

### Labels
mycelium, engineering, Splectrum

### Storyline

1. **Open with dirty** — an empty repository knows nothing about its own content. No mutability metadata, no guarantees. This is the starting point. Not a failure state — the honest default. Architecture of absence: what you don't declare doesn't exist as a guarantee.

2. **The three regimes as self-knowledge** — not lifecycle stages but paradigms. Each one says something different about what the fabric knows about change. Immutable: the fabric knows everything, the content is the fact. Mutable: the fabric knows the history through the queue, the current state is derived. Dirty: the fabric knows nothing, the current state is all there is. Three kinds of relationship between the fabric and its own content.

3. **The subject shapes the landscape** — as mutability metadata is placed in contexts, the reliability landscape takes shape. Not configured from outside. The subject declares its own commitments. Some areas become sealed. Some areas get controlled change. Some stay dirty. The landscape is locally shaped, discovered through traversal.

4. **The interrogative protocol** — `mycelium.mutability` gets and sets the regime. Get walks the ancestor axis, nearest wins, no declaration means dirty. Set writes the declaration into context metadata — the subject committing an area to a regime. Two operators, one value. The protocol reads and declares, it doesn't enforce.

5. **The mutable mechanism** — the interesting one. A service that manages a living surface derived from a sealed queue. The service lifecycle is its own concern — create, rebuild, discard. Data change records are immutable records in the fabric, written through the normal data access protocols. Sync applies pending changes to the surface — triggered automatically when a change lands, or manually. `mutable.put` as the convenience: register the change and sync in one call. The queue is the truth. The surface is the convenience. One-directional dependency: remove the surface and the queue doesn't notice. Remove the queue and the surface is orphaned.

6. **Expendability as first-class property** — rebuild is not emergency recovery. It is a first-class operation. Schema evolution? Rebuild. New projection? Rebuild. Corruption? Rebuild. The mutable surface is always expendable because the immutable queue is always there. This is what makes controlled change safe — not locking, not transactions, but the guarantee that truth never lives in the derived state.

7. **The transition** — dirty to immutable is a one-way creation act. A snapshot, a commitment. What happened in dirty before that moment is gone. No memory to carry forward. This is not a conversion — it is a birth. The immutable record begins its life at the moment of commitment. What existed before was not a previous version — it was a different kind of thing entirely.

8. **Close with the landscape** — the fabric itself has no opinion about change. What it has is a way for the subject to declare, area by area, what kind of self-knowledge it wants. The landscape is the sum of those declarations. It can be cautious or adventurous. Sealed or open. The mutability protocols don't impose a regime — they read whatever the subject has declared about itself.

### Key theme
Self-knowledge. What the fabric knows about its own content — everything, the history, or nothing. The three regimes as three kinds of self-relationship. The subject shaping its own reliability landscape through declarations.

### What the post is not
- Not a technical specification (that's the ref lib)
- Not about serialization (that's the xpath/data access concern)
- Not about write permissions (that's a separate write mode protocol)
- It's the discovery of self-knowledge as an architectural principle

### Connects to
- Mycelium Data Fabric post — the static substrate these protocols operate on
- Mycelium XPath post — where serialization lives, data access protocols
- Mycelium Layers post — synchronisation, replication as layering concerns
- Protocol post — carrier/meaning at the operational level (mutability/mutable as a pair)

### Open areas (not for the post)
- Write mode protocol — what operations are *permitted* (separate from what the regime *is*)
- Data change record format — how changes to a subtree are expressed as a schema
- Queue protocol — ordering, delivery, position tracking

---

## Tasks on scheduling

- [ ] Review/update ref pages
- [ ] Image selection
- [ ] Write narrative
- [ ] Schedule on Blogger
- [ ] Delete draft
- [ ] Delete submission
