# # Practice
# # Q1 — Customer Cohort. Create: First_Purchase, Cohort_Month, Purchase_Month
# # Q2 — Cohort Index Create: Cohort_Index Find the month number for every purchase.
# # Q3 — Cohort Customer Count Calculate the number of unique customers in each: Cohort_Month + Cohort_Index. 
# # Q4 — Retention Matrix. Create a pivot table: Rows → Cohort_Month, Columns → Cohort_Index, Values → unique customers. Then convert it into retention percentages, where Month 0 = 100%.
# # Q5 — Cohort Revenue Calculate: Total Sales by Cohort, Sales by Cohort Month + Cohort Index, Identify the cohort/month combination with the highest sales.

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

cohort_count = (
    df.groupby(["Cohort_Month", "Cohort_Index"])["Customer"]
      .nunique()
      .reset_index(name="Unique_Customers")
)

retention = cohort_count.pivot(
    index="Cohort_Month",
    columns="Cohort_Index",
    values="Unique_Customers"
)

retention_percentage = retention.div(
    retention[0],
    axis=0
) * 100

total_sales_by_cohort = (
    df.groupby("Cohort_Month")["Sales"]
      .sum()
      .reset_index(name="Total_Sales")
)

cohort_revenue = (
    df.groupby(["Cohort_Month", "Cohort_Index"])["Sales"]
      .sum()
      .reset_index(name="Total_Sales")
)

highest_sales = cohort_revenue.loc[
    cohort_revenue["Total_Sales"].idxmax()
]
print(df)
print(cohort_count)
print(retention_percentage.round(2))
print(total_sales_by_cohort)
print(cohort_revenue)
print(highest_sales)
