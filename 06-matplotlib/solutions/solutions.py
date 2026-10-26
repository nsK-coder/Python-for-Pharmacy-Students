# Solutions — Lesson 6 (try the exercises first!)

## Exercise 1: red dashed line

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
here = Path(__file__).parent.parent
df = pd.read_csv(here / "data" / "concentration_time.csv")
plt.figure()
plt.plot(df["time_hours"], df["concentration_mg_L"],
         marker="o", color="red", linestyle="--")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.savefig(here / "curve_red.png")

## Exercise 2: two curves + legend

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
here = Path(__file__).parent.parent
df = pd.read_csv(here / "data" / "concentration_time.csv")
plt.figure()
plt.plot(df["time_hours"], df["concentration_mg_L"],
         marker="o", label="Full dose")
plt.plot(df["time_hours"], df["concentration_mg_L"] / 2,
         marker="s", label="Half dose")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.legend(["Full dose", "Half dose"])
plt.savefig(here / "curve_two_doses.png")

## Exercise 3: AUC by the trapezoidal rule

import numpy as np
import pandas as pd
from pathlib import Path
here = Path(__file__).parent.parent
df = pd.read_csv(here / "data" / "concentration_time.csv")
auc = np.trapz(df["concentration_mg_L"], df["time_hours"])
print("AUC:", round(auc, 2), "mg*h/L")
