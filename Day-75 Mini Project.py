# # 💼 Mini Project — Business Customer Filter Using the same dataset: Create Profit_Margin using eval(), Find High-Value Customers → Sales ≥ ₹100k, Find High-Profit Customers → Profit ≥ ₹20k, Find customers with Sales ≥ ₹60k AND Profit_Margin ≥ 20%.
# # Find the best customer based on Sales, Find the best customer based on Profit, Write 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Priya","Karan","Neha"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Furniture","Clothing"],
    "Sales": [120000,75000,45000,150000,65000,30000],
    "Profit": [30000,12000,9000,40000,10000,5000]
})

# 1. Create Profit_Margin using eval()
df.eval("Profit_Margin = (Profit / Sales) * 100", inplace=True)

# 2. High-Value Customers
high_value = df.query("Sales >= 100000")

# 3. High-Profit Customers
high_profit = df.query("Profit >= 20000")

# 4. Sales >= ₹60k AND Profit Margin >= 20%
high_margin = df.query(
    "Sales >= 60000 and Profit_Margin >= 20"
)

# 5. Best customer based on Sales
best_sales = df.loc[df["Sales"].idxmax(), "Customer"]

# 6. Best customer based on Profit
best_profit = df.loc[df["Profit"].idxmax(), "Customer"]

print("High-Value Customers:")
print(high_value)

print("\nHigh-Profit Customers:")
print(high_profit)

print("\nSales >= 60k and Profit Margin >= 20%:")
print(high_margin)

print("\nBest Customer by Sales:", best_sales)
print("Best Customer by Profit:", best_profit)
