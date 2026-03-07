# Programming Languages — Map

## Initial phrases

**Kenneth Iverson** — "Notation as a Tool of Thought" (1979 Turing Award lecture). The notation we use significantly influences the types of problems we can tackle and how effectively we can solve them. Iverson believed the Sapir-Whorf hypothesis applies to programming languages: the language shapes what you can think, not just what you can say. He designed APL on this basis — a notation that enables thinking at a higher level.

**Abelson & Sussman** — Structure and Interpretation of Computer Programs (SICP, MIT). Every powerful language has three mechanisms: primitive expressions, means of combination, and means of abstraction. Programming is not writing instructions for a machine — it is constructing languages. Each layer of abstraction is a new language built on top of the previous one, enabling you to think about and express increasingly complex interactions.

**The abstraction hierarchy** — machine language (binary, pure syntax) → assembly (shorthand for machine instructions) → high-level languages (C, Python — abstractions enabling problem-level thinking) → domain-specific languages (languages built for specific fields). Each step up expands what can be expressed and thought with. Each step down is still there, being related to.

---

## Mapping statement

Programming languages make the principle visible. The abstraction hierarchy is a concrete case of languages built on languages — inter-relational by construction. Machine language is pure syntax: Hilbert's symbols and rules at the most literal level. Each level of abstraction adds a new language on top, expanding the reach — what can be expressed, what can be thought with, what interactions become possible. The lower levels do not disappear; they are related to. A Python program is interpreted through layers down to machine code. The inter-relational is structural and traceable.

Iverson's "Notation as a Tool of Thought" describes for formal languages what Whorf describes for natural languages: the notation shapes the thinking. A programmer working in assembly thinks in registers and memory addresses. The same programmer working in a high-level language thinks in objects, patterns, abstractions. Different language, different reach, different reality available to work with. Change the language, change what you can think. Iverson designed APL on this basis — a notation that enables thinking at a higher level.

Abelson and Sussman's framing — primitive expressions, means of combination, means of abstraction — describes how languages grow. You start with primitives, combine them, then abstract the combinations into new primitives for the next level. This is relational density increasing: each level of abstraction is a richer web of relations, enabling interactions that the level below cannot express directly. Complexity grows through the layering of languages.

The hierarchy also demonstrates equal standing in a specific sense. Machine language is not inferior to Python — it is a different language with a different reach. Python cannot do what machine language does (direct hardware control), and machine language cannot do what Python does (express high-level abstractions concisely). Each stands in its own right. The hierarchy is not a ranking of value but a structure of inter-relation, each level enabling and depending on the others.

From where we stand, this reads as the principle made engineering: relational structure at bare bones (machine language), experience shaped by the language available (Iverson), knowledge growing through shared abstraction (libraries, frameworks, APIs as accumulated shared knowledge), languages inter-relating through the hierarchy, and complexity increasing as languages layer on languages.
