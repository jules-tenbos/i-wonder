# Quality rubric

## 1. Purpose

This rubric is an internal standard for reviewing posts and pages on splectrum.world. It exists to make reviews more consistent — so two reads of the same page converge rather than diverge — to benchmark the site against external quality frameworks rather than only internal taste, and to surface drift over time: where the voice, the purpose, or the clarity of a piece slides without anyone noticing. It is a checking tool, not an authoring tool; it belongs after drafting, not during. The rubric layers three lenses — an external yardstick (Google), a purpose check (Diataxis), and site-specific criteria (SPLectrum) — so a weak score in one lens is legible on its own terms rather than collapsing into a single vague "it doesn't feel right".

## 2. External yardstick: Google E-E-A-T and Page Quality

Google's public [Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) give a common-sense definition of quality that most readers implicitly expect.

**E-E-A-T.** Four concerns, with Trust at the centre:

- **Experience** — does the creator have first-hand or life experience with what the page is about.
- **Expertise** — does the creator have the necessary knowledge or skill for the topic.
- **Authoritativeness** — is the creator or site a known go-to source for this topic.
- **Trustworthiness** — is the page accurate, honest, safe, reliable. Untrustworthy pages have low E-E-A-T regardless of expertise or experience.

**Page Quality scale (5 points):** Lowest / Low / Medium / High / Highest. The scale is anchored by two ideas: whether the page has a *beneficial purpose* and whether it *achieves that purpose well*. Medium pages meet their purpose adequately; High clearly; Highest exceptionally, with evident effort, originality, talent.

**Limits for this kind of site.** splectrum.world is reflective, thought-led writing. It isn't YMYL (your-money-your-life), so harm-focused parts of the Lowest/Low criteria don't apply. The "Main Content serves the Main Purpose" frame still lands — every post has a stance it's trying to hold, and the rubric can ask whether it holds. Experience and Trust land especially well for personal reflective writing; Authoritativeness lands less (the site isn't trying to be a go-to source in a searchable-topic sense).

## 3. Purpose check: Diataxis

[Diataxis](https://diataxis.fr/) separates documentation into four modes by what the reader needs:

- **Tutorial** — learning-oriented; the reader is a student being taught by doing.
- **How-to guide** — goal-oriented; the reader has a task and needs it done.
- **Reference** — information-oriented; the reader consults for accurate, austere description.
- **Explanation** — understanding-oriented; discursive, reflective, away from the machinery.

Most of splectrum.world is **Explanation** — reflective, understanding-oriented, things you could read in the bath. Some pages (vocabulary, namespace convention, engineering ref) are **Reference**. Very little is tutorial or how-to.

Staying in purpose per type:

- *Explanation* posts should discuss and reflect; anti-pattern is sliding into how-to steps.
- *Reference* pages should describe neutrally and completely; anti-pattern is opinion, narrative, or instruction leaking in.
- If a page mixes modes without signposting, it usually needs to be split.

## 4. Site-specific criteria (SPLectrum)

Six criteria drawn from the principles in this folder. Each includes a concrete "check" prompt.

### Voice consistency
The voice is one person across all personas — curious, anti-hierarchical, concrete-minded — but the register shifts across the site's three axes. Topnav speaks as the author (Jules, personal). Ref lib speaks as narrator (impersonal, structural). Blog posts vary by persona label. A page scores high when its register matches its axis; a ref lib page that slides into first person, or a topnav page that over-systematises, scores low. See `tone-of-voice.md`, persona profiles in this folder.

**Check:** Does the register of this page match its axis? Can you tell from the voice alone which axis it belongs to?

### Standing back
SPLectrum sets examples, not prescriptions. Pages should hold the content and let it speak, not add trailing commentary about how SPLectrum relates. No authority-claiming language, no magister tone, no humble disclaimers — magister and humble are the same off-balance position from opposite directions. "Is like", not "is". See `setting-examples-not-imposing.md`, `is-like-not-is.md`, `learning-tone.md`.

**Check:** Does the page step back when the content already speaks? Anything prescriptive or authority-claiming that doesn't need to be?

### Clarity / touchstone
Ref lib pages are touchstones — reference points that ground other work. Touch on the topic enough to hold the point, then stop. Lighter wins over heavier as long as the point lands. Three named thinkers beat five. Missing depth is fixable; cluttered reference pages are hard to clean up later. See `touchstone.md`.

**Check:** Does every paragraph earn its place? Would removing X make the point land worse, or just make the page heavier?

### Signposting
Open territory and in-progress work should be named, not hidden. Use concrete forward pointers — series, research direction, upcoming page, blog label — where they land. Embryonic areas can say so. Concepts used with technical meaning should be documented explicitly in vocabulary. Don't let terms drift in without definition. See `signpost-road-ahead.md`, `explicit-concepts.md`.

**Check:** If this page has open edges or technical vocabulary, are they signposted? Does the reader know where they are and where to go next?

### Substance
Real thinking behind the page — not framing without content, not convergence claims that over-reach, not bipolar framing (good/bad, right/wrong, safe/dangerous) that smuggles in judgement. Pattern recognition across domains scores high; filler or assertion without grounding scores low. See `no-bipolar-framing.md` and the shared-foundation section of `tone-of-voice.md`.

**Check:** Strip the scaffolding — is there a real observation, connection, or argument left? Any bipolar construction or unearned authority claim?

### Cohesion
The page sits inside an ecosystem of other pages and posts. In the informational axis, vocabulary must be consistent across pages so readers moving between them see the same terms meaning the same things. Cross-page links should land where the framing actually matches. See the vocabulary-consistency note and three-axes section of `tone-of-voice.md`.

**Check:** Does this page use terms the way other pages do? Do its outbound links land in pages that match the framing used here?

## 5. How to use

Score each criterion on a 1–5 scale, using the Google PQ anchors as reference points: 1 = Lowest, 2 = Low, 3 = Medium, 4 = High, 5 = Highest. Half-steps (e.g. "High+") are allowed where a criterion sits clearly between two anchors.

A review produces a table plus comments:

| Lens | Criterion | Score | Note |
|---|---|---|---|
| Google | Experience | | |
| Google | Expertise | | |
| Google | Authoritativeness | | |
| Google | Trustworthiness | | |
| Google | Page Quality (overall) | | |
| Diataxis | Type declared | Explanation / Reference / … | |
| Diataxis | Stays in type | | |
| SPLectrum | Voice consistency | | |
| SPLectrum | Standing back | | |
| SPLectrum | Clarity / touchstone | | |
| SPLectrum | Signposting | | |
| SPLectrum | Substance | | |
| SPLectrum | Cohesion | | |

The comments column is where the review actually lives — a number on its own is a signal, not a verdict. A piece is publishable when no cell scores below 3 and the weighted feel of the SPLectrum block is High. Anything below 3 on Trust or Stays-in-type is a blocking issue, not a polish issue.

---

**Sources:**
- Google Search Quality Rater Guidelines — https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf
- Diataxis framework — https://diataxis.fr/
