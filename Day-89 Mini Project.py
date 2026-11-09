# # 🏆 Mini Project — Customer Value Dashboard, Build a complete customer analysis 
# # Part A — Customer KPIs Create: Customer : Total_Sales, Total_Profit, Total_Orders, Profit_Margin_%, Sales_Rank, Profit_Rank, Customer_Type
# # Part B — Find Highest-value customer by Sales, Most profitable customer, Customer with highest profit margin, Top 3 customers by Sales, Number of customers in each segment, Best Customer + Category combination by Sales
# # Part C — Business Insights, Write 5 concise insights. Example: Amit generated the highest total sales among all customers
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
# Customer-level KPIs
customer_kpi = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Orders", "sum")
)
# Profit Margin
customer_kpi["Profit_Margin_%"] = (
    customer_kpi["Total_Profit"] /
    customer_kpi["Total_Sales"]
) * 100
# Rankings
customer_kpi["Sales_Rank"] = (
    customer_kpi["Total_Sales"]
    .rank(ascending=False, method="dense")
)
customer_kpi["Profit_Rank"] = (
    customer_kpi["Total_Profit"]
    .rank(ascending=False, method="dense")
)
# Customer segmentation
customer_kpi["Customer_Type"] = np.select(
    [
        customer_kpi["Total_Sales"] >= 200000,
        customer_kpi["Total_Sales"] >= 100000
    ],
    [
        "High Value",
        "Medium Value"
    ],
    default="Low Value"
)
print(customer_kpi)

highest_sales_customer = customer_kpi.loc[
    customer_kpi["Total_Sales"].idxmax()
]
print(highest_sales_customer)

most_profitable_customer = customer_kpi.loc[
    customer_kpi["Total_Profit"].idxmax()
]
print(most_profitable_customer)

highest_margin_customer = customer_kpi.loc[
    customer_kpi["Profit_Margin_%"].idxmax()
]
print(highest_margin_customer)

top_3_customers = customer_kpi.sort_values(
    "Total_Sales",
    ascending=False
).head(3)
print(top_3_customers)

segment_count = customer_kpi["Customer_Type"].value_counts()
print(segment_count)

customer_category = df.groupby(
    ["Customer", "Category"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

best_combination = customer_category.loc[
    customer_category["Total_Sales"].idxmax()
]
print(best_combination)

# 1. Amit generated the highest total sales among all customers, contributing ₹245,000 in sales.

# 2. Amit was also the most profitable customer, generating ₹57,000 in total profit.

# 3. Amit had the highest profit margin at 23.27%, indicating strong profitability relative to his sales.

# 4. Amit and Priya are High Value customers, while Rahul and Riya are Medium Value customers and Karan is a Low Value customer.

# 5. Amit's Electronics purchases formed the highest-sales Customer + Category combination, generating ₹215,000.
