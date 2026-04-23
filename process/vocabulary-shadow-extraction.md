# Vocabulary shadow pages — two-pass extraction

A shadow page in `/vocabulary/site/` catalogues the vocabulary of a specific content page. The keyword table is produced by combining two review passes: cold and warm. Cold for breadth, warm for depth.

## Why

A single pass misses half the picture.

A **cold pass** — an agent with no site context — reads the page on its own terms and picks up the terms the page itself weights. Face-value vocabulary, what a first-time reader actually encounters.

A **warm pass** — embedded in the site's prior material — catches what cold cannot: compression-drift (a term used in two senses across the site), cross-site idiom, origin-and-borrowing patterns, terms that look ordinary in English but are operationally narrow on the site.

The two-pass shape earned itself on the first shadow page (home). Each pass surfaces something the other misses; the outputs are genuinely different in kind, not just in degree.

## How to apply

1. **Cold pass.** Run an agent with no broader site context (a fresh subagent given only the target page). Ask it to list load-bearing terms and phrases — things a reader would need to understand to follow the page.
2. **Warm pass.** With the rest of the site in view, re-read the page and the cold output. Add terms the cold pass missed because they look ordinary but are site-specific; flag terms used in two senses on the site; surface borrowings (e.g. Wittgenstein's "language game") and external anchors.
3. **Alignment check.** Before going further, compare cold against warm: does the cold reading sufficiently reflect the aims of the page as the warm pass understands them? If yes, proceed. If not, the page is not carrying its intent cleanly — that is a signal for content rework, not for glossing over in the shadow. Rewrite the page to the extent warranted, then run a fresh cold pass (and re-run the warm pass if scope has moved). Only a page whose cold and warm readings align is ready to have its vocabulary finalised.
4. **Consolidate into the table.** Columns: *Term / phrase*, *Language*, *Comment*. *Language* names the provenance (SPLectrum, SPLectrum engineering, general English, Wittgenstein, and so on). *Comment* gives brief usage context, and where the term is already defined in `/vocabulary/splectrum/...`, a cross-reference link.
5. **Review against the content page.** Two criteria:
    - Every load-bearing term on the page should appear in the table; anything in the table that doesn't actually carry weight on this page comes out.
    - General-language terms are included only where they do site-language work — used in a narrowed or site-specific sense, or carrying an implicit reference the page depends on. Plain vocabulary the reader already understands without site context stays out.

Shadow page form: the page opens with the breadcrumb, then the title *[Breadcrumb] — vocabulary*, then a one-line intro *"The vocabulary of [link to the content page]."* — then the table. The table is followed by `{: .vocabulary-shadow}` on its own line so the CSS stacks the columns on mobile.

## Upkeep

A shadow is only useful if it reflects the current state of its content page. Once a shadow exists, updating the content page triggers a shadow refresh as part of the update — fresh cold and warm passes, alignment check, table update where needed. Don't ship a content-page change without re-running the shadow if one exists.

## Optional link from the content page

A content page may surface its shadow with a top-link at the breadcrumb level, floating right.

- **Label:** *Vocabulary*. Short enough to sit cleanly; "page vocabulary" reads heavier than needed.
- **Hover (title):** *To explore the vocabulary used on this page, go to the vocabulary section* — or a shorter variant in the same spirit.
- **Implementation:** a Jekyll include placed where the link should appear, so the same unit can be dropped into any content page that opts in.
- **Optional per page.** The link appears only where the author decides the shadow is ready to be surfaced to readers. Shadow pages can exist without the link — they remain internal until their content page opts in.

Implementation of the include and its styling is on hold until several shadow pages have stabilised the pattern; this note documents the intended shape.

## Status

First draft. Written after the home shadow page; will be checked and refined against the next shadow page (mycelium index is the likely candidate — richer content, different register, a harder test of the pattern).
