# # Practice 
# # Q1 — Customer Revenue Calculate:Total Sales by customer, Total Profit by customer, Number of orders by customer
# # Q2 — Customer AOV Create: Find the customer with the highest AOV.
# # Q3 — Customer Profit Margin Create: Find the customer with the highest profit margin.
# # Q4 — Customer Value Segmentation Create three segments using np.select(): Condition	Segment, Sales ≥ ₹150,000 AND Profit ≥ ₹30,000	High Value, Sales ≥ ₹80,000 OR Profit ≥ ₹15,000	Medium Value, Otherwise	Low Value
# # Q5 — Rank Customers Create: Sales Rank, Profit Rank, AOV Rank, Overall Value Score
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Order_ID": range(1001, 1013),
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya","Riya",
        "Karan","Amit","Priya","Rahul","Riya","Neha"
    ],
    "Category": [
        "Electronics","Furniture","Electronics","Clothing",
        "Furniture","Electronics","Clothing","Electronics",
        "Electronics","Furniture","Clothing","Furniture"
    ],
    "Sales": [
        50000,40000,35000,60000,55000,45000,
        30000,70000,65000,50000,55000,25000
    ],
    "Profit": [
        10000,8000,7000,12000,11000,9000,
        6000,14000,13000,10000,11000,5000
    ]
})
customer = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()
print(customer)

customer["AOV"] = customer["Total_Sales"] / customer["Total_Orders"]
highest_aov = customer.loc[customer["AOV"].idxmax()]
print(highest_aov)

customer["Profit_Margin_%"] = (
    customer["Total_Profit"] / customer["Total_Sales"] * 100
)

highest_margin = customer.loc[
    customer["Profit_Margin_%"].idxmax()
]
print(highest_margin)

conditions = [
    (customer["Total_Sales"] >= 150000) &
    (customer["Total_Profit"] >= 30000),

    (customer["Total_Sales"] >= 80000) |
    (customer["Total_Profit"] >= 15000)
]
choices = ["High Value", "Medium Value"]
customer["Segment"] = np.select(
    conditions,
    choices,
    default="Low Value"
)

customer["Sales Rank"] = customer["Total_Sales"].rank(
    ascending=False, method="min"
)
customer["Profit Rank"] = customer["Total_Profit"].rank(
    ascending=False, method="min"
)
customer["AOV Rank"] = customer["AOV"].rank(
    ascending=False, method="min"
)
customer["Overall Value Score"] = (
    customer["Sales Rank"] +
    customer["Profit Rank"] +
    customer["AOV Rank"]
)
customer = customer.sort_values("Overall Value Score")
print(customer)
