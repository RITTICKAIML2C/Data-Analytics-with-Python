# # Q1 — Rolling Analysis. Calculate: 3-month rolling average 3-month rolling standard deviation, Then identify the month with the highest rolling average.
# # Q2 — Z-Score Analysis Calculate: Z_Score Then identify: Highest Z-score month, Lowest Z-score month, Any months with abs(Z_Score) > 2
# # Q3 — IQR Outlier Detection. Calculate: Q1, Q3, IQR, Lower Bound, Upper Bound Then identify the outlier months.
# # Q4 — Business Interpretation . The dataset contains one unusually high sales value. Determine: Which month is unusual?, Why shouldn't we immediately assume it's an error?, What business events could explain it?, How could this affect a forecasting model?
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],
    "Sales": [
        100000,105000,110000,108000,
        115000,120000,118000,125000,
        130000,128000,180000,135000
    ]
})
df["Rolling_Avg_3M"] = df["Sales"].rolling(3).mean()

df["Rolling_Std_3M"] = df["Sales"].rolling(3).std()

highest_rolling_avg = df.loc[
    df["Rolling_Avg_3M"].idxmax()
]

print("Highest Rolling Average:")
print(highest_rolling_avg)
mean_sales = df["Sales"].mean()

std_sales = df["Sales"].std(ddof=0)

df["Z_Score"] = (
    (df["Sales"] - mean_sales)
    / std_sales
)

highest_z = df.loc[df["Z_Score"].idxmax()]

lowest_z = df.loc[df["Z_Score"].idxmin()]

z_outliers = df[
    np.abs(df["Z_Score"]) > 2
]

print("\nHighest Z-Score:")
print(highest_z)

print("\nLowest Z-Score:")
print(lowest_z)

print("\nZ-Score Outliers:")
print(z_outliers)

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

iqr_outliers = df[
    (df["Sales"] < lower_bound) |
    (df["Sales"] > upper_bound)
]

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nIQR Outliers:")
print(iqr_outliers)

print(df)
