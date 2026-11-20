# # 3️⃣ 🚀 Mini Project — Business Performance Dashboard Dataset
# # Use : Part A — KPI Table. Create a category-level table with: Total Sales, Total Profit, Total Orders, Profit Margin %, AOV, Revenue %, Profit %
# # Part B — Performance Ranking Create: Sales_Rank, Profit_Rank, Margin_Rank, AOV_Rank
# # Part C — Business Analysis Which category has the highest revenue?, Which category has the highest profit?, Which category has the highest profit margin?, Which category has the highest AOV?, What percentage of total revenue comes from the top category?, What percentage of total profit comes from the top category?
# # Part D — 🚨 Identify Business Problems. Find categories that satisfy: High Revenue + Low Profit Margin and explain what this could indicate from a business perspective.
# # Part E — 💼 Analyst Insights. Write 5 concise business insights based on your analysis.Example style:
import numpy as np 
import pandas as pd
df = pd.DataFrame({
    "Category": [
        "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing"
    ],
    "Sales": [
        120000, 90000, 60000,
        150000, 110000, 75000,
        130000, 95000, 85000,
        100000, 125000, 70000
    ],
    "Profit": [
        24000, 18000, 15000,
        30000, 16500, 18750,
        26000, 19000, 17000,
        20000, 22500, 14000
    ],
    "Orders": [
        12, 9, 8,
        15, 11, 10,
        13, 10, 9,
        10, 12, 8
    ]
})
kpi = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Orders", "sum")
)

kpi["Profit_Margin_%"] = (
    kpi["Total_Profit"] / kpi["Total_Sales"] * 100
)

kpi["AOV"] = (
    kpi["Total_Sales"] / kpi["Total_Orders"]
)

total_sales = kpi["Total_Sales"].sum()
total_profit = kpi["Total_Profit"].sum()

kpi["Revenue_%"] = (
    kpi["Total_Sales"] / total_sales * 100
)

kpi["Profit_%"] = (
    kpi["Total_Profit"] / total_profit * 100
)

print(kpi)

kpi["Sales_Rank"] = (
    kpi["Total_Sales"]
    .rank(ascending=False, method="dense")
)

kpi["Profit_Rank"] = (
    kpi["Total_Profit"]
    .rank(ascending=False, method="dense")
)

kpi["Margin_Rank"] = (
    kpi["Profit_Margin_%"]
    .rank(ascending=False, method="dense")
)

kpi["AOV_Rank"] = (
    kpi["AOV"]
    .rank(ascending=False, method="dense")
)

print(kpi)

highest_revenue = kpi["Total_Sales"].idxmax()
highest_profit = kpi["Total_Profit"].idxmax()
highest_margin = kpi["Profit_Margin_%"].idxmax()
highest_aov = kpi["AOV"].idxmax()

top_revenue_percentage = kpi.loc[
    highest_revenue, "Revenue_%"
]

top_profit_percentage = kpi.loc[
    highest_profit, "Profit_%"
]

print("Highest Revenue:", highest_revenue)
print("Highest Profit:", highest_profit)
print("Highest Profit Margin:", highest_margin)
print("Highest AOV:", highest_aov)
print("Top Category Revenue %:", top_revenue_percentage)
print("Top Category Profit %:", top_profit_percentage)

avg_revenue = kpi["Total_Sales"].mean()
avg_margin = kpi["Profit_Margin_%"].mean()

problem_categories = kpi[
    (kpi["Total_Sales"] > avg_revenue) &
    (kpi["Profit_Margin_%"] < avg_margin)
]

print(problem_categories)

# 1. Electronics generates the highest revenue at ₹500,000, contributing 41.32% of total revenue.
# 2. Electronics also generates the highest total profit at ₹100,000, representing 41.54% of total profit.
# 3. Clothing has the highest profit margin at 22.33%, despite generating the lowest revenue among the three categories.
# 4. Clothing has the highest AOV at ₹11,600, suggesting that its average order value is higher than Electronics and Furniture.
# 5. Furniture shows a potential profitability concern because it generates ₹420,000 in revenue but has the lowest profit margin at 18.10%, indicating that its relatively high sales are converting into profit less efficiently.
