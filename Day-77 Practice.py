# # Practice 
# # Q1 Perform a left merge.
# # Q2 Find the order(s) with missing customer information.
# # Q3 Calculate total sales by city.
# # Q4 Calculate total profit by city.
# # Q5 Find the city with the highest total sales.
import pandas as pd 
customers = pd.DataFrame({
    "Customer_ID": [101,102,103,104,105],
    "Customer": ["Amit","Riya","Rahul","Priya","Karan"],
    "City": ["Kolkata","Delhi","Mumbai","Pune","Delhi"]
})

orders = pd.DataFrame({
    "Order_ID": [1001,1002,1003,1004,1005,1006],
    "Customer_ID": [101,102,103,101,104,106],
    "Sales": [85000,60000,90000,75000,110000,70000],
    "Profit": [18000,12000,20000,15000,25000,16000]
})
merged = orders.merge(customers, on="Customer_ID", how="left")
print(merged)

print(merged[merged["Customer"].isna()])

sales_by_city = merged.groupby("City")["Sales"].sum()
print(sales_by_city)

profit_by_city = merged.groupby("City")["Profit"].sum()
print(profit_by_city)

highest_sales_city = sales_by_city.idxmax()
highest_sales = sales_by_city.max()
print(highest_sales_city)
print(highest_sales)

