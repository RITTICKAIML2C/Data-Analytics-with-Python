# # 1. Dataset
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

# # 2. Concepts
# # a. Customer-lebvel KPIs
customer_kpi = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Orders", "sum")
)

# # b. Customer Profit Margin 
customer_kpi["Profit_Margin_%"] = (
    customer_kpi["Total_Profit"] /
    customer_kpi["Total_Sales"]
) * 100

# # c. Customer Contribution
df["Customer_Total_Sales"] = (
    df.groupby("Customer")["Sales"].transform("sum")
)

# # 4. Customer Segmentation
df["Customer_Type"] = np.select(
    [
        df["Customer_Total_Sales"] >= 200000,
        df["Customer_Total_Sales"] >= 100000
    ],
    ["High Value", "Medium Value"],
    default="Low Value"
)


