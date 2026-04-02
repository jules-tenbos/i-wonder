# Let's Talk Software Languages
Labels: engineering, science

<img src="https://images.unsplash.com/photo-1625459201773-9b2386f53ca2?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Software code" style="float:left;margin:0 15px 10px 0;width:50vw;max-width:350px;" />

By nature, natural languages can be ambiguous, context-dependent, evolving, full of implication and unspoken meaning. This is a real strength. Software languages on the other hand are not. They are fully explicit. Every rule is written down, all is well-defined by definition. They are languages in the way that Russell always wanted them to be. That is their strength. It also makes them a good category to learn from.

Let's take the example of a simple addition. Written in Python language it is `x = 3 + 4` — calculate three plus four and assign it to variable x. The instruction is straightforward. But the computer processor can't read it that way. At the execution level computer processors only read binary — a language with an alphabet of two symbols: 0 and 1. Its vocabulary — the instruction set — is preconfigured and fixed. The exact instruction set depends on the specific processor.

For our example `x = 3 + 4` the instruction in binary language for a 6502 8-bit processor is:

```
10101001 00000011
01101001 00000100
10000101 00010000
```

Three instructions, six bytes. Each instruction is two bytes: an opcode (what to do) and an operand (with what). The result is 7, stored in memory. Humans don't easily read this, so to humanise the computer the first step is to translate it into an intermediate language, assembly, which gives human-readable mnemonics to the binary instructions:

```
LDA #$03    ; Load 3 into accumulator
ADC #$04    ; Add 4 to accumulator
STA $10     ; Store result in memory (variable x)
```

A one-to-one mapping with the binary. Same instructions, different notation. Already more readable without having 0s and 1s to decode. Next level up is a compiler that transforms higher-level language instructions — here Python — into assembly.

Three languages, one computation. Python, assembly and binary instructions all yielding the same result: 7.

In 1936, Alan Turing proved — mathematically — that computation is fundamentally about symbols and interaction between symbols. A tape, a read/write head, a set of rules: if you see this symbol, write that symbol, move, change state. Nothing else. No numbers, no logic, no meaning built in. The meaning emerges from the rules. And the minimum is already universal. This simple setup can compute anything there is to be computed.

Turing also proved there are limits. Some computations never halt — anything circular runs forever. And no general procedure can determine in advance whether an arbitrary program will halt or not. The language is universal but not omnipotent.

If binary already has the full power, why do we need higher languages? Because with full power and control comes complexity of expression. It is not easy to think in such language, to solve problems. Higher languages are there to reduce complexity of expression, to make complex operations simple. `x = 3 + 4` absorbs six bytes of binary instructions into five characters. The complexity doesn't disappear — it is encapsulated and unpacked by the compiler. The programmer can think and solve problems with simplicity. That's what higher languages do: they absorb the complexity of the level below into a vocabulary and grammar that lets you think in concepts that match the problem.

Each language is a different language game. The binary game: every bit matters, nothing is hidden. The assembly game: instructions with names, but still step by step. The Python game: think in higher-level concepts, the detail is taken care of. Same computation, different game. The game determines how to play and shapes how you think.

Getting here required evolution. The first binary computers started with only binary language — everything directly written in the most basic instruction set. The first assembler - mnemonics mapper - was 31 instructions long written by hand in binary — David Wheeler, Cambridge, 1949. Those 31 words, loaded into the machine, was all that was needed to allow the computer to accept programs in a more human-readable form. Subsequent programming languages were built on top and soon higher level languages were used to rebuild the lower level tools. Evolution in action. And it all started with those 31 hand-written binary instructions. No language is self-founding — each one needed another language first. Now we have an ecosystem of languages, each with their own strengths and weaknesses, each with their own language game — but eventually all executed as binary code at processor level. AI will change this landscape further — but that's for another time.

Compilation isn't unique to software. Our bodies do the same thing. Every word we speak is translated into electrical signals, muscle movements, sound waves. Every sensation we receive — light, pressure, temperature — is translated into nerve impulses and then into concepts we can think with. We speak different natural languages, do different language games — but eventually all of it is translated into and from bodily activity. The parallel is structural, not metaphorical. A stack of languages, each suited to its context, each absorbing complexity into its own vocabulary, all eventually becoming physical action.

The simplest language already has the full power. What higher languages add is not capacity — it's clarity. A language creates simplicity of thought for the concepts it focuses on. As thinking evolves, so do languages. It's only natural.



---
<small>Photo: <a href="https://unsplash.com/@carlgonz">Carl Gonzalez</a> / Unsplash</small>

