# 1. Core Concepts
# a. Global Ranking 
df["Sales_Rank"] = df["Sales"].rank(ascending=False, method="dense")

# b. Rank within each category 
df["Category_Rank"] = (df.groupby("Category")["Sales"].rank(ascending=False, method="dense"))

# c. Top N
top_3 = df.nlargest(3, "Sales")

# d. Top Performer in each group 
top_per_category = df.loc[df.groupby("Category")["Sales"].idxmax()]

