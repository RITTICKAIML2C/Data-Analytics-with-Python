# # Practice 
# # Q1 Create Sales_Level using np.select(): ≥ ₹100k → High ≥ ₹60k → Medium Otherwise → Low
# # Q2 Create Sales_Band using pd.cut(): 0–50k → Low 50k–100k → Medium, 100k+ → High
# # Q3 Create Profit_Margin.
# # Q4 Create Profit_Per_Sale.
# # Q5 Find the customer with the highest Profit Margin.
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

highest_margin = df.loc[df["Profit_Margin"].idxmax(), "Customer"]

print(highest_margin)
