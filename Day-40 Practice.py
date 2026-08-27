import pandas as pd 
import matplotlib.pyplot as plt
# # 1. Two Sales Charts 
# # Create two charts in one figure. 
# # Chart 1 - Month -> Sales, Use a line chart
# # Chart 2 - Month -> Profit, Use a bar chart 
# # Both charts must have: Title X-axis label Y-axis label Grid
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [45000, 52000, 48000, 61000, 68000, 72000],
    "Profit": [8000, 9500, 8500, 11000, 12500, 14000]
})
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.subplot(2, 1, 2)
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.tight_layout()
plt.show()

# # 2. Department Analysis 
# # Create two charts side-by-side:
# # Chart 1: Department -> Employees using a bar chart
# # Chart 2: Department -> Average Salary using a bar chart 
# # Use figsize and tight_layout()
df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "Marketing", "Sales"],
    "Employees": [25, 15, 20, 18, 30],
    "Average_Salary": [75000, 52000, 68000, 60000, 80000]
})
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(df["Department"], df["Employees"])
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.subplot(1, 2, 2)
plt.bar(df["Department"], df["Average_Salary"])
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()

# # Industrial Practice 
# # 1. Month → Orders — Line chart, Month → Revenue — Bar chart, Month → Profit — Line chart
# # Then calculate: Total Orders, Average Orders, Total Revenue, Average Revenue, Total Profit, Average Profit
# # Business Insights : Find: Month with highest orders, Month with highest revenue, Month with highest profit. Don't just print the values—identify the month.
df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ],
    "Orders": [120, 150, 135, 180, 210, 240],
    "Revenue": [
        45000, 52000, 48000,
        61000, 68000, 75000
    ],
    "Profit": [
        7000, 8500, 7800,
        10500, 12000, 14000
    ]
})
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(df["Month"], df["Orders"], marker="o")
plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.grid()

plt.subplot(1, 3, 2)
plt.bar(df["Month"], df["Revenue"])
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(df["Month"], df["Profit"], marker="o")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.tight_layout()
plt.show()

total_orders = df["Orders"].sum()
average_orders = df["Orders"].mean()
total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()
total_profit = df["Profit"].sum()
average_profit = df["Profit"].mean()
print("Total Orders:", total_orders)
print("Average Orders:", average_orders)
print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Total Profit:", total_profit)
print("Average Profit:", average_profit)

highest_orders_month = df.loc[df["Orders"].idxmax(), "Month"]
highest_revenue_month = df.loc[df["Revenue"].idxmax(), "Month"]
highest_profit_month = df.loc[df["Profit"].idxmax(), "Month"]
print("Month with highest orders:", highest_orders_month)
print("Month with highest revenue:", highest_revenue_month)
print("Month with highest profit:", highest_profit_month)
