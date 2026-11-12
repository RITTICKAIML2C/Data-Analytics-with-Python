# # Practice
# # Q1 — Recency Calculate each customer's: Latest Order Date → Recency
# # Q2 — Frequency Calculate each customer's: Number of Orders Sort customers from highest to lowest frequency.
# # Q3 — Monetary Calculate: Total Sales per Customer Then find the customer with the highest monetary value.
# # Q4 — Build RFM Table Create one DataFrame containing: Customer Recency, Frequency, Monetary
# # Q5 — RFM Ranking Create: Recency_Rank Frequency_Rank, Monetary_Rank Remember: Lower Recency is better → ascending rank, Higher Frequency is better → descending rank, Higher Monetary is better → descending rank
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

reference_date = df["Order_Date"].max() + pd.Timedelta(days=1)
recency = df.groupby("Customer")["Order_Date"].max()
recency = (reference_date - recency).dt.days
print(recency)

frequency = df.groupby("Customer")["Order_ID"].count()
frequency = frequency.sort_values(ascending=False)
print(frequency)

monetary = df.groupby("Customer")["Sales"].sum()
print(monetary)

rfm = pd.DataFrame({
    "Recency": recency,
    "Frequency": frequency,
    "Monetary": monetary
})
print(rfm)

rfm["Recency_Rank"] = rfm["Recency"].rank(
    ascending=True,
    method="min"
)
rfm["Frequency_Rank"] = rfm["Frequency"].rank(
    ascending=False,
    method="min"
)
rfm["Monetary_Rank"] = rfm["Monetary"].rank(
    ascending=False,
    method="min"
)
print(rfm)
