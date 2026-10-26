# Python for Pharmacy Students

Learn Python from zero, using pharmacy examples — not generic ones.

This repo is for **pharmacy students with no coding background**. You do not
need to know anything about programming to start. Every lesson teaches **one
concept at a time**, in plain words first, and then shows it working on a
small pharmacy task you already understand: a dose calculation, a BMI check,
an ADR report table, a concentration–time curve.

## Who this is for

- B.Pharm / Pharm.D students who want Python for pharmacovigilance, clinical
  research, data analysis, or drug-discovery work.
- Anyone who tried a general Python tutorial and got lost in examples about
  things they do not care about.

## What you need

- **Python 3** (version 3.10 or newer is fine).
- A computer, or just a browser: every lesson also runs in
  [Google Colab](https://colab.research.google.com) with nothing to install.
  Upload the lesson file to Colab and press Run.

## Learning path (in order)

| # | Lesson | Concept you learn | Pharmacy task |
|---|--------|-------------------|---------------|
| 1 | [01-variables](01-variables/) | Variables, `print()`, `input()` | Dose calculator |
| 2 | [02-conditionals](02-conditionals/) | `if` / `elif` / `else` | BMI calculator with categories |
| 3 | [03-lists-loops](03-lists-loops/) | Lists, `for` loops, filtering | Working through a drug list |
| 4 | [04-functions](04-functions/) | Writing reusable functions | Dose calculator as a function |
| 5 | [05-pandas](05-pandas/) | Reading and cleaning tables with pandas | Cleaning ADR reports |
| 6 | [06-matplotlib](06-matplotlib/) | Plotting with matplotlib | Concentration–time curve (Cmax, Tmax) |

**Do Lessons 1–4 in order.** They are the foundations — everything later
builds on them. Lessons 5 and 6 are marked "after foundations" because they
need the pandas and matplotlib libraries (see below).

## How to run a lesson

From inside a lesson folder, for example:

```bash
cd 01-variables
python3 dose_calculator.py
```

Each lesson folder has its own short README explaining the concept in plain
words, the script (with heavy comments on every step), and 2–3 practice
exercises. Solutions live in the `solutions/` subfolder of each lesson —
try the exercise first, then peek.

## Installing the data libraries (Lessons 5–6 only)

```bash
pip install -r requirements.txt
```

That installs pandas and matplotlib. Lessons 1–4 need nothing but Python.

## A note on the data

All datasets in this repo (`data/adr_reports.csv`,
`data/concentration_time.csv`) are **invented teaching examples**. They are
not real patient data and must never be treated as real clinical data.

## Licence

MIT — see [LICENSE](LICENSE). Free to use, share, and adapt for learning.
