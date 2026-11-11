import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Order_ID": range(1001, 1013),
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya","Riya",
        "Karan","Amit","Priya","Rahul","Riya","Neha"
    ],
    "Order_Date": [
        "2026-01-05","2026-01-15","2026-01-20","2026-02-10",
        "2026-02-18","2026-02-25","2026-03-05","2026-03-15",
        "2026-03-20","2026-03-25","2026-04-10","2026-04-15"
    ],
    "Sales": [
        50000,40000,35000,60000,55000,45000,
        30000,70000,65000,50000,55000,25000
    ]
})

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# # 1. Recency
analysis_date = pd.Timestamp("2026-05-01")
recency = (
    analysis_date -
    df.groupby("Customer")["Order_Date"].max()
).dt.days

# # 2. Frequency 
frequency = (
    df.groupby("Customer")["Order_ID"]
      .nunique()
)

# # 3. Monetary
monetary = (
    df.groupby("Customer")["Sales"]
      .sum()
)

