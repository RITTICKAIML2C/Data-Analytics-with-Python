# 1. map() - value by value 
df["Category"] = df["Category"].map({
    "Electronics": "Tech",
    "Furniture": "Home"
})

# 2. apply() - custom logic 
df["Sales_Level"] = df["Sales"].apply(
    lambda x: "High" if x >= 100000 else "Low"
)

# 3. transform() - group calculatio while keeping rows
df["Customer_Total"] = df.groupby("Customer")["Sales"].transform("sum")

