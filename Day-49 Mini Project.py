# # 🚀 Mini Project — Order Category Analysis
# # Create a DataFrame with 15 orders: Order_ID Department Order_Status
# # Use departments: Electronicsl Furniture Clothing IT
# # Use statuses: Completed Pending Cancelled
# # 📊 Analysis : Find: Number of orders by department, Number of orders by status, Most common department, Most common order status, Least common order status
# # 📈 Percentage Analysis : Find the percentage of orders belonging to each department.
# # df["Department"].value_counts(normalize=True) * 100
# # ⭐ Business Insights Answer in words: Which department receives the most orders? Which department receives the fewest orders? Which order status is most common? What percentage of total orders comes from the largest department?
import pandas as pd
df = pd.DataFrame({
    "Order_ID": range(1001, 1016),
    "Department": [
        "Electronics", "Furniture", "Clothing",
        "IT", "Electronics", "Clothing",
        "Electronics", "Furniture", "Electronics",
        "IT", "Clothing", "Electronics",
        "Furniture", "IT", "Electronics"
    ],
    "Order_Status": [
        "Completed", "Pending", "Completed",
        "Cancelled", "Completed", "Pending",
        "Completed", "Cancelled", "Pending",
        "Completed", "Completed", "Completed",
        "Pending", "Completed", "Pending"
    ]
})
print(df["Department"].value_counts())
print(df["Order_Status"].value_counts())
print(df["Department"].value_counts().index[0])
print(df["Order_Status"].value_counts().index[0])
print(df["Order_Status"].value_counts().index[-1])
print(df["Department"].value_counts(normalize=True)*100)
