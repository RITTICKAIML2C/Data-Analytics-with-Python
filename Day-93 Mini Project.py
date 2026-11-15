# # 3️⃣ Mini Project — Customer Retention Cohort Analysis
# # Build a complete Cohort Retention Dashboard.#
# # Part A — Customer-Level Table Create: Customer First_Purchase, Cohort_Month, Purchase_Month, Cohort_Index, Sales
# # Part B — Retention Analysis Create: Cohort_Month,, Cohort_Index, Customer_Count, Retention_%
# # Part C — Business Analysis Find: Largest customer cohort, Highest Month-1 retention, Highest Month-2 retention, Highest-revenue cohort, Overall average retention after Month 0
# # Part D — Business Insights Write 5 concise insights, for example: "The January cohort started with X customers and retained X% in Month 1."
import pandas as pd

df = pd.DataFrame({
    "Customer": [
        "Amit","Riya","Rahul","Amit","Priya",
        "Riya","Karan","Amit","Priya","Rahul",
        "Riya","Neha"
    ],
    "Order_Date": [
        "2026-01-05","2026-01-15","2026-01-20","2026-02-10",
        "2026-02-18","2026-02-25","2026-03-05","2026-03-15",
        "2026-03-20","2026-03-25","2026-04-10","2026-04-15"
    ],
    "Sales": [
        50000,40000,35000,60000,55000,
        45000,30000,70000,65000,50000,
        55000,25000
    ]
})

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["First_Purchase"] = df.groupby("Customer")["Order_Date"].transform("min")

df["Cohort_Month"] = df["First_Purchase"].dt.to_period("M")
df["Purchase_Month"] = df["Order_Date"].dt.to_period("M")

df["Cohort_Index"] = (
    (df["Purchase_Month"].dt.year - df["Cohort_Month"].dt.year) * 12
    + (df["Purchase_Month"].dt.month - df["Cohort_Month"].dt.month)
)

customer_table = df[
    [
        "Customer",
        "First_Purchase",
        "Cohort_Month",
        "Purchase_Month",
        "Cohort_Index",
        "Sales"
    ]
]
print(customer_table)

cohort_analysis = (
    df.groupby(["Cohort_Month", "Cohort_Index"])["Customer"]
      .nunique()
      .reset_index(name="Customer_Count")
)

cohort_analysis["Retention_%"] = (
    cohort_analysis.groupby("Cohort_Month")["Customer_Count"]
    .transform(lambda x: x / x.iloc[0] * 100)
)

print(cohort_analysis)

largest_cohort = (
    cohort_analysis[cohort_analysis["Cohort_Index"] == 0]
    .loc[lambda x: x["Customer_Count"].idxmax()]
)

print(largest_cohort)

month_1 = cohort_analysis[
    cohort_analysis["Cohort_Index"] == 1
]

highest_month_1 = month_1.loc[
    month_1["Retention_%"].idxmax()
]

print(highest_month_1)

month_2 = cohort_analysis[
    cohort_analysis["Cohort_Index"] == 2
]

highest_month_2 = month_2.loc[
    month_2["Retention_%"].idxmax()
]

print(highest_month_2)

revenue_by_cohort = (
    df.groupby("Cohort_Month")["Sales"]
      .sum()
      .reset_index(name="Total_Revenue")
)

highest_revenue_cohort = revenue_by_cohort.loc[
    revenue_by_cohort["Total_Revenue"].idxmax()
]

print(highest_revenue_cohort)

post_month_0 = cohort_analysis[
    cohort_analysis["Cohort_Index"] > 0
]

overall_avg_retention = post_month_0["Retention_%"].mean()

print(round(overall_avg_retention, 2))

# 1. January 2026 was the largest cohort, starting with 3 customers.

# 2. The January cohort retained 66.67% of customers in Month 1, with 2 of its original 3 customers making another purchase.

# 3. February 2026 recorded 100% Month-1 retention, as its single customer made another purchase in the following month.

# 4. January 2026 generated the highest total revenue at ₹405,000, substantially more than the other cohorts in this dataset.

# 5. Average retention after Month 0 was 66.67%, based on the available Month-1, Month-2, and Month-3 cohort observations.

