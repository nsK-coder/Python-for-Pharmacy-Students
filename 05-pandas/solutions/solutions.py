# Solutions — Lesson 5 (try the exercises first!)

## Exercise 1: most common adverse event

import pandas as pd
from pathlib import Path
df = pd.read_csv(Path(__file__).parent.parent / "data" / "adr_reports.csv")
print(df["adverse_event"].value_counts().head(1))

## Exercise 2: age groups

import pandas as pd
from pathlib import Path
df = pd.read_csv(Path(__file__).parent.parent / "data" / "adr_reports.csv")
df = df.drop_duplicates()
df["age"] = df["age"].fillna(df["age"].median())
df["age_group"] = ["Young" if age < 40 else "Older" for age in df["age"]]
print(df.groupby("age_group").size())

## Exercise 3: save the cleaned table

import pandas as pd
from pathlib import Path
df = pd.read_csv(Path(__file__).parent.parent / "data" / "adr_reports.csv")
df = df.drop_duplicates()
df["age"] = df["age"].fillna(df["age"].median())
df.to_csv(Path(__file__).parent / "adr_cleaned.csv", index=False)
print("Saved adr_cleaned.csv with", len(df), "rows")
