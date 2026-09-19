# Lectures

Slides and demo notebooks, published after each lecture.

[← back to course home](../README.md) · [exercises →](../exercises/)

## Files

| Session | Slides | Notebook |
|---|---|---|
| 01 — Foundations | [`01-foundations-slides.pdf`](01-foundations-slides.pdf) | [`01-foundations-demo.ipynb`](01-foundations-demo.ipynb) |
| 02 — Data and expressions | _tba_ | _tba_ |
| 03 — Input/output and conditionals | _tba_ | _tba_ |
| 04 — Iteration | _tba_ | _tba_ |
| 05 — Strings | _tba_ | _tba_ |
| 06 — Lists | _tba_ | _tba_ |
| 07 — Dictionaries, tuples, sets | _tba_ | _tba_ |
| 08 — Functions | _tba_ | _tba_ |
| 09 — Modules and files | _tba_ | _tba_ |
| 10 — Recursion | _tba_ | _tba_ |
| 11 — Object-oriented programming | _tba_ | _tba_ |
| 12 — Recap and mock exam | _tba_ | — |

---

## How a session works

Four hours, split into two blocks of two. Each block follows the same rhythm:

| | |
|---|---|
| **Theory** (~30 min) | New concepts. Slides, no typing. |
| **Worked example** (~35 min) | One problem solved end to end, usually in a notebook. |
| **Exercises** (~40 min) | You work, alone or in pairs. |
| **Discussion** (~15 min) | We go through the answers together. |

Bring a laptop from session 02 onwards. Session 01 works without one.

---

## What each session covers

### 01 — Foundations

How a computer represents and processes information, what an algorithm is, and how to write
one that is unambiguous. Then the Python toolchain, `print`, arithmetic, and how to read an
error message.

### 02 — Values, variables, data types and expressions

Literals and identifiers; `int`, `float`, `str` and `bool`; operators and precedence; type
conversion; readable naming. By the end you can predict the value *and* the type of any
expression built from these.

### 03 — Input/output and conditionals

`input()` and `print()`, f-strings and formatting. Then booleans, comparison and logical
operators, and `if` / `elif` / `else`. Your first programs that react to what the user typed.

### 04 — Iteration: `while` and `for` loops

Loop conditions, counters, the accumulator pattern, `break` and `continue`, `range()`,
nested loops. The skill to take away: tracing a loop by hand without running it.

### 05 — Strings

Indexing, slicing, immutability, and the string methods you will use constantly — `split`,
`join`, `replace`, `strip`, `find`. Worked example: text statistics on a paragraph.

### 06 — Lists and nested lists

Creating and modifying lists, list methods, iteration patterns, `enumerate` and `zip`,
aliasing versus copying, nested lists as matrices, and a first sorting algorithm.

### 07 — Dictionaries, tuples and sets

Key–value data, immutability, uniqueness — and how to choose between them. Worked example:
a word-frequency counter built from scratch.

### 08 — Functions

`def`, parameters versus arguments, `return` versus `print`, default and keyword arguments,
scope. Breaking a problem into functions instead of writing one long script.

### 09 — Modules, libraries and file I/O

Splitting a program across files, the import forms, `if __name__ == "__main__"`, a tour of
the standard library. Then reading and writing files, CSV, and a first `try` / `except`.

### 10 — Recursion

Base case and recursive case, the call stack, recursion versus iteration, and divide and
conquer. Worked example: binary search, written both ways.

### 11 — Introduction to object-oriented programming

Classes and objects, `__init__`, attributes, methods, and what `self` actually is. Then
`__str__`, encapsulation, and an honest look at when a class is *not* worth writing.

### 12 — Recap, Q&A and mock exam

A concept map of the whole course, the mistakes that cost the most marks, and open Q&A.
Then a full mock exam under exam conditions, followed by joint correction.

---

## The exam

Written, and shaped exactly like the session 12 mock:

1. **True/false** — statements about concepts.
2. **Multiple choice** — short code fragments: what is the output?
3. **Write a function** — one open question.
4. **Write a program** — one open question.
