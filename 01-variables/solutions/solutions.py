# Solutions — Lesson 1 (try the exercises first!)

## Exercise 1: ibuprofen dosing (10 mg/kg, max 400 mg)

weight_kg = float(input("Enter patient weight in kg: "))
mg_per_kg = 10
max_dose_mg = 400
dose_mg = min(weight_kg * mg_per_kg, max_dose_mg)
print("Ibuprofen dose:", dose_mg, "mg")
# For 70 kg: 70 * 10 = 700, capped at 400 mg.

## Exercise 2: dose in grams

weight_kg = float(input("Enter patient weight in kg: "))
dose_mg = min(weight_kg * 15, 1000)
dose_g = dose_mg / 1000
print("Dose:", dose_mg, "mg =", dose_g, "g")

## Exercise 3: include the patient's name

name = input("Enter patient name: ")
weight_kg = float(input("Enter patient weight in kg: "))
dose_mg = min(weight_kg * 15, 1000)
print("Dose for", name + ":", dose_mg, "mg")
