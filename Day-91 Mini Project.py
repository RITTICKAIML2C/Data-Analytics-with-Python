# # Mini Project — Customer RFM Segmentation
# # Create a complete RFM analysis.
# # Part A — RFM Table Build: Customer, Recency, Frequency, Monetary, Recency_Rank, Frequency_Rank, Monetary_Rank
# # Part B — Customer Segmentation. Create a simple segment using np.select(): High Value, Medium Value, Low Value. Use Frequency + Monetary to determine the segment. For example: High Value → high frequency AND high monetary, Medium Value → moderate values, Low Value → lower values
# # Part C — Business Analysis. Find Most recent customer, Most frequent customer, Highest-spending customer, High-value customer count, Average Monetary value, Customer with the highest overall RFM strength
# # Part D — 5 Business Insights. Write 5 concise insights explaining what the RFM analysis tells the business.
import pandas as pd
import numpy as np
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

reference_date = df["Order_Date"].max() + pd.Timedelta(days=1)

recency = (
    reference_date - df.groupby("Customer")["Order_Date"].max()
).dt.days

frequency = (
    df.groupby("Customer")["Order_ID"]
    .count()
)

monetary = (
    df.groupby("Customer")["Sales"]
    .sum()
)

rfm = pd.DataFrame({
    "Recency": recency,
    "Frequency": frequency,
    "Monetary": monetary
})

# Rankings
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

frequency_median = rfm["Frequency"].median()
monetary_median = rfm["Monetary"].median()

conditions = [
    (rfm["Frequency"] >= frequency_median) &
    (rfm["Monetary"] >= monetary_median),

    (rfm["Frequency"] >= frequency_median) |
    (rfm["Monetary"] >= monetary_median)
]

choices = [
    "High Value",
    "Medium Value"
]

rfm["Segment"] = np.select(
    conditions,
    choices,
    default="Low Value"
)

rfm["RFM_Strength"] = (
    (rfm["Recency_Rank"].max() + 1 - rfm["Recency_Rank"]) +
    (rfm["Frequency_Rank"].max() + 1 - rfm["Frequency_Rank"]) +
    (rfm["Monetary_Rank"].max() + 1 - rfm["Monetary_Rank"])
)

most_recent_customer = rfm["Recency"].idxmin()

most_frequent_customers = rfm[
    rfm["Frequency"] == rfm["Frequency"].max()
].index.tolist()

highest_spending_customer = rfm["Monetary"].idxmax()

high_value_count = (
    rfm["Segment"] == "High Value"
).sum()

average_monetary = rfm["Monetary"].mean()

highest_rfm_customer = rfm["RFM_Strength"].idxmax()


print("\nRFM TABLE")
print(rfm)

print("\nBUSINESS ANALYSIS")

print("Most recent customer:", most_recent_customer)

print(
    "Most frequent customer(s):",
    most_frequent_customers
)

print(
    "Highest-spending customer:",
    highest_spending_customer
)

print(
    "High-value customer count:",
    high_value_count
)

print(
    "Average Monetary value:",
    average_monetary
)

print(
    "Highest overall RFM strength:",
    highest_rfm_customer
)
