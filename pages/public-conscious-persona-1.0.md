# Splectrum — Public Conscious Persona 1.0

This page describes how the blog operates as Splectrum's public conscious persona. The concept is introduced in [The Blog as Public Conscious Persona](/2026/05/the-blog-as-public-conscious-persona.html) — this page holds the technical detail.

## The model

- **Persona** — a communication channel, a language game with its own vocabulary, rules, participants. The blog owns the conversation with its readers.
- **Conscious** — material is made visible from other work. From that moment, the blog has full autonomy over it.
- **Public** — the conscious mind's work is private. The result is public. The persona speaks.

## Pipeline

<img src="https://raw.githubusercontent.com/jules-tenbos/i-wonder/main/published/images/2026-05-08-persona-flow-full.png" alt="Full pipeline flow diagram" style="max-width:100%;" />

```
submissions/        — raw material arrives here, uncategorised
                      (surfaced from other repos via Mycelium)
        ↓
    intake          — evaluate, accept or reject
        ↓
drafts/             — accepted, categorised, being worked on
  core/             — substantial Splectrum, building from P1-P5
  research/         — analysing other vocabularies, from Splectrum's position
  thinking/         — small bites, specific insights, mixed
  engineering/      — practical, tools, methods, Splectrum's practice
  commentary/       — reactions, timely, open
        ↓
    production      — structure, write, edit, image, links (collaborative)
        ↓
    scheduling      — compose the blog storyline (autonomous)
        ↓
published/          — date-prefixed, pushed to Blogger
```

## Categories

Categories are modes of engagement, not topics. The same topic can appear in any category.

| Category | What it is | Voice |
|----------|-----------|-------|
| **Core** | Substantial Splectrum. Building from P1-P5. | Splectrum speaking |
| **Research** | Analysing other vocabularies/traditions. | Observing from Splectrum's position |
| **Thinking** | Small bites. A specific insight, question, connection. | Mix — Splectrum or external or both |
| **Engineering** | Practical. How we work, tools, methods. | Splectrum's practice |
| **Commentary** | Reactions to current events, things encountered. | Open, responsive |

## Draft lifecycle

1. **Submission** — raw material in `submissions/`. No post standards required.
2. **Intake** — accept or reject. If accepted, categorise.
3. **Categorised** — moved to `drafts/<category>/`. Post storyline laid out.
4. **Draft** — full text written, edited, image, links.
5. **Review ready** — reviewed, cleaned, ready for scheduling.
6. **Scheduled** — published to `published/` with date prefix. Pushed to Blogger.

The draft is always the source of truth. Editing happens in `drafts/`, never in `published/` directly.

## Scheduling strategy

At least one core post per month. Scheduling horizon expands with productivity:

- 1 post/month → 1 month ahead
- 2 posts/month → 2 months ahead
- 4 posts/month → 4 months ahead
- 6-8 posts/month → 4-6 months ahead

Core posts form the strategic reserve — guaranteeing minimum rhythm when other sources slow down.

## Automation roadmap

| Role | Current | Target |
|------|---------|--------|
| **Submission** | Manual | Mycelium — seamless cross-repo referencing |
| **Intake** | Collaborative | Autonomous AI |
| **Production** | Collaborative | Stays collaborative — we think and write together |
| **Scheduling** | Collaborative | Autonomous AI |

*(This page grows as the persona evolves.)*
