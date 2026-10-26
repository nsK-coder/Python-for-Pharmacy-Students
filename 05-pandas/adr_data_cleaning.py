# Lesson 5: Cleaning ADR data with pandas  [AFTER FOUNDATIONS]
#
# pandas is Python's table library. A DataFrame is just a table:
# rows are reports, columns are fields (drug, event, age, ...).
#   import pandas as pd
#   df = pd.read_csv("data/adr_reports.csv")   <- load a CSV file
#
# Real-world tables are messy, so the three classic cleaning steps are:
#   1. drop_duplicates()  - remove exact duplicate rows
#   2. fillna()           - fill missing values (here: missing age)
#   3. groupby()          - summarise, e.g. reports per drug
#
# Pharmacy task: clean a small invented ADR (adverse drug reaction)
# report table, then answer two pharmacovigilance questions:
#   - How many reports per drug?
#   - How many SERIOUS reports per drug?
#
# NOTE: this dataset is INVENTED for teaching. It is not real
# patient data and must never be treated as real safety data.

import pandas as pd
from pathlib import Path

# Find the data file next to this script, wherever you run it from.
csv_path = Path(__file__).parent / "data" / "adr_reports.csv"
df = pd.read_csv(csv_path)

print("Raw table:", len(df), "rows")
print(df.head())
print()

# Step 1: drop exact duplicate rows (same drug, event, age, outcome...).
before = len(df)
df = df.drop_duplicates()
print("Removed", before - len(df), "duplicate row(s).")

# Step 2: fill the missing age with the median age of the other reports.
# Median is used instead of the mean because one very old or young
# patient would pull the mean around.
median_age = df["age"].median()
df["age"] = df["age"].fillna(median_age)
print("Missing ages filled with median age:", median_age)
print()

# Question 1: how many reports per drug?
print("Reports per drug:")
print(df.groupby("drug").size())
print()

# Question 2: how many SERIOUS reports per drug?
serious = df[df["seriousness"] == "Serious"]
print("Serious reports per drug:")
print(serious.groupby("drug").size())
print()

print("Cleaned table:", len(df), "rows, no missing ages:",
      df["age"].isna().sum() == 0)
