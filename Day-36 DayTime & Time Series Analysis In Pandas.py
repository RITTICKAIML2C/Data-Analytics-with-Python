# # 1. Converting to DateTime 
import pandas as pd
df = pd.DataFrame({
    "Order_Date" : [
        "2026-08-01",
        "2026-08-02",
        "2026-08-03"
    ]
})
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df)
print(df.dtypes)

# # 2. Extract Date Components
# # a. Year
df["Year"] = df["Order_Date"].dt.year

# # b. Month
df["Month"] = df["Order_Date"].dt.month

# # c. Day
df["Day"] = df["Order_Date"].dt.day

# # d. Weekday Name
df["Weekday"] = df["Order_Date"].dt.day_name()

# # e. Month Name
df["Month_Name"] = df["Order_Date"].dt.month_name()

# # 4. Filtering Dates 
# # a. Orders after August 10:
df[df["Order_date"] > "2026-08-10"]

# # b. Orders between two dates:
df[
    (df["Order_Date"] >= "2026-08-01") &
    (df["Order_Date"] <= "2026-08-15")
]

# # 5. Sorting Dates
df.sort_values("Order_Date")

# # a. Newest First 
df.sort_values("Order_Date", ascending=False)

# # 6. Data Difference
df["Delivery_Days"] = (
    df["Delivery_Date"] - 
    df["Order_Date"]
).dt.days

# # 7. Current Date 
today = pd.Timestamp.today()

# # Difference from today:
df["Days_Ago"] = (
    today - 
    df["Order_Date"]
).dt.days

# # 8. Group by Month 
df.groupby(
    df["Order_date"].dt.month
)["Sales"].sum()

# # 9. Group by Year
df.groupby(
    df["Order_Date"].dt.year
)["Sales"].sum()

# # 10. Monthly Pivot Table 
pd.pivot_table(
    df,
    values="Sales",
    index=df["Order_Date"].dt.month_name(),
    aggfunc="sum"
)

