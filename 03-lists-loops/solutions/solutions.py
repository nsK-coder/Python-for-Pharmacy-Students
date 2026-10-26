# Solutions — Lesson 3 (try the exercises first!)

## Exercise 1: analgesics only

drugs = [
    ("Paracetamol", "Analgesic"),
    ("Amoxicillin", "Antibiotic"),
    ("Ibuprofen", "Analgesic"),
    ("Azithromycin", "Antibiotic"),
    ("Omeprazole", "Antacid"),
    ("Ciprofloxacin", "Antibiotic"),
]
for name, category in drugs:
    if category == "Analgesic":
        print("-", name)

## Exercise 2: adding drugs

# Just add pairs to the list, e.g.:
#     ("Metformin", "Antidiabetic"),
#     ("Doxycycline", "Antibiotic"),
# Yes, the count updates by itself: the loop reads whatever is in the
# list at run time, and len(antibiotics) counts what was collected.
# You never hard-coded the number 3 anywhere.

## Exercise 3: names in UPPERCASE

names = ["Paracetamol", "Amoxicillin", "Ibuprofen"]
for name in names:
    print(name.upper())
