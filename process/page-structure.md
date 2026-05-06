# Page structure — persons and subjects

Standard structure for positioning person and subject pages. Use these as templates when creating new pages.

## Person page

1. **Front matter**: title as "Firstname Lastname (born–died)", description, layout
2. **Breadcrumb**: Home > Positioning > Persons > Name
3. **Heading**: full name with dates
4. **Intro paragraph**: why this person matters to SPLectrum, with internal links to seed, positioning pieces, other persons
5. **Biographical paragraph**: external SEP link, life and career, one paragraph
6. **Key concepts**: bold term + explanation, one paragraph each
7. **Closing sections**: boundary or limitation sections — where the thinker stops, what SPLectrum picks up. These name the gap constructively, linking to other persons or seed pages where relevant
8. **Key works**: list with Wikipedia links, at the end before See also
9. **See also**: internal links to related seed, positioning, vocabulary pages

Reference: [Wittgenstein](/docs/positioning/persons/w/wittgenstein.md), [Rorty](/docs/positioning/persons/r/rorty.md)

## Subject page

1. **Front matter**: title (with abbreviation if applicable), description, layout
2. **Breadcrumb**: Home > Positioning > Subjects > Name
3. **Heading**: full name with abbreviation
4. **Intro paragraph**: why this subject matters to SPLectrum, with internal links
5. **Origin section**: where the concept comes from — the field it belongs to, but also where the pattern resonates beyond that field
6. **Core sections**: the substance — what the concept is, how it works, key distinctions. Internal links to persons and other subjects where relevant
7. **Meaning section**: what makes the concept more than technical — the semantic or philosophical weight of its constructs
8. **Why this matters**: connection to the seed principles, with a forward-pointing paragraph that opens the door without detailing what SPLectrum engineering will do
9. **Persons**: key figures associated with the subject, with links (Wikipedia for external, internal for persons with pages)
10. **See also**: internal links to related language, seed, engineering pages

Reference: [Domain Specific Languages](/docs/positioning/subjects/d/domain-specific-languages.md)

## Index pages

Both persons and subjects have an A–Z index page.

- **Persons**: Surname, Firstname (born–died) link · person type `<br>` keywords
- **Subjects**: Name (abbreviation) link · field `<br>` keywords
- Entries within a letter section get `li + li` spacing (handled by CSS)

## General

- Descriptions go in front matter on every page
- Internal links preferred over external; external links (SEP, Wikipedia) on the person/subject page itself, not scattered through posts
- Key works get Wikipedia links
- The page title in front matter matches the `# heading` on the page
