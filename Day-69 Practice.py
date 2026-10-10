# # Practice 
# # Q1 — Inner Merge : Merge orders and customers using an inner join. Then find: Number of rows in the merged DataFrame, Which order was removed and why?
# # Q2 — Left Merge : Perform a left join with orders as the left DataFrame. Find: Which order has missing customer information. Why?
# # Q3 — Outer Merge : Perform an outer merge. Find: Which customer has no orders?, Which order belongs to an unknown customer?
# # Q4 — Merge Validation : Merge using validate="many_to_one". Explain why this validation is appropriate.
# # Q5 — Business Analysis After Merge : Using the left-merged dataset, calculate: Total Sales by City, Total Profit by City, Number of Orders by City, Average Order Value by City. Also identify the unknown customer order separately instead of mixing it with city analysis.
import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Customer": [
        "Amit", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    "City": [
        "Kolkata", "Delhi", "Mumbai",
        "Pune", "Delhi", "Kolkata"
    ]
})

orders = pd.DataFrame({
    "Order_ID": [
        1001, 1002, 1003, 1004,
        1005, 1006, 1007, 1008
    ],
    "Customer_ID": [
        101, 102, 103, 101,
        104, 102, 105, 107
    ],
    "Sales": [
        85000, 60000, 90000, 75000,
        110000, 95000, 55000, 70000
    ],
    "Profit": [
        18000, 12000, 20000, 15000,
        25000, 22000, 10000, 16000
    ]
})
inner_merged = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="inner"
)
print(inner_merged)
print(len(inner_merged))

left_merged = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="left"
)
print(left_merged)
print(left_merged[left_merged["Customer"].isna()])

outer_merged = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="outer"
)
print(outer_merged)

validated_merge = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="left",
    validate="many_to_one"
)
print(validated_merge)

unknown_orders = left_merged[
    left_merged["Customer"].isna()
]
valid_orders = left_merged[
    left_merged["Customer"].notna()
]
total_sales = valid_orders.groupby("City")["Sales"].sum()
print(total_sales)

total_profit = valid_orders.groupby("City")["Profit"].sum()
print(total_profit)

order_count = valid_orders.groupby("City")["Order_ID"].count()
print(order_count)

average_order_value = valid_orders.groupby("City")["Sales"].mean()
print(average_order_value)

