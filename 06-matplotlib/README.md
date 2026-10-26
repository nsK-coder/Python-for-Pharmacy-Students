# Lesson 6: Concentration–time curves with matplotlib

> **After foundations** — finish Lessons 1–4 first, then install
> matplotlib: `pip install -r requirements.txt` (from the repo root).

## The concept in plain words

**matplotlib** is Python's plotting library. The basic recipe is always
the same:

```python
plt.plot(x_values, y_values)   # draw the line
plt.xlabel(...)                # label the x-axis
plt.ylabel(...)                # label the y-axis
plt.savefig("curve.png")       # save the picture
```

## The pharmacy task

Plot a concentration–time curve from a small **invented** single-dose
dataset, and mark its two key pharmacokinetic numbers:

- **Cmax** — the highest concentration reached (here 15.2 mg/L).
- **Tmax** — the time at which Cmax occurs (here 1 hour).

Finding them in code is one line each: take the row with the maximum
concentration, then read off its concentration (Cmax) and its time
(Tmax).

## Run it

```bash
python3 concentration_time_curve.py
```

It prints Cmax and Tmax and saves `concentration_time_curve.png` in this
folder. (The script uses the non-interactive "Agg" backend, so it works
even on machines with no display — including Google Colab, where you can
then download the PNG.)

## Practice exercises

1. Change the curve's colour and line style (for example a red dashed
   line: `plt.plot(..., color="red", linestyle="--")`).
2. Add a second, lower curve of your own invention (for example a
   half-strength dose) and a legend (`plt.legend(["Full dose",
   "Half dose"])`).
3. Estimate the AUC (area under the curve) with the trapezoidal rule
   (hint: `numpy.trapz(df["concentration_mg_L"], df["time_hours"])` —
   you will need `pip install numpy`, or use pandas' own tools).

Solutions are in [solutions/](solutions/) — try first, then peek.

> Reminder: this dataset is invented for teaching. Never treat it as real
> patient or study data.
