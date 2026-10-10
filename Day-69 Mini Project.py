# # 🏢 MINI PROJECT — CUSTOMER & ORDER ANALYTICS
# # Step 1 — Data Integration Create a clean customer-order dataset using a left merge. Use: validate="many_to_one". Check: merged.isna().sum(). Identify unmatched orders.
# # Step 2 — Customer Dashboard For each customer, calculate: Total Sales, Total Profit, Number of Orders, Average Order Value, Profit Margin. Use .groupby().agg(). ⚠️ Exclude unknown customers from the customer dashboard.
# # Step 3 — City Dashboard. For each city, calculate: Total Sales, Total Profit, Number of Orders, Average Order Value, Profit Margin. Again, exclude unknown customers.
# # Step 4 — Customer Ranking. Find: Top 3 customers by Sales, Top 3 customers by Profit, Customer with the most orders, Customer with the highest Profit Margin
# # Step 5 — Customer Feature Engineering. Using .transform(), add: Customer_Total_Sales, Customer_Total_Profit, Customer_Order_Count. Then calculate: Customer_Profit_Margin
# # Step 6 — Data Quality Analysis. Identify: Orders with unknown customers, Customers with no orders, Number of matched orders, Number of unmatched orders, Match rate. Formula: Matched Orders / Total Orders × 100
# # Step 7 — Business Insights. Write at least 5 insights based on your actual output. Think about: Which city generates the most revenue? Which customer is most valuable?, Are high sales always associated with the highest profit margin?, How good is the customer-data match rate?, Are there customers in the database who have never placed an order?
import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Customer": [
        "Amit", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    "City": [
        "Kolkata", "Delhi", "Mumbai",
        "Pune", "Delhi", "Kolkata"
    ]
})

orders = pd.DataFrame({
    "Order_ID": [
        1001, 1002, 1003, 1004,
        1005, 1006, 1007, 1008
    ],
    "Customer_ID": [
        101, 102, 103, 101,
        104, 102, 105, 107
    ],
    "Sales": [
        85000, 60000, 90000, 75000,
        110000, 95000, 55000, 70000
    ],
    "Profit": [
        18000, 12000, 20000, 15000,
        25000, 22000, 10000, 16000
    ]
})
merged = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="left",
    validate="many_to_one"
)
print("Missing Values:")
print(merged.isna().sum())

unmatched_orders = merged[
    merged["Customer"].isna()
]

matched_orders = merged[
    merged["Customer"].notna()
].copy()

customer_dashboard = (
    matched_orders
    .groupby("Customer")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order_ID", "count"),
        Average_Order_Value=("Sales", "mean")
    )
)

customer_dashboard["Profit_Margin"] = (
    customer_dashboard["Total_Profit"]
    / customer_dashboard["Total_Sales"]
    * 100
)

city_dashboard = (
    matched_orders
    .groupby("City")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order_ID", "count"),
        Average_Order_Value=("Sales", "mean")
    )
)

city_dashboard["Profit_Margin"] = (
    city_dashboard["Total_Profit"]
    / city_dashboard["Total_Sales"]
    * 100
)

top_3_sales = (
    customer_dashboard
    .sort_values(
        "Total_Sales",
        ascending=False
    )
    .head(3)
)

top_3_profit = (
    customer_dashboard
    .sort_values(
        "Total_Profit",
        ascending=False
    )
    .head(3)
)

most_orders = customer_dashboard[
    customer_dashboard["Number_of_Orders"]
    == customer_dashboard["Number_of_Orders"].max()
]

highest_margin = customer_dashboard.loc[
    customer_dashboard["Profit_Margin"].idxmax()
]


matched_orders["Customer_Total_Sales"] = (
    matched_orders
    .groupby("Customer")["Sales"]
    .transform("sum")
)

matched_orders["Customer_Total_Profit"] = (
    matched_orders
    .groupby("Customer")["Profit"]
    .transform("sum")
)

matched_orders["Customer_Order_Count"] = (
    matched_orders
    .groupby("Customer")["Order_ID"]
    .transform("count")
)

matched_orders["Customer_Profit_Margin"] = (
    matched_orders["Customer_Total_Profit"]
    / matched_orders["Customer_Total_Sales"]
    * 100
)

matched_order_count = (
    merged["Customer"]
    .notna()
    .sum()
)

unmatched_order_count = (
    merged["Customer"]
    .isna()
    .sum()
)

total_orders = len(merged)

match_rate = (
    matched_order_count
    / total_orders
    * 100
)

customers_with_orders = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="left"
)

customers_no_orders = customers_with_orders[
    customers_with_orders["Order_ID"].isna()
]

print(customer_dashboard)

print(city_dashboard)

print(top_3_sales)

print(top_3_profit)

print(most_orders)

print(highest_margin)

print(unmatched_orders)

print(customers_no_orders)

print("Matched Orders:", matched_order_count)
print("Unmatched Orders:", unmatched_order_count)
print("Match Rate:", match_rate)
