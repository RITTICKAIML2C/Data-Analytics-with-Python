# # Practice 
# # Q1 — Date Conversion, Convert Order_Date into datetime. Create: Year, Month, Month_Name, Day_Name
# # Q2 — Monthly Sales. Calculate: Total Sales by Month. using groupby() + to_period("M").
# # Q3 — Monthly Profit. Calculate: Total Profit by Month
# # Q4 — Monthly Growth. Calculate monthly sales growth percentage using: pct_change()
# # Q5 — Business Analysis. Find: Highest-sales month, Lowest-sales month, Highest-profit month, Average monthly sales, Total sales, Total profit
# # Q6 — Day Analysis. Find: Number of orders by weekday.
import pandas as pd

df = pd.DataFrame({
    "Order_ID": range(1001, 1017),

    "Order_Date": [
        "2026-01-05", "2026-01-12", "2026-01-20", "2026-02-03",
        "2026-02-14", "2026-02-25", "2026-03-02", "2026-03-18",
        "2026-03-27", "2026-04-05", "2026-04-17", "2026-04-28",
        "2026-05-06", "2026-05-19", "2026-06-08", "2026-06-22"
    ],

    "Category": [
        "Electronics", "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing", "Electronics", "Furniture",
        "Clothing", "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing", "Electronics"
    ],

    "Sales": [
        85000, 65000, 45000, 95000,
        70000, 50000, 110000, 75000,
        55000, 120000, 80000, 60000,
        130000, 90000, 65000, 140000
    ],

    "Profit": [
        18000, 12000, 9000, 21000,
        14000, 10000, 25000, 15000,
        11000, 28000, 16000, 12000,
        30000, 18000, 13000, 32000
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Day_Name"] = df["Order_Date"].dt.day_name()
print(df)

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
      .sum()
)
print(monthly_sales)

monthly_profit = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"]
      .sum()
)
print(monthly_profit)

monthly_growth = monthly_sales.pct_change() * 100
print(monthly_growth)

highest_sales_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
lowest_sales_month = monthly_sales.idxmin()
lowest_sales = monthly_sales.min()
highest_profit_month = monthly_profit.idxmax()
highest_profit = monthly_profit.max()
average_monthly_sales = monthly_sales.mean()
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print("Highest Sales Month:", highest_sales_month)
print("Highest Sales:", highest_sales)
print("Lowest Sales Month:", lowest_sales_month)
print("Lowest Sales:", lowest_sales)
print("Highest Profit Month:", highest_profit_month)
print("Highest Profit:", highest_profit)
print("Average Monthly Sales:", average_monthly_sales)
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

orders_by_weekday = (
    df["Order_Date"]
      .dt.day_name()
      .value_counts()
)
print(orders_by_weekday)
