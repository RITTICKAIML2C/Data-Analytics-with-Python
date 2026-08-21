import pandas as pd
# # 1. Data Conversion 
# # Create a DataFrame: Order_ID, Order_Date (strings)
# # Convert the date column to DateTime.
# # Print: DataFrame, Data types
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104],
    "Order_Date": ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04"]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df)
print(df.dtypes)

# # 2. Data Components 
# # Using the same DataFrame, create: Year Month Day Month_Name Weekday
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104],
    "Order_Date": ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04"]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Day"] = df["Order_Date"].dt.day
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Weekday"] = df["Order_Date"].dt.day_name()
print(df)

# # 3. Data Filtering 
# # Find: Orders after 2026-08-05, Orders between 2026-08-03 and 2026-08-08
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Order_Date": [
        "2026-08-01", "2026-08-03", "2026-08-05", "2026-08-06",
        "2026-08-07", "2026-08-08", "2026-08-09", "2026-08-10"
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
after_orders = df[df["Order_Date"] > "2026-08-05"]
print(after_orders)

between_orders = df[
    (df["Order_Date"] >= "2026-08-03") &
    (df["Order_Date"] <= "2026-08-08")
]
print(between_orders)

# # 4. Date Sorting 
# # Display: Oldest orders first, Newest orders first
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Order_Date": [
        "2026-08-01", "2026-08-03", "2026-08-05", "2026-08-06",
        "2026-08-07", "2026-08-08", "2026-08-09", "2026-08-10"
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
oldest = df.sort_values("Order_Date")
print(oldest)
newest = df.sort_values("Order_Date", ascending=False)
print(newest)

# # 5. Delivery Analysis 
# # Create : Order_Date, Delivery_Date
# # Calculate : Delivery_Days
# # Find : Average Delivery Time, Maximum Delivery TIme, Minimum Delivery Time
df = pd.DataFrame({
    "Order_Date": [
        "2026-08-01",
        "2026-08-03",
        "2026-08-05",
        "2026-08-07",
        "2026-08-09"
    ],
    "Delivery_Date": [
        "2026-08-04",
        "2026-08-06",
        "2026-08-07",
        "2026-08-12",
        "2026-08-10"
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

df["Delivery_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days
print(df)

print(df["Delivery_Days"].mean())
print(df["Delivery_Days"].max())
print(df["Delivery_Days"].min())

# 6. Monthly Sales
# Create: Order_Date, Sales
# Display: Monthly total sales, Monthly average sales
df = pd.DataFrame({
    "Order_Date": [
        "2026-01-05", "2026-01-15",
        "2026-02-10", "2026-02-20",
        "2026-03-08", "2026-03-18"
    ],
    "Sales": [1200, 1800, 1500, 2200, 2500, 1700]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_total = df.groupby(df["Order_Date"].dt.month_name())["Sales"].sum()
print(monthly_total)

monthly_average = df.groupby(df["Order_Date"].dt.month_name())["Sales"].mean()
print(monthly_average)

# # Industry Practice = Sales Analytics Dashboard 
# # Create a DataFrame with: Order_ID, Customer, Order_Date, Delivery_Date, Department, Sales, Profit
# # 📊 Order Analytics : Convert dates, Year, Month, Day, Weekday, Month Name
# # 🚚 Delivery Analytics : Delivery days, Average delivery time, Maximum delivery time,  Minimum delivery time
# # 💰 Sales Analytics : Total sales by month, Average sales by month, Total profit by month
# # 📈 Department Analytics: Average sales by department, Maximum sales by department, Order count by department
# # ⭐ Business Insights : Find: Highest sales order, Highest profit order, Fastest delivery, Slowest delivery, Best sales month
df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["Electronics", "Furniture", "Electronics",
                   "Clothing", "Furniture", "Clothing"],
    "Order_Date": [
        "2026-01-05", "2026-01-15", "2026-02-10",
        "2026-02-20", "2026-03-08", "2026-03-18"
    ],
    "Delivery_Date": [
        "2026-01-08", "2026-01-20", "2026-02-12",
        "2026-02-26", "2026-03-10", "2026-03-25"
    ],
    "Sales": [1200, 1800, 1500, 2200, 2500, 1700],
    "Profit": [250, 400, 300, 550, 700, 350]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

df["Delivery_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days
print(df[["Order_ID", "Delivery_Days"]])
print(df["Delivery_Days"].mean())
print(df["Delivery_Days"].mean())
print(df["Delivery_Days"].max())
print(df["Delivery_Days"].min())

print(df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum())
print(df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].mean())
print(df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"].sum())

print(df.groupby("Department")["Sales"].mean())
print(df.groupby("Department")["Sales"].max())
print(df.groupby("Department")["Order_ID"].count())

print(df.loc[df["Sales"].idxmax()])
print(df.loc[df["Profit"].idxmax()])
print(df.loc[df["Delivery_Days"].idxmin()])
print(df.loc[df["Delivery_Days"].idxmax()])
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()
print(monthly_sales.idxmax(), monthly_sales.max())
