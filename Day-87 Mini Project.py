# # 💼 Mini Project — Monthly Growth Analyzer
# # Create: Previous_Sales, Sales_Change, MoM_Growth_%, Previous_Profit
# # Profit_Growth_%, Find the month with the highest Sales growth, Find the month with the largest Sales decline, Print 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Sales":[50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit":[10000,12000,11000,14000,15000,16000,14500,18000]
})
df["Previous_Sales"] = df["Sales"].shift()

df["Sales_Change"] = df["Sales"].diff()

df["MoM_Growth_%"] = df["Sales"].pct_change() * 100

df["Previous_Profit"] = df["Profit"].shift()

df["Profit_Growth_%"] = df["Profit"].pct_change() * 100

highest_growth = df.loc[df["MoM_Growth_%"].idxmax()]

largest_decline = df.loc[df["Sales_Change"].idxmin()]

print(df)
print(highest_growth)
print(largest_decline)

# 1. August had the highest Sales growth compared with the previous month
# 2. July had the largest Sales decline compared with the previous month
# 3. Sales reached their highest level in August at ₹90,000.
