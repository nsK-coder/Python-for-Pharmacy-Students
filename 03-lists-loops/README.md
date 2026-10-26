# Lesson 3: Lists and `for` loops

## The concept in plain words

- A **list** holds several values in one variable, in order:
  `drugs = ["Paracetamol", "Ibuprofen"]`.
- A **`for` loop** repeats a block of code once for each item in the list.
  Inside the loop, the loop variable (here `name`) holds the current item.
- Put an **`if` inside the loop** and you can filter: only do something
  for items that match a condition.

This lesson stores each drug as a pair, `(name, category)` — a simple way
to keep two related facts together before you learn about tables in
Lesson 5.

## The pharmacy task

Work through a small drug list, print every drug with its category, then
filter out just the antibiotics and count them.

## Run it

```bash
python3 drug_list.py
```

## Practice exercises

1. Print only the analgesics instead of the antibiotics.
2. Add three more drugs of your own to the list (any categories) and
   re-run. Does the antibiotic count update by itself? Why?
3. Make a second list containing only drug names (no categories) and
   print each name in UPPERCASE using `.upper()`.

Solutions are in [solutions/](solutions/) — try first, then peek.
