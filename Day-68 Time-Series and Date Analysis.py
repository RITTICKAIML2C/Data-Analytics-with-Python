# 1. Datetime Basics 
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Day"] = df["Order_Date"].dt.day
df["Day_Name"] = df["Order_Date"].dt.day_name()

# 2. Monthly Analysis 
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
      .sum()
)

# 3. Monthly Growth 
monthly_sales.pct_change() * 100

# 4. Rolling Average - smooths short term fluctuations 
monthly_sales.rolling(3).mean()

# 5. resample()
df = df.set_index("Order_Date")
df["Sales"].resample("ME").sum()

