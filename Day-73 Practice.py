# # Practice 
# # Q1 : Use map() to change: Electronics → Tech, Furniture → Home, Clothing → Fashion
# # Q2 : Create Sales_Level using apply(): ≥ ₹100,000 → "High", ≥ ₹60,000 → "Medium", otherwise → "Low"
# # Q3 : Create Customer_Total_Sales using transform("sum").
# # Q4 : Create Profit_Margin using apply().
# # Q5 : Find the customer with the highest total sales.
import pandas as pd
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Amit","Rahul","Riya","Amit"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Clothing","Furniture"],
    "Sales": [120000,75000,30000,90000,55000,110000],
    "Profit": [30000,12000,5000,18000,10000,25000]
})
df["Category"] = df["Category"].map({
    "Electronics" : "Tech",
    "Furniture" : "Home",
    "Clothing" : "Fashion"
})

df["Sales_Level"] = df["Sales"].apply(
    lambda x: "High" if x >= 100000
    else "Medium" if x >= 60000
    else "Low"
)

df["Customer_Total_Sales"] = df.groupby("Customer")["Sales"].transform("sum")

df["Profit_Margin"] = df.apply(
    lambda row: (row["Profit"] / row["Sales"]) * 100,
    axis=1
)

customer_sales = df.groupby("Customer")["Sales"].sum()
print(customer_sales.idxmax())

print(customer_sales.max())
