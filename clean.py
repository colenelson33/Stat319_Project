import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("UN.csv")
print(df.head())
print(df.info())

# This will look for missing values in this column
print(df['infantMortality'].isna().sum())

# This will clear the rows with missing data
df_clean = df.dropna(subset=['infantMortality'])

# Should not be negative values
print(df_clean[df_clean['infantMortality'] < 0])

summary_stats = df_clean['infantMortality'].describe()
print(summary_stats)

plt.hist(df_clean['infantMortality'], bins=20, edgecolor='black')
plt.title("Distribution of Infant Mortality Rates (per 1,000 live births)")
plt.xlabel("Infant Mortality Rate")
plt.ylabel("Number of Countries")
plt.show()

