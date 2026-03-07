# I Wonder

Where Splectrum meets the world. Blog and research repository for [julestenbos.blogspot.com](https://julestenbos.blogspot.com).

Coauthored by Jules Tenbos and Claude AI.

## Structure

- **[published/](published/)** — Published blog posts
- **[pages/](pages/)** — Published blog pages
- **[upcoming/](upcoming/)** — Drafts and working material
- **[foundation/](foundation/)** — The Splectrum principle, methodology, and voice
- **[materials/](materials/)** — Research corpus (language research, thinker maps)

## Foundation

1. **A View from the Perimeter** — Scientific convergence on relational/structural understanding
2. **The Primordial Seed** — The five core statements of the principle
3. **The Seed Unpacked** — What the principle contains and where it points
4. **Ways of Working** — Methodology across exploratory, diversification, and consolidation phases
5. **Tone of Voice** — Personal, accessible, question-driven writing style

## Blog Management

`manage.py` — CLI tool for managing posts and pages via Blogger API v3.

```bash
python3 manage.py list                          # list published posts
python3 manage.py publish <markdown-file>       # publish from markdown
python3 manage.py draft <markdown-file>         # create as draft
python3 manage.py update <post-id> <md-file>    # update existing post
python3 manage.py sync                          # diff repo vs live blog
python3 manage.py page-list                     # list pages
python3 manage.py page-publish <markdown-file>  # publish a page
```

See [posting-guide.md](posting-guide.md) for details.
