# # Mini Project — MultiIndex Sales Analysis
# # Using the same dataset: Create a Month × Category MultiIndex sales table.
# # Convert it using unstack().
# # Calculate total sales for each month.
# # Calculate total sales for each category.
# # Find the highest-selling Month + Category combination.
# # Identify the lowest-selling combination.
# # Write 3 business insights.
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

sales_table = sales.unstack()
print(sales_table)

monthly_sales = sales_table.sum(axis=1)
print(monthly_sales)

category_sales = sales_table.sum(axis=0)
print(category_sales)

highest = sales.idxmax()
print("Highest:", highest)
print("Sales:", sales.max())

lowest = sales.idxmin()
print("Lowest:", lowest)
print("Sales:", sales.min())

# Insight 1 — Electronics is the strongest category
# Insight 2 — March was the strongest month
