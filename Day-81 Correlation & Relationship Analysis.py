# 1. Core Concepts
# a. Correlation
df["Sales"].corr(df["Profit"])

Correlation ranges from -1 to +1:
+1 → perfect positive relationship
0 → no linear relationship
-1 → perfect negative relationship

# b. Correlation Matrix
df.corr(numeric_only=True)

# c. Covariance
df["Sales"].cov(df["Profit"])
