# 1. Concepts
# a. Conditional Columns
df["High_Value"] = df["Sales"] > 100000

# b. Multiple Conditions
import numpy as np
df["Customer_Type"] = np.select(
    [
        df["Sales"] >= 100000,
        df["Sales"] >= 60000
    ],
    [
        "High Value",
        "Medium Value"
    ],
    default="Low Value"
)

# c. Conditional Counting 
high_value_count = df["High_Value"].sum()

# d. Conditional Aggregation by Group
category_kpi = df.groupby("Category").agg(
    Total_sales=("Sales", "sum"),
    Avg_Sales=("Sales", "mean"),
    Customer_Count=("Customer", "count"),
    High_Value_Customers=("High_Value", "sum")
)

Day-84 Conditional Aggregation & Business FlagsConditional Aggregation & Business Flags.py
