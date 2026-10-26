# Solutions — Lesson 2 (try the exercises first!)

## Exercise 1: reject zero or negative inputs

weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in metres: "))
if weight_kg <= 0 or height_m <= 0:
    print("Please enter a positive number")
else:
    bmi = weight_kg / (height_m * height_m)
    print("BMI:", round(bmi, 1))

## Exercise 2: "Severely obese" for BMI 40+

# The 40+ check MUST come before the 30+ check, because Python runs the
# FIRST true branch and stops. If "Obese" (bmi >= 30) came first, a BMI
# of 42 would match it and never reach the severe branch.
bmi = float(input("Enter BMI: "))
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
elif bmi < 40:
    category = "Obese"
else:
    category = "Severely obese"
print("Category:", category)

## Exercise 3: BMI category + paracetamol dose together

weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in metres: "))
bmi = weight_kg / (height_m * height_m)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
dose_mg = min(weight_kg * 15, 1000)
print("BMI:", round(bmi, 1), "-", category)
print("Paracetamol dose:", dose_mg, "mg")
