# Lesson 1: Variables, `print()` and `input()`

## The concept in plain words

- A **variable** is a labelled box that holds a value. `weight_kg = 60`
  means: "remember 60 under the name `weight_kg`."
- **`print()`** shows something on the screen.
- **`input()`** asks the person running the program to type something in.
  One catch: `input()` always gives back **text**, even if the person typed
  a number. So `float(input(...))` converts that text into a number you
  can do maths with.

## The pharmacy task

A paracetamol dose calculator. Paracetamol is commonly dosed at **15 mg per
kg of body weight per dose**, capped at a **maximum single dose of 1000 mg**.
The script asks for a weight, works out the dose, and tells you how many
500 mg tablets that is.

## Run it

```bash
python3 dose_calculator.py
```

Type a weight (for example `60`) when it asks, and press Enter.

## Practice exercises

1. Change the dose rule to ibuprofen: 10 mg/kg per dose, maximum 400 mg.
   Run it for a 70 kg patient. What dose do you get?
2. Add a line that also prints the dose in grams (1 g = 1000 mg).
3. Ask for the patient's name too, and print it in the result, for
   example: "Dose for Rahul: 900 mg".

Solutions are in [solutions/](solutions/) — try first, then peek.
