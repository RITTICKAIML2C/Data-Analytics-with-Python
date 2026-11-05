# 1. Core Concepts
# a. shift()
df["Previous_Sales"] = df["Sales"].shift(1)

# b. Month-over-Month Growth
df["MoM_Growth_%"] = ((df["Sales"] - df["Previous_Sales"]) / df["Previous_Sales"]) * 100
              or 
df["MoM_Growth_%"] = df["Sales"].pct_change() * 100

# c. Previous Profit
df["Previous_Profit"] = df["Profit"].shift(1)

# d. Difference from Previous Month
df["Sales_Change"] = df["Sales"].diff()

df["Sales"].diff()
