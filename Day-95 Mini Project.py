# # 🏆 3️⃣ Mini Project — Revenue Concentration Dashboard
# # Build a Customer Revenue Concentration Dashboard.
# # Part A — Customer Table Create: Customer, Total_Sales, Total_Profit, Revenue_%, Cumulative_Revenue_%, Profit_%, Cumulative_Profit_%,, Revenue_Rank. Profit_Rank
# # Part B — Pareto Analysis Create: areto_Group Then calculate: Customer count, Total revenue, Revenue percentage, Total profit, Profit percentage
# # Part C — Business Analysis Find: Highest-revenue customer, Highest-profit customer, Top 3 customers by revenue, Top 3 revenue contribution %, Number of customers needed to reach/exceed 80% revenue, Number of customers needed to reach/exceed 80% profit, Average customer revenue
# # Part D — Business Insights Write 5 concise insights.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Customer": [
        "Amit","Riya","Rahul","Priya",
        "Karan","Neha","Vikram","Anu"
    ],
    "Total_Sales": [
        180000,140000,85000,120000,
        30000,25000,95000,65000
    ],
    "Total_Profit": [
        36000,28000,17000,24000,
        6000,5000,19000,13000
    ]
})

total_revenue = df["Total_Sales"].sum()
total_profit = df["Total_Profit"].sum()

df["Revenue_%"] = (
    df["Total_Sales"] / total_revenue * 100
)

df["Profit_%"] = (
    df["Total_Profit"] / total_profit * 100
)

df = df.sort_values(
    "Total_Sales",
    ascending=False
).reset_index(drop=True)

df["Cumulative_Revenue_%"] = (
    df["Revenue_%"].cumsum()
)

profit_sorted = df.sort_values(
    "Total_Profit",
    ascending=False
).copy()

profit_sorted["Cumulative_Profit_%"] = (
    profit_sorted["Profit_%"].cumsum()
)

df = df.drop(columns=["Cumulative_Profit_%"], errors="ignore")

df = df.merge(
    profit_sorted[
        ["Customer", "Cumulative_Profit_%"]
    ],
    on="Customer",
    how="left"
)

df["Revenue_Rank"] = (
    df["Total_Sales"]
    .rank(method="min", ascending=False)
    .astype(int)
)

df["Profit_Rank"] = (
    df["Total_Profit"]
    .rank(method="min", ascending=False)
    .astype(int)
)

customer_table = df[
    [
        "Customer",
        "Total_Sales",
        "Total_Profit",
        "Revenue_%",
        "Cumulative_Revenue_%",
        "Profit_%",
        "Cumulative_Profit_%",
        "Revenue_Rank",
        "Profit_Rank"
    ]
]

print(customer_table)
