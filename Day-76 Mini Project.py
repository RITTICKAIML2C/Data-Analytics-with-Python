# # 💼 Mini Project — Business KPI Dashboard Using the same dataset:
# # Create a Customer KPI Dashboar Create a Category KPI Dashboar Add Profit Margin to bot Rank customers by Total Sales.
# # Rank categories by Total Profit.
# # Identify : Best customer, Most profitable customer, Best category by sales, Best category by margin
# # Write 3 business insights.
import pandas as pd

df = pd.DataFrame({
    "Customer": ["Amit","Riya","Amit","Rahul","Riya","Amit"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Clothing","Furniture"],
    "Sales": [120000,75000,30000,90000,55000,110000],
    "Profit": [30000,12000,5000,18000,10000,25000]
})
customer_kpi = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Order_Value=("Sales", "mean"),
    Number_of_Orders=("Sales", "count")
)

customer_kpi["Profit_Margin"] = (
    customer_kpi["Total_Profit"] /
    customer_kpi["Total_Sales"]
) * 100

customer_kpi["Sales_Rank"] = (
    customer_kpi["Total_Sales"]
    .rank(ascending=False, method="dense")
)


category_kpi = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Sales=("Sales", "mean"),
    Number_of_Orders=("Sales", "count")
)

category_kpi["Profit_Margin"] = (
    category_kpi["Total_Profit"] /
    category_kpi["Total_Sales"]
) * 100

category_kpi["Profit_Rank"] = (
    category_kpi["Total_Profit"]
    .rank(ascending=False, method="dense")
)

best_customer = customer_kpi["Total_Sales"].idxmax()

most_profitable_customer = customer_kpi["Total_Profit"].idxmax()

best_category_by_sales = category_kpi["Total_Sales"].idxmax()

best_category_by_margin = category_kpi["Profit_Margin"].idxmax()


print("CUSTOMER KPI DASHBOARD")
print(customer_kpi)

print("\nCATEGORY KPI DASHBOARD")
print(category_kpi)

print("\nBest Customer:", best_customer)
print("Most Profitable Customer:", most_profitable_customer)
print("Best Category by Sales:", best_category_by_sales)
print("Best Category by Margin:", best_category_by_margin)
