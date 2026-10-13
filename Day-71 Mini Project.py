# # 💼 Mini Project — Sales Reshaping
# # Create a long-format dataset using melt() and then Calculate total sales by category
# # Calculate total sales by month. Find the best category. Find the best month. Create a Month × Category pivot table. Write 3 business insights
import pandas as pd 
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Electronics": [180000, 95000, 225000],
    "Furniture": [65000, 180000, 75000],
    "Clothing": [45000, 55000, 80000]
})
long_df = df.melt(id_vars="Month", var_name="Category", value_name="Sales")
print(long_df)

category_sales = long_df.groupby("Category")["Sales"].sum()
print(category_sales)

month_sales = long_df.groupby("Month")["Sales"].sum()
print(month_sales)

best_category = category_sales.idxmax()
print(best_category)

best_month = month_sales.idxmax()
print(best_month)

pivot = long_df.pivot_table(index="Month", columns="Category", values="Sales", aggfunc="sum")
print(pivot)

# Electronics is the strongest category, generating ₹5,00,000 in total sales.
# March is the best-performing month, with ₹3,80,000 total sales.
# Furniture sales are strongest in February, while Electronics peaks strongly in March. This suggests category demand varies significantly by month.
