# # 💼 Mini Project — Sales Ranking Dashboard
# # Create: Sales_Rank, Category_Sales_Rank, Profit_Rank
# # Top 3 customers by Sales, Top 2 customers within each Category, Top customer in each Category, Print 3 business insights
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Category":["Electronics","Furniture","Electronics","Furniture",
                "Electronics","Furniture","Electronics","Furniture"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
df["Sales_Rank"] = df["Sales"].rank(
    ascending=False,
    method="dense"
)

df["Category_Sales_Rank"] = (
    df.groupby("Category")["Sales"]
      .rank(ascending=False, method="dense")
)

df["Profit_Rank"] = df["Profit"].rank(
    ascending=False,
    method="dense"
)

top_3_sales = df.nlargest(3, "Sales")

top_2_category = (
    df.sort_values("Sales", ascending=False)
      .groupby("Category")
      .head(2)
)

top_customer_category = df.loc[
    df.groupby("Category")["Sales"].idxmax()
]

print(df)
print(top_3_sales)
print(top_2_category)
print(top_customer_category)

# 1. Vikram is the highest-sales customer with sales of ₹3,00,000
# 2. Electronics has Vikram and Karan as its top 2 customers
# 3. Vikram is also the most profitable customer with a profit of ₹60,000
