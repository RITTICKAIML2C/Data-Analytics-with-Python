# # 1. Concepts
# # A. Descriptive Statistics
# df.describe()

# # B. Mean vs Median 
# # Mean 
# df["Sales"].mean()

# # Median 
# df["Sales"].median()

# # C. Percentiles 
# df["Sales"].quantile(0.25)
# df["Sales"].quantile(0.50)
# df["Sales"].quantile(0.75)

# # D. Variance 
# df["Sales"].var()

# # E. Standard Deviation
# df["Sales"].std()

# # F. Coefficient of Variation
# cv = (
#     df["Sales"].std() /
#     df["Sales"].mean()
# ) * 100
