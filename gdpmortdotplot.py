import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("UN_clean.csv")

# Use GDP in thousands (doesn't affect grouping, just consistent with rest of project)
df["ppgdp_1000"] = df["ppgdp"] / 1000

mean_gdp = df["ppgdp_1000"].mean()

below = df[df["ppgdp_1000"] <= mean_gdp].copy()
above = df[df["ppgdp_1000"] > mean_gdp].copy()

# Jitter so dots don't all sit on the same horizontal line
rng = np.random.default_rng(0)  # fixed seed so the plot is reproducible

y_below = rng.uniform(0.05, 0.45, size=len(below))   # top band (below-avg GDP)
y_above = rng.uniform(-0.45, -0.05, size=len(above)) # bottom band (above-avg GDP)

plt.figure(figsize=(9, 4))

plt.scatter(below["infantMortality"], y_below, s=15)
plt.scatter(above["infantMortality"], y_above, s=15)

plt.axhline(0, linewidth=1)  # dividing line between the two bands

plt.xlabel("infantMortality")
plt.ylabel("gdpStrength")

plt.yticks(
    [0.25, -0.25],
    ["Below-average GDP", "Above-average GDP"]
)

plt.title("Infant Mortality by Strength of Country's GDP")
plt.tight_layout()
plt.savefig("dotplot_infantMortality_by_gdpStrength.png", dpi=300)
plt.show()