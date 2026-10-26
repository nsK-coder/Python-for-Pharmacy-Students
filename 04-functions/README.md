# Lesson 4: Functions

## The concept in plain words

A **function** is a named block of code you can reuse. You define it once
with `def`, it does its job, and it hands a value back with `return`:

```python
def calculate_dose(weight_kg):
    dose = weight_kg * 15
    return dose
```

After that, `calculate_dose(70)` runs the whole block and gives you back
the answer. The point: instead of copying the same calculation ten times,
you write it once and call it ten times — with different inputs.

Default values (like `mg_per_kg=15`) mean callers can skip an argument
and get the sensible default, or pass their own value for another drug.

## The pharmacy task

The Lesson 1 dose calculator, rebuilt as a function, then used for three
patients — plus the same function reused for ibuprofen just by passing
different numbers.

## Run it

```bash
python3 dose_calculator_function.py
```

## Practice exercises

1. Write a function `bmi(weight_kg, height_m)` that returns the BMI, and
   use it for two patients.
2. Write a function `tablets_needed(dose_mg, tablet_mg=500)` that returns
   how many tablets a dose needs.
3. Combine them: for a list of weights, print each weight, its dose, and
   the number of 500 mg tablets.

Solutions are in [solutions/](solutions/) — try first, then peek.
