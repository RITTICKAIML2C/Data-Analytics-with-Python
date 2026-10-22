# # 💼 Mini Project — Customer & Order Dashboard. Merge customers + orders. Check unmatched orders.
# # Calculate: Sales by city, Profit by city, Orders by city, Average Order Value by city
# # Find the best city by sales, Find the most profitable city, Rank customers by total sales, Write 3 business insights.
import pandas as pd 
customers = pd.DataFrame({
    "Customer_ID": [101,102,103,104,105],
    "Customer": ["Amit","Riya","Rahul","Priya","Karan"],
    "City": ["Kolkata","Delhi","Mumbai","Pune","Delhi"]
})

orders = pd.DataFrame({
    "Order_ID": [1001,1002,1003,1004,1005,1006],
    "Customer_ID": [101,102,103,101,104,106],
    "Sales": [85000,60000,90000,75000,110000,70000],
    "Profit": [18000,12000,20000,15000,25000,16000]
})
merged = customers.merge(orders, on="Customer_ID", how="left")
print(merged)

unmatched_orders = orders.merge(customers[["Customer_ID"]], on="Customer_ID", how="left", indicator=True)
unmatched_orders = unmatched_orders[unmatched_orders["_merge"] == "left_only"]
print(unmatched_orders)

sales_by_city = (merged.groupby("City")["Sales"].sum().sort_values(ascending=False))
print(sales_by_city)

profit_by_city = (merged.groupby("City")["Profit"].sum().sort_values(ascending=False))
print(profit_by_city)

orders_by_city = (merged.groupby("City")["Order_ID"].count().sort_values(ascending=False))
print(orders_by_city)

aov_by_city = (merged.groupby("City")["Sales"].mean().sort_values(ascending=False))
print(aov_by_city)

best_city = sales_by_city.idxmax()
best_sales = sales_by_city.max()
print("Best City:", best_city)
print("Total Sales:", best_sales)

most_profitable_city = profit_by_city.idxmax()
highest_profit = profit_by_city.max()
print("Most Profitable City:", most_profitable_city)
print("Total Profit:", highest_profit)

customer_sales = (
    merged.groupby(["Customer_ID", "Customer"])["Sales"]
    .sum()
    .reset_index()
)
customer_sales["Rank"] = (
    customer_sales["Sales"]
    .rank(method="dense", ascending=False)
    .astype(int)
)
customer_sales = customer_sales.sort_values("Rank")
print(customer_sales)

# Insight 1 : Kolkata is the strongest-performing city
# Insight 2 : Pune has the highest Average Order Value at ₹110,000.
# Insight 3 : Amit is the top customer by sales
