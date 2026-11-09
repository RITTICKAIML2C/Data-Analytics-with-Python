# # Practice 
# # Q1 — Customer KPI Create a customer-level table containing: Total Sales. Total Profit, Total Orders, Profit Margin %
# # Q2 — Ranking Add: Customer_Sales_Rank, Customer_Profit_Rank, Find the Top 3 customers by Sales.
# # Q3 — Customer Contribution, Using transform():, Customer_Total_Sales, Then calculate: Sales_Contribution_%. Hint: (df["Customer_Total_Sales"] / df["Sales"].sum()) * 100
# # Q4 — Segmentation Create: High Value, Medium Value, Low Value based on customer total sales. Then find how many unique customers belong to each segment.
# # Q5 — Category × Customer Analysis Find total Sales and Profit for every: Customer + Category combination. Hint: df.groupby(["Customer", "Category"]).agg(...)
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Amit","Priya",
                 "Riya","Karan","Priya","Rahul","Amit"],
    "Category": ["Electronics","Furniture","Electronics","Clothing","Furniture",
                 "Electronics","Clothing","Electronics","Furniture","Electronics"],
    "Sales": [120000,75000,90000,30000,85000,
              110000,45000,130000,65000,95000],
    "Profit": [30000,12000,18000,5000,14000,
               25000,8000,32000,10000,22000],
    "Orders": [12,8,9,4,7,11,5,13,6,10]
})
customer_kpi = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Orders", "sum")
)
customer_kpi["Profit_Margin_%"] = (
    customer_kpi["Total_Profit"] /
    customer_kpi["Total_Sales"]
) * 100
print(customer_kpi)

customer_kpi["Customer_Sales_Rank"] = (
    customer_kpi["Total_Sales"]
    .rank(ascending=False, method="dense")
)
customer_kpi["Customer_Profit_Rank"] = (
    customer_kpi["Total_Profit"]
    .rank(ascending=False, method="dense")
)
print(customer_kpi)

top_3_sales = customer_kpi.sort_values(
    "Total_Sales",
    ascending=False
).head(3)
print(top_3_sales)

df["Customer_Total_Sales"] = (
    df.groupby("Customer")["Sales"].transform("sum")
)
df["Sales_Contribution_%"] = (
    df["Customer_Total_Sales"] /
    df["Sales"].sum()
) * 100
print(
    df[[
        "Customer",
        "Sales",
        "Customer_Total_Sales",
        "Sales_Contribution_%"
    ]]
)
df["Sales"].sum()

df["Customer_Type"] = np.select(
    [
        df["Customer_Total_Sales"] >= 200000,
        df["Customer_Total_Sales"] >= 100000
    ],
    [
        "High Value",
        "Medium Value"
    ],
    default="Low Value"
)
customer_segments = (
    df.groupby("Customer_Type")["Customer"]
      .nunique()
)
print(customer_segments)

customer_category = df.groupby(
    ["Customer", "Category"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)
print(customer_category)

df.groupby("Customer")["Sales"].sum()

df.groupby("Customer")["Sales"].transform("sum")
