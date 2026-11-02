# # 💼 Mini Project — Category KPI Dashboard
# # Build a dashboard containing: High_Value flag.
# # Customer_Type, Total Sales by Category, Average Sales by Category, Total Profit by Category, Customer count by Category, High-value customer count by Category.
# # High-value customer percentage by Category.
# # Print 3 business insights.
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Category":["Electronics","Furniture","Electronics","Furniture",
                "Electronics","Furniture","Electronics","Furniture"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
df["High_Value"] = df["Sales"] >= 100000
df["Customer_Type"] = np.where(
    df["Sales"] >= 100000, "High Value",
    np.where(df["Sales"] >= 60000, "Medium Value", "Low Value")
)
kpi = df.groupby("Category").agg({
    "Sales": ["sum", "mean", "count"],
    "Profit": "sum",
    "High_Value": "sum"
})
print(kpi)
kpi["High_Value_Percentage"] = (
    kpi[("High_Value", "sum")] / kpi[("Sales", "count")] * 100
)
print(kpi)

# 1. Electronics has higher total sales
# 2. Electronics has higher average sales
# 3. Electronics has more high-value customers
