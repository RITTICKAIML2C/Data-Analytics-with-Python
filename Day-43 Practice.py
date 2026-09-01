import pandas as pd 
# # 1. Basic agg()
# # Using one groupby().agg() calculate : Average Salary, Maximum Salary, Minimum Salary, Average Performance, Maximum Performance, Employee Count
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Salary": [50000, 65000, 45000, 48000, 70000, 75000],
    "Performance": [80, 90, 75, 85, 88, 95]
})
summary = df.groupby("Department").agg(
    Average_Salary = ("Salary", "mean"), 
    Maximum_Salary = ("Salary", "max"),
    Minimum_Salary = ("Salary", "min"),
    Average_Performance = ("Performance", "mean"), 
    Maximum_Performance = ("Performance", "max"), 
    Employee_Count = ("Salary", "count")
)
print(summary)

# # Industrial Practice — Sales Analytics
# # Create one table : Total sales, Avergae Sale, Maximum Sales, Total Profit, Average Profit, Total Orders, Average Orders
# # Use : groupby().agg()
# # Business Insights : Department with the highest total sales, Department with the highest total profit, Department with the highest average order volume
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics",
        "Furniture", "Furniture",
        "Clothing", "Clothing",
        "Electronics", "Furniture"
    ],
    "Sales": [
        50000, 65000,
        40000, 55000,
        30000, 45000,
        70000, 60000
    ],
    "Profit": [
        8000, 12000,
        6000, 9000,
        4000, 7000,
        15000, 10000
    ],
    "Orders": [
        50, 65,
        40, 55,
        30, 45,
        70, 60
    ]
})
summary = df.groupby("Department").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Maximum_Sales=("Sales", "max"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean"),
    Total_Orders=("Orders", "sum"),
    Average_Orders=("Orders", "mean")
)
print(summary)

# 1. Highest Total Sales → Electronics
# 2. Highest Total Profit → Electronics
# 3. Highest Average Order Volume → Electronics

print(summary["Total_Sales"].idxmax())
print(summary["Total_Profit"].idxmax())
print(summary["Average_Orders"].idxmax())

