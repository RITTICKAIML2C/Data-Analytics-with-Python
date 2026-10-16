# # 💼 Mini Project — Customer Sales Analysis
# # Using the dataset: Map categories into broader groups, Create a Sales Level, Calculate Customer Total Sales using transform(), Calculate Profit Margin.
# # Rank customers by total sales, Identify the highest-value customer, Write 3 business insights.
import pandas as pd 
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Amit","Rahul","Riya","Amit"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Clothing","Furniture"],
    "Sales": [120000,75000,30000,90000,55000,110000],
    "Profit": [30000,12000,5000,18000,10000,25000]
})

df["Category"] = df["Category"].map({
    "Electronics": "Tech",
    "Furniture": "Home",
    "Clothing": "Fashion"
})

df["Sales_Level"] = df["Sales"].apply(
    lambda x: "High" if x >= 100000
    else "Medium" if x >= 60000
    else "Low"
)

df["Customer_Total_Sales"] = (
    df.groupby("Customer")["Sales"].transform("sum")
)

df["Profit_Margin"] = df.apply(
    lambda row: (row["Profit"] / row["Sales"]) * 100,
    axis=1
)

customer_rank = (
    df[["Customer", "Customer_Total_Sales"]]
    .drop_duplicates()
)

customer_rank["Rank"] = (
    customer_rank["Customer_Total_Sales"]
    .rank(method="dense", ascending=False)
)

highest_customer = customer_rank.loc[
    customer_rank["Customer_Total_Sales"].idxmax()
]
print(highest_customer)

