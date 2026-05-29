---
layout: default
lastmod: 2026-05-29
title: "Ecosystem and adoption"
description: "Git's near-universal adoption, the hosting platforms built on top of it, the independent implementations of the format, and its reach beyond source code."
---

[Home](/) > [Positioning](/positioning/) > [Subjects](/positioning/subjects/) > [Git](/positioning/subjects/g/git/) > Ecosystem and adoption

# Ecosystem and adoption

Git is the dominant version-control system: by the early 2020s developer surveys put its use among professionals at roughly 95%, displacing the centralised systems (CVS, Subversion) and the competitors ([Mercurial](https://en.wikipedia.org/wiki/Mercurial), [Perforce](https://en.wikipedia.org/wiki/Perforce)) that preceded or accompanied it.

## Hosting

Much of Git's reach comes through hosting platforms that add collaboration around the bare protocol — pull/merge requests, issues, review, continuous integration. The largest are [GitHub](https://en.wikipedia.org/wiki/GitHub) (the market leader), [GitLab](https://en.wikipedia.org/wiki/GitLab), [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket), and [SourceForge](https://en.wikipedia.org/wiki/SourceForge); these are services built on top of Git, not Git itself.

## Implementations

The canonical implementation is the C "core Git" maintained by [Junio Hamano](https://en.wikipedia.org/wiki/Junio_Hamano) at [git.kernel.org](https://git.kernel.org/) under GPL-2.0; the trademark is held by the [Software Freedom Conservancy](https://sfconservancy.org/). Independent implementations include [libgit2](https://libgit2.org/) (a portable C library with bindings for many languages), [JGit](https://www.eclipse.org/jgit/) (Java; used by Eclipse and Gerrit), [go-git](https://github.com/go-git/go-git) (Go), and [isomorphic-git](https://isomorphic-git.org/) (pure JavaScript, for Node and the browser).

## Reach beyond code

Git's content-addressed, history-preserving model has been taken up well beyond source code — for configuration, infrastructure-as-code, documentation, and data — wherever versioned, verifiable, decentralised state is useful.

## Sources

- [Software Freedom Conservancy](https://sfconservancy.org/) — Git's institutional home and trademark holder.
- [Git](https://en.wikipedia.org/wiki/Git) — Wikipedia, for adoption figures and ecosystem.
