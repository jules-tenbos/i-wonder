---
layout: default
lastmod: 2026-05-29
title: "Addressing"
---

[Home](/) > [Engineering](/engineering/) > [Substrate](/engineering/substrate/) > Addressing

# Addressing

Addressing — the "where" of the four substrate roles (structure, historicity, addressing, mobility) — is committed to two complementary languages: URI addresses which resource, and XPath navigates where within a resource's structure. Together they cover both scopes of "where." For each on its own terms — URI's syntax and the identity/location split, XPath's axis model and history — see the [URI subject](/positioning/subjects/u/uri/) and the [XPath subject](/positioning/subjects/x/xpath/); this page is the commitment and the role.

## Two scopes of "where"

A URI identifies a resource uniformly — which thing, by name or location — without committing to its internal shape. XPath navigates inside a structured resource — position in a tree, reached by stepping along axes. One says which resource; the other says where within it. The architecture needs both, and commits to each as a language rather than inventing its own.

## The two compose into one address

A full address layers them: a URI to the resource, an XPath into its structure — the pattern XPointer makes explicit, carrying an XPath expression in a URI fragment. Addressing in the architecture takes the same two-layer shape: locate the node, then descend into it.

## Uniform addressing without a central registry

URI's uniform identification and XPath's compositional navigation both let things be referred to without a central index of what is addressable — addresses are composed at the point of use, not enrolled in advance. That fits a decentralised architecture with no central controller: anything can be named and reached the same way, and any structure navigated the same way, wherever it lives.
