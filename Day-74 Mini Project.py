# # 💼 Mini Project — Customer Value Segmentation
# # Using the same dataset: Create Sales_Level, Create Sales_Band, Calculate Profit_Margin, Calculate Profit_Per_Sale
# # Rank customers by Sales, Rank customers by Profit, Identify the highest-value customer, Write 3 business insights
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Priya","Karan","Neha"],
    "Sales": [120000,75000,45000,150000,65000,30000],
    "Profit": [30000,12000,9000,40000,10000,5000]
})

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

df["Sales_Band"] = pd.cut(
    df["Sales"],
    bins=[0, 50000, 100000, np.inf],
    labels=["Low", "Medium", "High"]
)

df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

df["Profit_Per_Sale"] = df["Profit"]

df["Sales_Rank"] = df["Sales"].rank(
    ascending=False,
    method="dense"
)

df["Profit_Rank"] = df["Profit"].rank(
    ascending=False,
    method="dense"
)

highest_value = df.loc[df["Sales"].idxmax(), "Customer"]

print(df)
print("Highest-value customer:", highest_value)
