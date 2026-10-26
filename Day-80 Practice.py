# # Practice
# # 1. Display descriptive statistics for Sales.
# # Q2 Find: Mean Sales, Median Sales, Maximum Sales, Minimum Sales
# # Q3 Calculate the 75th percentile of Sales.
# # Q4 Calculate Sales skewness and determine whether Sales are left/right skewed.
# # Q5 Calculate the Coefficient of Variation of Sales.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
print(df["Sales"].describe())

mean_sales = df["Sales"].mean()
median_sales = df["Sales"].median()
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()
print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Maximum Sales:", max_sales)
print("Minimum Sales:", min_sales)

percentile_75 = df["Sales"].quantile(0.75)
print("75th Percentile:", percentile_75)

skewness = df["Sales"].skew()
print("Sales Skewness:", skewness)
if skewness > 0:
    print("Sales are right-skewed.")
elif skewness < 0:
    print("Sales are left-skewed.")
else:
    print("Sales are approximately symmetric.")

mean_sales = df["Sales"].mean()
std_sales = df["Sales"].std()
cv = (std_sales / mean_sales) * 100
print("Coefficient of Variation:", cv, "%")

