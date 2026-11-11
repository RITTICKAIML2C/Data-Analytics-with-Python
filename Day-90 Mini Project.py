# # 🏆 Mini Project — Customer Retention Dashboard. Build a complete retention analysis.
# # Part A — Customer-Level Table Create: Customer, Total_Sales, Total_Profit Order_Count, Average_Order_Value. Repeat_Customer
# # Part B — Retention Analysis. Find: Total unique customers, Number of repeat customers, Repeat customer percentage, Total revenue from repeat customers, Total revenue from one-time customers, Most valuable repeat customer by Sales, Customer with the highest number of orders
# # Part C — Business Insights. Write 5 concise insights. For example: Most customers placed multiple orders during the analysis period, Don't just describe the number—explain what it means for the business.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Order_ID": range(1001, 1013),
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya","Riya",
        "Karan","Amit","Priya","Rahul","Riya","Neha"
    ],
    "Month": [
        "Jan","Jan","Jan","Feb","Feb","Feb",
        "Mar","Mar","Mar","Mar","Apr","Apr"
    ],
    "Sales": [
        50000,40000,35000,60000,55000,45000,
        30000,70000,65000,50000,55000,25000
    ],
    "Profit": [
        10000,8000,7000,12000,11000,9000,
        6000,14000,13000,10000,11000,5000
    ]
})
# ==========================================
# CUSTOMER RETENTION DASHBOARD
# ==========================================

# Part A — Customer-Level Table

customer_table = (
    df.groupby("Customer")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "nunique")
    )
    .reset_index()
)

customer_table["Average_Order_Value"] = (
    customer_table["Total_Sales"] /
    customer_table["Order_Count"]
)

customer_table["Repeat_Customer"] = (
    customer_table["Order_Count"]
    .apply(lambda x: "Repeat" if x > 1 else "One-Time")
)

print("CUSTOMER-LEVEL TABLE")
print(customer_table)


# ==========================================
# Part B — RETENTION ANALYSIS
# ==========================================

total_unique_customers = df["Customer"].nunique()

repeat_customer_count = (
    customer_table["Repeat_Customer"] == "Repeat"
).sum()

repeat_customer_percentage = (
    repeat_customer_count /
    total_unique_customers
) * 100

repeat_revenue = customer_table.loc[
    customer_table["Repeat_Customer"] == "Repeat",
    "Total_Sales"
].sum()

one_time_revenue = customer_table.loc[
    customer_table["Repeat_Customer"] == "One-Time",
    "Total_Sales"
].sum()


# Most valuable repeat customer

repeat_customers = customer_table[
    customer_table["Repeat_Customer"] == "Repeat"
]

most_valuable_repeat_customer = repeat_customers.loc[
    repeat_customers["Total_Sales"].idxmax()
]


# Customer(s) with highest number of orders

max_orders = customer_table["Order_Count"].max()

highest_order_customers = customer_table[
    customer_table["Order_Count"] == max_orders
]


# ==========================================
# FINAL RESULTS
# ==========================================

print("\nRETENTION ANALYSIS")

print("Total Unique Customers:",
      total_unique_customers)

print("Repeat Customer Count:",
      repeat_customer_count)

print(f"Repeat Customer Percentage: "
      f"{repeat_customer_percentage:.2f}%")

print("Repeat Customer Revenue:",
      repeat_revenue)

print("One-Time Customer Revenue:",
      one_time_revenue)

print("\nMost Valuable Repeat Customer:")
print(most_valuable_repeat_customer)

print("\nCustomer(s) with Highest Orders:")
print(highest_order_customers)
