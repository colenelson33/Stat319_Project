import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("UN_clean.csv")

summary_stats = df['infantMortality'].describe()
print(summary_stats)

# Create graph for infant mortality variable

plt.hist(df['infantMortality'], bins=20, edgecolor='black')
plt.title("Distribution of Infant Mortality Rates (per 1,000 live births)")
plt.xlabel("Infant Mortality Rate")
plt.ylabel("Number of Countries")
plt.show()
