# # Mini Project — Customer Lifetime Value Dashboard
# # Part A — Customer Value Table Create: Customer Total_Sales, Total_Orders, Total_Profit, AOV, Profit_Margin_%, Sales_Rank, Profit_Rank, Segment
# # Part B — Segment KPIs Calculate: Segment Customer_Count, Total_Sales, Average_Sales, Total_Profit, Average_Profit, Average_AOV
# # Part C — Business Analysis Find: Highest revenue customer Highest profit customer, Highest AOV customer, Highest profit-margin customer, Largest customer segment, Highest-revenue segment, Highest-profit segment, Average customer revenue
# # Part D — Business Insights Write 5 concise business insights.
import pandas as pd
import numpy as np 
df = pd.DataFrame({
    "Order_ID": range(1001, 1013),
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya","Riya",
        "Karan","Amit","Priya","Rahul","Riya","Neha"
    ],
    "Category": [
        "Electronics","Furniture","Electronics","Clothing",
        "Furniture","Electronics","Clothing","Electronics",
        "Electronics","Furniture","Clothing","Furniture"
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
customer = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Profit=("Profit", "sum")
).reset_index()

customer["AOV"] = customer["Total_Sales"] / customer["Total_Orders"]

customer["Profit_Margin_%"] = (
    customer["Total_Profit"] / customer["Total_Sales"] * 100
)

customer["Sales_Rank"] = customer["Total_Sales"].rank(
    ascending=False, method="min"
)

customer["Profit_Rank"] = customer["Total_Profit"].rank(
    ascending=False, method="min"
)

conditions = [
    (customer["Total_Sales"] >= 150000) &
    (customer["Total_Profit"] >= 30000),

    (customer["Total_Sales"] >= 80000) |
    (customer["Total_Profit"] >= 15000)
]

customer["Segment"] = np.select(
    conditions,
    ["High Value", "Medium Value"],
    default="Low Value"
)

print("PART A")
print(customer)

segment = customer.groupby("Segment").agg(
    Customer_Count=("Customer", "count"),
    Total_Sales=("Total_Sales", "sum"),
    Average_Sales=("Total_Sales", "mean"),
    Total_Profit=("Total_Profit", "sum"),
    Average_Profit=("Total_Profit", "mean"),
    Average_AOV=("AOV", "mean")
).reset_index()

print("\nPART B")
print(segment)

highest_revenue = customer.loc[customer["Total_Sales"].idxmax()]
highest_profit = customer.loc[customer["Total_Profit"].idxmax()]
highest_aov = customer.loc[customer["AOV"].idxmax()]
highest_margin = customer.loc[customer["Profit_Margin_%"].idxmax()]

largest_segment = segment.loc[segment["Customer_Count"].idxmax()]
highest_revenue_segment = segment.loc[segment["Total_Sales"].idxmax()]
highest_profit_segment = segment.loc[segment["Total_Profit"].idxmax()]

average_customer_revenue = customer["Total_Sales"].mean()

print("\nPART C")
print("1. Highest Revenue Customer:", highest_revenue["Customer"])
print("2. Highest Profit Customer:", highest_profit["Customer"])
print("3. Highest AOV Customer:", highest_aov["Customer"])
print("4. Highest Profit Margin Customer:", highest_margin["Customer"])
print("5. Largest Customer Segment:", largest_segment["Segment"])
print("6. Highest Revenue Segment:", highest_revenue_segment["Segment"])
print("7. Highest Profit Segment:", highest_profit_segment["Segment"])
print("8. Average Customer Revenue:", average_customer_revenue)

# Amit is the highest-value customer, generating ₹180,000 sales and ₹36,000 profit.
# Medium Value is the largest segment, containing 3 of the 6 customers.
# High Value customers generate the highest revenue and profit despite having only 1 customer.
# Amit and Priya have the highest AOV at ₹60,000 per order.
# All customers have a 20% profit margin, indicating consistent profitability across the customer base.
