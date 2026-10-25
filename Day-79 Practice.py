# # Practice 
# # Q1 Calculate Q1, Q3 and IQR for Sales.
# # Q2 Calculate the lower and upper bounds.
# # Q3 Find the Sales outlier(s).
# # Q4 Create an Outlier column containing True/False.
# # Q5 Calculate the average Sales with and without the outlier.
import pandas as pd
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales": [50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit": [10000,12000,11000,13000,14000,10500,60000,11500]
})
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
print("IQR:", IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[
    (df["Sales"] < lower_bound) |
    (df["Sales"] > upper_bound)
]
print(outliers)

df["Outlier"] = (
    (df["Sales"] < lower_bound) |
    (df["Sales"] > upper_bound)
)
print(df)

avg_with = df["Sales"].mean()
avg_without = df[df["Outlier"] == False]["Sales"].mean()
print(avg_with)
print(avg_without)
