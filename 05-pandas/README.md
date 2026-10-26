# Lesson 5: Cleaning ADR data with pandas

> **After foundations** — finish Lessons 1–4 first, then install pandas:
> `pip install -r requirements.txt` (from the repo root).

## The concept in plain words

**pandas** is Python's table library. A **DataFrame** is a table: rows are
individual records, columns are fields.

- `pd.read_csv(...)` loads a CSV file into a DataFrame.
- Real tables are messy, so the three classic cleaning steps are:
  1. **`drop_duplicates()`** — remove exact duplicate rows (the same report
     entered twice).
  2. **`fillna(value)`** — fill missing values. Here a missing age is
     filled with the **median** age, because one extreme age would pull
     the mean around.
  3. **`groupby(...)`** — summarise: count reports per drug, or serious
     reports per drug.

## The pharmacy task

Clean a small **invented** ADR (adverse drug reaction) report table, then
answer two pharmacovigilance questions: reports per drug, and serious
reports per drug. This is the same kind of first step a drug-safety team
does before any signal analysis.

## Run it

```bash
python3 adr_data_cleaning.py
```

## Practice exercises

1. Also print the most common adverse event overall (hint:
   `df["adverse_event"].value_counts()`).
2. Add a column `age_group` that says "Young" if age < 40, else "Older",
   and count reports per age group.
3. Save the cleaned table to a new file `adr_cleaned.csv` (hint:
   `df.to_csv("adr_cleaned.csv", index=False)`).

Solutions are in [solutions/](solutions/) — try first, then peek.

> Reminder: this dataset is invented for teaching. Never treat it as real
> patient or safety data.
