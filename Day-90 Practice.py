# # Practice
# # Q1 — Customer Order Frequency. Find Number of unique customers, Number of unique orders, Orders per customer
# # Q2 — Repeat Customers. Identify all customers who placed more than one order. Also calculate: Repeat Customer Count, Repeat Customer Percentage
# # Q3 — Customer Revenue. Using groupby(), calculate for every customer: Total Sales, Total Profit, Number of Orders Average Order Value
# # Q4 — Repeat vs One-Time Customers Create: Repeat_Customer with: "Repeat", "One-Time" Then compare: Total Sales Total Profit, Average Sales between the two groups.
# # Q5 — Customer Retention by Month Find the number of unique customers in each month. Then determine how many customers from each month also appeared in a later month.
import pandas as pd
import numpy as np
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
unique_customers = df["Customer"].nunique()
unique_orders = df["Order_ID"].nunique()

orders_per_customer = (
    df.groupby("Customer")["Order_ID"]
    .nunique()
    .reset_index(name="Number_of_Orders")
)

print("Unique Customers:", unique_customers)
print("Unique Orders:", unique_orders)
print(orders_per_customer)


# Q2
customer_orders = (
    df.groupby("Customer")["Order_ID"]
    .nunique()
)

repeat_customers = customer_orders[
    customer_orders > 1
]

repeat_customer_count = repeat_customers.shape[0]

repeat_customer_percentage = (
    repeat_customer_count / unique_customers
) * 100

print("\nRepeat Customers:")
print(repeat_customers)

print("Repeat Customer Count:", repeat_customer_count)
print(
    f"Repeat Customer Percentage: "
    f"{repeat_customer_percentage:.2f}%"
)


# Q3
customer_revenue = (
    df.groupby("Customer")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order_ID", "nunique")
    )
    .reset_index()
)

customer_revenue["AOV"] = (
    customer_revenue["Total_Sales"] /
    customer_revenue["Number_of_Orders"]
)

print("\nCustomer Revenue:")
print(customer_revenue)


# Q4
customer_revenue["Repeat_Customer"] = (
    customer_revenue["Number_of_Orders"]
    .apply(
        lambda x: "Repeat" if x > 1 else "One-Time"
    )
)

customer_comparison = (
    customer_revenue
    .groupby("Repeat_Customer")
    .agg(
        Total_Sales=("Total_Sales", "sum"),
        Total_Profit=("Total_Profit", "sum"),
        Average_Sales=("Total_Sales", "mean")
    )
    .reset_index()
)

print("\nRepeat vs One-Time:")
print(customer_comparison)


# Q5
month_order = ["Jan", "Feb", "Mar", "Apr"]

customers_by_month = {
    month: set(
        df.loc[df["Month"] == month, "Customer"]
    )
    for month in month_order
}

retention = []

for i, month in enumerate(month_order):

    current_customers = customers_by_month[month]

    later_customers = set()

    for later_month in month_order[i + 1:]:
        later_customers.update(
            customers_by_month[later_month]
        )

    retained_customers = (
        current_customers & later_customers
    )

    retention.append({
        "Month": month,
        "Unique_Customers": len(current_customers),
        "Retained_Customers": len(retained_customers)
    })

retention_df = pd.DataFrame(retention)

print("\nCustomer Retention:")
print(retention_df)
