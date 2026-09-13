import pandas as pd 
# # 🚀 Mini Project — Order Status Analysis
# # Departments: Electronics, Furniture, Clothing, IT
# # Statuses : Completed, Pending, Cancelled
# # 📊 Calculate 1. Number of orders by department., 2. Number of orders by department + status., 3. Total sales by department + status.
# # ⭐ Business Insights : Find: Department with the most orders., Department with the most Completed orders., Department with the most Pending orders., Department + Status combination with the most orders.
df = pd.DataFrame({
    "Order_ID": range(1, 16),

    "Department": [
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "Clothing", "IT",
        "Electronics", "Furniture", "IT"
    ],

    "Status": [
        "Completed", "Pending", "Completed", "Pending",
        "Completed", "Cancelled", "Pending", "Completed",
        "Pending", "Completed", "Cancelled", "Completed",
        "Completed", "Pending", "Pending"
    ],

    "Sales": [
        60000, 30000, 25000, 45000,
        55000, 12000, 18000, 50000,
        22000, 40000, 10000, 35000,
        70000, 28000, 20000
    ]
})
print(df.groupby("Department").size())
print(df.groupby(["Department", "Status"]).size())
print(df.groupby(["Department", "Status"]).sum())

print(df.groupby("Department").size())
print(df[df["Status"] == "Completed"].groupby("Department").size().idxmax())
print(df[df["Status"] == "Pending"].groupby("Department").size().idxmax())
print(df.groupby(["Department", "Status"]).size().idxmax())
