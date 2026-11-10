# # 1. Dataset
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Order_ID": range(1001, 1013),
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya","Riya",
        "Karan","Amit","Priya","Rahul","Riya","Neha"
    ],
    "Month": [
        "Jan","Jan","Jan","Feb","Feb","Feb",
        "Mar","Mar","Mar","Mar","Apr","Apr"
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

# # a. Number of Orders per Customer
customer_orders = df.groupby("Customer")["Order_ID"].nunique()

# # b. Identify repeat customers
order_count = df.groupby("Customer")["Order_ID"].nunique()
repeat_customers = order_count[order_count > 1]

# # c. Repeat Customer Flag
df["Order_Count"] = df.groupby("Customer")["Order_ID"].transform("nunique")
df["Repeat_Customer"] = np.where(
    df["Order_Count"] > 1,
    "Yes",
    "No"
)

# # d. Repeat Customer Revenue 
repeat_sales = df.loc[
    df["Repeat_Customer"] == "Yes",
    "Sales"
].sum()

