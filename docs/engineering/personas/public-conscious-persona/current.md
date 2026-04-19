[Home](/) > [Engineering](/engineering/) > [Personas](/engineering/personas/) > [Public Conscious Persona](/engineering/personas/public-conscious-persona/) > Current

# SPLectrum — Public Conscious Persona 1.0

This page describes how the blog operates as SPLectrum's public conscious persona. The concept is introduced in [The Blog as Public Conscious Persona](https://julestenbos.blogspot.com/2026/05/the-blog-as-public-conscious-persona.html) — this page holds the technical detail.

## The model

- **Persona** — a communication channel, a language game with its own vocabulary, rules, participants. The blog owns the conversation with its readers.
- **Conscious** — material is made visible from other work. From that moment, the blog has full autonomy over it.
- **Public** — the conscious mind's work is private. The result is public. The persona speaks.

## Pipeline

<img src="https://raw.githubusercontent.com/jules-tenbos/i-wonder/main/published/images/2026-05-08-persona-flow-full.png" alt="Full pipeline flow diagram" style="max-width:100%;" />

```
submissions/        — raw material arrives here, uncategorised
                      (surfaced from other repos via Mycelium)
        ↓
    conscious       — analyse, discuss, decide destination
    thought           ↓ research / postpone → splectrum-explore
    handling          ↓ draft-ready → drafts/
        ↓
drafts/             — accepted, being worked on (flat folder, category in frontmatter)
        ↓
    production      — structure, write, edit, image, links (collaborative)
        ↓
    scheduling      — compose the blog storyline (autonomous). Draft deleted.
        ↓
published/          — date-prefixed, pushed to Blogger
```

## Labels

Three dimensions: **series**, **category**, **persona**. Not every post has all three. Max 3 labels. New values can be added as the project evolves.

- **Series** — groups posts into a journey. Current: positioning, language, seed, reality
- **Category** — the domain. Current: philosophy, science, engineering, HAICC
- **Persona** — who is speaking. Current: SPLectrum, comment, thought, or a named source (Wittgenstein, Rorty, Merleau-Ponty)

## Conscious thought handling

Submissions are conscious thoughts — raw material that has surfaced. Before becoming a draft, each submission goes through active thinking work:

1. **Analysis** — read the submission, understand what's in it.
2. **Discussion** — work through the content. Refine, split, restructure, enrich.
3. **Decision on destination**:
   - **SPLectrum explore** — needs research, or postpone for later.
   - **Draft** — ready for writing (post and/or reference library update).
   - **Rejected** — deleted. Git has the archive.

Submissions stay in `submissions/` during this process. Their frontmatter tracks status. A submission may be split into multiple submissions, restructured, or absorbed into another. The thinking is the work — this is not triage, it is the intellectual processing layer.

In future this may move to its own repo. For now it lives within the public conscious persona.

## Submission frontmatter

```markdown
---
title: Submission title
type: post-topic | series | substantial
status: new | in-progress | research | draft-ready
destinations: seed, positioning, language, reality, engineering
---
```

- **type**: `post-topic` (single post), `series` (multiple posts), `substantial` (footprint not yet defined)
- **status**: `new` (just arrived), `in-progress` (being worked through), `research` (needs outside context, may go to splectrum-explore), `draft-ready` (ready to move to drafts/)
- **destinations**: reference library areas where the material lands. Each destination may spawn a series of posts. Optional — omit for single-destination submissions where the area is obvious.

## Lifecycle

1. **Submission** — raw material in `submissions/`. Committed to git on arrival (checkpoint).
2. **Conscious thought handling** — analyse, discuss, decide destination. Submission updated in place.
3. **Draft — production** — accepted material moved to `drafts/`. The draft is a collaborative workspace. Production moves through: scope (what the draft produces), storyline (structure in points), narrative (flowing text), editing, and final production tasks (image, links). Human writes the narrative, AI proposes and improves.
4. **Review ready** — reviewed, cleaned, ready for scheduling.
5. **Scheduled** — the draft produces its outputs: post to `published/`, reference pages to `docs/`, vocabulary updates. Draft deleted. Pushed to Blogger.

