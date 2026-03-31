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
python3 manage.py update <post-id> <markdown-file>  # update existing post
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
- Body converted markdown → HTML via `markdown` library (extra, sane_lists)

## Publishing Workflow

See `blog-management.md` for full draft pipeline, categories, and scheduling strategy.

1. Submissions arrive in `submissions/` — raw thoughts, uncategorised
2. Accepted submissions move to `drafts/<category>/` — one file containing: notes, post storyline/prose, page(s) content, tasks
3. Drafts mature through: storyline → draft → review-ready (collaborative)
4. On scheduling, the draft produces multiple outputs:
   - Post → `published/` with date prefix → Blogger (scheduled)
   - Page(s) → `pages/` → Blogger (published)
   - Tasks → flagged in scheduled tasks
5. **The draft is always the master.** To update a live post or page: edit the draft, then republish. Never edit in `published/` or `pages/` directly.
6. `manage.py sync` to verify everything matches (checks LIVE + SCHEDULED)

## Images

- Use Unsplash URLs with size/crop parameters (e.g. `w=350&h=230&fit=crop&crop=center`)
- Float left styling: `style="float:left;margin:0 15px 10px 0;width:350px;"`
- Place `<img>` tag directly in markdown — passes through to HTML

## Line Breaks

- Paragraph breaks: empty line between paragraphs (standard markdown)
- Line breaks within a paragraph: use `<br>` explicitly
- Trailing two-space trick does NOT work (spaces get stripped by tooling)

## Links

### General
- Maximum 5 links per post (internal + external combined)
- Link on first mention, not every mention
- Not in the first sentence — let the reader settle in
- Every link should add value — if the reader wouldn't learn anything useful by clicking, don't link

### Internal links
- Posts that reference other posts should link to them
- Add links only when the target post is live
- "Next up" / "previous post" references should be actual links
- Standalone posts — links only if a natural reference point exists

### External links
Three categories, all for the curious reader, woven into text, never academic:

1. **People** — first mention of a philosopher/scientist links to a biography (SEP preferred for philosophers if an entry exists, Wikipedia otherwise)
2. **Key works** — when mentioned by name, link to accessible version (arXiv, publisher, SEP)
3. **Topics/theories** — important concepts link to accessible explanation (Wikipedia, SEP)

No footnotes, no bibliography, no academic citation apparatus.

## Content structure — posts and pages

The blog builds two things simultaneously:

- **Posts** — individual explorations. The journey, in chronological order. Each makes one or a few points and moves on.
- **Pages** — the body of work. The accumulated understanding. Synthesis, not timeline.

A reader arriving at a page sees the synthesis. A reader following posts sees the journey. Both paths work.

### Page types
- **Main pages** (sidebar) — compact overviews, updated with each new post. Link to territory pages.
- **Territory pages** (hidden or offlink — discoverable through main pages or posts, not in sidebar) — fuller exposition for a post series. Summarise the arc, link back to individual posts. These are where the thinking lives.

### How it works
- Posts are moments. Pages are where the body of work accumulates.
- Each post publication triggers a page update — synopsis when scheduled, full text with links when live.
- Territory pages grow as post series develop. When a main page gets crowded, split exposition into a territory page and keep the main page compact.
- Regular page updates support search engine freshness.

## Dependencies

`requirements.txt`: google-api-python-client, google-auth-oauthlib, markdown
