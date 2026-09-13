import pandas as pd 
# # 1. Basic Practice 
# # Find : Number of orders in each department, Number of orders for each Department + Status, Which department has the most orders?, Which department has the most Completed orders?
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "Finance"
    ],
    "Status": [
        "Completed", "Pending", "Completed",
        "Completed", "Pending", "Completed"
    ]
})
print(df.groupby("Department").size())
print(df.groupby(["Department", "Status"]).size())
print(df.groupby("Department").size().idxmax())
print(df[df["Status"] == "Completed"].groupby("Department").size())

# # 2. Business Practice 
# # Find : Analysis : Number of orders by department, Number of orders by Department + Status, Total sales by Department + Status.
# # Business Insights : Department with the most orders, Department with the most Completed orders, Department with the most Pending orders, Department + Status combination with the most orders.
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "IT", "IT"
    ],
    "Status": [
        "Completed", "Pending", "Completed",
        "Completed", "Pending", "Cancelled",
        "Completed", "Pending", "Completed", "Pending"
    ],
    "Sales": [
        50000, 20000, 45000,
        40000, 25000, 10000,
        30000, 15000, 55000, 25000
    ]
})
print(df.groupby("Department").size())
print(df.groupby(["Department", "Status"]).size())
print(df.groupby(["Department", "Status"]).sum())

print(df.groupby(["Department", "Status"]).size().idxmax())
print(df[df["Status"] == "Completed"].groupby("Department").size().idxmax())
print(df[df["Status"] == "Pending"].groupby("Department").size().idxmax())
print(df.groupby(["Department", "Status"]).size().idxmax())
