---
layout: default
lastmod: 2026-05-29
title: "Schemas and encoding"
description: "Avro's data model — schemas written in JSON, the primitive and complex type system, and the compact binary and JSON encodings the schema drives."
---

[Home](/) > [Positioning](/positioning/) > [Subjects](/positioning/subjects/) > [Apache Avro](/positioning/subjects/a/avro/) > Schemas and encoding

# Schemas and encoding

An Avro schema describes the shape of the data; an encoding turns a value conforming to that schema into bytes. The two are inseparable — without the schema, the bytes cannot be read, because the encoding records no type information of its own.

## Schemas in JSON

Avro schemas are written in [JSON](https://en.wikipedia.org/wiki/JSON). A schema is one of three things: a JSON string naming a type (`"int"`, `"string"`), a JSON object describing a type with attributes (`{"type": "array", "items": "string"}`), or a JSON array, which denotes a union of the listed types. A record schema, the workhorse, is a JSON object naming the record and listing its fields, each with a name and a type:

```json
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "id", "type": "long"},
    {"name": "name", "type": "string"},
    {"name": "email", "type": ["null", "string"], "default": null}
  ]
}
```

A higher-level alternative, [Avro IDL](https://avro.apache.org/docs/) (`.avdl`), offers a C-like declaration syntax for schemas and protocols that compiles down to this JSON form. The JSON representation remains the canonical one.

## The type system

Avro defines eight **primitive types**: `null`, `boolean`, `int` (32-bit signed), `long` (64-bit signed), `float`, `double`, `bytes` (a byte sequence), and `string` (a UTF-8 character sequence).

It defines six **complex types**:

- **record** — a named, ordered collection of fields, each with its own type. The composite at the centre of most schemas.
- **enum** — a named set of symbols.
- **array** — a sequence of items, all of one type.
- **map** — a collection of key–value pairs with string keys and values of one type.
- **union** — a value that may take any one of several listed types, written as a JSON array of those types. Nullable fields are expressed as a union with `null`, as in the `email` field above.
- **fixed** — a named type holding a fixed number of bytes.

Records, enums, and fixed types are *named*: they carry a name (and optional namespace and aliases), which is what later allows a reader and writer to line their schemas up.

## Binary encoding

The binary encoding is compact and carries no type tags — the schema supplies the structure, so the bytes carry only values.

- **Integers** (`int`, `long`) use a variable-length [zig-zag](https://en.wikipedia.org/wiki/Variable-length_quantity) encoding: small-magnitude numbers, positive or negative, take few bytes.
- **`string` and `bytes`** are length-prefixed — a `long` byte count followed by exactly that many bytes.
- **Records** are the concatenation of their field values in declared order, with nothing between them.
- **Arrays and maps** are written as one or more blocks, each a `long` item count followed by the items (for maps, key–value pairs), terminated by a zero-count block.
- **Unions** are written as a `long` branch index — the zero-based position of the chosen type within the union — followed by the value encoded according to that branch.
- **Enums** are written as the integer position of the symbol; **fixed** values as their raw bytes; `boolean` as a single byte; `float` and `double` in fixed-width [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) layout.

The [specification](https://avro.apache.org/docs/) gives the exhaustive byte-level rules.

## JSON encoding

Alongside the binary encoding, Avro defines a JSON encoding, useful for debugging and for human-readable interchange. Most values map to their natural JSON form. The exception worth knowing is the **union**: in binary a union value is a numeric branch index, but in JSON a non-null union value is wrapped in a single-member object whose key is the branch type's name — `{"string": "abc"}` for a string branch — while a `null` branch is written as bare JSON `null`. This makes the chosen branch explicit where JSON has no positional index to carry it.

## Sources

- [Apache Avro specification](https://avro.apache.org/docs/) — the schema declaration and encoding rules in full.
