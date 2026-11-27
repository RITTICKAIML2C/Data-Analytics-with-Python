# # Part A — Statistical Summary. Create a statistical summary containing: Mean, Median, Std, Variance, Min, Max, 25th Percentile, 50th Percentile, 75th Percentile, Sales, Profit, Orders
# # Part B — Distribution Analysis. For each variable determine: Mean, Median, Difference between mean and median. Whether the data appears skewed. Then identify which variable appears to have the strongest skew.
# # Part C — Customer Segmentation Using Percentiles. Create: Sales_Percentile using: Then classify customers: Top 25%, Middle 50%, Bottom 25%
# # Part D — Variability Analysis. Calculate the coefficient of variation for: Sales, Profit, Orders. Determine: Which variable is most variable?, Which is most consistent?
# # Part E — Outlier Investigation Then investigate: Customer, Sales, Profit, Orders, Profit Margin %
# # Part F — 💼 Business Insights. Write 5–7 insights. Your insights should connect statistics to business decisions. For example: Finding: Customer sales are positively skewed, Evidence: The mean is substantially higher than the median because of a small number of high-value customers, Business implication: Customer-level reporting should include median revenue alongside mean revenue to avoid overstating typical customer value.
# # ⭐ Bonus Challenge — Mean vs Median Business Decision. Answer: Scenario: A company reports: Average Customer Revenue = ₹70,000, Median Customer Revenue = ₹52,000. The management team says: "Our typical customer generates ₹70,000." Would you agree?. Explain why median may be a better representation of the typical customer in this situation.
import numpy as np 
import pandas as pd 
df = pd.DataFrame({
    "Customer": [
        "A","B","C","D","E","F","G","H",
        "I","J","K","L","M","N","O"
    ],
    "Sales": [
        42000,48000,51000,55000,60000,
        63000,47000,52000,68000,72000,
        49000,58000,65000,150000,46000
    ],
    "Profit": [
        8400,9600,10200,11000,12000,
        12600,9400,10400,13600,14400,
        9800,11600,13000,30000,9200
    ],
    "Orders": [
        4,5,5,6,6,
        7,4,5,7,8,
        5,6,7,15,4
    ]
})
summary = df[["Sales", "Profit", "Orders"]].agg([
    "mean", "median", "std", "var", "min", "max"
]).T

summary["25th Percentile"] = df[["Sales", "Profit", "Orders"]].quantile(0.25)
summary["50th Percentile"] = df[["Sales", "Profit", "Orders"]].quantile(0.50)
summary["75th Percentile"] = df[["Sales", "Profit", "Orders"]].quantile(0.75)

print(summary.round(2))

for col in ["Sales", "Profit", "Orders"]:
    mean = df[col].mean()
    median = df[col].median()
    difference = mean - median
    skew = "Positively Skewed" if mean > median else "Negatively Skewed" if mean < median else "Approximately Symmetric"

    print(f"{col}: Mean={mean:.2f}, Median={median:.2f}, Difference={difference:.2f}, {skew}")

df["Sales_Percentile"] = df["Sales"].rank(pct=True) * 100

conditions = [
    df["Sales_Percentile"] >= 75,
    df["Sales_Percentile"] >= 25
]

choices = ["Top 25%", "Middle 50%"]

df["Customer_Segment"] = np.select(
    conditions,
    choices,
    default="Bottom 25%"
)

print(df[["Customer", "Sales", "Sales_Percentile", "Customer_Segment"]])

cv = df[["Sales", "Profit", "Orders"]].std() / df[["Sales", "Profit", "Orders"]].mean() * 100

print("Coefficient of Variation (%):")
print(cv.round(2))

print("\nMost Variable:", cv.idxmax())
print("Most Consistent:", cv.idxmin())

df["Profit_Margin_%"] = df["Profit"] / df["Sales"] * 100

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Upper Outlier Limit:", upper_limit)

outliers = df[df["Sales"] > upper_limit]

print("\nSales Outliers:")
print(
    outliers[
        ["Customer", "Sales", "Profit", "Orders", "Profit_Margin_%"]
    ].round(2)
)

print("""
1. Finding: Customer sales are positively skewed.
   Evidence: A small number of high-value customers push the mean above the median.
   Business implication: Use median alongside mean when reporting typical customer spending.

2. Finding: Customer N is a major sales outlier.
   Evidence: Its Sales value is far above the IQR-based upper limit.
   Business implication: Investigate and retain high-value customers like N.

3. Finding: Sales show greater variability than Orders.
   Evidence: Sales has a higher coefficient of variation.
   Business implication: Customer spending differs more substantially than order frequency.

4. Finding: High-value customers contribute disproportionately to revenue.
   Evidence: Top-percentile customers have substantially higher Sales.
   Business implication: VIP retention and personalized offers can protect revenue.

5. Finding: Profit generally follows Sales.
   Evidence: High-sales customers also generate high absolute Profit.
   Business implication: Increasing high-value customer activity can improve total profitability.

6. Finding: Outlier customers need separate analysis.
   Evidence: Extreme Sales values can distort mean-based summaries.
   Business implication: Segment high-value customers separately for better business decisions.
""")

print("""
No, I would not agree.

Mean Revenue = ₹70,000
Median Revenue = ₹52,000

The median is a better representation of the typical customer because
a few very high-value customers may pull the mean upward.

Therefore, the typical customer is closer to ₹52,000 than ₹70,000.
""")
