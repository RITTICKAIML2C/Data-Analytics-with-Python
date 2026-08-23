# # 🚀 Mini Project — Sales Performance Dashboard
# # Keep this one small. Create a DataFrame with 10 orders:
# # Order_ID, Department, Sales, Profit
# # Use departments such as: Electronics, Furniture, Clothing, IT
# # 📊 Analysis : Calculate: Total Sales, Average Sales, Highest Sales, Total Profit, Average Profit
# # 📈 Visualization : Create:
# # 1. Bar chart : Department → Total Sales, Use: df.groupby("Department")["Sales"].sum()
# # 2. Line chart : Create a simple order sequence: Order_ID → Sales
# # ⭐ Business Insights : Find: Highest-selling order, Highest-profit order, Best-performing department

import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Department": [
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Clothing", "IT", "Furniture",
        "Electronics", "Clothing"
    ],
    "Sales": [
        45000, 32000, 18000, 52000, 61000,
        24000, 48000, 39000, 72000, 28000
    ],
    "Profit": [
        8000, 5500, 3500, 10000, 12000,
        4500, 9000, 7000, 15000, 5000
    ]
})
print(df)

print(df["Sales"].sum())
print(df["Sales"].mean())
print(df["Sales"].max())
print(df["Profit"].sum())
print(df["Profit"].mean())

department_sales = df.groupby("Department")["Sales"].sum()
plt.bar(department_sales.index, department_sales.values)
plt.title("Department-wise Total Sales")
plt.xlabel("Department")
plt.ylabel("Total Sales")
plt.show()

plt.plot(df["Order_ID"], df["Sales"], markers="o")
plt.title("Sales by Order")
plt.xlabel("Order ID")
plt.ylabel("Sales")
plt.grid()
plt.show()

print(df.loc[df["Sales"].idxmax(), "Order_ID"])
print(df.loc[df["Profit"].idxmax(), "Order_ID"])
