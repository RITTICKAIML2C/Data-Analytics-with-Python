# 1️. Multiple aggregations
df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Sales=("Sales", "mean"),
    Total_Profit=("Profit", "sum"),
    Orders=("Sales", "count")
)

# 2️. Named aggregation - This is the clean, industry-friendly approach:
summary = df.groupby("Customer").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Avg_Order=("Sales", "mean")
)

# 3️. Add calculated KPIs
summary["Profit_Margin"] = (
    summary["Total_Profit"] / summary["Total_Sales"] * 100
)
