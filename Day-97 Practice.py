# # Practice
# # Q1 — Date Preparation. Create: Date, Year, Month, Month_Name. Then sort the data by date.
# # Q2 — Monthly Performance. Create a monthly table containing: Total Sales, Total Profit, Total Orders/Transactions. Then calculate: Profit Margin %, Average Sales per Transaction
# # Q3 — Growth Analysis. Create: Previous_Month_Sales, Sales_Change, MoM_Growth_%. Then find: Highest-growth month, Largest sales increase, Largest sales decrease
# # Q4 — Trend Analysis. Create: Cumulative_Sales, Cumulative_Profit, Rolling_3M_Sales, Rolling_3M_Profit. Then find: Month with highest rolling sales average, Month with highest rolling profit average
# # Q5 — Business Performance. Find: Highest-sales month Lowest-sales month, Highest-profit month, Lowest-profit month, Overall sales growth from January to June
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Date": [
        "2026-01-05", "2026-01-18",
        "2026-02-07", "2026-02-20",
        "2026-03-10", "2026-03-25",
        "2026-04-08", "2026-04-22",
        "2026-05-05", "2026-05-19",
        "2026-06-10", "2026-06-24"
    ],
    "Sales": [
        45000, 55000,
        50000, 60000,
        58000, 65000,
        62000, 70000,
        68000, 78000,
        75000, 85000
    ],
    "Profit": [
        9000, 11000,
        10000, 12000,
        11600, 13000,
        12400, 14000,
        13600, 15600,
        15000, 17000
    ]
})

# Q1 — Date Preparation
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()

df = df.sort_values("Date").reset_index(drop=True)


# Q2 — Monthly Performance
monthly = df.groupby(
    ["Year", "Month", "Month_Name"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Transactions=("Sales", "count")
).reset_index()

monthly["Profit_Margin_%"] = (
    monthly["Total_Profit"] /
    monthly["Total_Sales"] * 100
)

monthly["Average_Sales_per_Transaction"] = (
    monthly["Total_Sales"] /
    monthly["Total_Transactions"]
)


# Q3 — Growth Analysis
monthly["Previous_Month_Sales"] = (
    monthly["Total_Sales"].shift(1)
)

monthly["Sales_Change"] = (
    monthly["Total_Sales"] -
    monthly["Previous_Month_Sales"]
)

monthly["MoM_Growth_%"] = (
    monthly["Sales_Change"] /
    monthly["Previous_Month_Sales"] * 100
)


# Q4 — Trend Analysis
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


# Q5 — Business Performance
highest_sales_month = monthly.loc[
    monthly["Total_Sales"].idxmax(),
    "Month_Name"
]

lowest_sales_month = monthly.loc[
    monthly["Total_Sales"].idxmin(),
    "Month_Name"
]

highest_profit_month = monthly.loc[
    monthly["Total_Profit"].idxmax(),
    "Month_Name"
]

lowest_profit_month = monthly.loc[
    monthly["Total_Profit"].idxmin(),
    "Month_Name"
]

overall_sales_growth = (
    (monthly["Total_Sales"].iloc[-1] -
     monthly["Total_Sales"].iloc[0])
    / monthly["Total_Sales"].iloc[0] * 100
)


print(monthly)

print("\nBusiness Performance")
print("Highest Sales Month:", highest_sales_month)
print("Lowest Sales Month:", lowest_sales_month)
print("Highest Profit Month:", highest_profit_month)
print("Lowest Profit Month:", lowest_profit_month)
print("Overall Sales Growth:", overall_sales_growth, "%")
