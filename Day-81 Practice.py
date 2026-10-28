# # Practice
# # Q1 Find the: 25th percentile, 50th percentile, 75th percentile, 90th percentile of Sales.
# # Q2 Create a Sales_Band using: 0–50,000 → Low, 50,001–100,000 → Medium, 100,001–200,000 → High, 200,001+ → Very High
# # Q3 Count customers in each Sales Band. 
# # Q4 Calculate the percentage distribution of Sales Bands.
# # Q5 Create a Sales_Quartile using pd.qcut() with 4 groups.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
Q1 = df["Sales"].quantile(0.25)
Q2 = df["Sales"].quantile(0.50)
Q3 = df["Sales"].quantile(0.75)
Q90 = df["Sales"].quantile(0.90)
print("25th Percentile:", Q1)
print("50th Percentile:", Q2)
print("75th Percentile:", Q3)
print("90th Percentile:", Q90)

bins = [0, 50000, 100000, 200000, float("inf")]
labels = [
    "Low",
    "Medium",
    "High",
    "Very High"
]
df["Sales_Band"] = pd.cut(
    df["Sales"],
    bins=bins,
    labels=labels,
    include_lowest=True
)
print(df[["Customer", "Sales", "Sales_Band"]])

band_counts = df["Sales_Band"].value_counts().sort_index()
print(band_counts)

band_percentage = (
    df["Sales_Band"]
    .value_counts(normalize=True)
    .sort_index() * 100
)
print(band_percentage)

df["Sales_Quartile"] = pd.qcut(
    df["Sales"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)
print(df[["Customer", "Sales", "Sales_Quartile"]])
