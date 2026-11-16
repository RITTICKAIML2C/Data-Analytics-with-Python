# # CLV = Total Customer Revenue 
# customer_clv = df.groupby("Customer")["Sales"].sum()

# # 1. Total Revenue 
# Total_Revenue = Sales.sum()

# # 2. Average Order Value (AOV)
# AOV = Total_Sales / Number_of_Orders

# # 3. Purchase Frequency
# Frequency = Number_of_Orders

# # 4. Profit
# Total_Profit = Profit.sum()

# # 5. Profit Margin 
# Profit_Margin = Total_Profit / Total_Sales * 100

# # Customer-Level CLV table 
# customer_clv = df.groupby("Customer").agg(
#     Total_Sales=("Sales", "sum"),
#     Total_Orders=("Order_ID", "nunique"),
#     Total_Profit=("Profit", "sum")
# ).reset_index()

# customer_clv["AOV"] = (
#     customer_clv["Total_Sales"] /
#     customer_clv["Total_Orders"]
# )

# customer_clv["Profit_Margin_%"] = (
#     customer_clv["Total_Profit"] /
#     customer_clv["Total_Sales"] * 100
# )
