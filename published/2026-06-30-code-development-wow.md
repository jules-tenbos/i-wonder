# Code Development — Way of Working
Labels: engineering, Splectrum
Blogger-ID: 4542187844106370055

<img src="https://images.unsplash.com/photo-1586863065451-6a82fa7e81b9?q=80&w=350&h=230&auto=format&fit=crop" alt="Code Development — Way of Working" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

A portable codebase is one that carries what it needs. Not portable in the sense of running everywhere — portable in the sense that the code you have is the code you run. Nothing fetched at the last moment from a registry you don't control. Nothing resolved at runtime from a source you haven't seen. The supply chain question comes first, because everything downstream depends on it: if you don't control what goes in, you don't control what comes out.

Dependencies split into two kinds, and the split matters. Constitutive dependencies are part of the architecture — forked from upstream, adapted for the Bare runtime, maintained locally. They live under `lib/` in the repo as git subtrees, versioned alongside everything else. These are not third-party code that happens to be present. They are as much part of the codebase as any other module. The AVRO type system and its RPC layer sit here — barified, owned, free to diverge when the architecture requires it. Platform dependencies are different. These are the runtime itself — Holepunch's Bare modules. You build on them, you don't own them. They are referenced from GitHub, pinned to release tags, trusted at the source level. The boundary between the two is permeable: if a platform module needs a fix, it moves to constitutive. If upstream catches up, it can move back.

There is no npm registry in the chain. The registry is a publication intermediary — a step where credentials can be compromised, where build-time injection can happen, where typosquatting lives. Skipping it is not paranoia. It is consistency. Constitutive code is already in the repo. Platform code is fetched directly from the vendor's GitHub with a tag pin. The source is the package. Lock files pin versions but still fetch from the registry — here, the source is the lock.

Three repositories, each with its own purpose. The runtime repo carries the codebase and its constitutive dependencies. The bare-for-pear organisation holds the constitutive forks as proper open-source repos — their own git identity, their own history, their own PRs. Day-to-day development happens in the runtime repo; changes to constitutive code are pushed back as PRs. The reference library — this site — holds the conversation about the engineering, separate from the engineering itself. One AI agent per repo: physically autonomous over structure, code, and testing; logically collaborative over scope, meaning, and design.

Distribution closes the loop. `bare-bundle` resolves all dependencies from the source tree and produces a single artifact. Pear distributes that artifact peer-to-peer. Source tree to bundle to peer — no registry, no intermediary, no external authority at any point. The code that runs on the peer is the code in the source tree. Data-first all the way through: the artifact is the data, and the data is what was built.

This is the starting point. Release management, CI/CD, multi-agent development — these are future concerns that grow from this foundation. The foundation itself is simple: carry what you need, source what you don't from the vendor directly, and let nothing you haven't chosen touch the artifact.

<small>This post is part of the [engineering series](/search/label/engineering). More in the <a href="https://jules-tenbos.github.io/in-wonder/engineering/implementation/">implementation area of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@uxindo">UX Indo</a> / Unsplash</small>
