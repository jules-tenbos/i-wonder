# Let's Talk Software Languages

<img src="https://images.unsplash.com/photo-1625459201773-9b2386f53ca2?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Software code" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

Natural languages are ambiguous by nature, context-dependent, evolving, full of implication and unspoken meaning. Software languages on the other hand are fully explicit. Every rule is written down, every translation is specified, every ambiguity is eliminated by design. A compiler either accepts a statement or rejects it — there's no "roughly what you mean." The difference between the two is in how much is explicit versus implicit. That's why software languages are a clean place to look for insight. The structure that's hidden in natural language is exposed in software. You can see it, verify it, prove it.

Software languages at the lower level are procedural by nature, sets of instructions that need to be executed in order.

Consider a simple instruction: `x = 3 + 4` — calculate three plus four and assign it to variable x. No problem for us to understand the instruction. However, it's not in the form that a computer can understand and execute it.
At the execution and storage level computers use the binary language, a language written with an alphabet containing only two symbols: 0 and 1. At the heart of a computer is a processor, a unit with a fixed instruction set to execute this binary language - these are the vocabulary and rules of the computer language game. 

The simple instruction in binary language for a 6502 8-bit processor is:

```
10101001 00000011
01101001 00000100
10000101 00010000
```

Three instructions, six bytes. Each instruction is two bytes: an opcode (what to do) and an operand (with what). The result is 7, stored in memory.
We can't really work easily with binary language, so binary language gets translated into an intermediate language, assembly, which gives human-readable names to the binary instructions:

```
LDA #$03    ; Load 3 into accumulator
ADC #$04    ; Add 4 to accumulator
STA $10     ; Store result in memory (variable x)
```

One-to-one mapping with the binary. Same instructions, different notation. Already more readable — the reader can follow the logic without decoding 0s and 1s.
Three languages, one computation. Python, assembly, binary. Each a different language. Same result: 7.

This isn't coincidence. In 1936, Alan Turing proved — mathematically — that computation is fundamentally about symbols and interaction between symbols. A tape, a read/write head, a set of rules: if you see this symbol, write that symbol, move, change state. Nothing else. No numbers, no logic, no meaning built in. The meaning emerges from the rules.

And the minimum is already universal. Turing showed that this simple setup can compute anything that can be computed — anything any computer ever built can do. The simplest level already has the full power. Binary, assembly, Python — all equivalent in capacity. The vocabulary changes. The power doesn't.

He also proved there are limits. Some computations never halt — anything circular runs forever. And no general procedure can determine in advance whether an arbitrary program will halt or not. The language is universal but not omnipotent.

A computer is only as capable as its binary instruction set. Irrespective of what a computer is used for — complex documents, spreadsheets, images — all instructions are executed as binary codes. Why then those 'higher' languages?

Because higher languages don't add power — they reduce complexity to simplicity. `x = 3 + 4` absorbs six bytes of binary instructions into five characters. The complexity doesn't disappear — it's handled by the compiler. The programmer sees simplicity. That's what higher languages do: they absorb the complexity of the level below into a vocabulary and grammar that lets you think in concepts that match the problem.

Each language level is a different language game. The binary game: every bit matters, nothing is hidden. The assembly game: instructions with names, but still step by step. The Python game: think in concepts, the machine details are taken care of. Same computation, different game. The game determines what you see and what you don't — and shapes how you think.

Getting here was not easy. The first binary computers only had binary language — everything had to be written in the most basic instruction set. The first assembler was 31 instructions written by hand in binary — David Wheeler, Cambridge, 1949. Those 31 words, loaded into the machine, allowed it to accept programs in a slightly more readable form. Every programming language since has been built on top of something that came before, all the way back to those 31 hand-written binary instructions. No language is self-founding — each one needed another language first. Now we have an ecosystem of languages, each with their own strengths and weaknesses, each with their own language game — but eventually all executed as binary code at processor level. AI is changing this landscape further — but that's for another time.

Think of humans speaking different natural languages, doing different language games — but eventually all translated into the same type of muscle movement and bodily activity. The parallel is structural, not metaphorical. A stack of languages, each suited to its context, each absorbing complexity into its own vocabulary, all eventually becoming physical action.



---
<small>Photo: <a href="https://unsplash.com/@carlgonz">Carl Gonzalez</a> / Unsplash</small>

---


### 5. Python — thinking changes

`x = 3 + 4`. The programmer isn't telling the machine what to do step by step. They're expressing an idea — "x is the sum of 3 and 4." The language shapes the thinking. In assembly you think in operations. In Python you think in concepts.

The Python programmer doesn't think about the binary underneath. Doesn't need to. But it's all there — every level active, every translation happening. The same content, expressed in a language that shapes a different kind of thinking.

The surprise: Python isn't more powerful than binary. It's easier to think in. The vocabulary matches how humans reason — variables, functions, names. Binary matches how the machine operates. Same capacity, different fit. A language's power isn't in its vocabulary size — it's in how it fits the context.

### 5b. Entities, encapsulation, message passing

At the Python level, another pattern becomes visible: object-oriented programming. Software is organised into entities (objects), each with its own internal state that others can't directly access (encapsulation). They communicate through message passing — one object sends a message, another receives it and acts. Alan Kay, who coined "object-oriented programming," said the big idea was messaging, not objects.

This is a structural pattern: entities with internal state, a medium between them, messages that carry meaning, actions that follow. It holds at every level of the software stack — a processor instruction is a message to a register, a function call is a message between parts of a programme. The pattern is the same; the language changes.

### 6. What the stacking reveals

**Meaning at every level.** Binary already has meaning. Machine code has richer meaning. Each level adds expressiveness but doesn't add meaning to something that had none.

**Equivalence.** The same computation at every level. If the program runs, the translation preserved the meaning. Different languages, same content — provably.

**Bootstrapping.** No language appears from nothing. Someone had to write the first assembler in binary by hand (Wheeler, 31 words, 1949). Every language needed another language first. And the simplest language needs a far more complex language to explain it — the simple can't account for itself. Complex can be reduced to simple, but complex remains required to explain it.

**Language shapes thinking.** A programmer thinks differently in Python than in assembly — not because one is smarter but because the vocabulary makes different things visible. The language you use determines what you can see.

---

### Key sources

- **Wheeler's 31 words** (1949) — bootstrapping story
- **Shannon** — letter-level statistics carry information about the language
- **Turing** — given a carrier and rules, you get universality

