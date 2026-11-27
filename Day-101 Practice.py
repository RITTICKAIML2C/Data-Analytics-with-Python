# # 🟢 Q1 — Descriptive Statistics. Calculate for Sales: Mean, Median, Minimum, Maximum, Standard deviation, Variance
# # 🟢 Q2 — Percentile Analysis. Calculate: 10th percentile, 25th percentile, 50th percentile, 75th percentile, 90th percentile. Then explain what the 25th, 50th and 75th percentiles mean.
# # 🟡 Q3 — Distribution Comparison. Calculate mean and median for: Sales, Profit, Orders. Then determine whether each variable appears: Approximately symmetric, Positively skewed, Negatively skewed. You don't need a formal skewness test yet—use the relationship between mean and median as your first indicator.
# # 🟡 Q4 — Variability. Calculate: Sales Standard Deviation, Sales Variance, Sales CV %. Then determine whether customer sales are relatively consistent or highly variable.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Customer": [
        "A","B","C","D","E",
        "F","G","H","I","J"
    ],
    "Sales": [
        45000,52000,48000,61000,55000,
        72000,50000,49000,95000,47000
    ],
    "Profit": [
        9000,10400,9600,12200,11000,
        14400,10000,9800,19000,9400
    ],
    "Orders": [
        5,6,5,7,6,
        8,5,5,10,5
    ]
})
print("Mean:", df["Sales"].mean())
print("Median:", df["Sales"].median())
print("Minimum:", df["Sales"].min())
print("Maximum:", df["Sales"].max())
print("Standard Deviation:", df["Sales"].std())
print("Variance:", df["Sales"].var())

print("10th Percentile:", df["Sales"].quantile(0.10))
print("25th Percentile:", df["Sales"].quantile(0.25))
print("50th Percentile:", df["Sales"].quantile(0.50))
print("75th Percentile:", df["Sales"].quantile(0.75))
print("90th Percentile:", df["Sales"].quantile(0.90))

for col in ["Sales", "Profit", "Orders"]:
    mean = df[col].mean()
    median = df[col].median()

    if abs(mean - median) < 0.05 * median:
        shape = "Approximately Symmetric"
    elif mean > median:
        shape = "Positively Skewed"
    else:
        shape = "Negatively Skewed"

    print(f"{col}: Mean={mean:.2f}, Median={median:.2f}, {shape}")


sales_std = df["Sales"].std()
sales_variance = df["Sales"].var()
sales_cv = sales_std / df["Sales"].mean() * 100

print("Sales Standard Deviation:", round(sales_std, 2))
print("Sales Variance:", round(sales_variance, 2))
print("Sales CV %:", round(sales_cv, 2), "%")

print(
    "Sales are:",
    "Highly Variable" if sales_cv > 30 else "Relatively Consistent"
)

