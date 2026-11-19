# # Practice 
# # 🟢 Q1 — Overall KPIs Calculate: Total Sales, Total Profit, Total Orders, Overall Profit Margin %, Average Order Value
# # 🟢 Q2 — Category KPIs Create a category-level table containing: Category, Total_Sales, Total_Profit, Total_Orders, Profit_Margin_%, Average_Order_Value, Sort it by Total_Sales descending.
# # 🟡 Q3 — Category Comparison, Find: Highest-revenue category, Highest-profit category, Highest-profit-margin category, Category with the highest AOV, Category with the lowest AOV
# # 🟡 Q4 — Performance Contribution Calculate each category's: Revenue_% Profit_%. Then calculate: Cumulative Revenue % after sorting categories by revenue.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Category": [
        "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing"
    ],
    "Sales": [
        120000, 90000, 60000,
        150000, 110000, 75000,
        130000, 95000, 85000
    ],
    "Profit": [
        24000, 18000, 15000,
        30000, 16500, 18750,
        26000, 19000, 17000
    ],
    "Orders": [
        12, 9, 8,
        15, 11, 10,
        13, 10, 9
    ]
})
# Q1
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Orders"].sum()

profit_margin = (total_profit / total_sales) * 100
aov = total_sales / total_orders


# Q2
category_kpi = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Orders", "sum")
)

category_kpi["Profit_Margin_%"] = (
    category_kpi["Total_Profit"] / category_kpi["Total_Sales"] * 100
)

category_kpi["Average_Order_Value"] = (
    category_kpi["Total_Sales"] / category_kpi["Total_Orders"]
)

category_kpi = category_kpi.sort_values(
    "Total_Sales", ascending=False
)


# Q3
highest_revenue = category_kpi["Total_Sales"].idxmax()
highest_profit = category_kpi["Total_Profit"].idxmax()
highest_margin = category_kpi["Profit_Margin_%"].idxmax()
highest_aov = category_kpi["Average_Order_Value"].idxmax()
lowest_aov = category_kpi["Average_Order_Value"].idxmin()


# Q4
category_kpi["Revenue_%"] = (
    category_kpi["Total_Sales"] / total_sales * 100
)

category_kpi["Profit_%"] = (
    category_kpi["Total_Profit"] / total_profit * 100
)

category_kpi["Cumulative_Revenue_%"] = (
    category_kpi["Revenue_%"].cumsum()
)
