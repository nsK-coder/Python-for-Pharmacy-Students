# Lesson 1: Variables, print() and input()
#
# A variable is just a labelled box that holds a value.
#   weight_kg = 60        <- the box is called "weight_kg", it holds 60
# print() shows something on the screen.
# input() asks the person running the program to type something.
#
# Pharmacy task: a paracetamol dose calculator.
# Paracetamol is commonly dosed at 15 mg per kg of body weight per dose,
# with a maximum single dose of 1000 mg.

# Ask the user for the patient's weight.
# input() always gives back TEXT, so float() converts it to a number.
weight_kg = float(input("Enter patient weight in kg: "))

# Store the dosing rule in variables, so the numbers are easy to change.
mg_per_kg = 15        # paracetamol dose per kg of body weight
max_dose_mg = 1000    # maximum single dose, in mg

# Calculate the dose. min() picks the smaller of the two values,
# so the dose never goes above the maximum.
dose_mg = min(weight_kg * mg_per_kg, max_dose_mg)

# A 500 mg tablet is the common tablet strength.
tablet_strength_mg = 500
tablets = dose_mg / tablet_strength_mg

# Show the result.
print("Patient weight:", weight_kg, "kg")
print("Paracetamol dose:", dose_mg, "mg")
print("That is", tablets, "tablet(s) of 500 mg")
