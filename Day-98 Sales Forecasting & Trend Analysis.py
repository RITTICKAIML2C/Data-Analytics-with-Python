# Concepts
# 1. Simple Growth-Based Forecasting
forecast = last_sales * (1 + average_growth_rate)

# 2. Average growth Rate 
monthly["MoM_Growth_%"] = (
    monthly["Sales"].pct_change() * 100
)

# 3. Forecasting Multiple Months
forecast = []
last_sales = monthly["Sales"].iloc[-1]
for i in range(3):
    last_sales = last_sales * (1 + avg_growth / 100)
    forecast.append(last_sales)

# 4. Linear Trend Forecasting
x = np.arange(len(monthly))
y = monthly["Sales"].values
slope, intercept = np.polyfit(x, y, 1)

