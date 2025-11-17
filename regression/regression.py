import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

# Load cleaned dataset
df = pd.read_csv("UN_regression_clean.csv")

# Define variables
X = df['lifeExpF']
y = df['infantMortality']

# Add constant for intercept
X_with_const = sm.add_constant(X)

# Fit regression model
model = sm.OLS(y, X_with_const).fit()
print(model.summary())

# Predict values for smooth line
x_sorted = np.linspace(X.min(), X.max(), 200)
x_sorted_const = sm.add_constant(x_sorted)
y_predicted = model.predict(x_sorted_const)

# -----------------------------
# BEAUTIFUL APPLE-STYLE FIGURE
# -----------------------------
plt.figure(figsize=(9,6), dpi=150)

# Scatter plot
plt.scatter(
    X, y,
    color="#1A73E8",
    alpha=0.7,
    edgecolors="white",
    linewidth=0.5,
    s=70
)

# Regression line
plt.plot(
    x_sorted, y_predicted,
    color="#D93283",
    linewidth=2.5
)

# Style adjustments
plt.xlabel("Female Life Expectancy (Years)", fontsize=13)
plt.ylabel("Infant Mortality (per 1,000 births)", fontsize=13)
plt.title("Infant Mortality vs. Female Life Expectancy", fontsize=15, weight="bold")

plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()

# Remove top and right borders for clean modern look
for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)

plt.show()
