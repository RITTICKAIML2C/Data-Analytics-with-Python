# # Practice 
# # Q1 — Concatenate All Months Combine: January + February + March into one DataFrame. Requirements: Use pd.concat() Use ignore_index=True, Check the final number of rows, Check the final number of columns
# # Q2 — Add Month Information Before concatenating, add: Month = January Month = February, Month = March Then combine them. Verify the number of orders per month.
# # Q3 — Business Analysis Using the combined dataset, calculate: Total Sales Total Profit, Total Orders, Average Order Value, Overall Profit Margin
# # Q4 — Monthly Analysis Calculate: Sales by Month, Profit by Month, Orders by Month, Average Order Value by Month, Profit Margin by Month. Use: groupby().agg()
# # Q5 — Category Analysis. Calculate: Sales by Category, Profit by Category, Orders by Category, Average Sales by Category, Profit Margin by Category. Then find: Highest-sales category, Most profitable category
# # Q6 — Customer Analysis. Calculate: Total Sales by Customer Total Profit by Customer, Number of Orders by Customer, Average Order Value by Customer. Then find : Top 3 customers by Sales Top 3 customers by Profit Customer with the most orders
import pandas as pd

jan = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer": ["Amit", "Riya", "Rahul", "Priya"],
    "Category": ["Electronics", "Furniture", "Clothing", "Electronics"],
    "Sales": [85000, 65000, 45000, 95000],
    "Profit": [18000, 12000, 9000, 21000]
})

feb = pd.DataFrame({
    "Order_ID": [1005, 1006, 1007, 1008],
    "Customer": ["Karan", "Riya", "Amit", "Neha"],
    "Category": ["Furniture", "Electronics", "Clothing", "Furniture"],
    "Sales": [110000, 95000, 55000, 70000],
    "Profit": [25000, 22000, 10000, 16000]
})

mar = pd.DataFrame({
    "Order_ID": [1009, 1010, 1011, 1012],
    "Customer": ["Rahul", "Priya", "Karan", "Amit"],
    "Category": ["Furniture", "Electronics", "Clothing", "Electronics"],
    "Sales": [75000, 120000, 80000, 105000],
    "Profit": [15000, 28000, 16000, 24000]
})
combined = pd.concat([jan, feb, mar], ignore_index=True)
print(combined)
print("Rows:", combined.shape[0])
print("Columns:", combined.shape[1])

jan["Month"] = "January"
feb["Month"] = "February"
mar["Month"] = "March"
combined = pd.concat([jan, feb, mar], ignore_index=True)
print(combined)
print(combined["Month"].value_counts())

total_sales = combined["Sales"].sum()
print(total_sales)

total_profit = combined["Profit"].sum()
print(total_profit)

total_orders = combined["Order_ID"].nunique()
print(total_orders)

average_order_value = combined["Sales"].mean()
print(average_order_value)

profit_margin = (total_profit / total_sales) * 100
print(profit_margin)

monthly_analysis = combined.groupby("Month").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Order_Value=("Sales", "mean")
)
monthly_analysis["Profit_Margin"] = (
    monthly_analysis["Profit"] / monthly_analysis["Sales"]
) * 100
print(monthly_analysis)

category_analysis = combined.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Sales=("Sales", "mean")
)
category_analysis["Profit_Margin"] = (
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100
print(category_analysis)

highest_sales_category = category_analysis["Sales"].idxmax()
print(highest_sales_category)

most_profitable_category = category_analysis["Profit"].idxmax()
print(most_profitable_category)

customer_analysis = combined.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Order_Value=("Sales", "mean")
)
print(customer_analysis)

top_3_sales = customer_analysis.sort_values(
    "Total_Sales",
    ascending=False
).head(3)
print(top_3_sales)

top_3_profit = customer_analysis.sort_values(
    "Total_Profit",
    ascending=False
).head(3)
print(top_3_profit)

most_orders_customer = customer_analysis["Orders"].idxmax()
print(most_orders_customer)
