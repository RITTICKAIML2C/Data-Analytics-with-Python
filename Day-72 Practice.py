# # Practice 
# # Q1 Create: sales = long_df.groupby(["Month", "Category"])["Sales"].sum()
# # Q2 Use unstack() to convert Category into columns.
# # Q3 Use stack() to convert it back.
# # Q4 Use reset_index() to turn the MultiIndex into normal columns.
# # Q5 Find the highest-selling Month + Category combination.
import pandas as pd 
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Electronics": [180000, 95000, 225000],
    "Furniture": [65000, 180000, 75000],
    "Clothing": [45000, 55000, 80000]
})
long_df = df.melt(
    id_vars="Month",
    var_name="Category",
    value_name="Sales"
)
sales = long_df.groupby(["Month", "Category"])["Sales"].sum()
print(sales)

sales_unstacked = sales.unstack()
print(sales_unstacked)

sales_stacked = sales_unstacked.stack()
print(sales_stacked)

sales_df = sales_stacked.reset_index()
sales_df.columns = ["Month", "Category", "Sales"]
print(sales_df)

highest = sales_df.loc[sales_df["Sales"].idxmax()]
print(highest)

# Highest-selling combination = March + Electronics
# Sales = ₹225,000
