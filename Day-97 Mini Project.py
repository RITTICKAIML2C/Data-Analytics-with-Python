# # 🚀 Mini Project — Monthly Sales Performance Dashboard
# # Part A — Monthly KPI Table. Create: Month, Total_Sales, Total_Profit, Profit_Margin_%, MoM_Growth_%, Cumulative_Sales, Cumulative_Profit, Rolling_3M_Sales, Rolling_3M_Profit
# # Part B — Monthly Rankings. Create: Sales_Rank, Profit_Rank, Growth_Rank. Then identify the top 3 months by sales.
# # Part C — Category × Month Analysis. Use: groupby(["Month", "Category"]). Calculate: Total Sales, Total Profit, Profit Margin %. Then determine which category performed best in each month.
# # Part D — Business Analysis. Find: Highest-sales month, Highest-profit month, Highest-growth month, Highest rolling-3-month sales month, Highest rolling-3-month profit month, Highest-performing category overall, Total sales generated during the period, Overall profit margin, January → August sales growth %
# # Part E — 📈 Business Insights. Write 5 meaningful insights.
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-05","2026-01-20",
        "2026-02-05","2026-02-18",
        "2026-03-08","2026-03-22",
        "2026-04-04","2026-04-19",
        "2026-05-07","2026-05-21",
        "2026-06-05","2026-06-20",
        "2026-07-08","2026-07-23",
        "2026-08-05","2026-08-20"
    ],
    "Category": [
        "Electronics","Furniture",
        "Electronics","Clothing",
        "Furniture","Electronics",
        "Clothing","Electronics",
        "Furniture","Electronics",
        "Clothing","Furniture",
        "Electronics","Clothing",
        "Furniture","Electronics"
    ],
    "Sales": [
        45000,55000,
        50000,60000,
        58000,65000,
        62000,70000,
        68000,78000,
        75000,85000,
        80000,90000,
        88000,100000
    ],
    "Profit": [
        9000,11000,
        10000,12000,
        11600,13000,
        12400,14000,
        13600,15600,
        15000,17000,
        16000,18000,
        17600,20000
    ]
})
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly = df.groupby("Month").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

monthly["Profit_Margin_%"] = (
    monthly["Total_Profit"] /
    monthly["Total_Sales"] * 100
)

monthly["MoM_Growth_%"] = (
    monthly["Total_Sales"].pct_change() * 100
)

monthly["Cumulative_Sales"] = (
    monthly["Total_Sales"].cumsum()
)

monthly["Cumulative_Profit"] = (
    monthly["Total_Profit"].cumsum()
)

monthly["Rolling_3M_Sales"] = (
    monthly["Total_Sales"].rolling(3).mean()
)

monthly["Rolling_3M_Profit"] = (
    monthly["Total_Profit"].rolling(3).mean()
)
monthly["Month"] = pd.to_datetime(
    monthly["Month"],
    format="%m"
).dt.month_name()

monthly["Sales_Rank"] = (
    monthly["Total_Sales"]
    .rank(ascending=False, method="dense")
)

monthly["Profit_Rank"] = (
    monthly["Total_Profit"]
    .rank(ascending=False, method="dense")
)

monthly["Growth_Rank"] = (
    monthly["MoM_Growth_%"]
    .rank(ascending=False, method="dense")
)

top_3_sales = monthly.nlargest(3, "Total_Sales")

df["Month"] = df["Date"].dt.month_name()

category_monthly = df.groupby(
    ["Month", "Category"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

category_monthly["Profit_Margin_%"] = (
    category_monthly["Total_Profit"] /
    category_monthly["Total_Sales"] * 100
)

best_category_each_month = (
    category_monthly
    .loc[
        category_monthly.groupby("Month")["Total_Sales"].idxmax()
    ]
)

highest_sales_month = monthly.loc[monthly["Total_Sales"].idxmax()]

highest_profit_month = monthly.loc[monthly["Total_Profit"].idxmax()]

highest_growth_month = monthly.loc[monthly["MoM_Growth_%"].idxmax()]

highest_rolling_sales_month = monthly.loc[monthly["Rolling_3M_Sales"].idxmax()]

highest_rolling_profit_month = monthly.loc[monthly["Rolling_3M_Profit"].idxmax()]

category_overall = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

highest_performing_category = category_overall.loc[
    category_overall["Total_Sales"].idxmax()
]

total_sales = df["Sales"].sum()

overall_profit_margin = (
    df["Profit"].sum() /
    df["Sales"].sum() * 100
)

jan_sales = monthly.loc[
    monthly["Month"] == "January",
    "Total_Sales"
].iloc[0]

aug_sales = monthly.loc[
    monthly["Month"] == "August",
    "Total_Sales"
].iloc[0]

jan_aug_growth = (
    (aug_sales - jan_sales) /
    jan_sales * 100
)
print(monthly)
print(top_3_sales)
print(category_monthly)
print(best_category_each_month)
print("Highest Sales Month:",highest_sales_month["Month"])
print("Highest Profit Month:",highest_profit_month["Month"])
print("Highest Growth Month:",highest_growth_month["Month"])
print("Highest Rolling Sales Month:",highest_rolling_sales_month["Month"])
print("Highest Rolling Profit Month:",highest_rolling_profit_month["Month"])
print("Highest Performing Category:",highest_performing_category["Category"])
print("Total Sales:", total_sales)
print("Overall Profit Margin:",overall_profit_margin, "%")
print("January → August Growth:",jan_aug_growth, "%")
