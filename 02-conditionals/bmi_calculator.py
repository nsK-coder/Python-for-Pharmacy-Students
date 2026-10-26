# Lesson 2: if / elif / else (conditionals)
#
# A conditional lets the program choose between different actions.
#   if <condition>:       <- do this when the condition is true
#   elif <condition>:     <- otherwise, check this condition
#   else:                 <- otherwise, do this
#
# Pharmacy task: a BMI calculator with categories.
# BMI = weight (kg) / height (m) squared.
# Categories used here (WHO adult cut-offs):
#   under 18.5        -> Underweight
#   18.5 to under 25  -> Normal
#   25 to under 30    -> Overweight
#   30 and above      -> Obese

# Ask for weight and height.
weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in metres (e.g. 1.78): "))

# Calculate BMI.
bmi = weight_kg / (height_m * height_m)

# Decide the category. Python checks from top to bottom and
# runs the FIRST branch whose condition is true, then stops.
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Show the result, rounded to 1 decimal place.
print("BMI:", round(bmi, 1))
print("Category:", category)
