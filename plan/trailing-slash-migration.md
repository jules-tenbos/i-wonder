# Trailing slash migration plan

Convert all site pages from `name.md` to `name/index.md` so every URL has a trailing slash. This future-proofs pages that may grow into sections.

## Why

A standalone `name.md` serves at `/name`. If later a directory `name/` is created with `index.md`, the old URL breaks. Converting everything now means any page can become a section without URL changes.

## Scope

- **113 site pages** to move (standalone `.md` → `directory/index.md`)
- **113 HTML redirect files** to create at the old path (meta-refresh pattern already used on the site)
- **All internal links** across site pages and blog posts to update (add trailing slashes)
- **Sitemap** to update (all trailing slashes)
- **Blog posts are excluded** from the move — they already have trailing slashes via `permalink:` in `_config.yml`
- **Blog label pages** (21 files in `blog/label/`) included in the move

## Redirect pattern

Same as existing redirects on the site (e.g., `positioning/close-affinity/seed/the-turn-in-science/index.html`):

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="canonical" href="https://splectrum.world/path/name/" />
  <meta http-equiv="refresh" content="0; url=/path/name/" />
</head>
<body>
  <p>This page has moved to <a href="/path/name/">/path/name/</a>.</p>
</body>
</html>
```

Redirects are NOT added to the sitemap. They will be retired once Google drops the old URLs from its index.

## Execution steps

### Step 1 — File moves (scripted)

For each standalone `.md` file:
1. Create the directory: `mkdir -p path/name/`
2. Move the file: `mv path/name.md path/name/index.md`
3. Create redirect: write `name.html` at the old location with meta-refresh to `/path/name/`

### Step 2 — Internal link updates (scripted)

Sweep all `.md` files (posts and pages) for internal links. For each link pattern `](/path/to/page)` where the target is a moved page, add trailing slash: `](/path/to/page/)`.

Exceptions:
- Links that already have trailing slashes — skip
- Anchor links (`#section`) — don't touch
- External links — don't touch
- Blog post links — already have trailing slashes

### Step 3 — Sitemap update

Replace all non-trailing-slash URLs with trailing-slash equivalents.

### Step 4 — Local test

Start Jekyll locally, spot-check:
- A few person pages load at new URL
- Old URLs redirect
- Internal links work
- Sitemap validates

### Step 5 — Commit and push

Single commit: "Trailing slash migration — move all pages to directory/index.md, add redirects"

## Pages by section

| Section | Count | Example |
|---------|-------|---------|
| Positioning persons | 34 | `persons/w/wittgenstein.md` → `persons/w/wittgenstein/index.md` |
| Positioning subjects | 11 | `subjects/p/pragmatism.md` → `subjects/p/pragmatism/index.md` |
| Positioning seed | 6 | `seed/the-turn-in-science.md` → `seed/the-turn-in-science/index.md` |
| Seed | 8 | `seed/original.md` → `seed/original/index.md` |
| Language | 5 | `language/software-languages.md` → `language/software-languages/index.md` |
| Engineering | ~25 | `engineering/substrate/avro.md` → `engineering/substrate/avro/index.md` |
| Vocabulary | 6 | `vocabulary/structure.md` → `vocabulary/structure/index.md` |
| Reality | 1 | `reality/relational-reading.md` → `reality/relational-reading/index.md` |
| Top-level | 3 | `about.md` → `about/index.md` |
| Blog labels | 21 | `blog/label/seed.md` → `blog/label/seed/index.md` |
| **Total** | **~120** | |

## Risk

- External links and bookmarks to old URLs will get the HTML redirect — not a 301, but Google follows meta-refresh redirects and will reindex
- Large commit but fully mechanical and scriptable
- Local test before push catches any broken links
