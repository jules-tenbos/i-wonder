[Home](/) > [Engineering](/engineering/) > Substrate

# Substrate

The committed languages SPLectrum's architecture is built on. Each is a language in its own right — with its own vocabulary, grammar, and idioms — and each plays a specific structural role. Pre-decided commitments, not discoveries of necessity; the fit between architectural requirement and chosen language is what makes each a good commitment.

## Committed languages

- **[AVRO](avro)** — language of structure. Schemas as carriers, namespaces as meaning contexts, conformance discovered through reader/writer resolution.
- **[Git](git)** — language of historicity. Commits, refs, DAG, hard boundary, decentralised exchange.
- **[Kafka](kafka)** — language of mobility. Record envelope, context-in-transit, arrival order and timestamp.
- **[Bare](bare/)** — language of runtime. Minimal JavaScript runtime with module system and platform primitives.
- **[Pear](pear)** — language of peer-to-peer. Discovery, replication, identity. Early stage.

## Relation to the rest

The logical design in [SPLectrum](/engineering/splectrum/) speaks through these languages — it describes what the system must look like; the substrate provides the committed carriers.

Implementation — the specific software that realises each language in the Bare runtime — lives in [Infrastructure](/engineering/infrastructure/).
