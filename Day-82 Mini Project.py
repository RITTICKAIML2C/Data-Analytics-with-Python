# # 💼 Mini Project — Business Relationship Analyzer
# # Using the same dataset: Create the numerical correlation matrix.
# # Calculate: Sales ↔ Profit, Sales ↔ Orders, Profit ↔ Orders, Calculate the corresponding covariance values, Identify the strongest positive relationship, Print 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500],
    "Orders":[5,6,5,7,8,5,20,6]
})
correlation_matrix = df[["Sales", "Profit", "Orders"]].corr()
print(correlation_matrix)

sales_profit_corr = df["Sales"].corr(df["Profit"])
sales_orders_corr = df["Sales"].corr(df["Orders"])
profit_orders_corr = df["Profit"].corr(df["Orders"])
print("Sales ↔ Profit:", sales_profit_corr)
print("Sales ↔ Orders:", sales_orders_corr)
print("Profit ↔ Orders:", profit_orders_corr)

sales_profit_cov = df["Sales"].cov(df["Profit"])
sales_orders_cov = df["Sales"].cov(df["Orders"])
profit_orders_cov = df["Profit"].cov(df["Orders"])
print("Sales ↔ Profit:", sales_profit_cov)
print("Sales ↔ Orders:", sales_orders_cov)
print("Profit ↔ Orders:", profit_orders_cov)

relationships = {
    "Sales ↔ Profit": sales_profit_corr,
    "Sales ↔ Orders": sales_orders_corr,
    "Profit ↔ Orders": profit_orders_corr
}
strongest = max(relationships, key=relationships.get)
