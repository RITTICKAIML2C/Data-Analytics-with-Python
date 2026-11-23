# # Part A — Historical Analysis Calculate: MoM Sales Growth %, MoM Profit Growth, Average Sales Growth %, Average Profit Growth %, Total Sales, Total Profit, Overall Profit Margin
# # Part B — Growth-Based Forecast. Using average historical sales growth, forecast: January, February and March of the following year. Create: Month, Forecast_Sales
# # Part C — Linear Forecast. Use: x = np.arange(len(df)), y = df["Sales"].values. slope, intercept = np.polyfit(x, y, 1). Forecast the next 3 months. # # Part D — Compare Forecasts. Create a table: Month	Growth Forecast	Linear Forecast	Difference Jan, Feb, Ma4r. Then determine: Which method predicts higher? What's the average difference? Which method appears more aggressive?
# # Part E — Business Insights
# # Write 5 analyst-style insights.
# # ⭐ Bonus Challenge Calculate the forecasted profit for the next 3 months assuming the historical overall profit margin remains constant.
import pandas as pd
import numpy as np

# Dataset
df = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],
    "Sales": [
        85000, 90000, 94000, 98000,
        105000, 112000, 118000, 125000,
        131000, 140000, 148000, 157000
    ],
    "Profit": [
        17000, 18000, 18800, 19600,
        21000, 22400, 23600, 25000,
        26200, 28000, 29600, 31400
    ]
})

df["Sales_Growth_%"] = df["Sales"].pct_change() * 100
df["Profit_Growth_%"] = df["Profit"].pct_change() * 100

avg_sales_growth = df["Sales_Growth_%"].mean()
avg_profit_growth = df["Profit_Growth_%"].mean()

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

overall_profit_margin = (
    total_profit / total_sales
) * 100

print("Average Sales Growth:", avg_sales_growth)
print("Average Profit Growth:", avg_profit_growth)
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Overall Profit Margin:", overall_profit_margin)


avg_growth = avg_sales_growth / 100

forecast_sales = []

last_sales = df["Sales"].iloc[-1]

for i in range(3):
    last_sales = last_sales * (1 + avg_growth)
    forecast_sales.append(last_sales)

growth_forecast = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Forecast_Sales": forecast_sales
})

print("\nGrowth Forecast:")
print(growth_forecast)

x = np.arange(len(df))
y = df["Sales"].values

slope, intercept = np.polyfit(x, y, 1)

future_x = np.arange(len(df), len(df) + 3)

linear_sales = (
    slope * future_x + intercept
)

linear_forecast = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Forecast_Sales": linear_sales
})

print("\nLinear Forecast:")
print(linear_forecast)

comparison = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Growth Forecast": forecast_sales,
    "Linear Forecast": linear_sales
})

comparison["Difference"] = (
    comparison["Growth Forecast"] -
    comparison["Linear Forecast"]
)

average_difference = comparison["Difference"].mean()

print("\nForecast Comparison:")
print(comparison)

print("\nAverage Difference:", average_difference)

profit_margin = overall_profit_margin / 100

growth_forecast["Forecast_Profit"] = (
    growth_forecast["Forecast_Sales"]
    * profit_margin
)

linear_forecast["Forecast_Profit"] = (
    linear_forecast["Forecast_Sales"]
    * profit_margin
)

print("\nGrowth Forecast with Profit:")
print(growth_forecast)

print("\nLinear Forecast with Profit:")
print(linear_forecast)

