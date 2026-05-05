# SEO implementation plan

Implementing the standards from `tone-of-voice/seo-standards.md`. Work is grouped into phases that can be done incrementally without blocking publishing.

---

## Phase 1 — Template changes (do once)

These are one-off code changes that make the `description:` field work site-wide.

1. **Update `home.html` layout** — use `post.description` for the blog summary, falling back to `post.content | strip_html | truncatewords: 30` when no description exists yet.
2. **Update `blog/index.md` listing** — same change: prefer `post.description` over truncated content.
3. **Update all label pages** (`blog/label/*.md`) — same pattern.
4. **Verify `jekyll-seo-tag`** generates `<meta name="description">` from front matter — it should already, but confirm in rendered output.

## Phase 2 — Descriptions for published posts (batch)

Add `description:` to front matter of the 23 posts with status ready/final. These are live and indexable now.

- Each description: 120–155 characters, captures the argument or insight.
- Also serves as the listing summary once Phase 1 is done.
- Can be done in batches (e.g. 5–8 posts per session).

Posts to cover:
- All posts from 2026-03-07 through 2026-08-24 that have status `ready` or `final review` or similar.
- Skip the 20 storyline/stub posts — they aren't published yet and will get descriptions when written.

## Phase 3 — Descriptions for reference pages (batch)

Add `description:` to the ~50 reference pages (seed, positioning/persons, positioning/subjects, language, reality).

- Each description: 120–155 characters, states what the page is.
- Can be done in batches by section (e.g. all person pages in one session, all subject pages in another).

Sections:
- `seed/*.md` (8 pages)
- `positioning/persons/*/*.md` (22 pages)
- `positioning/subjects/*/*.md` (9 pages)
- `language/*.md` (6 pages)
- `reality/*.md` (4 pages)
- Top-level pages: `about.md`, `haicc.md`, `p2p.md`, `index.md` (4 pages)

## Phase 4 — Post length compliance

Check the 23 published posts against the 300–600 word band.

- **Over 600 words** (roughly 10 posts): decide per post whether to trim or accept as-is. Some long posts may justify their length if the argument needs it — the standard is a guideline, not a guillotine.
- **Under 300 words**: currently only the storyline/stub posts, which aren't published. No action needed unless one goes live.

## Phase 5 — Sitemap hygiene

- Add `<lastmod>` to the handful of sitemap-site.xml entries that lack it.
- Confirm all recently added pages (Rovelli, RQM, Solé, mutualism subject page, from-arrow-to-historicity) are in the sitemap. Cross-check against the file system.

## Phase 6 — Ongoing habits (no deadline)

These are not tasks but practices to fold into the publishing process:

- Every post gets a `description:` when it moves to `status: ready`.
- Every new reference page gets a `description:` at creation time.
- New pages added to sitemap at creation time (already in posting-guide).
- Internal link density grows naturally as pages arrive — no forced retrofit.

---

## Order of work

Phase 2 and 3 first — get descriptions written across posts and reference pages. Then Phase 1 flips the templates to use them (a clean switch rather than a gradual rollout with fallbacks). Phase 4 and 5 are low-priority cleanup. Phase 6 is just "how we work from now on".
