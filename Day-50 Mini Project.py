import pandas as pd 
# # 🚀 Mini Project — Department Order Analysis
# # Use: Departments: Electronics Furniture Clothing IT
# # Statuses: Completed Pending Cancelled
# # 📊 Analysis
# # Calculate: 1. Total sales by department, 2. Total sales by department + status, 3. Number of orders by department + status
# # For the third one, use: df.groupby(["Department", "Status"])["Order_ID"].count()
# # ⭐ Business Insights Find: Highest-selling department, Department with highest Completed sales, Department with highest Pending sales, Department with the most Completed orders
df = pd.DataFrame({
    "Order_ID": range(1, 16),

    "Department": [
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "IT"
    ],

    "Status": [
        "Completed", "Completed", "Pending", "Completed",
        "Pending", "Cancelled", "Completed", "Pending",
        "Completed", "Pending", "Cancelled", "Completed",
        "Cancelled", "Completed", "Pending"
    ],

    "Sales": [
        50000, 30000, 15000, 45000,
        20000, 10000, 25000, 18000,
        40000, 22000, 8000, 35000,
        12000, 28000, 25000
    ]
})
print(df.groupby("Department")["Sales"].sum())
print(df.groupby(["Department", "Status"])["Sales"].sum())
print(df.groupby(["Department", "Status"])["Order_ID"].count())

print(df.groupby("Department")["Sales"].sum().idxmax())
print(df[df["Status"] == "Completed"].groupby("Department")["Sales"].sum().idxmax())
print(df[df["Status"] == "Pending"].groupby("Department")["Sales"].sum().idxmax())
print(df[df["Status"] == "Completed"].groupby("Department")["Order_ID"].count().idxmax())
