# Peer to Peer, As It Should Be

In the previous post I argued that privacy isn't a policy — it's a structural fact. The second principle of the seed tells us that every subject meets reality through its own medium. That medium is inherently private. It's where you think, process, become. And I argued that what's gone wrong isn't sharing itself, but pathological P3 — sharing that has been centralised, decontextualised, and made permanent to the point where it invades and erodes the very space a subject needs to function.

I ended with a question: what if the architecture itself could be different?

Let's talk about that.

## The Architecture Is the Problem

When I say the problem is architectural, I mean something specific. The internet started as a network of peers. Machines talking to machines, no hierarchy, no centre. And then, gradually, we let a handful of companies become the infrastructure of sharing itself. Not just participants in the network, but the network — or at least the parts of it that matter to most people. Search, social, messaging, commerce, payments. The bridges between subjects got bought up and turned into toll roads.

This isn't some conspiracy. It's what happens when you build sharing infrastructure on a business model that requires capturing data, keeping it, and monetising it. Centralisation wasn't a design choice that went wrong. It was the design choice that made the business work. The pathology is the product.

So if the problem is structural, the fix has to be structural too. Not better terms of service. Not stricter regulation — though regulation has its place. What we need is architecture that makes pathological P3 *impossible by design*. Architecture where sharing is what it was always supposed to be: relational, subject to subject, without the middleman.

That's peer to peer. And it turns out there are two kinds of privacy that need protecting — and two very different architectural answers.

## Encapsulated Privacy

The first kind is what I'd call encapsulated privacy. This is the sealed room. P2 — the subject's own medium — kept intact, contained, unbreached. Your data stays on your device. Your connections are direct. Nothing leaves your medium unless you choose to bridge it. The walls hold.

[Pear](https://docs.pears.com/), built by [Holepunch](https://holepunch.to/), is the engineering expression of this. It's a peer-to-peer runtime for building and deploying applications with no servers, no cloud, no data centres. None. Your data lives on your device and connects directly to other devices through a technique called hole-punching — a way of bypassing the network restrictions that normally force traffic through central servers.

Think about what that means in Splectrum terms. P3 — sharing — happens directly between subjects. No platform sits in the middle deciding what gets shared, how it's stored, who gets to see it. The bridge between you and the person you're communicating with is *yours*. It's not owned, monitored, or monetised by a third party. That's not a feature. That's the architecture.

Pear is built on [Hypercore](https://github.com/holepunchto/hypercore), a distributed append-only log, and [Hyperswarm](https://github.com/holepunchto/hyperswarm), a networking stack for finding and connecting peers. Together they provide the plumbing for applications that are, by design, decentralised. [Keet](https://keet.io), a messaging app built on Pear, is the living proof that this works — real-time communication with no server in the loop. No data collection. End-to-end encrypted. Not because of a privacy policy, but because there's nowhere for the data to go except to the peers involved.

Encapsulated privacy. P2 sealed. P3 returned to its natural form — subject to subject.

## Externalised Privacy

But life isn't only sealed rooms and direct connections. Sometimes you need to step into shared space. You need to prove something — your identity, your eligibility, your ownership — to people or systems you don't have a direct relationship with. Think regulated finance, healthcare, legal contracts. Situations where trust matters, where verification matters, but where pouring all your data onto a public ledger would be just another form of pathological P3.

This is where blockchain has historically stumbled. The whole point of a public ledger is transparency — everyone can verify everything. Great for trust, terrible for privacy. Most blockchain architectures force you into a binary: either everything is public, or you're off-chain entirely.

[Midnight](https://midnight.network/), which went live just days ago, takes a different approach. Built by Input Output Global as a partner chain to Cardano, it uses zero-knowledge proofs to enable what they call "rational privacy" — private by default, disclosure by choice. The architecture separates what's visible on-chain from what remains shielded. You can prove you meet a requirement without showing the underlying data. Your identity stays on your device, and only cryptographic proofs travel to the network.

Here's the image that works for me: privacy bubbles, floating. When a subject needs to interact with shared infrastructure — a ledger, a market, a regulatory framework — it doesn't crack open its private medium and dump everything out. Instead, it sends out a bubble. Sealed, self-contained, carrying just enough to be verified but never popping open. The bubble floats through P3 space, interacts where it needs to, proves what's necessary, and the subject behind it stays intact.

That's externalised privacy. Not the absence of sharing, but sharing that preserves the boundary of P2 even as it crosses into P3. The subject participates in the shared world without dissolving into it.

## Two Sides of the Same Boundary

Encapsulated and externalised. The sealed room and the floating bubble. They're not competing approaches — they address privacy at two structurally distinct points.

Pear protects P2 by keeping it contained. Your medium, your device, your direct connections. Midnight protects P2 at the moment it touches P3 — the threshold where pathology normally kicks in. One keeps the walls intact. The other lets you send something through the wall without breaking it.

And here's where it connects back to the seed's fifth principle: *together they form a web of growing complexity*. These bubbles floating through shared space, interacting without merging, contributing to the web without sacrificing the integrity of the subjects they came from — that's healthy P3 generating healthy P5. Complexity that grows because subjects share freely, not because their data was captured and ground into raw material.

That's the web as it should be. Not a web that *traps*. A web that *grows*.

## Where This Goes

I'm not going to pretend that peer-to-peer and privacy-preserving blockchains will fix everything overnight. There are real challenges — usability, adoption, the sheer inertia of centralised platforms that have spent two decades building moats around pathological P3. The world doesn't change just because better architecture exists.

But I find it encouraging that the engineering is catching up with the principle. That there are people building systems where pathological P3 isn't just discouraged but structurally impossible. Where the default is privacy, not surveillance. Where sharing means what it's supposed to mean — subjects choosing to bridge, not bridges capturing subjects.

The seed didn't predict any of this. Five sentences about language and reality and complexity. But the more I look at what's being built, the more I see it rhyming.

I wonder where this goes.

---

*This is the third post exploring the Splectrum seed. Previously: [Splectrum is Born](https://julestenbos.blogspot.com/2026/03/splectrum-is-born.html) introduced the five principles, and [Privacy, Naturally!](https://julestenbos.blogspot.com/2026/04/privacy-naturally.html) explored how pathological sharing erodes the freedom to think and be.*
