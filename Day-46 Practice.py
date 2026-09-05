import pandas as pd 
# # Industry Practice
# # Sales Dataset : Create two DataFrames. January
# # Columns: Order_ID, Department, Sales, Profit
# # Create 5 orders. February, Use the same columns and create another 5 orders.
# # A. Combine January + February using: pd.concat()
# # B. Use: ignore_index=True
# # C. Calculate from the combined dataset:
# # Total Sales, Average Sales, Total Profit, Average Profit, Highest Sales Order
# # D. Find: Department with highest total sales, Department with highest total profit
january = pd.DataFrame({
    "Order_ID": ["JAN001", "JAN002", "JAN003", "JAN004", "JAN005"],
    "Department": ["Electronics", "Clothing", "Electronics", "Furniture", "Clothing"],
    "Sales": [120000, 75000, 95000, 110000, 65000],
    "Profit": [18000, 12000, 15000, 22000, 10000]
})
february = pd.DataFrame({
    "Order_ID": ["FEB001", "FEB002", "FEB003", "FEB004", "FEB005"],
    "Department": ["Furniture", "Electronics", "Clothing", "Electronics", "Furniture"],
    "Sales": [130000, 140000, 85000, 115000, 90000],
    "Profit": [25000, 24000, 14000, 19000, 16000]
})
combined = pd.concat([january, february], ignore_index=True)
print(combined)

print(combined["Sales"].sum())
print(combined["Sales"].mean())
print(combined["Profit"].sum())
print(combined["Profit"].mean())
print(combined.loc[combined["Sales"].idxmax()])

department_sales = combined.groupby("Department")["Sales"].sum()
print(department_sales.idxmax())
print(department_sales.max())

department_profit = combined.groupby("Department")["Profit"].sum()
print(department_profit.idxmax())
print(department_profit.max())

