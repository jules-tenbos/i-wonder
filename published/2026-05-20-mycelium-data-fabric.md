# Mycelium — The Data Fabric
Labels: mycelium, engineering, Splectrum
Blogger-ID: 2725312844865805306

<img src="https://images.unsplash.com/photo-1718049942873-58bd663206dc?q=80&w=2067&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Mycelium — The Data Fabric" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

This post is the first of the mycelium series. The [splectrum engineering post](https://julestenbos.blogspot.com/2026/05/splectrum-engineering.html) describes three pillars of a Splectrum system — mycelium (state), splectrum (meaning), HAICC (cognition). Mycelium is what I call the main pillar: it provides the fabric structure for data, and is the base fabric on which the other two build.

Data is stored in a tree structure, wrapped into individual repositories — *subject realities* — under [git](https://git-scm.com/) as distributed version control. Git provides the hard boundary: identity, history, integrity. Each repository is a distinct entity — what you see is what there is. No hidden data, no hidden process. There is no central data world. Only subject realities exist. The totality of data is a logical concept, never a physical repository. Data lives where it is created and is referenced for consumption elsewhere. A consuming repository may hold local copies, but its data state for consumed data is not authoritative. The writer owns the data.

The subject reality owns its own historicity. This is not an outside system applying checkpoints — the subject itself controls what gets remembered and how. Operational data can be backed up separately and gitignored — git handles configuration and structural state, not high-volume operational flow. The fabric supports layered setup — a referenced read-only base providing initial configuration, with local overlay for what the subject changes. Read wide, write local.

A living subject needs to forget, not just preserve. Git's conventional philosophy is to never lose anything — append-only, content-addressable, complete audit trail. But a living reality needs selective memory. Attention determines memory resolution: what the subject attends to gets detailed treatment, background fades. Recent history stays granular, older history progressively consolidates, eventually only the significant shape remains. Git provides mechanisms for both — the immutable store preserves, history rewriting and garbage collection allow forgetting. The subject shapes its own memory.

Git gives reality operations for free. Clone — spawn a new subject reality, complete with full history and embedded processes. Closer to cell division than anything else: identical at the split, divergent through life. Branch — diversify within a reality without losing the original. Merge — reconcile divergent realities. Conflicts as how decentralised realities deal with divergence. No central authority needed for any of them. These are not metaphors mapped onto git. They are git operations read through the framework.

Git makes the subject reality portable. A repository can go into quiescence — completely dormant, switched off, moved anywhere — and reactivate where it left off. Everything needed to resume is embedded: data state, process definitions, referential structure, history. This is not a backup-and-restore pattern. It is a living subject going quiet and waking up. The same mechanism serves hot standby — a clone tracking the active reality, ready to take over. It serves peer-to-peer exchange — subjects moving between environments without losing identity. It serves disaster recovery — the repo is the recovery unit, self-contained by design.

Git is snapshot-based — commit, store, done. It has no concept of continuous flow, and for streaming or high-volume operational data it is ill suited. But git isn't asked to be a database. It is asked to be a container for a fabric. Git holds the structure, the references, the embedded process definitions, the historicity. The data itself can live elsewhere. The scene is local, the resources can be anywhere. Git and AVRO are the two constitutive technology dependencies with deep integration into the fabric. The platform dependencies — bare and pear — are to come.

The fabric is built from one primitive: an immutable key-value record with opaque bytes in the value. Why opaque? Because the fabric doesn't interpret content. Any data, any language, any process can sit on top. The fabric is universal by design. A node in the tree becomes a context when metadata nodes are added to it. The context is where behaviour lives — process definitions, schemas, language declarations. All embedded in the metadata, all discoverable during traversal.

Structure is behaviour. What you build is how it behaves. What you don't build can't happen — architecture of absence. No configuration, no flags. The source of truth is always immutable records. Mutable structures — tables, indexes, document libraries — are projections maintained by embedded processes. You can throw them away and rebuild them from the immutable base.

As with the whole Splectrum design, the fabric describes how data must look — not how it must be physically stored. Physical implementations are free to use whatever fits, as long as they are compatible with the logical design.

Processes live in the fabric alongside the data — embedded in context metadata, dormant until a data state change wakes them. No orchestration. The data state is the relay. Schema is the contract between a record and the process that operates on it — a process concern, not a fabric concern. The process declares what it needs through its reader schema. The data either conforms or it doesn't.

Properties such as structured data access, mutability, and referencing are implemented in separate protocol layers on top of the base. The data protocols at the base level use XPath syntax for addressing and querying — I am going to do a separate post on the base layer data protocols. These protocol layers are where the fabric grows in capability without changing the base. The base stays minimal, universal, unchanged. Everything above it is articulation.

<small>This post is part of the [mycelium series](/search/label/mycelium). More on mycelium in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium area of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@chiara_01">chiara_01</a> / Unsplash</small>

<!-- CHANGE NOTES (ref lib update 2026-04-13)

Fabric ref page rewritten — scoped to static structure only:

ON FABRIC PAGE:
- The primitive (record + context)
- The metadata dimension (underscore prefix, cascading subtrees, portability)
- Records (immutable/dirty, projections)
- Mycelium context (structure is behaviour, metadata embedding of higher-level elements)
- Point of view, references, addressing (context for how fabric fits the bigger picture)
- Layering (mention — detail on future mycelium.fabric.layering page/post)

MOVED OUT to new pages:
- Message shape and fabric schemas → schema page
- 6 data protocols (3 opaque + 3 schema-aware) → xpath page
- Traversal mechanics → xpath page
- Flat contexts → xpath page (query result shape)
- Layers detail (read modes, synchronisation, safe mode, replication) → layering page
- Interaction modes (data state propagation) → layering page
- Node self-containment → meaning layer
- Security model, "what fabric does not do" → removed from fabric scope

POST IMPACT:
- Post says "I am going to do a separate post on the base layer data APIs" — still valid, now 6 contexts not 3
- Fabric basics in post (primitive, structure is behaviour, immutability, projections) still accurate
- Metadata dimension, metadata embedding, references are new ref lib depth not in post
-->
