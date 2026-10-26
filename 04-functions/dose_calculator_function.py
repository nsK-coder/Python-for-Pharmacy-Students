# Lesson 4: Functions
#
# A function is a named block of code you can reuse.
#   def calculate_dose(weight_kg):
#       ...do the maths...
#       return dose_mg
# "def" defines it, "return" hands a value back to whoever called it.
# Once defined, you can call it as many times as you like with
# different inputs, instead of copying the same code over and over.
#
# Pharmacy task: the Lesson 1 dose calculator, rebuilt as a
# reusable function, then used for several patients.

def calculate_dose(weight_kg, mg_per_kg=15, max_dose_mg=1000):
    """Return a single oral dose in mg for a given body weight.

    Default rule is paracetamol: 15 mg/kg, capped at 1000 mg.
    Pass different mg_per_kg / max_dose_mg values for other drugs.
    """
    dose_mg = weight_kg * mg_per_kg
    if dose_mg > max_dose_mg:
        dose_mg = max_dose_mg
    return dose_mg


# Use the function for three patients (weights in kg).
patients = [55, 70, 90]
for weight in patients:
    dose = calculate_dose(weight)
    print("Weight", weight, "kg -> paracetamol dose", dose, "mg")

# Reuse the SAME function for a different drug: ibuprofen,
# 10 mg/kg per dose, maximum 400 mg.
print()
print("Ibuprofen for 70 kg:", calculate_dose(70, mg_per_kg=10, max_dose_mg=400), "mg")
