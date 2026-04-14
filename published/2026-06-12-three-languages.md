# Three Languages
Labels: mycelium, engineering, Splectrum
Blogger-ID: 7293775566762044447

<img src="https://images.unsplash.com/photo-1650844228078-6c3cb119abcd?q=80&w=350&h=230&auto=format&fit=crop" alt="Three Languages" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

Mycelium is not a language. It is where three languages meet. AVRO provides the language of structure — schema, conformance, the relationship between record and process. Git provides the language of historicity — identity, boundary, the memory of what was. Kafka provides the language of mobility — streaming, context carriage, data that travels. Each addresses one orthogonal concern. None overlaps. None is mycelium. Mycelium is the fabric, the tree structure, the context model, the protocols — the relational space in which three equal-standing languages interoperate.

These are commitments, not discoveries of necessity. The capability requirements are necessary — you need self-describing shape, you need history with forgetting, you need streaming with context. But the choice of which language fulfils each is Splectrum's commitment. Another framework could commit differently — choose Protocol Buffers instead of AVRO, choose a different version control model, choose a different streaming platform. P4 — equal standing in potential. What makes these the right commitments is the fit between requirement and language, not a law that excludes alternatives. And each language has its own grammar that mycelium conforms to rather than invents. Mycelium does not wrap them in an abstraction that hides their nature. It speaks all three.

What does data need to travel self-sufficiently? Five things. Identity — a key that makes it addressable outside the tree. Context carriage — headers that carry whatever interpretive context the extraction requires. Arrival order — an offset, because every arrival has an order whether it matters for the content or not. Historicity — a timestamp, the moment of extraction as itself a datum. Self-description — headers about headers, so the envelope can describe itself. The Kafka record fulfils all five. That is what makes it the right commitment for the streaming language.

Data in the tree is data at rest. It speaks tree language — position, hierarchy, context through ancestry. It does not carry a motion envelope. Data extracted into a Kafka record is data in motion. It speaks Kafka. The tree provided context through ancestry. Once extracted, context must travel explicitly in headers. The mutable protocol sits at the boundary between the two modes — where motion becomes rest. Kafka records arrive, get unpacked, the change is applied, the living surface updates.

Extraction does not impose fidelity requirements on context carriage. Memory and forgetting — you carry what you choose. Headers can carry full provenance, partial provenance, or none. If origin coordinates are present, the data can travel a long transformation chain and still find its way home. If not carried, it cannot. The architecture makes both possible. No imposition. Architecture of absence applied to the streaming language.

And this is what makes Kafka constitutive, not just convenient — protocol operations themselves are data in motion. A get, put, or delete is a Kafka record. The streaming language does not distinguish data transfer from operation. Both are records with context. The committed language is not just the carrier of data — it is the carrier of action.

A subject reality as a whole can be the value payload of a Kafka record. Key identifies it. Headers carry whatever context matters. And that subject reality contains Kafka records in its own queues. Records contain realities that contain records. The grammar does not scale differently at different magnitudes. The envelope is the envelope. Replication, migration, cloning — all natural expressions of the streaming language. No special protocol needed. Kafka already handles it.

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@aedrian">aedrian</a> / Unsplash</small>
