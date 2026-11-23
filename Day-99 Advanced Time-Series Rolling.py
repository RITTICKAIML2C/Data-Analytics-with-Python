# 1. Concepts 
# A. Rolling Mean
df["Rolling_3M_Avg"] = (
    df["Sales"].rolling(3).mean()
)

# B.Rolling Standard Deviation
df["Rolling_3M_Std"] = (
    df["Sales"].rolling(3).std()
)

# C. Z-Score
df["Z_Score"] = (
    (df["Sales"] - df["Sales"].mean())
    / df["Sales"].std()
)

# D. D. IQR-Based Outlier Detection
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
