# Solutions — Lesson 4 (try the exercises first!)

## Exercise 1: BMI as a function

def bmi(weight_kg, height_m):
    return weight_kg / (height_m * height_m)

print("BMI:", round(bmi(60, 1.78), 1))
print("BMI:", round(bmi(80, 1.70), 1))

## Exercise 2: tablets needed

def tablets_needed(dose_mg, tablet_mg=500):
    return dose_mg / tablet_mg

print("Tablets:", tablets_needed(900))
print("Tablets:", tablets_needed(400, tablet_mg=200))

## Exercise 3: weights -> dose -> tablets

def calculate_dose(weight_kg, mg_per_kg=15, max_dose_mg=1000):
    return min(weight_kg * mg_per_kg, max_dose_mg)

def tablets_needed(dose_mg, tablet_mg=500):
    return dose_mg / tablet_mg

for weight in [55, 70, 90]:
    dose = calculate_dose(weight)
    print(weight, "kg ->", dose, "mg ->", tablets_needed(dose), "tablets")
