# # Practice 
# # Q1 Create High_Value: Sales ≥ ₹100,000 → True, Otherwise → False
# # Q2 Create Customer_Type: Sales ≥ ₹100,000 → "High Value", Sales ≥ ₹60,000 → "Medium Value", Otherwise → "Low Value"
# # Q3 Count the total number of High Value customers.
# # Q4 Create a category KPI table containing: Total Sales, Average Sales, Customer Count, High Value Customer Count
# # Q5 Find which category has the highest number of High Value customers.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Category":["Electronics","Furniture","Electronics","Furniture",
                "Electronics","Furniture","Electronics","Furniture"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
df["High_Value"] = df["Sales"] >= 100000
print(df[["Customer", "Sales", "High_Value"]])

conditions = [
    df["Sales"] >= 100000,
    df["Sales"] >= 60000
]
choices = [
    "High Value",
    "Medium Value"
]
df["Customer_Type"] = np.select(
    conditions,
    choices,
    default="Low Value"
)
print(df[["Customer", "Sales", "Customer_Type"]])

high_value_count = df["High_Value"].sum()
print(high_value_count)

category_kpi = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Customer_Count=("Customer", "count"),
    High_Value_Customer_Count=("High_Value", "sum")
)
print(category_kpi)

highest_high_value_category = (
    category_kpi["High_Value_Customer_Count"].idxmax()
)
print(highest_high_value_category)

