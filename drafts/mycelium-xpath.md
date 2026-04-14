---
title: Six Protocols, One Pattern
series: mycelium
category: engineering
persona: Splectrum
status: draft
---

# Six Protocols, One Pattern
Labels: mycelium, engineering, Splectrum

<img src="https://plus.unsplash.com/premium_photo-1669048178541-582bd478d7d4?q=80&w=350&h=230&auto=format&fit=crop" alt="Six Protocols, One Pattern" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

In the mycelium fabric post I described the tree structure of data nodes with colocated metadata nodes containing the functionality to operate on them. This tree structure is logical, and aims to create a consistent view of data irrespective of its actual physical origin. That can most easily be appreciated within the context of a (git) repository - which represents in Splectrum a subject reality. P2 - the way a subject experiences reality. This involves data: present in mycelium fabric, this involves language: colocated to the data in metadata nodes.

XPath is a language that is particularly suited to address and query tree structures. And at the base level, the mycelium repository 'sees' only key value pairs in the tree structure - opaque bytes. Next level up AVRO schemas are used to throw light on the data structure within the values - these structures can be equally addressed and queried using XPath. AVRO does another logical rewrite, reaching deep into the data structures. Mycelium does not care about the physical structure of the underlying data as long as it can be transformed to a logical tree structure. At higher levels more traditional repository data structures will be created: tables, indexes, document stores - only at higher levels.

There are three different views exposed through XPath: a data view, a metadata view (the colocated functionality), and a raw view (all nodes). Each view comes with two modes: with or without AVRO visibility:
```
mycelium.xpath.data
mycelium.xpath.data.uri
mycelium.xpath.metadata
mycelium.xpath.metadata.uri
mycelium.xpath.raw
mycelium.xpath.raw.uri
```
These view are contexts - APIs - on which methods are defined. In Splectrum speak an API is a protocol and the methods are called operators. There are only three operators at this low level: *get*, *put* and *delete*. Again, think key value.

The rationale of data addressing and functionality discovery within Splectrum is as follow. <br/>
1. the current position in the node from where data is selected is considered the (local) data root '/'. Only the data on self or descendants is visible.
2. the context of the current position keeps track of the current node as cwd equivalent relative to the (git) repo root. Functionality colocated to the data is resolved along this ancestor axis starting from self (metadata nodes). 
3. The (git) repositories are federated, there will be cross linking between them at the fabric level but never explicitly for XPath navigation. For data to be in scope and addressable / queriable it must be within the scope of self-or-descendant.

The default navigation of the tree is from context node to context node, flattening all simple nodes in between. A node whose interior has no contexts returns a flat list of key-value pairs. A node with nested contexts returns structure — the contexts are the natural boundaries. The query syntax does not change. What changes is the shape of the result set. This is not a mode switch — it is a natural property of the tree. Structure produces structure. Absence of structure produces flat.

The current prototypes are using the local filesystem as physical data structure, wrapped in a git repo. Integration of other physical repositories into this structure is on the roadmap. At this moment a lot of prototyping is around metadata colocation and building a thorough understanding of the context this metadata creates. Splectrum engineering starts from a philosophical framework that focusses on language and meaning. Each time a fabric data tree node contains metadata, a context is created with a change of meaning.  

<small>This post is part of the [mycelium series](/search/label/mycelium). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/mycelium/">mycelium section of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@jsbco">jsbco</a> / Unsplash</small>

---

# Notes

## Review before scheduling
- [ ] Check prototyping paragraph still reflects current state
- [ ] Image selection
- [ ] Schedule on Blogger
- [ ] Delete draft
