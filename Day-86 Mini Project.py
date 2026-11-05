# # 💼 Mini Project — Sales Trend Analyzer
# # Create: Sales_Rolling_Avg_3M, Sales_Rolling_Sum_3M, Profit_Rolling_Avg_3M, Sales_Rolling_Max_3M
# # Find the month with the highest rolling Sales average, Find the month with the highest rolling Sales sum, Print 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Sales":[50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit":[10000,12000,11000,14000,15000,16000,14500,18000]
})
df["Sales_Rolling_Avg_3M"] = df["Sales"].rolling(3).mean()

df["Sales_Rolling_Sum_3M"] = df["Sales"].rolling(3).sum()

df["Profit_Rolling_Avg_3M"] = df["Profit"].rolling(3).mean()

df["Sales_Rolling_Max_3M"] = df["Sales"].rolling(3).max()

highest_avg_month = df.loc[df["Sales_Rolling_Avg_3M"].idxmax()]

highest_sum_month = df.loc[df["Sales_Rolling_Sum_3M"].idxmax()]

print(df)
print(highest_avg_month)
print(highest_sum_month)

# 1. Sales momentum is improving toward August.
# 2. August has the strongest recent sales period.
# 3. Sales show an overall upward trend despite some fluctuations.
