# # Practice 
# # Q1 Create a global Sales_Rank, where highest Sales = Rank 1.
# # Q2 Create Category_Sales_Rank, ranking customers within their category.
# # Q3 Find the Top 3 customers by Sales.
# # Q4 Find the Top customer in each Category.
# # Q5 Create Profit_Rank where highest Profit = Rank 1.
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

top_3 = df.nlargest(3, "Sales")

top_per_category = df.loc[
    df.groupby("Category")["Sales"].idxmax()
]

df["Profit_Rank"] = df["Profit"].rank(
    ascending=False,
    method="dense"
)

print(df)
print(top_3)
print(top_per_category)
