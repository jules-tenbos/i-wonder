# Blog Posting Guide

## Setup

- Blog: splectrum.world
- API: Blogger API v3 via `manage.py`
- OAuth: `credentials.json` (Google Cloud project "i-wonder-blog") + cached `token.json`
- Both files gitignored
- First run opens browser for OAuth consent; subsequent runs reuse cached token
- Blog ID auto-discovered from URL, cached in `token.json`
- WSL2: uses `open_browser=False` — copy the URL manually
- Google Search Console: when requesting indexing, use `?m=1` suffix on URLs (Blogger mobile redirect), otherwise redirect error

## Commands

```bash
python3 manage.py list                              # list published posts
python3 manage.py get <post-id>                     # show a specific post
python3 manage.py publish <markdown-file>           # publish immediately
python3 manage.py draft <markdown-file>             # create as draft
python3 manage.py schedule <markdown-file> <datetime>  # schedule for future date
python3 manage.py update <markdown-file>             # update (uses Blogger-ID from file)
python3 manage.py update <markdown-file> <post-id>  # update with explicit ID
python3 manage.py delete <post-id>                  # delete (with confirmation)
python3 manage.py sync                              # diff repo vs live blog
python3 manage.py page-list                         # list pages
python3 manage.py page-publish <markdown-file>      # publish a page
python3 manage.py page-update <page-id> <md-file>   # update a page
python3 manage.py page-delete <page-id>             # delete a page
```

## Markdown Format

- `# Title` on first line → post title
- Optional `Labels: label1, label2` on line after title
- Optional `Blogger-ID: <id>` on line after labels — enables `manage.py update <file>` without explicit ID
- Body converted markdown → HTML via `markdown` library (extra, sane_lists)

## Publishing Workflow

Pipeline, categories, scheduling strategy, and operational checklists are in the [Public Conscious Persona spec](https://splectrum.world/engineering/personas/public-conscious-persona/current) (source: `docs/engineering/personas/public-conscious-persona/current.md`).

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
2. Update `docs/vocabulary.md`
3. Update reference library index pages
4. Update `docs/sitemap.xml` if new pages were added
5. Render diagrams to images if any
6. Create clean post file in `published/` (prose + image refs only, no notes)
7. Schedule on Blogger
8. Delete draft from `drafts/`
9. Delete submission from `submissions/` (if not already deleted)
10. Commit and push

## Images

- Use Unsplash URLs with size/crop parameters (e.g. `w=350&h=230&fit=crop&crop=center`)
- Float left styling: `style="float:left;margin:0 15px 10px 0;width:350px;"`
- Place `<img>` tag directly in markdown — passes through to HTML

### Comment template

All comment posts use the same image and credit:

```markdown
<img src="https://images.unsplash.com/photo-1421789665209-c9b2a435e3dc?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Comment" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />
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

The reference library lives in `docs/` and is served at `splectrum.world/`. It is the primary — the blog promotes it, not the other way around.

### Page template

Every reference library page follows this structure:

```markdown
[In Wonder - The World of SPLectrum](link-to-root) > [Parent](link) > Page Title

# Page Title

Content...

---

*© 2026 In Wonder - The World of SPLectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://splectrum.world).*
```

- **Breadcrumb** at the top — relative links back to root. Root `index.md` has no breadcrumb.
- **Footer** — standard navigational footer on every page.
- **No blog links** in content — the library doesn't link to blog posts. Blog posts link into the library.
- **External links** — SEP, Wikipedia for stable references.

### Linking from blog posts

- Series label link: `/blog/label/<series>` (Blogger label filter)
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

## Dependencies

`requirements.txt`: google-api-python-client, google-auth-oauthlib, markdown
