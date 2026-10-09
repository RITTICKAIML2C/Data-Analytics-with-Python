# # 🏢 MINI PROJECT — MONTHLY SALES PERFORMANCE ANALYSIS
# # Step 1 — Time Features Create: Year, Month, Month_Name, Quarter, Day_Name. Hint: df["Quarter"] = df["Order_Date"].dt.quarter
# # Step 2 — Monthly Dashboard. Calculate: Metric	Analysis Sales	Monthly, Profit	Monthly, Orders	Monthly, Profit Margin	Monthly, Profit margin: (Profit / Sales) * 100
# # Step 3 — Growth Analysis Calculate: Monthly Sales Growth % Monthly Profit Growth %. Also calculate a: 3-month rolling average of Sales.#
# # Step 4 — Category Analysis Calculate: Sales by Category, Profit by Category, Orders by Category, Profit Margin by Category
# # Step 5 — Time-Based Analysis. Find: Best month, Worst month, Best quarter, Best weekday, Highest-growth month, Most profitable category
# # Step 6 — Visualization .Create: 📈 Chart 1 Monthly Sales trend → Line chart 📈 Chart 2 Monthly Profit trend → Line chart 📊 Chart 3 Sales by Category → Bar chart 📊 Chart 4 Profit by Category → Bar chart 📈 Chart 5 Monthly Sales + 3-month Rolling Average
# # 🧠 Step 7 — Business Insights Write at least 5 insights. For example: "Sales increased significantly from March to April." But don't simply guess from the chart. Use your calculated values to support the insight.
import pandas as pd
import matplotlib.pyplot as plt
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
df["Quarter"] = df["Order_Date"].dt.quarter
df["Day_Name"] = df["Order_Date"].dt.day_name()
print(df)

monthly = (
    df.groupby(df["Order_Date"].dt.to_period("M"))
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "count")
      )
)

monthly["Profit_Margin"] = (
    monthly["Profit"] / monthly["Sales"]
) * 100
print(monthly)

monthly["Sales_Growth_%"] = monthly["Sales"].pct_change() * 100
monthly["Profit_Growth_%"] = monthly["Profit"].pct_change() * 100
monthly["Sales_3M_Rolling_Avg"] = (
    monthly["Sales"].rolling(window=3).mean()
)
print(
    monthly[
        [
            "Sales",
            "Profit",
            "Sales_Growth_%",
            "Profit_Growth_%",
            "Sales_3M_Rolling_Avg"
        ]
    ]
)

category = (
    df.groupby("Category")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "count")
      )
)
category["Profit_Margin"] = (
    category["Profit"] / category["Sales"]
) * 100
print(category)

# Best month
best_month = monthly["Sales"].idxmax()
best_month_sales = monthly["Sales"].max()

# Worst month
worst_month = monthly["Sales"].idxmin()
worst_month_sales = monthly["Sales"].min()

# Best quarter
quarterly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("Q"))["Sales"]
      .sum()
)
best_quarter = quarterly_sales.idxmax()
best_quarter_sales = quarterly_sales.max()

# Best weekday
weekday_sales = (
    df.groupby("Day_Name")["Sales"]
      .sum()
)
best_weekday = weekday_sales.idxmax()
best_weekday_sales = weekday_sales.max()

# Highest-growth month
highest_growth_month = monthly["Sales_Growth_%"].idxmax()
highest_growth = monthly["Sales_Growth_%"].max()

# Most profitable category
most_profitable_category = category["Profit"].idxmax()
most_profitable_category_profit = category["Profit"].max()

print("Best Month:", best_month)
print("Best Month Sales:", best_month_sales)

print("Worst Month:", worst_month)
print("Worst Month Sales:", worst_month_sales)

print("Best Quarter:", best_quarter)
print("Best Quarter Sales:", best_quarter_sales)

print("Best Weekday:", best_weekday)
print("Best Weekday Sales:", best_weekday_sales)

print("Highest Growth Month:", highest_growth_month)
print("Highest Sales Growth:", highest_growth)

print(
    "Most Profitable Category:",
    most_profitable_category
)
print(
    "Most Profitable Category Profit:",
    most_profitable_category_profit
)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly.index.astype(str),
    monthly["Sales"],
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly.index.astype(str),
    monthly["Profit"],
    marker="o"
)
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(
    category.index,
    category["Sales"]
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(
    category.index,
    category["Profit"]
)
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly.index.astype(str),
    monthly["Sales"],
    marker="o",
    label="Monthly Sales"
)
plt.plot(
    monthly.index.astype(str),
    monthly["Sales_3M_Rolling_Avg"],
    marker="o",
    label="3-Month Rolling Average"
)
plt.title("Monthly Sales vs 3-Month Rolling Average")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
