# # 💼 Mini Project — Customer Performance Analyzer
# # Build a small dashboard: Calculate average Sales by Category.
# # Add Avg_Category_Sales to every row using transform(), Add Above_Category_Avg, Add Sales_vs_Category_Avg_%, Find the top performer in each category, Find the customer with the largest positive deviation from their category average, Print 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Category":["Electronics","Furniture","Electronics","Furniture",
                "Electronics","Furniture","Electronics","Furniture"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
avg_sales_by_category = (df.groupby("Category")["Sales"].mean())
print(avg_sales_by_category)

df["Avg_Category_Sales"] = (df.groupby("Category")["Sales"].transform("mean"))

df["Above_Category_Avg"] = (df["Sales"] > df["Avg_Category_Sales"])

df["Sales_vs_Category_Avg_%"] = ((df["Sales"] - df["Avg_Category_Sales"])/ df["Avg_Category_Sales"] * 100)

top_performers = (df.loc[df.groupby("Category")["Sales"].idxmax()])
print(top_performers[["Category", "Customer", "Sales"]])

largest_deviation = df.loc[df["Sales_vs_Category_Avg_%"].idxmax()]
print(largest_deviation[["Customer", "Category", "Sales", "Avg_Category_Sales", "Sales_vs_Category_Avg_%"]])
print(df)

# 1. Vikram is the strongest Electronics performer
# 2. Priya is the strongest Furniture performer
# 3. Electronics has a higher average sales value than Furniture
