# # 💼 Mini Project — Customer Sales Segmentation
# # Using the same dataset:
# # Create Sales_Band.
# # Create Sales_Quartile. Count customers in each band. Calculate percentage distribution. Find the highest-sales customer in each Sales Band. Calculate average Profit by Sales_Band. Print 3 business insights.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
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

df["Sales_Quartile"] = pd.qcut(
    df["Sales"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)
print(df[["Customer", "Sales", "Sales_Quartile"]])

band_count = (
    df["Sales_Band"]
    .value_counts()
    .sort_index()
)
print(band_count)

band_percentage = (
    df["Sales_Band"]
    .value_counts(normalize=True)
    .sort_index() * 100
)
print(band_percentage)

highest_customer = (
    df.loc[
        df.groupby("Sales_Band", observed=True)["Sales"].idxmax(),
        ["Sales_Band", "Customer", "Sales"]
    ]
    .sort_values("Sales_Band")
)
print(highest_customer)

avg_profit = (
    df.groupby("Sales_Band", observed=True)["Profit"]
    .mean()
    .sort_index()
)
print(avg_profit)

# 1. The Medium Sales Band contains most customers, indicating that the majority of customers generate moderate sales.
# 2. Vikram is the only Very High Sales customer, with ₹300,000 in sales and ₹60,000 profit.
# 3. Average Profit increases substantially for the Very High Sales Band, showing that the highest-sales segment contributes significantly more profit per customer.
