import pandas as pd

# Load original dataset
df = pd.read_csv("./../UN.csv")

# Check structure
print(df.info())
print(df.head())

# Drop rows missing EITHER infant mortality or life expectancy
df_clean = df.dropna(subset=['infantMortality', 'lifeExpF'])

# Remove any impossible values (negative IMR)
df_clean = df_clean[df_clean['infantMortality'] >= 0]

# Optional: Remove outliers where IMR > 150 or lifeExpF < 30 if they appear
# df_clean = df_clean[(df_clean['infantMortality'] < 150) & (df_clean['lifeExpF'] > 30)]

# Print final structure
print("Remaining rows:", len(df_clean))
print(df_clean.describe())

# Save cleaned version
df_clean.to_csv("UN_regression_clean.csv", index=False)
print("Saved cleaned dataset as UN_regression_clean.csv")
