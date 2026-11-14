# # 🏆 Mini Project — Customer Segmentation Dashboard
# # Build a complete dashboard containing:
# # Part A — Customer Table Customer Recency Frequency Monetary R_Score F_Score M_Score RFM_Score Segment
# # Part B — Segment KPIs Create: SegmentCustomer_Count Total_Sales Average_Sales Total_Profit Average_RFM_Score
# # Part C — Business Analysis Find: Highest RFM-score customer Largest customer segment, Highest-revenue segment, Highest-profit segment, Average RFM score, Percentage of customers in each segment
# # Part D — Business Insights Write 5 concise insights. For example: "The Loyal Customer segment contains X customers and generates ₹X in sales."
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
reference_date = df["Order_Date"].max()

rfm = df.groupby("Customer").agg(
    Recency=(
        "Order_Date",
        lambda x: (reference_date - x.max()).days
    ),

    Frequency=(
        "Order_ID",
        "count"
    ),

    Monetary=(
        "Sales",
        "sum"
    )
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
    rfm["R_Score"]
    + rfm["F_Score"]
    + rfm["M_Score"]
)
conditions = [

    # Loyal Customers
    (rfm["R_Score"] >= 4) &
    (rfm["F_Score"] >= 4),

    # High Value
    (rfm["M_Score"] >= 4) &
    (rfm["R_Score"] >= 3),

    # At Risk
    (rfm["R_Score"] <= 2) &
    (rfm["F_Score"] >= 2),

    # Potential Churn
    (rfm["R_Score"] <= 2) &
    (rfm["F_Score"] <= 2),

    # Regular
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
customer_profit = (
    df.groupby("Customer")["Profit"]
      .sum()
      .reset_index(name="Total_Profit")
)


rfm = rfm.merge(
    customer_profit,
    on="Customer",
    how="left"
)

customer_table = rfm[
    [
        "Customer",
        "Recency",
        "Frequency",
        "Monetary",
        "R_Score",
        "F_Score",
        "M_Score",
        "RFM_Score",
        "Segment"
    ]
]


print("\n")
print("=" * 80)
print("PART A — CUSTOMER RFM TABLE")
print("=" * 80)

print(customer_table.to_string(index=False))

segment_kpis = (
    rfm.groupby("Segment")
       .agg(
           Customer_Count=("Customer", "count"),
           Total_Sales=("Monetary", "sum"),
           Average_Sales=("Monetary", "mean"),
           Total_Profit=("Total_Profit", "sum"),
           Average_RFM_Score=("RFM_Score", "mean")
       )
       .reset_index()
)

segment_kpis["Customer_Percentage"] = (
    segment_kpis["Customer_Count"]
    / len(rfm)
    * 100
)


print("\n")
print("=" * 80)
print("PART B — SEGMENT KPIs")
print("=" * 80)

print(
    segment_kpis.to_string(
        index=False,
        formatters={
            "Average_Sales": "{:,.2f}".format,
            "Total_Sales": "{:,.0f}".format,
            "Total_Profit": "{:,.0f}".format,
            "Average_RFM_Score": "{:.2f}".format,
            "Customer_Percentage": "{:.2f}%".format
        }
    )
)

highest_rfm_customer = rfm.loc[
    rfm["RFM_Score"].idxmax()
]
largest_segment = segment_kpis.loc[
    segment_kpis["Customer_Count"].idxmax()
]
highest_revenue_segment = segment_kpis.loc[
    segment_kpis["Total_Sales"].idxmax()
]

highest_profit_segment = segment_kpis.loc[
    segment_kpis["Total_Profit"].idxmax()
]

average_rfm_score = rfm["RFM_Score"].mean()

customer_percentage = segment_kpis[
    [
        "Segment",
        "Customer_Count",
        "Customer_Percentage"
    ]
]


print("\n")
print("=" * 80)
print("PART C — BUSINESS ANALYSIS")
print("=" * 80)


print(
    f"\nHighest RFM-score customer: "
    f"{highest_rfm_customer['Customer']}"
)

print(
    f"RFM Score: "
    f"{highest_rfm_customer['RFM_Score']}"
)


print(
    f"\nLargest customer segment: "
    f"{largest_segment['Segment']}"
)

print(
    f"Customers: "
    f"{largest_segment['Customer_Count']}"
)


print(
    f"\nHighest-revenue segment: "
    f"{highest_revenue_segment['Segment']}"
)

print(
    f"Total Sales: "
    f"₹{highest_revenue_segment['Total_Sales']:,.0f}"
)


print(
    f"\nHighest-profit segment: "
    f"{highest_profit_segment['Segment']}"
)

print(
    f"Total Profit: "
    f"₹{highest_profit_segment['Total_Profit']:,.0f}"
)


print(
    f"\nAverage RFM Score: "
    f"{average_rfm_score:.2f}"
)


print("\nCustomer Percentage by Segment:")

print(
    customer_percentage.to_string(
        index=False,
        formatters={
            "Customer_Percentage": "{:.2f}%".format
        }
    )
)
segment_ranking = (
    segment_kpis
    .sort_values(
        "Total_Sales",
        ascending=False
    )
    .reset_index(drop=True)
)


segment_ranking["Sales_Rank"] = (
    segment_ranking["Total_Sales"]
    .rank(
        method="dense",
        ascending=False
    )
    .astype(int)
)


print("\n")
print("=" * 80)
print("Q5 — SEGMENT RANKING BY TOTAL SALES")
print("=" * 80)


print(
    segment_ranking[
        [
            "Sales_Rank",
            "Segment",
            "Customer_Count",
            "Total_Sales",
            "Average_Sales"
        ]
    ].to_string(
        index=False,
        formatters={
            "Total_Sales": "₹{:,.0f}".format,
            "Average_Sales": "₹{:,.2f}".format
        }
    )
)
print("\n")
print("=" * 80)
print("PART D — BUSINESS INSIGHTS")
print("=" * 80)


loyal = segment_kpis[
    segment_kpis["Segment"] == "Loyal Customers"
]


if len(loyal) > 0:

    print(
        f"\n1. The Loyal Customers segment contains "
        f"{loyal['Customer_Count'].iloc[0]} customers "
        f"and generates ₹"
        f"{loyal['Total_Sales'].iloc[0]:,.0f} "
        f"in sales."
    )

else:

    print(
        "\n1. There are currently no customers in "
        "the Loyal Customers segment."
    )

print(
    f"\n2. The {highest_revenue_segment['Segment']} segment "
    f"generates the highest revenue, with total sales "
    f"of ₹{highest_revenue_segment['Total_Sales']:,.0f}."
)

print(
    f"\n3. The largest customer segment is "
    f"{largest_segment['Segment']}, containing "
    f"{largest_segment['Customer_Count']} customers "
    f"({largest_segment['Customer_Percentage']:.2f}% "
    f"of the customer base)."
)

print(
    f"\n4. The average RFM score across all customers "
    f"is {average_rfm_score:.2f}."
)

print(
    f"\n5. The {highest_profit_segment['Segment']} segment "
    f"generates the highest total profit of "
    f"₹{highest_profit_segment['Total_Profit']:,.0f}."
)

