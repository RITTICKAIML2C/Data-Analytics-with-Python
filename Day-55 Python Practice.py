import numpy as np
import pandas as pd 
# # 1. Salary Classification
# # Create: Employee, Salary : Classify employees: Salary >= 80,000 → "High", Salary >= 60,000 → "Medium", Salary < 60,000 → "Low". Use .apply(). 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Salary": [85000, 65000, 55000, 92000, 60000]
})
df["Salary Classification"] = df["Salary"].apply(
    lambda salary: "High" if salary >= 80000
    else "Medium" if salary >= 60000
    else "Low"
)
print(df)

# # 2. Performance Classification 
# # Create: Employee, Performance. Create Performance_Category: >= 90 → Excellent, >= 75 → Good, >= 60 → Average, < 60 → Poor
# # Use np.select().
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Performance": [95, 82, 68, 55, 90]
})
conditions = [
    df["Performance"] >= 90,
    df["Performance"] >= 75,
    df["Performance"] >= 60, 
    df["Performance"] < 60 
]
choices = [
    "Excellent", 
    "Good", 
    "Average", 
    "Poor"
]
df["Performance_Category"] = np.select(conditions, choices, default="Unknown")
print(df)

# # Industrial Practice 
# # Create: Product, Sales, Profit
# # Then create: Profit_Margin, Sales_Category, Profit_Category
# # Where: Profit Margin, Profit / Sales × 100
# # Sales category: Sales >= 100000 → High, Sales >= 60000  → Medium, Sales < 60000   → Low
# # Profit category: Profit >= 20000 → High, Profit >= 10000 → Medium, Profit < 10000  → Low
df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Sales": [120000, 85000, 55000, 70000, 40000],
    "Profit": [25000, 18000, 8000, 12000, 5000]
})
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100
df["Sales_Category"] = df["Sales"].apply(
    lambda sales: "High" if sales >= 100000
    else "Medium" if sales >= 60000
    else "Low"
)
df["Profit_Category"] = df["Profit"].apply(
    lambda profit: "High" if profit >= 20000
    else "Medium" if profit >= 10000
    else "Low"
)
print(df)
