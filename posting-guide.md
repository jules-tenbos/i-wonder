# Blog Posting Guide

## Setup

- Site: splectrum.world (GitHub Pages from docs/)
- Blog: splectrum.world/blog/ (Jekyll posts in docs/_posts/)
- Reference library: splectrum.world/ (Jekyll pages in docs/)
- Theme: minima with custom head.html, header.html, footer.html, post.html, home.html

## Publishing

Posts live in `docs/_posts/` as Jekyll markdown with front matter. Future-dated posts are hidden by Jekyll until their date arrives. To publish: commit to main and push.

## Cadence

- Substantial posts: every 4 days.
- Lighter posts: optionally in between, 2 days after the preceding post.
- Schedule time: 10:00 UTC.
- Active schedule tracked in `scheduled-tasks.md`.

## Markdown Format

Jekyll front matter:

```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
labels: [series, category, persona]
---
```

Filename: `YYYY-MM-DD-slug.md` in `docs/_posts/`.

## Publishing Workflow

Pipeline, categories, scheduling strategy, and operational checklists are in the [Public Conscious Persona spec](https://splectrum.world/engineering/splectrum/haicc/personas/public-conscious-persona/current) (source: `docs/engineering/splectrum/haicc/personas/public-conscious-persona/current.md`).

## Production — Way of Working

### Conscious thought handling

Collaborative. Submissions go through analysis, discussion, and decision before becoming drafts. The submission's frontmatter tracks status: `new → in-progress → draft-ready`.

### Draft template

The draft file is the single workspace. The post section is extractable as-is on scheduling.

```markdown
---
title: Post title
series: e.g. mycelium, language
category: e.g. engineering, philosophy
persona: e.g. SPLectrum, comment, thought
status: storyline | draft | review-ready
---

# Post Title
Labels: label1, label2, label3

<img src="IMAGE_URL" alt="ALT" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

[post content]

<small>This post is part of the [series name](/blog/label/series). More in the <a href="https://splectrum.world/area/">area of the reference library</a>.</small>

---
<small>Photo: <a href="https://unsplash.com/@photographer">Name</a> / Unsplash</small>

---

# Notes

## Storyline

### 1. Section
- point
- point

---

## Reference page — docs/path/to/page.md

[page content ready to copy]

---

## Vocabulary updates

- **Term** — definition

---

## Tasks on scheduling

- [ ] task
```

### Collaborative flow

1. **Scope** — discuss what the draft produces: post, reference pages, vocabulary updates
2. **Storyline** — Claude proposes storyline items (points, not prose). Jules steers, adds, corrects. Iterative until agreed
3. **Reference pages** — Claude organises reference page content in the draft, drawing from storyline and submission
4. **Narrative** — Jules writes the flowing text from the storyline
5. **Improve** — Claude improves on the narrative
6. **Edit cycles** — collaborative until review-ready
7. **Production tasks** — image selection, links, final review

### On scheduling

The draft produces its outputs and is then deleted:

1. Create/update reference pages in `docs/`
2. Update the relevant vocabulary page under `docs/vocabulary/`
3. Update reference library index pages
4. Update `docs/sitemap-site.xml` if new pages were added
5. Render diagrams to images if any
6. Create clean post file in `docs/_posts/` (Jekyll front matter + prose, no notes)
7. Delete draft from `drafts/`
8. Delete submission from `submissions/` (if not already deleted)
9. Commit and push

### Pending ref lib → blog links

Ref lib pages can point into the blog, but only once the post is published. Pre-wire pending links now using the `pending-link` include — they emit the sentence only after the publish date has passed, as evaluated at build time.

Syntax:

```
{% include pending-link.html date="YYYY-MM-DDT00:00:00Z" text="See [Title](/blog/YYYY/MM/slug/) for the blog conversation." %}
```

The include compares `site.time` (build time) against the `date` parameter. If the build is on or after the publish date, the sentence is emitted into the page; otherwise, nothing. This guarantees the link can only appear in a build that also includes the target post.

A daily rebuild runs at 10:00 UTC via `.github/workflows/daily-rebuild.yml`, re-evaluating all pending links against the current date.

**Local preview of pending links.** The include honours Jekyll's `--future` flag — when set, all pending links emit regardless of date (same flag that exposes future-dated posts). To preview everything as it will eventually look:

```
jekyll serve --watch --host 0.0.0.0 --future
```

Without the flag, local behaviour matches production: pending links and future-dated posts stay hidden until their date.

When scheduling a post, scan ref lib pages for ones that would benefit from a pointer to it and add the include. Common targets:

- The relevant area's index.
- Seed incarnation pages if the post unpacks a principle.
- Touchstone pages adjacent to the post's topic.

### Blog post review checklist

When reviewing existing or new posts, check:

1. **Front matter** — layout: post, title, date, labels (max 3, from series/category/persona)
2. **Image** — no inline float styles (CSS handles sizing). Just `<img src="..." alt="..." />`
3. **Internal links** — use absolute paths (`/seed`, `/engineering/splectrum/mycelium/`). No old Blogger URLs, no `jules-tenbos.github.io`, no `.html` extensions
4. **External links** — max 5 total. People → SEP/Wikipedia. Works → accessible version. Topics → Wikipedia/SEP. Open in new tab handled by JavaScript
5. **Series footer** — `<small>This post is part of the [series name](/blog/label/series). More in the <a href="/area/page">page name</a> of the reference library.</small>` Link to the specific ref lib page, not just the area
6. **Photo credit** — `<small>Photo: <a href="...">Name</a> / Unsplash</small>` separated by `---`
7. **No old Blogger artefacts** — no `Blogger-ID:`, no `Labels:` line (use front matter), no bold date lines in body, no `/search/label/`, no `/p/xxx.html`
8. **Voice** — matches the persona label. Author voice for thought/comment, SPLectrum voice for seed/engineering, narrator for named sources

## Images

- Use Unsplash URLs with size/crop parameters (e.g. `w=350&h=230&fit=crop&crop=center`)
- No inline styles — CSS handles sizing (80% centered on desktop, responsive on mobile)
- Place `<img>` tag directly in markdown — passes through to HTML

### Comment template

All comment posts use the same image and credit:

```markdown
<img src="https://images.unsplash.com/photo-1421789665209-c9b2a435e3dc?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Comment" />
```

Credit footer:
```markdown
---
<small>Photo: <a href="https://unsplash.com/@whale">Matthew Smith</a> / Unsplash</small>
```

## Line Breaks

- Paragraph breaks: empty line between paragraphs (standard markdown)
- Line breaks within a paragraph: use `<br>` explicitly
- Trailing two-space trick does NOT work (spaces get stripped by tooling)

## Labels

Three dimensions: **series, category, persona**.

- **Series** — groups posts into a journey (e.g., positioning, language)
- **Category** — the domain (e.g., philosophy, science, engineering, HAICC)
- **Persona** — who is speaking: SPLectrum (official voice), comment (observing existing work), thought (original, loosely offered), or a named source (Wittgenstein, RQM, etc.)

Not every post has all three. Max 3 labels.

## Reference Library

The reference library lives in `docs/` and is served at `splectrum.world/`. Content roles:

- **Ref lib** — reference style. Concise, structural. No event narratives or stories.
- **Blog** — the conversation. Happenings, events, the stories behind how things evolved.
- **Documentation** — depth material, downloadable when needed (not on the live site).

Keep each surface doing its own job. If a page starts telling a story, that material belongs in a blog post; link from the ref lib to it. If a ref lib page needs depth beyond reference style, the depth belongs in a separate document.

### Sitemap lastmod

Sitemap structure: `docs/sitemap.xml` is the index pointing at `sitemap-site.xml` (ref lib, manually maintained) and `sitemap-blog.xml` (blog posts, auto-generated from `site.posts`). Only the site sitemap needs hand edits.

When a ref lib page changes substantively — new page, structural rework, major content update — add or bump `<lastmod>YYYY-MM-DD</lastmod>` on its entry in `docs/sitemap-site.xml`. Crawlers (Google confirmed re-reads regularly) use lastmod to prioritise re-crawl. Changes should be visible there.

Skip lastmod bumps for minor changes (typos, link fixes, sentence polish). The goal is signal-of-substance, not coverage of every commit — noise dilutes the signal.

New URLs added to the site sitemap get `<lastmod>` on first appearance. Moved URLs (structural rename) likewise get lastmod at the move date; the old URL is removed in the same sitemap edit.

### Page template

Every reference library page follows this structure:

```markdown
[Home](/) > [Area](/area/) > Page Title

# Page Title

Content...
```

- **Breadcrumb** at the top — absolute links. Root `index.md` has no breadcrumb.
- **Footer** — handled by template (footer.html). No inline footer in pages.
- **Links to blog** — allowed, and encouraged when a blog post tells the story behind a concept, event, or historical note. Keep them functional (not promotional): "For the story of how P0 joined the seed, see [And Then There Were Six](/blog/...)." Blog posts also link back into the ref lib for depth — both directions are fine. For pending links to scheduled future posts, use the `pending-link` include (see "Pending ref lib → blog links" above) — it only emits the sentence after the publish date has passed.
- **External links** — SEP, Wikipedia for stable references.

### Linking from blog posts

- Series label link: `/blog/label/<series>` (Jekyll label page)
- Reference library link: `https://splectrum.world/<area>/`
- Post footer pattern: `<small>This post is part of the [series](/blog/label/series). More in the <a href="url">area of the reference library</a>.</small>`

## Links

### General
- Maximum 5 links per post (internal + external combined)
- Link on first mention, not every mention
- Not in the first sentence — let the reader settle in
- Every link should add value — if the reader wouldn't learn anything useful by clicking, don't link

### Internal links
- No forward links to future/scheduled posts
- Back-references to other posts: prefer series label link (`/blog/label/<series>`) over direct post links
- Reference library links for depth — the blog points into the library
- Series/reference footer at the bottom when applicable

### External links
Three categories, all for the curious reader, woven into text, never academic:

1. **People** — first mention of a philosopher/scientist links to a biography (SEP preferred for philosophers if an entry exists, Wikipedia otherwise)
2. **Key works** — when mentioned by name, link to accessible version (arXiv, publisher, SEP)
3. **Topics/theories** — important concepts link to accessible explanation (Wikipedia, SEP)

No footnotes, no bibliography, no academic citation apparatus.
