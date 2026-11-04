# # Practice 
# # Q1 Create a 3-month rolling average of Sales.
# # Q2 Create a 3-month rolling sum of Sales.
# # Q3 Create a 3-month rolling average of Profit.
# # Q4 Find the month with the highest 3-month rolling Sales average.
# # Q5 Create a 3-month rolling maximum of Sales.
import pandas as pd

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Sales":[50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit":[10000,12000,11000,14000,15000,16000,14500,18000]
})

df["Sales_Rolling_Avg_3M"] = df["Sales"].rolling(window=3).mean()

df["Sales_Rolling_Sum_3M"] = df["Sales"].rolling(window=3).sum()

df["Profit_Rolling_Avg_3M"] = df["Profit"].rolling(window=3).mean()

highest_month = df.loc[df["Sales_Rolling_Avg_3M"].idxmax(), "Month"]

df["Sales_Rolling_Max_3M"] = df["Sales"].rolling(window=3).max()

print(df)
print(highest_month)
