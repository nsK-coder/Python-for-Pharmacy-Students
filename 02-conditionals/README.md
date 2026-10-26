# Lesson 2: `if` / `elif` / `else` (conditionals)

## The concept in plain words

A **conditional** is a fork in the road: the program checks a condition and
picks one branch.

```python
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
else:
    category = "Obese"
```

Python checks from top to bottom and runs the **first** branch whose
condition is true, then skips the rest. That is why the order matters: once
`bmi < 25` is true, the `else` never runs.

## The pharmacy task

A BMI calculator. BMI = weight (kg) / height (m)². The script works out
the BMI and puts it in a WHO adult category: Underweight (< 18.5), Normal
(18.5–24.9), Overweight (25–29.9), Obese (30+).

## Run it

```bash
python3 bmi_calculator.py
```

## Practice exercises

1. Add a check at the start: if the weight or height is zero or negative,
   print "Please enter a positive number" instead of calculating.
2. Add a new category: BMI of 40 or above prints "Severely obese"
   (it must come before the plain "Obese" branch — why?).
3. Combine Lessons 1 and 2: ask for a weight, print the BMI category
   AND a paracetamol dose for that weight.

Solutions are in [solutions/](solutions/) — try first, then peek.
