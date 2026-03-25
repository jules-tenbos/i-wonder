# Let's Talk Software Languages

<img src="https://images.unsplash.com/photo-1627453999411-dd9c2604c109?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Letters" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

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

A computer is only as capable as its binary instruction set. Irrespective of what a computer is used for - complex documents, spreadsheets, images - all instructions are executed as binary codes. Why then those 'higher' languages?

Because they have a vocabulary and grammar - language game - that is more suitable to write the software needed to solve a problem. The language game influences the way we think, how we get and express insight.

Creating such languages is not an easy task. The first binary computers only had binary language - everything had to be written in the most basic instruction set.

---
<small>Photo: <a href="https://unsplash.com/@brett_jordan">Brett Jordan</a> / Unsplash</small>

---

## Notes

### 2. Binary — already a language

Start at the bottom. Two symbols: 0 and 1. Presence and absence. That's it.

But it's already a language. Vocabulary (0, 1), grammar (position, sequence), meaning (absence/presence). Not meaningless data waiting for interpretation.

Outside computers, the same pattern: Morse code — signal/no signal, with grammar (dot/dash, spacing). A light switch — on/off becomes language the moment you add time (one flash = yes, two = no, SOS). The carrier is binary; grammar makes it a language.

### 3. Processor level — binary gets grammar

Groups of bits become words: opcodes, registers, values. The processor "reads" these words. A language game between the programmer and the machine — vocabulary, rules, meaning. All still in binary, but structured.

This is where the stacking starts. The sentences of binary (sequences of 0s and 1s) become the vocabulary of a new language (machine instructions). Same bits, but now with structure on top.

### 4. Assembly — human-readable, one-to-one

The same processor words, given human-readable names: MOV, ADD, JMP. One-to-one mapping with the processor language. Letters forming words — the reader sees the natural language parallel immediately.

Already a different language: different rules of expression, different way of thinking about what you're doing. But informationally equivalent to the binary underneath.

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

