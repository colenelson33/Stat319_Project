import pandas as pd

df = pd.read_csv("UN.csv")
print(df.head())
print(df.info())

# This will look for missing values in this column
print(df['infantMortality'].isna().sum())

# This will clear the rows with missing data
df_clean = df.dropna(subset=['infantMortality'])

# Should not be negative values
print(df_clean[df_clean['infantMortality'] < 0])

# Download cleaned version

df_clean.to_csv("UN_clean.csv", index=False)


