import pandas as pd
import numpy as np

df = pd.read_csv("UN_clean.csv")
df["ppgdp_1000"] = df["ppgdp"] / 1000

vars_of_interest = {
    "infantMortality": "Infant mortality",
    "ppgdp_1000": "Per-capita GDP (thousands USD)",
    "lifeExpF": "Female life expectancy",
}


summary_rows = []

for col, label in vars_of_interest.items():
    s = df[col].dropna()  
    
    n = int(s.shape[0])
    mean = s.mean()
    sd = s.std(ddof=1)  
    min_val = s.min()
    q1 = s.quantile(0.25)
    median = s.median()
    q3 = s.quantile(0.75)
    max_val = s.max()
    
    summary_rows.append({
        "Variable": label,
        "n": n,
        "Mean": mean,
        "SD": sd,
        "Min": min_val,
        "Q1": q1,
        "Median": median,
        "Q3": q3,
        "Max": max_val,
    })

summary_df = pd.DataFrame(summary_rows)

summary_df_rounded = summary_df.copy()
summary_df_rounded[["Mean", "SD", "Min", "Q1", "Median", "Q3", "Max"]] = (
    summary_df_rounded[["Mean", "SD", "Min", "Q1", "Median", "Q3", "Max"]].round(2)
)

print("Descriptive statistics for key variables")
print(summary_df_rounded.to_string(index=False))

summary_df_rounded.to_csv("descriptive_stats_table.csv", index=False)