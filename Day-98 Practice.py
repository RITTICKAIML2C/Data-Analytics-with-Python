# # Q1 — Growth Analysis. Calculate: MoM Sales Growth %, MoM Profit Growth %, Average Sales Growth %, Average Profit Growth %
# # Q2 — Simple Forecast. Using the average sales growth rate, forecast: September, October, November
# # Q3 — Linear Forecast. Using np.polyfit(). Forecast sales for: September, October, November. Compare your linear forecast with your growth-based forecast.
# # Q4 — Forecast Comparison. Calculate the difference between the two forecasting methods: Growth Forecast, Linear Forecast, Difference. Then identify which method predicts higher sales.
import pandas as pd
import numpy as np

monthly = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug"
    ],
    "Sales": [
        100000, 108000, 115000, 121000,
        130000, 138000, 145000, 155000
    ],
    "Profit": [
        20000, 21600, 23000, 24200,
        26000, 27600, 29000, 31000
    ]
})
monthly["Sales_Growth_%"] = monthly["Sales"].pct_change() * 100
monthly["Profit_Growth_%"] = monthly["Profit"].pct_change() * 100

avg_sales_growth = monthly["Sales_Growth_%"].mean()
avg_profit_growth = monthly["Profit_Growth_%"].mean()

print("Average Sales Growth:", avg_sales_growth)
print("Average Profit Growth:", avg_profit_growth)

avg_growth = avg_sales_growth / 100

aug_sales = monthly["Sales"].iloc[-1]

sep_sales = aug_sales * (1 + avg_growth)
oct_sales = sep_sales * (1 + avg_growth)
nov_sales = oct_sales * (1 + avg_growth)

x = np.arange(1, 9)
y = monthly["Sales"]

slope, intercept = np.polyfit(x, y, 1)

future_months = np.array([9, 10, 11])

linear_forecast = slope * future_months + intercept


comparison = pd.DataFrame({
    "Month": ["September", "October", "November"],
    "Growth Forecast": [sep_sales, oct_sales, nov_sales],
    "Linear Forecast": linear_forecast
})

comparison["Difference"] = (
    comparison["Growth Forecast"] -
    comparison["Linear Forecast"]
)

comparison["Higher Method"] = np.where(
    comparison["Growth Forecast"] > comparison["Linear Forecast"],
    "Growth Forecast",
    "Linear Forecast"
)
print(comparison)
