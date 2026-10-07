# # Practice 
# # Question 1 — Business KPIs Find: Total Sales Total Profit Average Order Value Total Orders Overall Profit Margin 
# # Question 2 — Customer Analysis For every customer, calculate: Total Sales Total Profit, Number of Orders, Average Order Value. Use one .groupby().agg().
# # Question 3 — Customer Ranking Find: Top 3 customers by Total Sales Top 3 customers by Total Profit, Customer with the most orders
# # Question 4 — Customer Feature Engineering Add these columns to the original DataFrame: Customer_Total_Sales Customer_Total_Profit, Customer_Order_Count. Use .transform().
# # Question 5 — Customer Segmentation Create: High Value → Customer_Total_Sales >= 250000, Medium Value → Customer_Total_Sales >= 150000, Low Value → Otherwise. Use np.select().
# # Then find the unique customer and their segment.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Order_ID": range(1001, 1016),

    "Customer": [
        "Amit", "Riya", "Rahul", "Amit", "Priya",
        "Riya", "Karan", "Priya", "Rahul", "Amit",
        "Neha", "Karan", "Priya", "Riya", "Neha"
    ],

    "Category": [
        "Electronics", "Furniture", "Electronics",
        "Clothing", "Furniture", "Electronics",
        "Clothing", "Electronics", "Furniture",
        "Electronics", "Clothing", "Furniture",
        "Electronics", "Clothing", "Furniture"
    ],

    "Sales": [
        120000, 75000, 90000,
        30000, 85000, 110000,
        45000, 130000, 65000,
        95000, 40000, 70000,
        150000, 35000, 80000
    ],

    "Profit": [
        30000, 12000, 18000,
        5000, 14000, 25000,
        8000, 32000, 10000,
        22000, 6000, 11000,
        40000, 4000, 15000
    ]
})
total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

average_order_value = df["Sales"].mean()

total_orders = df["Order_ID"].count()

overall_profit_margin = (
    df["Profit"].sum() / df["Sales"].sum()
) * 100

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Order Value:", average_order_value)
print("Total Orders:", total_orders)
print("Overall Profit Margin:", overall_profit_margin)

customer_analysis = (
    df.groupby("Customer")
      .agg(
          Total_Sales=("Sales", "sum"),
          Total_Profit=("Profit", "sum"),
          Number_of_Orders=("Order_ID", "count"),
          Average_Order_Value=("Sales", "mean")
      )
)

print(customer_analysis)

top_3_sales = (
    customer_analysis
    .sort_values("Total_Sales", ascending=False)
    .head(3)
)

print(top_3_sales)

top_3_profit = (
    customer_analysis
    .sort_values("Total_Profit", ascending=False)
    .head(3)
)

print(top_3_profit)

customer_with_most_orders = customer_analysis[
    "Number_of_Orders"
].idxmax()

print(customer_with_most_orders)

max_orders = customer_analysis["Number_of_Orders"].max()

customers_with_most_orders = customer_analysis[
    customer_analysis["Number_of_Orders"] == max_orders
]

print(customers_with_most_orders)

df["Customer_Total_Sales"] = (
    df.groupby("Customer")["Sales"]
      .transform("sum")
)

df["Customer_Total_Profit"] = (
    df.groupby("Customer")["Profit"]
      .transform("sum")
)

df["Customer_Order_Count"] = (
    df.groupby("Customer")["Order_ID"]
      .transform("count")
)
print(df)

conditions = [
    df["Customer_Total_Sales"] >= 250000,
    df["Customer_Total_Sales"] >= 150000
]

choices = [
    "High Value",
    "Medium Value"
]

df["Customer_Segment"] = np.select(
    conditions,
    choices,
    default="Low Value"
)

customer_segments = (
    df[["Customer", "Customer_Total_Sales", "Customer_Segment"]]
    .drop_duplicates()
    .sort_values("Customer_Total_Sales", ascending=False)
)

print(customer_segments)
