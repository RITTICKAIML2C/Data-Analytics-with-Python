# # Industrial EDA Challenge
# # 📊 Industrial Analysis
# # Step 1 — Dataset Overview Find: Number of orders Number of departments, Number of products, Average sales, Average profit, Average delivery days, Maximum sales, Maximum profit, Maximum delivery days
# # Step 2 — Department Analysis Calculate: A. Total sales by department, B. Average sales by department C. Total profit by department D. Average profit by department E. Average delivery days by department F. Number of orders by department
# # 💼 Step 3 — Business Question Find: Which department generates the highest total sales? Which department generates the highest total profit? Which department has the highest average order value? Which department has the fastest average delivery? Which department receives the most orders? Which product has the highest sales? Which product generates the highest profit? Which order took the longest to deliver?
# # 🧮 Step 4 — Profit Margin. Create: df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100. Then find: A. Average profit margin B. Product with the highest profit margin C. Department with the highest average profit margin D. Products with profit margin above 20%
# # 🔥 Step 5 — Business Classification Create: Sales_Category Sales >= 100000 → Hig Sales >= 60000  → Medium Sales < 60000   → Low
# # Then create: Delivery_Category Delivery_Days <= 2 → Fas Delivery_Days <= 5 → Normal Delivery_Days > 5   → Delayed
# # ⭐ Step 6 — Final Business Insights, This is the most important part, Don't simply give me:idxmax()
import pandas as pd 
import numpy as np 
df = pd.DataFrame({
    "Order_ID": range(1001, 1016),

    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing",
        "IT", "IT", "IT",
        "Electronics", "Furniture", "IT"
    ],

    "Product": [
        "Laptop", "Phone", "Tablet",
        "Chair", "Table", "Sofa",
        "Shirt", "Jeans", "Jacket",
        "Server", "Software", "Cloud",
        "Monitor", "Desk", "Database"
    ],

    "Sales": [
        120000, 85000, 70000,
        50000, 75000, 90000,
        30000, 45000, 60000,
        150000, 110000, 95000,
        80000, 65000, 125000
    ],

    "Profit": [
        25000, 18000, 14000,
        8000, 12000, 15000,
        5000, 7000, 10000,
        35000, 28000, 22000,
        16000, 11000, 30000
    ],

    "Delivery_Days": [
        2, 4, 3,
        5, 3, 6,
        4, 2, 7,
        3, 5, 2,
        4, 3, 6,
        2, 5
    ]
})
print("Orders:", len(df))
print("Departments:", df["Department"].nunique())
print("Products:", df["Product"].nunique())
print("Average Sales:", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())
print("Average Delivery:", df["Delivery_Days"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Maximum Profit:", df["Profit"].max())
print("Maximum Delivery:", df["Delivery_Days"].max())

print(df.groupby("Department")["Sales"].sum())
print(df.groupby("Department")["Sales"].mean())
print(df.groupby("Department")["Profit"].sum())
print(df.groupby("Department")["Profit"].mean())
print(df.groupby("Department")["Delivery_Days"].mean())
print(df["Department"].value_counts())

print("1.", df.groupby("Department")["Sales"].sum().idxmax())
print("2.", df.groupby("Department")["Profit"].sum().idxmax())
print("3.", df.groupby("Department")["Sales"].mean().idxmax())
print("4.", df.groupby("Department")["Delivery_Days"].mean().idxmin())
print("5.", df["Department"].value_counts().idxmax())
print("6.", df.loc[df["Sales"].idxmax(), "Product"])
print("7.", df.loc[df["Profit"].idxmax(), "Product"])
print("8.", df.loc[df["Delivery_Days"].idxmax(), "Order_ID"])

df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100
print("A.", df["Profit_Margin"].mean())
print("B.", df.loc[df["Profit_Margin"].idxmax(), "Product"])
print("C.", df.groupby("Department")["Profit_Margin"].mean().idxmax())
print("D.", df.query("Profit_Margin > 20")["Product"])

conditions = [df["Sales"] >= 100000, df["Sales"] >= 60000]
df["Sales_Category"] = np.select(conditions, ["High", "Medium"], default="Low")
conditions = [df["Delivery_Days"] <= 2, df["Delivery_Days"] <= 5]
df["Delivery_Category"] = np.select(conditions, ["Fast", "Normal"], default="Delayed")

print("Highest Sales Department:", df.groupby("Department")["Sales"].sum().idxmax())
print("Highest Profit Department:", df.groupby("Department")["Profit"].sum().idxmax())
print("Highest Average Order Value:", df.groupby("Department")["Sales"].mean().idxmax())
print("Fastest Department:", df.groupby("Department")["Delivery_Days"].mean().idxmin())
print("Most Orders:", df["Department"].value_counts().idxmax())
print("Top Sales Product:", df.loc[df["Sales"].idxmax(), "Product"])
print("Top Profit Product:", df.loc[df["Profit"].idxmax(), "Product"])
print("Longest Delivery Order:", df.loc[df["Delivery_Days"].idxmax(), "Order_ID"])
print("Average Profit Margin:", df["Profit_Margin"].mean())
