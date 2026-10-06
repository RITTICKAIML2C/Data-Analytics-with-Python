# # 1. KPI Analysis 
# # a. Total Revenue
df["Sales"].sum()

# # b. Total Profit 
df["Profit"].sum()

# # c. Average Order Value 
df["Sales"].mean()

# # d. Total number of orders 
df["Order_ID"].nunique()

# # e. Profit Margin 
(df["Profit"].sum() / df["Sales"].sum()) * 100

# # 2. Customer Segmentation
df["Customer_Segment"] = pd.cut(
    df["Total_Sales"],
    bins=[0, 50000, 100000, float("inf")],
    labels=["Low Value", "Medium Value", "High Value"]
)
customer_sales = (
    df.groupby("Customer")["Sales"]
      .sum()
      .reset_index()
)

# # 3. transform()
df["Customer_Total_Sales"] = (
    df.groupby("Customer")["Sales"]
      .transform("sum")
)

