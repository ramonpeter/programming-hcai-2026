# Programming — Human-Centered Artificial Intelligence

**Università degli Studi di Milano — A.Y. 2026/2027**

| | |
|---|---|
| **Course** | Programming (INFO-01/A) |
| **Programme** | Human-Centered Artificial Intelligence (LM-55 R) |
| **Credits** | 6 ECTS — 48 hours (12 sessions × 4 h) |
| **Language** | English |
| **Period** | First semester |
| **Instructor** | [Ramon Winterhalder](https://www.rpwinterhalder.com) |
| **Official page** | [unimi.it course page](https://www.unimi.it/en/education/degree-programme-courses/2027/programming-0) |

---

## All course material is here

Slides, notebooks, exercise sheets and solutions are published in **this repository**.

> **Just started, or still waiting for your enrolment to go through?**
> Nothing to do. Bookmark this page and click **Watch → Custom → Releases** (top right) if you
> want a notification whenever new material appears.

| What | Where |
|---|---|
| Slides (PDF) and live-coding notebooks | [`lectures/`](lectures/) |
| Exercise sheets and solutions | [`exercises/`](exercises/) |
| Session-by-session plan | [`lectures/README.md`](lectures/README.md) |

### Release policy

| Item | Published |
|---|---|
| Slides + demo notebook | right after the lecture |
| Exercise sheet | at the end of the lecture |
| Solutions | after we have discussed them in class |

---

## Course description

The course introduces programming in Python and the solution of computational problems
through algorithms. It covers the main notions of imperative programming — variables,
expressions, control flow, functions, recursion, input/output — and the fundamental
elements of object-oriented programming.

**Prerequisites:** basic computer skills. *No previous programming experience is required.*

By the end of the course you should be able to:

- read a small Python program and predict what it does;
- write a program that automates a simple computational task;
- find the cause of a malfunction and fix it.

---

## Schedule

Each session is 4 hours, organised in two blocks of theory → worked example → exercises.

| # | Session | Topics |
|---|---|---|
| 01 | [Foundations](lectures/README.md#session-01--foundations) | Computers, algorithms, pseudocode, the Python toolchain, first program |
| 02 | [Data and expressions](lectures/README.md#session-02--values-variables-data-types-and-expressions) | Literals, variables, `int` / `float` / `str` / `bool`, operators, conversion |
| 03 | [Input/output and conditionals](lectures/README.md#session-03--inputoutput-and-conditionals) | `input`, `print`, f-strings, booleans, `if` / `elif` / `else` |
| 04 | [Iteration](lectures/README.md#session-04--iteration-while-and-for-loops) | `while`, `for`, `range`, accumulators, nested loops, `break` / `continue` |
| 05 | [Strings](lectures/README.md#session-05--strings) | Indexing, slicing, immutability, string methods, formatting |
| 06 | [Lists](lectures/README.md#session-06--lists-and-nested-lists) | Mutability, list methods, iteration, aliasing, nested lists |
| 07 | [Dictionaries, tuples, sets](lectures/README.md#session-07--dictionaries-tuples-and-sets) | Key–value data, immutability, uniqueness, choosing a structure |
| 08 | [Functions](lectures/README.md#session-08--functions) | `def`, parameters vs arguments, `return`, scope, decomposition |
| 09 | [Modules and files](lectures/README.md#session-09--modules-libraries-and-file-io) | `import`, `__main__`, standard library, reading and writing files |
| 10 | [Recursion](lectures/README.md#session-10--recursion) | Base case, call stack, recursion vs iteration, divide and conquer |
| 11 | [Object-oriented programming](lectures/README.md#session-11--introduction-to-object-oriented-programming) | Classes, objects, `__init__`, attributes, methods |
| 12 | [Recap and mock exam](lectures/README.md#session-12--recap-qa-and-mock-exam) | Review, Q&A, mock exam, joint correction |

---

## Getting set up

You need Python 3.10 or newer and an editor. Any of the following works:

**Option A — the simple one.** Install [Anaconda](https://www.anaconda.com/download).
It bundles Python, Jupyter and the scientific libraries in one installer.

**Option B — the lightweight one.** Install [Python](https://www.python.org/downloads/)
and [VS Code](https://code.visualstudio.com/), then add the Microsoft *Python* and
*Jupyter* extensions.

**Option C — nothing to install.** Open the notebooks directly in
[Google Colab](https://colab.research.google.com/) — paste the notebook URL from this
repository into *File → Open notebook → GitHub*.

Check your installation:

```bash
python --version      # or: python3 --version
python -c "print('ready')"
```

Download this repository either with the green **Code → Download ZIP** button, or — if you
already use git:

```bash
git clone https://github.com/<user>/<repo>.git
cd <repo>
git pull            # run this before each lecture to get the new material
```

---

## Assessment

Written exam. It tests both the understanding of programming concepts and the ability to
apply them. The evaluation considers correctness, understanding of the concepts, clarity of
the algorithmic reasoning, and the ability to write readable, working Python code.

The exam has the same shape as the mock exam in session 12: true/false statements,
multiple choice questions on short code fragments, and two open questions in which you
write a complete Python function or program.

---

## Resources

**Recommended textbook**
R. Sedgewick, K. Wayne, R. Dondero, *Introduction to Programming in Python:
An Interdisciplinary Approach*, Addison-Wesley.

**Free and useful**
- [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official one, well written
- [Python Tutor](https://pythontutor.com/) — visualises code execution step by step, excellent for loops and recursion
- [Real Python](https://realpython.com/) — readable articles on single topics

---

## Questions

Open an [issue](../../issues) if you spot a mistake in the material or have a question that
others would benefit from. For anything personal, write me an email.

---

## License

Course material (slides, exercises, texts): [CC BY-NC-SA 4.0](LICENSE).
Code and notebooks: [MIT](LICENSE).
