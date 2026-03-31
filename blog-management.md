# Blog Management

The blog is the public conscious mind — where all the things I am and do that I want to share come together. Material arrives from different sources (engineering, research, personal thinking) and gets composed into a reading experience.

## Post categories

Categories are modes of engagement, not topics. The same topic can appear in any category.

| Category | What it is | Voice | Scope |
|----------|-----------|-------|-------|
| **Core** | Substantial Splectrum. Building from P1-P5. | Splectrum speaking | Philosophy, science, language, ethics, evolution |
| **Research** | Analysing other vocabularies/traditions. | Observing from Splectrum's position | Other thinkers, papers, traditions |
| **Thinking** | Small bites. A specific insight, question, connection. | Mix — Splectrum or external or both | Open |
| **Engineering** | Practical. How we work, tools, methods, AI collaboration. | Splectrum's practice | Tools, workflow, methodology |
| **Commentary** | Reactions to current events, things read, things encountered. | Open, responsive | Anything timely |

## Pipeline structure

```
submissions/        — raw material arrives here, uncategorised
drafts/             — accepted, categorised, being worked on
  core/
  research/
  thinking/
  engineering/
  commentary/
published/          — scheduled/live, date-prefixed
```

### Lifecycle

1. **Submission** — raw material lands in `submissions/`. Raw thoughts, no post standards. Just the information, the insight, the material.
2. **Intake** — review the submission. Accept or reject as blog-worthy.
3. **Draft** — if accepted, moved to `drafts/<category>/`. The draft file is shaped from the submission and contains everything in one place:
   - **Notes** — filtered from submission, raw material, references
   - **Post storyline and prose** — the post being written
   - **Page(s)** — any new pages to be created alongside the post
   - **Tasks** — scheduled tasks triggered by publication (page updates, anchor links, etc.)
4. **Production** — structure, write, edit, image, links. Collaborative.
5. **Review ready** — reviewed, cleaned, ready for scheduling.
6. **Schedule** — one draft in, multiple outputs. Checklist:
   1. Render any Mermaid diagrams to images → `published/images/` (named with post date prefix)
   2. Upload images to hosting, get URLs
   3. Create clean post file (prose + image refs only, no notes) → `published/` with date prefix
   4. Create page file(s) if any → `pages/`
   5. Publish page(s) on Blogger (unlinked initially if needed)
   6. Schedule post on Blogger (from published file, not draft)
   7. Add image references to post and page with hosted URLs
   8. Update draft frontmatter status to "scheduled"
   9. Flag tasks from draft in scheduled tasks file
   10. Commit and push

### Source of truth

**The draft is always the master.** `published/` and `pages/` are snapshots generated from the draft.

- Drafts stay forever — they don't get deleted when published
- Editing always happens in `drafts/` — never in `published/` or `pages/` directly
- Updates flow one way: `drafts/` → `published/`/`pages/` → Blogger
- To update a live post or page: edit the draft, then republish

This ensures one source of truth. The draft contains everything — notes, storyline, page content, tasks, and the final text. Published outputs are clean snapshots.

Use frontmatter in draft files:

```markdown
---
title: Post title
category: core | research | thinking | engineering | commentary
topic: e.g. ethics, language, Russell, workflow
status: idea | storyline | accepted | draft | review-ready
---
```

### Submission

A draft is submitted when it has a storyline that works. It may be accepted or rejected as a blog post. Rejection is not a judgement — the material may not be right for the blog, or not ready yet.

### From draft to published

When a draft is review-ready and scheduled: move from `drafts/` to `published/` with date prefix. Existing workflow kicks in.

## Scheduling strategy

### The baseline

At least one core post per month. That's the only rigid requirement.

### The algorithm

Scheduling horizon expands with density:

- **1 post/month** — schedule 1 month ahead. Core post on the 1st.
- **2 posts/month** — schedule 2 months ahead. Add the 16th.
- **4 posts/month** — schedule 4 months ahead. Add the 8th and 24th. Start interleaving categories and topical bunching.
- **6-8 posts/month** — schedule 4-6 months ahead. Fill in 4th, 12th, 20th, 28th. Compose the reading experience.

### Preferred dates

- 1st, 16th — core slots (priority)
- 8th, 24th — other category slots
- 4th, 12th, 20th, 28th — overflow when productive

### Scheduling decisions

- **Variety vs depth** — alternate categories for variety, or cluster the same topic across categories for a deep dive
- **Flavour balance** — check: has it been too long since an engineering post? Too many heavy core posts in a row? A thinking post works as a breather.
- **Topical bunching** — related posts close together when they build on each other
- **Gap scheduling** — place a post where it makes sense given its neighbours

### Strategic reserve

Core posts are the reserve. When there's plenty of material, hold core posts back rather than scheduling immediately. This guarantees the minimum rhythm (1 core/month) even if other sources dry up. Aim to have 6-12 months of core posts available in the pipeline at steady state.

### Scheduling sessions

Regular activity: look at the pipeline, look at the calendar, place the next post. Not tied to writing — scheduling is a separate decision from drafting.

## Workflow roles and automation roadmap

### The flow

1. **Other repos submit** a draft to i-wonder (storyline with enough structure to evaluate)
2. **i-wonder intake** evaluates, accepts/rejects, categorises
3. **i-wonder production** finishes, edits, sets up image, links
4. **Scheduling agent** composes the calendar from what's review-ready

Four roles, each with its own responsibility. The submitting repo doesn't care about scheduling. The scheduling agent doesn't care where the draft came from.

### Current state — collaborative

All four roles are handled collaboratively (Jules + AI in conversation).

### Target state

| Role | Current | Target | Notes |
|------|---------|--------|-------|
| **Submission** | Manual copy between repos | Mycelium | Seamless cross-repo referencing, no manual copying |
| **Intake** | Collaborative | Autonomous AI | Evaluate submissions, categorise, accept/reject |
| **Production** | Collaborative | Stays collaborative | The voice is human. AI assists with craft — editing, structure, images. The creative core doesn't automate. |
| **Scheduling** | Collaborative | Autonomous AI | Compose the calendar, apply the algorithm, maintain strategic reserve |

### What stays collaborative

The thinking. The writing. The voice. The decisions about what matters. Production stays collaborative because the blog's voice is personal and the thinking is dialogue — it can't be delegated without losing what makes it work.

### What becomes autonomous

The management around the creative work. Intake, scheduling, pipeline housekeeping. These are structured decisions that follow rules — exactly what AI does well. The aim: we think and write together, AI manages everything else.
