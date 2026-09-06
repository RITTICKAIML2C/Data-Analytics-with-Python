# # Mini Project — Quarterly Sales Dataset
# # 📈 Step 2 — Analysis
# # Calculate: Total Sales Average Sales Total Profit Average Profit Highest-selling order Lowest-selling order
# # 🏢 Step 3 — Department Analysis
# # Calculate: Total sales by department Average sales by department Total profit by department
# # ⭐ Step 4 — Business Insights
# # Find: Highest-selling department Highest-profit department Highest-selling order Lowest-selling order
import pandas as pd 
q1 = pd.DataFrame({
    "Order_ID": ["Q1_001", "Q1_002", "Q1_003", "Q1_004", "Q1_005"],
    "Department": ["Electronics", "Furniture", "Clothing", "IT", "Electronics"],
    "Sales": [120000, 85000, 65000, 150000, 95000],
    "Profit": [18000, 15000, 10000, 30000, 14000]
})
q2 = pd.DataFrame({
    "Order_ID": ["Q2_001", "Q2_002", "Q2_003", "Q2_004", "Q2_005"],
    "Department": ["Furniture", "IT", "Clothing", "Electronics", "IT"],
    "Sales": [110000, 175000, 72000, 135000, 160000],
    "Profit": [20000, 35000, 12000, 21000, 32000]
})
q3 = pd.DataFrame({
    "Order_ID": ["Q3_001", "Q3_002", "Q3_003", "Q3_004", "Q3_005"],
    "Department": ["Clothing", "Electronics", "Furniture", "IT", "Clothing"],
    "Sales": [80000, 145000, 100000, 185000, 70000],
    "Profit": [13000, 23000, 18000, 38000, 11000]
})
all_sales = pd.concat([q1, q2, q3], ignore_index=True)
print(all_sales)

print(all_sales["Sales"].sum())
print(all_sales["Sales"].mean())
print(all_sales["Profit"].sum())
print(all_sales["Profit"].mean())
print(all_sales.loc[all_sales["Sales"].idxmax()])
print(all_sales.loc[all_sales["Sales"].idxmin()])

print(all_sales.groupby("Department")["Sales"].sum())
print(all_sales.groupby("Department")["Sales"].mean())
print(all_sales.groupby("Department")["Profit"].sum())

print(all_sales.groupby("Department")["Sales"].sum().idxmax())
print(all_sales.groupby("Department")["Profit"].sum().idxmax())

print(all_sales.loc[all_sales["Sales"].idxmax()])
print(all_sales.loc[all_sales["Sales"].idxmin()])
