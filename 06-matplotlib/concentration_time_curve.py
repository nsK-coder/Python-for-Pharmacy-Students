# Lesson 6: Concentration–time curves with matplotlib  [AFTER FOUNDATIONS]
#
# matplotlib is Python's plotting library.
#   import matplotlib.pyplot as plt
#   plt.plot(x_values, y_values)   <- draw a line through the points
#   plt.xlabel(...) / plt.ylabel(...)  <- label the axes
#   plt.savefig("curve.png")       <- save the picture to a file
#
# Pharmacy task: plot a concentration–time curve from an invented
# single-dose dataset, and mark its two key pharmacokinetic numbers:
#   Cmax = the highest concentration reached
#   Tmax = the time at which Cmax occurs
#
# NOTE: this dataset is INVENTED for teaching. It is not real
# patient or study data.

import matplotlib
matplotlib.use("Agg")  # draw without opening a window (works everywhere)
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

here = Path(__file__).parent
df = pd.read_csv(here / "data" / "concentration_time.csv")

# Find Cmax and Tmax: the row with the highest concentration.
peak_row = df.loc[df["concentration_mg_L"].idxmax()]
cmax = peak_row["concentration_mg_L"]
tmax = peak_row["time_hours"]

print("Cmax:", cmax, "mg/L")
print("Tmax:", tmax, "hours")

# Plot: time on the x-axis, concentration on the y-axis.
plt.figure()
plt.plot(df["time_hours"], df["concentration_mg_L"], marker="o")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.title("Concentration–time curve (single dose, invented data)")

# Mark the peak with a dot and a label.
plt.plot([tmax], [cmax], marker="o", markersize=10, markerfacecolor="none")
plt.annotate(
    f"Cmax = {cmax} mg/L\nTmax = {tmax} h",
    xy=(tmax, cmax),
    xytext=(tmax + 1.5, cmax + 1),
    arrowprops=dict(arrowstyle="->"),
)

plt.grid(True)
plt.savefig(here / "concentration_time_curve.png")
print("Saved plot to concentration_time_curve.png")
