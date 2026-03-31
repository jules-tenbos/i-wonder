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

Pipeline, categories, scheduling strategy, and operational checklists are in the [Public Conscious Persona spec](https://jules-tenbos.github.io/i-wonder/engineering/personas/public-conscious-persona/current) (source: `docs/engineering/personas/public-conscious-persona/current.md`).

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

## Dependencies

`requirements.txt`: google-api-python-client, google-auth-oauthlib, markdown
