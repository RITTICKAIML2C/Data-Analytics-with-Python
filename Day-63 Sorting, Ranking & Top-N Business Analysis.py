# # 1. Sorting Data 
# # A. .sort_values() - sorting arranges your data in ascending or descending order.

# #  Sort Salary from Lowest to Highest
df.sort_values("Salary")

# # Sort Salary from Highest to Lowest 
df.sort_values("Salary", ascending=False)

# # Sorting using multiple columns 
# # 1. Performance from highest to lowest.
# # 2. If two employees have the same performance, experience from highest to lowest.
df.sort_values(["Performance", "Experience"], ascending=[False, False])

# # 2. Ranking - Ranking creates a new numerical ranking column.
df["Salary_Rank"] = df["Salary"].rank(ascending=False, method="dense")

# # dense 
df["Rank"] = df["Salary"].rank(ascending=False, method="dense")

# # 3 Top-N and Bottom-N
# # Top 3 
df.nlargest(3, "Salary")

# # Bottom 3
df.nsmallest(3, "Salary")
# 
