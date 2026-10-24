# 1. IQR Method 
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
]

# 2. Create an Outlier Flag 
df["Outlier"] = (
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
)

# 3. Outlier ≠ bad data 
# An unusually large sale could be a genuine high-value transaction. Don't automatically delete it.

