# Lesson 3: Lists and for loops
#
# A list holds several values in one variable, in order.
#   drugs = ["Paracetamol", "Amoxicillin", "Ibuprofen"]
# A for loop runs the same block once for EACH item in the list.
#   for drug in drugs:
#       print(drug)
# An if inside the loop lets you filter: only act on items that
# match a condition.
#
# Pharmacy task: work through a small drug list, pick out the
# antibiotics, and count them.

# Each drug is stored as a small pair: (name, category).
# A list of pairs is a simple way to keep related facts together.
drugs = [
    ("Paracetamol", "Analgesic"),
    ("Amoxicillin", "Antibiotic"),
    ("Ibuprofen", "Analgesic"),
    ("Azithromycin", "Antibiotic"),
    ("Omeprazole", "Antacid"),
    ("Ciprofloxacin", "Antibiotic"),
]

print("All drugs in the list:")
for name, category in drugs:
    print("-", name, "(" + category + ")")

# Filter: collect only the antibiotics.
print()
print("Antibiotics only:")
antibiotics = []
for name, category in drugs:
    if category == "Antibiotic":
        antibiotics.append(name)
        print("-", name)

print()
print("Total drugs:", len(drugs))
print("Total antibiotics:", len(antibiotics))
