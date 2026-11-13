# # Practice
# # Q1 — RFM Scores. Create: R_Score, F_Score, M_Score using 1–5 scoring.
# # Q2 — Overall RFM Score: Create: RFM_Score Then find the customer with the highest score.
# # Q3 — Segment Customers Create:Loyal Customer High Value, At Risk, Potential Churn, Regular using np.select().
# # Q4 — Segment Summary Use: groupby("Segment") Calculate: Customer Count, Total Sales, Average Sales, Total Profit, Average RFM Score
# # Q5 — Segment Ranking Rank segments by: Total Sales and identify which segments contribute the most revenue.
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

reference_date = df["Order_Date"].max()

rfm = df.groupby("Customer").agg(
    Recency=("Order_Date", lambda x: (reference_date - x.max()).days),
    Frequency=("Order_ID", "count"),
    Monetary=("Sales", "sum")
).reset_index()

rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    q=5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    q=5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    q=5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"] +
    rfm["F_Score"] +
    rfm["M_Score"]
)


# Highest RFM customer
highest_rfm_customer = rfm.loc[
    rfm["RFM_Score"].idxmax()
]

print("Highest RFM Customer:")
print(highest_rfm_customer)

conditions = [
    (rfm["R_Score"] >= 4) & (rfm["F_Score"] >= 4),
    (rfm["M_Score"] >= 4) & (rfm["R_Score"] >= 3),
    (rfm["R_Score"] <= 2) & (rfm["F_Score"] >= 2),
    (rfm["R_Score"] <= 2) & (rfm["F_Score"] <= 2),
    (rfm["RFM_Score"].between(6, 11))
]

choices = [
    "Loyal Customers",
    "High Value",
    "At Risk",
    "Potential Churn",
    "Regular"
]

rfm["Segment"] = np.select(
    conditions,
    choices,
    default="Regular"
)

segment_summary = (
    rfm.groupby("Segment")
       .agg(
           Customer_Count=("Customer", "count"),
           Total_Sales=("Monetary", "sum"),
           Average_Sales=("Monetary", "mean"),
           Average_RFM_Score=("RFM_Score", "mean")
       )
       .reset_index()
)

print("\nSegment Summary:")
print(segment_summary)

segment_ranking = (
    segment_summary
    .sort_values("Total_Sales", ascending=False)
    .reset_index(drop=True)
)

segment_ranking["Sales_Rank"] = (
    segment_ranking["Total_Sales"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

print("\nSegment Ranking:")
print(segment_ranking)
