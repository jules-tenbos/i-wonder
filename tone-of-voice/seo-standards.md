# SEO standards — help the page be found

Every published page should be discoverable by someone who doesn't yet know SPLectrum exists. SEO is not marketing language or keyword stuffing — it is making sure the page carries enough structural signal that a search engine can match it to the right query.

## Why

SPLectrum deals in concepts that people search for — relational philosophy, pragmatism, philosophy of language, decentralised systems. The content is there; the structural signals often aren't. Without them, Google picks its own snippet, guesses the topic, and the page sits invisible. A few small habits at authoring time change that entirely.

## How to apply

### Meta descriptions

- Every page and post must have a `description:` field in front matter.
- 120–155 characters. One sentence that says what the page offers a reader.
- Unique per page — never duplicate across pages.
- Include the core concept the page addresses, phrased the way a searcher would type it.
- Blog posts: capture the argument or insight, not the topic label. "How SPLectrum's six seed principles map onto the history of Western philosophy" over "A post about philosophy".
- Reference pages: state what the page is. "Rorty's key concepts — anti-representationalism, conversation, edifying philosophy — and where SPLectrum positions relative to them."

### Page length

- **Blog posts: 300–600 words.** This band is long enough to avoid thin-content penalties and short enough that headings are unnecessary. Posts are conversations — one argument, one point, no subdivisions.
- **Reference pages (persons, subjects, seed): 300+ words.** Use `##` headings to structure sections. No hard maximum — the touchstone principle governs upper length.
- **Landing/hub pages** (seed index, positioning index, etc.) may start lighter and grow as the site develops organically. A sparse landing page with clear purpose is not thin content — it becomes a problem only if it stays empty indefinitely with no reason to exist.

### Internal linking

- Aim for 3–5 internal links per post and per reference page. This is a direction of travel, not a hard gate — the site is growing organically and link density will build as pages arrive.
- Reference pages should link to other reference pages where the connection is genuine (not forced).
- Hub pages will naturally gain contextual links as child pages are created.
- Link text should be descriptive: `[Wittgenstein's language games](/positioning/persons/w/wittgenstein)` not `[click here](/positioning/persons/w/wittgenstein)`.

### Titles

- The front matter `title:` becomes the HTML `<title>` (via jekyll-seo-tag). It should be clear and specific.
- For reference pages: name the subject. "Rorty", "Pragmatism", "The SPLectrum Seed".
- For blog posts: name the insight or question. Titles that work as standalone phrases rank better than clever-but-opaque ones.
- Keep titles under 60 characters where possible — Google truncates beyond that.

### Images

- Every `<img>` must have an `alt` attribute.
- Alt text should describe what the image shows or represents — not repeat the page title verbatim unless the image is literally of that thing.
- Decorative images (thumbnails, dividers) may use `alt=""` but this should be the exception.

### Sitemap

- Every new page must be added to `sitemap-site.xml` at creation time.
- Include a `<lastmod>` date — update it when the page content changes materially.
- The blog sitemap is auto-generated; no action needed there.

### What not to do

- Don't write for search engines at the expense of the reader. The tone-of-voice principles (non-claiming, touchstone, is-like-not-is) take precedence over SEO phrasing.
- Don't stuff keywords. One or two natural mentions of the core concept is enough.
- Don't add descriptions that promise more than the page delivers — that harms bounce rate, which harms ranking.
- Don't duplicate content across pages for SEO purposes. Each page earns its own place.
