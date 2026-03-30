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

## Draft pipeline

```
drafts/
  core/           — substantial, from P1-P5
  research/       — analysing other vocabularies
  thinking/       — small bites, specific insights
  engineering/    — practical, tools, methods
  commentary/     — reactions, timely
```

### Draft lifecycle

1. **Idea** — a topic and category. A sentence or two.
2. **Storyline** — enough structure to judge whether it works as a post. This is the submission.
3. **Accepted** — the storyline works. Post is approved for writing.
4. **Draft** — first full text written.
5. **Review ready** — reviewed, cleaned, ready for scheduling.

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
