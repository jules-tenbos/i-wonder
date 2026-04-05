# Blog Posting Guide

## Setup

- Blog: julestenbos.blogspot.com
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

Pipeline, categories, scheduling strategy, and operational checklists are in the [Public Conscious Persona spec](https://jules-tenbos.github.io/in-wonder/engineering/personas/public-conscious-persona/current) (source: `docs/engineering/personas/public-conscious-persona/current.md`).

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
- **Persona** — who is speaking: Splectrum (official voice), comment (observing existing work), thought (original, loosely offered), or a named source (Wittgenstein, RQM, etc.)

Not every post has all three. Max 3 labels.

## Reference Library

The reference library lives in `docs/` and is served at `jules-tenbos.github.io/in-wonder/`. It is the primary — the blog promotes it, not the other way around.

### Page template

Every reference library page follows this structure:

```markdown
[In Wonder - The World of Splectrum](link-to-root) > [Parent](link) > Page Title

# Page Title

Content...

---

*© 2026 In Wonder - The World of Splectrum, Jules ten Bos. The conversation lives at [In Wonder - The Conversation](https://julestenbos.blogspot.com).*
```

- **Breadcrumb** at the top — relative links back to root. Root `index.md` has no breadcrumb.
- **Footer** — standard navigational footer on every page.
- **No blog links** in content — the library doesn't link to blog posts. Blog posts link into the library.
- **External links** — SEP, Wikipedia for stable references.

### Linking from blog posts

- Series label link: `/search/label/<series>` (Blogger label filter)
- Reference library link: `https://jules-tenbos.github.io/in-wonder/<area>/`
- Post footer pattern: `<small>This post is part of the [series](/search/label/series). More in the <a href="url">area of the reference library</a>.</small>`

## Links

### General
- Maximum 5 links per post (internal + external combined)
- Link on first mention, not every mention
- Not in the first sentence — let the reader settle in
- Every link should add value — if the reader wouldn't learn anything useful by clicking, don't link

### Internal links
- No forward links to future/scheduled posts
- Back-references to other posts: prefer series label link (`/search/label/<series>`) over direct post links
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
