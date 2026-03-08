# Blog Posting Guide

## Setup

- Blog: julestenbos.blogspot.com
- API: Blogger API v3 via `manage.py`
- OAuth: `credentials.json` (Google Cloud project "i-wonder-blog") + cached `token.json`
- Both files gitignored
- First run opens browser for OAuth consent; subsequent runs reuse cached token
- Blog ID auto-discovered from URL, cached in `token.json`
- WSL2: uses `open_browser=False` — copy the URL manually

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

1. Write/edit in `published/` (with date prefix) or `upcoming/`
2. Schedule or publish via `manage.py`
3. Update on Blogger as edits are made: `manage.py update <id> <file>`
4. `manage.py sync` to verify everything matches (checks LIVE + SCHEDULED)

## Images

- Use Unsplash URLs with size/crop parameters (e.g. `w=350&h=230&fit=crop&crop=center`)
- Float left styling: `style="float:left;margin:0 15px 10px 0;width:350px;"`
- Place `<img>` tag directly in markdown — passes through to HTML

## Line Breaks

- Paragraph breaks: empty line between paragraphs (standard markdown)
- Line breaks within a paragraph: use `<br>` explicitly
- Trailing two-space trick does NOT work (spaces get stripped by tooling)

## Dependencies

`requirements.txt`: google-api-python-client, google-auth-oauthlib, markdown
