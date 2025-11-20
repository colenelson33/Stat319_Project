import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("UN_clean.csv")

df["ppgdp_1000"] = df["ppgdp"] / 1000

ppgdp_1000 = df["ppgdp_1000"].dropna()
lifeF = df["lifeExpF"].dropna()

plt.figure()
plt.hist(ppgdp_1000, bins=20, edgecolor="black")
plt.xlabel("Per-capita GDP (thousands USD)")
plt.ylabel("Count of countries")
plt.title("Histogram of Per-capita GDP (thousands USD)")
plt.tight_layout()
plt.savefig("hist_ppgdp_1000.png", dpi=300)
plt.show()

plt.figure()
plt.hist(lifeF, bins=20, edgecolor="black")
plt.xlabel("Female life expectancy (years)")
plt.ylabel("Count of countries")
plt.title("Histogram of Female Life Expectancy")
plt.tight_layout()
plt.savefig("hist_lifeExpF.png", dpi=300)
plt.show()

plt.figure()
plt.boxplot(ppgdp_1000, vert=False)
plt.xlabel("Per-capita GDP (thousands USD)")
plt.title("Boxplot of Per-capita GDP (thousands USD)")
ax = plt.gca()
ax.set_yticks([])
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("box_ppgdp_1000_horizontal.png", dpi=300)
plt.show()

plt.figure()
plt.boxplot(lifeF, vert=False)
plt.xlabel("Female life expectancy (years)")
plt.title("Boxplot of Female Life Expectancy")
ax = plt.gca()
ax.set_yticks([])
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("box_lifeExpF_horizontal.png", dpi=300)
plt.show()

data = df[["ppgdp_1000", "lifeExpF"]].dropna()
x = data["ppgdp_1000"].values
y = data["lifeExpF"].values

slope, intercept = np.polyfit(x, y, 1)

plt.figure()
plt.scatter(x, y, alpha=0.7)
plt.xlabel("Per-capita GDP (thousands USD)")
plt.ylabel("Female life expectancy (years)")
plt.title("Female Life Expectancy vs Per-capita GDP (thousands USD)")

x_line = np.linspace(x.min(), x.max(), 200)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, linewidth=2)

plt.tight_layout()
plt.savefig("scatter_lifeExpF_vs_ppgdp_1000_LSRL.png", dpi=300)
plt.show()