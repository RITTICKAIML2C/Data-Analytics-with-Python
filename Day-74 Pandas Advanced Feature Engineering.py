# 1. np.select() - Multiple Conditions 
conditions = [
    df["Sales"] >= 100000,
    df["Sales"] >= 60000
]
choices = ["High", "Medium"]
df["Sales_Level"] = np.select(
    conditions,
    choices,
    default="Low"
)

# 2. pd.cut() - Create Ranges
df["Sales_Band"] = pd.cut(
    df["Sales"],
    bins=[0, 50000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

# 3. Feature Engineering 
df["Profit_Margin"] = df["Profit"] / df["Sales"] * 100
df["Profit_Per_Sale"] = df["Profit"] / df["Sales"]