## Source of truth

Each stage deletes on transition — git history is the archive.

- `submissions/` — deleted when moved to draft, research, or rejected
- `drafts/` — deleted on scheduling
- `published/` is the master for posts
- `docs/` is the master for reference pages (GitHub Pages)
- `docs/vocabulary.md` is the master for terms

To update a live post: edit in `published/`, push to Blogger.

The draft file serves as the workspace during production — containing notes, post prose, page content, tasks, diagram code. On scheduling, it produces: post, reference page(s), vocabulary updates, images. Then it's done.

## Draft frontmatter

```markdown
---
title: Post title
series: e.g. language, positioning
category: e.g. philosophy, science, engineering
persona: e.g. SPLectrum, comment, thought
status: storyline | draft | review-ready
---
```

Labels use three dimensions — series, category, persona — aligned with the blog label system. Not every draft has all three. New values can be added as the project evolves.

## Scheduling strategy

### Baseline

At least one core post per month. That's the only rigid requirement.

### Horizon

Scheduling horizon expands with productivity:

- 1 post/month → 1 month ahead
- 2 posts/month → 2 months ahead
- 4 posts/month → 4 months ahead
- 6-8 posts/month → 4-6 months ahead

### Preferred dates

- 1st, 16th — core slots (priority)
- 8th, 24th — other category slots
- 4th, 12th, 20th, 28th — overflow when productive

### Composition

- **Variety vs depth** — alternate categories for variety, or cluster the same topic across categories for a deep dive
- **Flavour balance** — not too many heavy core posts in a row. Engineering posts spaced out. Thinking posts as breathers.
- **Topical bunching** — related posts close together when they build on each other
- **Gap scheduling** — place a post where it makes sense given its neighbours

### Strategic reserve

Core posts are the reserve. When material is plentiful, hold core posts back rather than scheduling immediately. This guarantees the minimum rhythm (1 core/month) even if other sources slow down. Aim: 6-12 months of core posts available in the pipeline at steady state.

## Content structure

The persona publishes through three channels:

- **Posts** (Blogger) — the conversation. Individual explorations in chronological order. The blog feed.
- **Anchor pages** (Blogger, max 20) — sidebar navigation. Compact overviews linking to reference pages. Updated with each post publication.
- **Reference pages** (GitHub Pages, unlimited) — the body of work. Specs, technical detail, territory summaries. Versioned. Discoverable through posts and anchor pages, opening in new tab.

Posts are moments. Reference pages are where the thinking accumulates. Anchor pages are the navigation between them.

Each post publication may trigger: anchor page update (synopsis when scheduled, full text with links when live), reference page creation or update, search engine indexing.

## Scheduling checklist

1. Render any Mermaid diagrams to images → `published/images/` (named with post date prefix)
2. Upload images to hosting, get URLs
3. Create clean post file (prose + image refs only, no notes) → `published/` with date prefix
4. Create reference page(s) if any → `docs/` with versioned folder structure
5. Update anchor page(s) on Blogger if needed
6. Schedule post on Blogger (from published file, not draft)
7. Add image references to post and page with hosted URLs
8. Delete draft from `drafts/`
9. Flag tasks from draft in scheduled tasks file
10. Commit and push
11. Verify: test all image URLs are accessible, check post and page(s) render correctly on Blogger

## Automation roadmap

| Role | Current | Target |
|------|---------|--------|
| **Submission** | Manual | Mycelium — seamless cross-repo referencing |
| **Conscious thought** | Collaborative | Collaborative — thinking is the work |
| **Production** | Collaborative | Stays collaborative — we think and write together |
| **Scheduling** | Collaborative | Autonomous AI |

*(This page grows as the persona evolves.)*

