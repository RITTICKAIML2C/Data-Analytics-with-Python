# # Practice 
# # Q1 — KPI Analysis Calculate: Total Sales, Total Profit, Average Sales, Total Orders, Overall Profit Margin %
# # Q2 — Growth Analysis Find: Highest Sales Growth month: Largest Sales decline month, Month with highest Sales
# # Q3 — Rolling Analysis Create: Rolling_3M_Sales Then find the month with the highest 3-month rolling average.
# # Q4 — Ranking Create: Sales_Rank, Profit_Rank. Find the top 3 months by Sales.
# # Q5 — Category Analysis. Use groupby() + agg() to calculate for each category: Total Sales, Total Profit, Average Sales, Average Profit, Total Orders
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Category": ["Electronics","Furniture","Electronics","Furniture",
                 "Electronics","Furniture","Electronics","Furniture"],
    "Sales": [50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit": [10000,12000,11000,14000,15000,16000,14500,18000],
    "Orders": [50,55,52,60,65,70,68,75]
})
total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

average_sales = df["Sales"].mean()

total_orders = df["Orders"].sum()

profit_margin = (total_profit / total_sales) * 100

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", average_sales)
print("Total Orders:", total_orders)
print("Overall Profit Margin %:", profit_margin)
