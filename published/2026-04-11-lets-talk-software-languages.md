# Let's Talk Software Languages

<img src="https://images.unsplash.com/photo-1627453999411-dd9c2604c109?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Letters" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

In this post we ask the question: is there a simplest language? Can one expect languages to stack from simple to complex?

Living in the era of computers there is a good place to ask this question: the stack of programming languages. Programming languages are simpler to reason within since they have strict internal logic, but otherwise are no different in essence. And there has already been enough evolution so that we are presented with a layered stack.

The evolution of natural language is no different, but more difficult to appreciate since the 'content language' using the same underlying natural language isn't strictly versioned, and the natural lanuage carrier has its own coupled evolution. 



---
<small>Photo: <a href="https://unsplash.com/@brett_jordan">Brett Jordan</a> / Unsplash</small>

---

## Notes

### What this post does

Searches for the simplest language. Uses programming languages as the concrete, provable example — they're fully documented, every rule explicit, every translation verifiable. The reader sees structural patterns in programming languages, then recognises them in their own natural language. The post earns structural vocabulary that later posts can build on.

### What this post is NOT

- Not about the seed. Does not introduce or reference the principle
- Not about "exotic" languages (physics, biology, cells, quantum). Stays within programming languages and natural language
- Not a philosophical argument. Shows structure through a concrete, verifiable domain

### The reader walks away with

- **Language stacking** — languages built on languages, sentences of one becoming vocabulary of the next. Not hierarchy (simple to complex) but context switching — each language complete for its context
- **The carrier is a language** — meaning at every level, no meaning-free bottom
- **Compositionality** — the same mechanism at every level
- **Bootstrapping** — no language is self-founding, every language needs another first. And the simplest language needs a far more complex language to explain it
- **Equivalence** — different languages, same content, provably (if the program runs, the translation preserved the meaning)
- **The simplest language is a myth** — simplicity is about vocabulary and grammar fitting a context, not about capacity. Binary has two symbols but can express anything Python expresses

### Arc

**1. The question.** What is the simplest language? Not the simplest human language — the simplest language, period. Programming languages offer a clean place to look.

**2. Binary as a language.** Two symbols: 0 and 1. Already a language — vocabulary (0, 1), grammar (position, sequence, endianness), meaning (absence/presence). Not meaningless data waiting for interpretation. The bottom is already a language.

Grammar on top of a binary carrier: sequence (which bit first), grouping (8 bits = byte), frequency (clock speed), direction (endianness). Outside computers: Morse code — same binary carrier (signal/no signal), different grammar (dot/dash, spacing). A light switch — on/off becomes language the moment you add time (one flash = yes, two = no, SOS). The carrier is binary; grammar makes it a language. Stacking starts immediately.

**3. The stacking.** Walk up the programming language stack. Binary → machine code → assembly → high-level (C) → very high-level (Python) → AI (natural language in, natural language out, computed in binary). At each step, the outputs of one language become the inputs of the next. Each a complete language in its own context, with its own vocabulary, grammar, and meaning.

**4. What the stacking reveals.** Meaning at every level. Compositionality — same mechanism at every level. Bootstrapping — no language appears from nothing (Wheeler's 31 words of binary, 1949). Equivalence — same computation expressed at every level, provably (5! in binary, machine code, assembly, C, Python — same result).

**5. The pattern in natural language.** Letters → words → composite words → sentences → paragraphs → narratives. Same stacking, same compositionality. The programming language stack and natural language use the same structural mechanism. Not metaphor — same pattern.

**6. Closing.** The search for the simplest language doesn't find a bottom — it finds language already there. Even binary is already a language with meaning. And it needs a far more complex language to explain it — the simple can't account for itself. Complex can be reduced to simple, but complex remains required to explain it.

The "simplest language" is a myth. Every language is about the right vocabulary and grammar for the context it operates in. A language's capacity to express is independent of the size of its vocabulary. Language shapes thinking — a programmer thinks differently in Python than in assembly, not because one is smarter but because the language makes different things visible.

### Key sources

- **Wheeler's 31 words** (1949) — bootstrapping story
- **Shannon** — letter-level statistics carry information about the language
- **Turing** — given a carrier and rules, you get universality
- **The factorial example** — same computation at every level, concrete proof of equivalence

### Tone

Accessible, concrete, no philosophical prerequisites. First person (blog voice). The reader is intelligent but not necessarily technical — programming examples explained clearly enough that a non-programmer follows the structural point. The technical detail supports the insight; it's not the point itself.

Curious, not assertive. "Here's what I found when I looked" rather than "language is X."
