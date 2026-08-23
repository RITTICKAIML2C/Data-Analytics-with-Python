import pandas as pd
import matplotlib.pyplot as plt
# # 1. Monthly Sales Trend 
# # Create a line chart 
# # Requirements: Title, X-axis, Y-axis label, Marker, Grid
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 17000, 22000, 25000, 28000]
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()
# Month - June

# # 2. Department Sales
# # Create a bar chart 
# # Requirements: Title, X-axis label, Y-axis label
departments = ["IT", "HR", "Finance", "Marketing", "Sales"]
sales = [85000, 52000, 73000, 64000, 95000]
plt.bar(departments, sales)
plt.title("Department Sales")
plt.xlabel("Department")
plt.ylabel("Sales")
plt.show()
# Sales Department - highest sales

# #  Industrial Practice
# # a. Dataset Inspection - DataFrame, Shape, Columns, Data types.
# # b. Sales analysis - Total Sales, Average Sales, Highest Sales, Lowest Sales
# # c. Sales Visualization - Month -> Sales
# # Include : Title, Axis labels, Markers, Grid
# # d. Profit visualization - Create another line chart: Month -> Profit
# # e. Business Insights - find : Highest Sales month, Highest Profit Month
df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ],
    "Sales": [
        45000, 52000, 48000,
        61000, 68000, 72000
    ],
    "Profit": [
        8000, 9500, 8500,
        11000, 12500, 14000
    ]
})
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df["Sales"].sum())
print(df["Sales"].mean())
print(df["Sales"].max())
print(df["Sales"].min())

plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.plot(df["Month"], df["Profit"], markers="o")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

print(df.loc[df["Sales"].idxmax(), "Month"])
print(df.loc[df["Profit"].idxmax(), "Month"])


