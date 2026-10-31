# # Practice
# # Q1 Create Avg_Category_Sales using groupby() + transform().
# # Q2 Create Above_Category_Avg: True if Sales > category average, False otherwise
# # Q3 Create Sales_vs_Category_Avg_%. 
# # Q4 Find all customers whose Sales are above their category average.
# # Q5 Find the customer who is furthest above their category average in percentage terms.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Category":["Electronics","Furniture","Electronics","Furniture",
                "Electronics","Furniture","Electronics","Furniture"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
df["Avg_Category_Sales"] = (
    df.groupby("Category")["Sales"]
      .transform("mean")
)

df["Above_Category_Avg"] = (
    df["Sales"] > df["Avg_Category_Sales"]
)

df["Sales_vs_Category_Avg_%"] = (
    (df["Sales"] - df["Avg_Category_Sales"])
    / df["Avg_Category_Sales"] * 100
)

above_avg = df[df["Above_Category_Avg"]]

furthest_above = df.loc[
    df["Sales_vs_Category_Avg_%"].idxmax()
]

print(df)
print(above_avg[["Customer", "Category", "Sales"]])
print(furthest_above[[
    "Customer",
    "Category",
    "Sales",
    "Avg_Category_Sales",
    "Sales_vs_Category_Avg_%"
]])
