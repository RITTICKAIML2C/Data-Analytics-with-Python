# # Practice 
# # Q1 Create Previous_Sales using shift().
# # Q2 Create Sales_Change using diff().
# # Q3 Calculate MoM_Growth_% using pct_change().
# # Q4 Find the month with the highest positive Sales growth.
# # Q5 Find the month with the largest decrease in Sales.
import pandas as pd
df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Sales":[50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit":[10000,12000,11000,14000,15000,16000,14500,18000]
})
df["Previous_Sales"] = df["Sales"].shift()
print(df)

df["Sales_Change"] = df["Sales"].diff()
print(df)

df["MoM_Growth_%"] = df["Sales"].pct_change() * 100
print(df)

highest_growth_month = df.loc[df["MoM_Growth_%"].idxmax()]
print(highest_growth_month)

largest_decrease_month = df.loc[df["Sales_Change"].idxmin()]
print(largest_decrease_month)
