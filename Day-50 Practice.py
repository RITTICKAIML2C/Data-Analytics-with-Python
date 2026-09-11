import pandas as pd 
# # 1. Basic Practice 
# # Find : Total Sales by Department, Total Sales by Department + Status 
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR"
    ],
    "Status": [
        "Completed", "Pending", "Completed",
        "Completed", "Pending", "Cancelled"
    ],
    "Sales": [
        50000, 30000, 45000,
        40000, 25000, 10000
    ]
})
print(df.groupby("Department")["Sales"].sum())
print(df.groupby(["Department", "Status"])["Sales"].sum())

# # 2. Business Analysis 
# # Find : 1. Total Sales by Department, 2. Total Sales by Department + Status, 3. Which dept has the highest total sales, Which dept has the highest completed sales, which dept has the highest pending sales.
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing"
    ],
    "Status": [
        "Completed", "Pending", "Completed",
        "Completed", "Pending", "Cancelled",
        "Completed", "Pending", "Completed"
    ],
    "Sales": [
        80000, 40000, 65000,
        55000, 30000, 15000,
        35000, 20000, 45000
    ]
})
print(df.groupby("Department")["Sales"].sum())
print(df.groupby(["Department", "Status"])["Sales"].sum())

print(df.groupby("Department")["Sales"].sum().idxmax())
print(df[df["Status"] == "Completed"].groupby("Department")["Sales"].sum().idxmax())
print(df[df["Status"] == "Pending"].groupby("Department")["Sales"].sum().idxmax())
