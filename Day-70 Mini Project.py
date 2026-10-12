# # Mini Project - 📊 MULTI-MONTH SALES CONSOLIDATION & BUSINESS ANALYSIS
# # Step 1 — Data Consolidation dd the appropriate Month column to: jan feb mar Then concatenate them. Perform basic data-quality checks: df.shape df.info() df.isna().sum() df.duplicated().sum()
# # Step 2 — Overall KPI Dashboard Calculate: Total Sales Total Profit, Total Orders, Average Order Value, Overall Profit Margin
# # Step 3 — Monthly Performance Dashboard Create a dashboard containing: Month Sales Profit Orders Average Order Value Profit Margin. Then calculate: Monthly Sales Growth % Monthly Profit Growth %
# # Step 4 — Category Performance Create: Categor Sales Profit Orders Average Order Value Profit Margin. Identify: Best category by sales Best category by profit Highest-margin category 
# # Step 5 — Customer Performance Create: Customer Total Sales Total Profit Orders Average Order Value Profit Margin Find: Top 3 customers by revenue Top 3 customers by profit Most frequent customer Highest-margin customer
# # Step 6 — Cross Analysis 🔥 Now answer: Which category performs best in each month? You can use: df.groupby(["Month", "Category"])["Sales"].sum() Then determine the best category for each month. Also determine: Which customer generated the most revenue in each month?
# # Step 7 — Visualizations 📈 Create 5 charts: Monthly Sales Trend → Line chart Monthly Profit Trend → Line chart Sales by Category → Bar chart Sales by Customer — Top 5 → Bar chart Monthly Sales by Category → Grouped bar chart
# # Step 8 — Business Insights 🧠 Write at least 7 data-supported insights. Don't just say: "Sales increased." Instead say something like: "Sales increased from ₹X in January to ₹Y in February, representing a Z% increase." Your insights should cover: Monthly performance Growth Category performance Customer performance Profitability Best/worst performers 
# Any unusual pattern
import pandas as pd
import matplotlib.pyplot as plt
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
jan["Month"] = "January"
feb["Month"] = "February"
mar["Month"] = "March"

df = pd.concat(
    [jan, feb, mar],
    ignore_index=True
)

print(df.shape)
df.info()
print(df.isna().sum())
print(df.duplicated().sum())

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order_ID"].nunique()

average_order_value = df["Sales"].mean()

overall_profit_margin = (
    total_profit / total_sales
) * 100

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
print("Overall Profit Margin:", overall_profit_margin)
monthly = df.groupby("Month").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Order_Value=("Sales", "mean")
)

monthly["Profit_Margin"] = (
    monthly["Profit"] / monthly["Sales"]
) * 100

monthly["Monthly_Sales_Growth_%"] = (
    monthly["Sales"].pct_change() * 100
)

monthly["Monthly_Profit_Growth_%"] = (
    monthly["Profit"].pct_change() * 100
)

print(monthly.round(2))

category = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Order_Value=("Sales", "mean")
)

category["Profit_Margin"] = (
    category["Profit"] / category["Sales"]
) * 100

print(category.round(2))

category["Sales"].idxmax()

category["Profit"].idxmax()

category["Profit_Margin"].idxmax()

customer = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Average_Order_Value=("Sales", "mean")
)

customer["Profit_Margin"] = (
    customer["Total_Profit"] /
    customer["Total_Sales"]
) * 100

print(customer.round(2))

customer.sort_values(
    "Total_Sales",
    ascending=False
).head(3)

customer.sort_values(
    "Total_Profit",
    ascending=False
).head(3)

customer["Orders"].idxmax()

customer["Profit_Margin"].idxmax()

monthly_category = df.groupby(
    ["Month", "Category"]
)["Sales"].sum()

print(monthly_category)

monthly_customer = df.groupby(
    ["Month", "Customer"]
)["Sales"].sum()

print(monthly_customer)
monthly["Sales"].plot(
    kind="line",
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

monthly["Profit"].plot(
    kind="line",
    marker="o",
    title="Monthly Profit Trend"
)

plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()
category["Sales"].plot(
    kind="bar",
    title="Sales by Category"
)

plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

top5 = customer.sort_values(
    "Total_Sales",
    ascending=False
).head(5)

top5["Total_Sales"].plot(
    kind="bar",
    title="Sales by Customer — Top 5"
)

plt.xlabel("Customer")
plt.ylabel("Sales")
plt.show()
monthly_category_pivot = df.pivot_table(
    index="Month",
    columns="Category",
    values="Sales",
    aggfunc="sum"
)

monthly_category_pivot.plot(
    kind="bar",
    figsize=(10, 6),
    title="Monthly Sales by Category"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 1. Strong overall revenue performance

# The business generated ₹10,00,000 in total sales across 12 orders, with an average order value of ₹83,333.33.

# 2. Sales consistently increased

# Sales increased from ₹2,90,000 in January to ₹3,30,000 in February, representing a 13.79% growth.

# Sales then increased further to ₹3,80,000 in March, representing another 15.15% growth.

# 3. Profit grew even faster than sales initially

# Profit increased from ₹60,000 in January to ₹73,000 in February, a 21.67% increase, considerably higher than February's 13.79% sales growth.

# 4. March was the strongest month

# March generated ₹3,80,000 sales and ₹88,000 profit, making it the strongest month in both revenue and absolute profit.

# March also achieved the highest AOV of ₹95,000 and highest monthly profit margin of 23.16%.

# 5. Electronics is the strongest category

# Electronics generated ₹5,00,000, representing 50% of total company sales, and generated ₹1,15,000 profit, making it the most profitable category.

# 6. Clothing is the weakest category

# Clothing generated only ₹1,80,000 sales and ₹35,000 profit. Its 19.44% profit margin was also the lowest among the three categories.

# 7. Electronics had the highest average order value

# Electronics generated an average sale of ₹1,00,000 per order, compared with ₹80,000 for Furniture and ₹60,000 for Clothing.

# 8. Amit is the most valuable customer by revenue

# Amit generated ₹2,85,000 in sales and ₹63,000 profit across 3 orders, making him the top customer by both revenue and absolute profit.

# 9. Neha has the highest customer profitability margin

# Although Neha generated only ₹70,000 revenue, her 22.86% profit margin is the highest among all customers.

# This demonstrates why revenue alone should not be used to evaluate customers.

# 10. Category leadership changed in February

# Electronics dominated January with ₹1,80,000 sales, but Furniture became the leading category in February with ₹1,80,000 sales.

# Electronics regained the lead in March with ₹2,25,000 sales, indicating that category demand can vary significantly by month.
