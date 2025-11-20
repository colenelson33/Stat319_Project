import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("UN_clean.csv")

y = df["infantMortality"]
X = df["lifeExpF"]

data = pd.concat([y, X], axis=1).dropna()
y_clean = data["infantMortality"]
X_clean = data["lifeExpF"]

X_with_const = sm.add_constant(X_clean)
model = sm.OLS(y_clean, X_with_const).fit()

params = model.params
bse = model.bse
r2 = model.rsquared

intercept = params["const"]
slope = params["lifeExpF"]

print("=== LSRL: infantMortality vs female life expectancy ===")
print(f"const    coef = {intercept:8.4f}, SE = {bse['const']:8.4f}")
print(f"lifeExpF coef = {slope:8.4f}, SE = {bse['lifeExpF']:8.4f}")
print(f"R-squared: {r2:.4f}")

sign = "+" if slope >= 0 else "-"
abs_slope = abs(slope)
print(f"\nLSRL formula:")
print(f"  ŷ = {intercept:.4f} {sign} {abs_slope:.4f} * lifeExpF")