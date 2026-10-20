# # Practice 
# # Q1 Create a Category KPI table containing: Total Sales Total Profit, Average Sales, Number of Orders
# # Q2 Create a Customer KPI table containing: Total Sales Total Profit Average Order Value
# # Q3 Add Profit_Margin to the customer table.
# # Q4 Find the customer with the highest Total Profit.
# # Q5 Find the category with the highest Profit Margin.
import pandas as pd

df = pd.DataFrame({
    "Customer": ["Amit","Riya","Amit","Rahul","Riya","Amit"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Clothing","Furniture"],
    "Sales": [120000,75000,30000,90000,55000,110000],
    "Profit": [30000,12000,5000,18000,10000,25000]
})

# Q1: Category KPI
category_kpi = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Sales=("Sales", "mean"),
    Number_of_Orders=("Sales", "count")
)

# Q2: Customer KPI
customer_kpi = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Order_Value=("Sales", "mean")
)

# Q3: Customer Profit Margin
customer_kpi["Profit_Margin"] = (
    customer_kpi["Total_Profit"] /
    customer_kpi["Total_Sales"]
) * 100

# Q4: Highest Total Profit Customer
highest_profit_customer = customer_kpi["Total_Profit"].idxmax()

# Q5: Category Profit Margin
category_kpi["Profit_Margin"] = (
    category_kpi["Total_Profit"] /
    category_kpi["Total_Sales"]
) * 100

highest_margin_category = category_kpi["Profit_Margin"].idxmax()

print("Category KPI:")
print(category_kpi)

print("\nCustomer KPI:")
print(customer_kpi)

print("\nHighest Profit Customer:", highest_profit_customer)
print("Highest Margin Category:", highest_margin_category)

