# 1. Key Concepts 

# A. Time-Series Data
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%b")

# B. Monthly Sales
monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
) 

# C. Month-over-Month Growth
monthly["MoM_Growth_%"] = (
    monthly["Sales"].pct_change() * 100
)

# D. Cumulative Sales 
monthly["Cumulative_Sales"] = (
    monthly["Sales"].cumsum()
)

# E. Rolling Average
monthly["Rolling_3M_Avg"] = (
    monthly["Sales"].rolling(3).mean()
)
