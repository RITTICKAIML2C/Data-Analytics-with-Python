import pandas as pd 
# # 1. Basic Practice 
# # Find : Average salary of each department, Add a column called Department_Avg, Find employees whose salary is above their department average, Find employees whose salary is below their department average.
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "Finance", "Finance"
    ],
    "Salary": [
        50000, 70000, 90000,
        45000, 55000, 60000, 80000
    ]
})
print(df.groupby("Department")["Salary"].mean())
df["Department_Avg"] = df.groupby("Department")["Salary"].transform("mean")
print(df)
print(df[df["Salary"] > df["Department_Avg"]])
print(df[df["Salary"] < df["Department_Avg"]])

# # 2. Calculate : Average sales by department, Add Department_Avg_Sales, Find products whose sales are above their department average, Find products whose sales are below their department average.
# # Business Insight : Which department has the highest average sales?, Which product has the highest sales?, Which products are performing above their department average?
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Chair", "Table", "Sofa",
        "Shirt", "Jeans", "Jacket"
    ],
    "Sales": [
        120000, 80000, 100000,
        50000, 70000, 90000,
        30000, 45000, 60000
    ]
})
print(df.groupby("Department")["Sales"].mean())
df["Department_Avg_Sales"] = df.groupby("Department")["Sales"].transform("mean")
print(df)
print(df[df["Sales"] > df["Department_Avg_Sales"]])
print(df[df["Sales"] < df["Department_Avg_Sales"]])

print(df.groupby("Department")["Sales"].mean().idxmax())
print(df.loc["Sales"].idxmax(), ["Product", "Sales"])
print(df.loc[df["Sales"] > df["Department_Avg_Sales"], ["Department", "Product", "Sales"]])
