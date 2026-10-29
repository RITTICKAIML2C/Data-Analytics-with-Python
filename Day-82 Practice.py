# # Practice
# # Q1 Calculate the correlation between Sales and Profit.
# # Q2 Calculate the correlation between Sales and Orders.
# # Q3 Create a correlation matrix for all numerical columns.
# # Q4 Calculate covariance between Sales and Profit.
# # Q5 Based on the correlations, identify which pair has the strongest positive linear relationship.
import pandas as pd

df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500],
    "Orders":[5,6,5,7,8,5,20,6]
})
correlation = df["Sales"].corr(df["Profit"])
print(correlation)

correlation = df["Sales"].corr(df["Orders"])
print(correlation)

corr_matrix = df[["Sales", "Profit", "Orders"]].corr()
print(corr_matrix)

covariance = df["Sales"].cov(df["Profit"])
print(covariance)

# Sales ↔ Profit  = 0.999995
# Sales ↔ Orders  = 0.990382
# Profit ↔ Orders = 0.990270
