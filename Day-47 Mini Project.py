# # Mini Project — Sales Pivot Analysis
# # Create a DataFrame with 12 orders containing: Order_ID, Department, Month, Sales, Profit
# # Use 4 departments: Electronics, Furniture, Clothing, IT
# # Use 3 months: Jan, Feb, Mar
# # 📊 Analysis : Create: 1. Department × Month → Total Sales, 2. Department × Month → Average Sales, 3. Department × Month → Total Profit
# # ⭐ Business Insights : Find: Highest-selling department, Highest-profit department, Best sales month, Department with the highest average sales
import pandas as pd 
df = pd.DataFrame({
    "Order_ID": [
        101, 102, 103,
        104, 105, 106,
        107, 108, 109,
        110, 111, 112
    ],

    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing",
        "IT", "IT", "IT"
    ],

    "Month": [
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar"
    ],

    "Sales": [
        50000, 65000, 70000,
        40000, 55000, 60000,
        30000, 45000, 50000,
        45000, 60000, 75000
    ],

    "Profit": [
        8000, 10000, 12000,
        6000, 9000, 11000,
        4000, 7000, 8500,
        9000, 11000, 15000
    ]
})
print(pd.pivot_table(df, values="Sales", index="Department", columns="Month", aggfunc="sum"))
print(pd.pivot_table(df, values="Sales", index="Department", columns="Month", aggfunc="mean"))
print(pd.pivot_table(df, values="Profit", index="Department", columns="Month", aggfunc="sum"))

print(df.groupby("Department")["Sales"].sum().idxmax())
print(df.groupby("Department")["Profit"].sum().idxmax())
print(df.groupby("Month")["Sales"].sum().idxmax())
print(df.groupby("Department")["Sales"].mean().idxmax())

