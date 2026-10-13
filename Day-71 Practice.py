# # Practice
# # Q1 Convert the DataFrame from wide → long using melt().
# # Q2 Convert it back to a Month × Category format using pivot().
# # Q3 Create a pivot_table() showing total sales by Month and Category.
# # Q4 Which month had the highest total sales?
# # Q5 Which category had the highest total sales?
import pandas as pd 
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Electronics": [180000, 95000, 225000],
    "Furniture": [65000, 180000, 75000],
    "Clothing": [45000, 55000, 80000]
})
long_df = df.melt(id_vars="Month", var_name="Category", value_name="Sales")
print(long_df)

wide_df = long_df.pivot(index="Month", columns="Category", values="Sales")
print(wide_df)

pivot = pd.pivot_table(long_df, index="Month", columns="Category", values="Sales", aggfunc="sum")
print(pivot)

# March — ₹380,000
# Electronics — ₹500,000
