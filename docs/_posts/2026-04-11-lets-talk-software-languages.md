---
layout: post
title: "Let's Talk Software Languages"
date: 2026-04-11
labels: [language, engineering, SPLectrum]
blogger_id: 8542284925731887164
---
<img src="https://images.unsplash.com/photo-1625459201773-9b2386f53ca2?q=80&w=350&h=230&auto=format&fit=crop&crop=center" alt="Software code" />

SPLectrum has a very broad view of language. It recognises a wide variety of language categories, although many categories may not feel that close to us. Natural languages and software languages are two categories that we as humans do have a close affinity with. By nature, natural languages can be ambiguous, context-dependent, evolving, full of implication and unspoken meaning. This is a real strength. Software languages on the other hand are not. They are fully explicit. Every rule is written down, all is well-defined by definition. Software languages are languages in the way that Russell always wanted them to be. That is their strength. It also makes them a good category to learn from.

Let's take a look using a simple addition as an example. In the Python language it is written as `x = 3 + 4` — calculate three plus four and assign it to variable x. It's a straightforward instruction. But the computer processor can't read it that way. At the execution level a computer processor only reads binary — a language with an alphabet of two symbols: 0 and 1. Its vocabulary — the instruction set — is preconfigured and fixed. Note that the instruction set depends on the specific processor.

For our example `x = 3 + 4` the translation of the instruction in binary language (for a [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) 8-bit processor) is:

```
10101001 00000011
01101001 00000100
10000101 00010000
```

Three instructions, six bytes. Each instruction is two bytes: an opcode (what to do) and an operand (with what). The result is 7, stored in memory. Binary is not very readable to humans. So the first step is to humanise the binary language and to assign human-readable mnemonics to the instructions — the assembly language. A computer then uses a program — the assembler — to convert the assembly into binary instructions which can then be executed.

```
LDA #$03    ; Load 3 into accumulator
ADC #$04    ; Add 4 to accumulator
STA $10     ; Store result in memory (variable x)
```

A one-to-one mapping with the binary. Same instructions, different notation. Already more readable without having 0s and 1s to decode. Next level up are the higher level programming languages using compilers to transform them all the way down into assembly.

Three languages, one computation. Python, assembly and binary instructions all yielding the same result: 7.

In 1936, [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) proved mathematically that computation is fundamentally about symbols and interaction between symbols. A tape, a read/write head, a set of rules: if you see this symbol, write that symbol, move, change state. Nothing else. No numbers, no logic, no meaning built in. The meaning emerges from the rules. And the minimum is already universal. A simple setup that can compute anything there is to be computed.

Turing also proved there are limits. Some computations never halt — anything circular runs forever. And no general procedure can determine in advance whether an arbitrary program will halt or not. The language is universal but not omnipotent.

If binary already has the full power, why do we need higher languages? Because with full power and control comes complexity of expression. It is not easy to think in such language, to solve problems. Higher languages are there to reduce complexity of expression, to make complex operations simple. `x = 3 + 4` absorbs six bytes of binary instructions into five characters. The complexity hasn't disappeared — it is encapsulated and unpacked by the compiler. This allows the programmer to think and solve problems with simplicity. That's what higher languages do: absorb the complexity into a vocabulary and grammar that lets you think in concepts appropriate for the problems to be solved.

Each language is a different language game. The binary game: every bit matters, nothing is hidden, the raw power, all of it. The assembly game: instructions with names, but still raw power. The Python or any other higher language game: thinking in higher-level concepts, the details encapsulated. The rules of the game set the shape of how to think.

Getting here required evolution. The first binary computers started with only binary language — everything directly written in the most basic instruction set. The first assembler — mnemonics mapper — was 31 instructions long written by hand in binary — [David Wheeler](https://en.wikipedia.org/wiki/David_Wheeler_(computer_scientist)), Cambridge, 1949. Those 31 words, loaded into the machine, were all that was needed to allow the computer to accept programs in a more human-readable form. Next followed higher level languages that used compilers to rewrite the instructions into assembly.

Soon higher level languages were used to rebuild the lower level tools. Evolution in action. The concept of intermediate language (IL) appeared, an assembly-like instruction set that is not processor specific. Higher level languages get compiled to IL, and then from IL to assembly. An ever-growing interrelated ecosystem of languages building a web of complexity.

All languages have this in common: none of them self-founding. It takes one language to spawn another. But wait, what about the beginning? What is the language used to create the first one, the primordial binary instruction set from which all other languages are created? The binary language, the binary instruction set is hardwired into the processor. That is a different language game altogether but it is a language spawning a language. Likewise are we now seeing another emergence taking place: with AI formal languages are spawning natural language. Gone is the formal straitjacket, a computer can now be addressed in natural language, ambiguities included. One can only guess how that will change the landscape, but that is for another time.

Assemblers and compilers aren't unique to software. Language mapping and transformation can equally be found in other places like in our bodies. Every word we speak is mapped to electrical signals, transformed into muscle movements, sound waves. Every sensation we receive — light, pressure, temperature — gets rewritten into nerve impulses and transformed into concepts we can think with. We speak different natural languages, do different language games — but eventually all of it comes from or is transformed into bodily activity. The parallel is structural, not metaphorical. An ecosystem of languages, each suited to its context, each absorbing complexity into its own vocabulary, all eventually becoming or originating from physical action.

The primordial hardwired language brings the raw power of execution. Higher languages bring the power of thought through the clarity and simplicity of its concepts and grammar. As thinking evolves, so do languages. It's only natural.

<small>This post is part of the [language series](/blog/label/language). More in <a href="/language/software-languages">software languages</a> of the reference library.</small>

---
<small>Photo: <a href="https://unsplash.com/@carlgonz">Carl Gonzalez</a> / Unsplash</small>

