# 1. Core Concepts 
# a. describe
df["Sales"].describe()
# Gives : count, mean, std, min, 25%, 50%(median), 75%, max

# b. Skewness 
df["Sales"].skew()

# c. Coefficient of Variation
cv = (df["Sales"].std()) / df["Sales"].mean()) * 100


