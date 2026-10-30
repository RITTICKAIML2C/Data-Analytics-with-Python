# 1. Core Concepts
# a. transform("mean")
df["Avg_Category_Sales"] = (
    df.groupby("Category")["Sales"]
      .transform("mean")
)

# b. Compare individual perofrmance with group average
df["Above_Avg"] = df["Sales"] > df["Avg_Category_Sales"]

# c. Percentage Difference from group average 
df["Sales_vs_Avg_%"] = (
    (df["Sales"] - df["Avg_Category_Sales"])
    / df["Avg_Category_Sales"]
) * 100

