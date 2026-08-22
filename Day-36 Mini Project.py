# # Mini Project - Company Sales Time_Series Dashboard 
# # Create a DataFrame with 15 orders containing:
# # Order_ID, Customer, Order_Date, Delivery_Date, Department, Sales, Profit
# # Build a dashboard that displays:
# # 📊 Dataset Overvie : Shape, Columns, Data types
# # 📅 Date Dashboard : Extract: Year, Month, Day, Month Name, Weekday
# # 🚚 Delivery Dashboard : Calculate: Delivery days, Average delivery days, Maximum delivery days, Minimum delivery days
# # 💰 Sales Dashboard : Using groupby(): Monthly total sales, Monthly average sales, Monthly total profit, Using pivot_table(): Monthly average sales by department
# # 📈 Department Dashboard : Total sales, Average sales, Maximum sales, Order count
# # ⭐ Business Insights : Find: Highest sales order, Highest profit order, Best sales month, Department with highest average sales, Orders taking more than 5 delivery days
# # 🎁 Bonus : Create a new column: Delivery_Status
# # Rules: Fast → Delivery ≤ 2 days, Normal → Delivery 3–5 days, Delayed → Delivery > 5 days. Then display:
# # pd.crosstab(
# #     df["Department"],
# #     df["Delivery_Status"]
# # )
import pandas as pd 
df = pd.DataFrame({
    "Order_ID":[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    "Customer":[
        "Amit","Riya","Rahul","Priya","Karan",
        "Sneha","Ankit","Neha","Rohit","Pooja",
        "Vikas","Meera","Arjun","Simran","Nikhil"
    ],
    "Order_Date":[
        "2026-01-05","2026-01-12","2026-01-20",
        "2026-02-02","2026-02-10","2026-02-18",
        "2026-03-03","2026-03-09","2026-03-15",
        "2026-03-25","2026-04-02","2026-04-11",
        "2026-04-20","2026-05-05","2026-05-15"
    ],
    "Delivery_Date":[
        "2026-01-07","2026-01-16","2026-01-28",
        "2026-02-05","2026-02-12","2026-02-25",
        "2026-03-05","2026-03-14","2026-03-17",
        "2026-03-30","2026-04-05","2026-04-18",
        "2026-04-23","2026-05-08","2026-05-24"
    ],
    "Department":[
        "Electronics","Furniture","Clothing",
        "Electronics","Furniture","Clothing",
        "Electronics","Furniture","Clothing",
        "Electronics","Furniture","Clothing",
        "Electronics","Furniture","Clothing"
    ],
    "Sales":[
        1200,2500,1800,
        3000,2700,1600,
        3500,2200,1900,
        4100,2800,2100,
        3900,2600,1700
    ],
    "Profit":[
        250,500,320,
        700,550,300,
        850,420,350,
        900,600,400,
        820,520,310
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

print(df.shape)
print(df.columns)
print(df.dtypes)

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Day"] = df["Order_Date"].dt.day
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Weekday"] = df["Order_Date"].dt.day_name()

print(df[["Order_Date", "Year", "Month", "Day", "Month_Name", "Weekday"]])

df["Delivery_Days"] = (
    df["Delivery_Date"]-df["Order_Date"]
).dt.days
print(df[["Order_ID","Delivery_Days"]])
print(df["Delivery_Days"].mean())
print(df["Delivery_Days"].max())
print(df["Delivery_Days"].min())

print(df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum())
print(df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].mean())
print(df.groupby(df["Order_Date"].dt.to_period("M"))["Profit"].sum())

print(pd.pivot_table(df, values="Sales", index=df["Order_Date"].dt.to_period("M"), columns="Department", aggfunc="mean"))

print(df.groupby("Department")["Sales"].sum())
print(df.groupby("Department")["Sales"].mean())
print(df.groupby("Department")["Sales"].max())
print(df.groupby("Department")["Order_ID"].count())

print(df.loc[df["Sales"].idxmax()])
print(df.loc[df["Profit"].idxmax()])
monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()
print(monthly_sales.idxmax(), ":", monthly_sales.max())
dept_avg = df.groupby("Department")["Sales"].mean()
print(dept_avg.idxmax(), ":", dept_avg.max())
print(df[df["Delivery_Days"]>5])

df["Delivery_Status"] = np.where(
    df["Delivery_Days"]<=2,
    "Fast",
    np.where(
        df["Delivery_Days"]<=5,
        "Normal",
        "Delayed"
    )
)
print(df[[
    "Order_ID",
    "Delivery_Days",
    "Delivery_Status"
]])
print(
    pd.crosstab(
        df["Department"],
        df["Delivery_Status"]
    )
)
