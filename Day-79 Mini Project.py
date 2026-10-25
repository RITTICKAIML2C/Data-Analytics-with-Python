# # 💼 Mini Project — Sales Outlier Analysis
# # Detect Sales outliers using IQR. Create an Outlier flag.
# # Compare : Average Sales with outlier, Average Sales without outlier, Total Sales with outlier, Total Sales without outlier, Calculate Profit Margin, Determine whether the outlier should be removed or retained, Write 3 business insights
import pandas as pd
df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales": [50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit": [10000,12000,11000,13000,14000,10500,60000,11500]
})
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Outlier"] = (df["Sales"] < lower) | (df["Sales"] > upper)
print(df)

avg_with = df["Sales"].mean()
avg_without = df[df["Outlier"] == False]["Sales"].mean()
print("Average with outlier:", avg_with)
print("Average without outlier:", avg_without)

total_with = df["Sales"].sum()
total_without = df[df["Outlier"] == False]["Sales"].sum()
print("Total with outlier:", total_with)
print("Total without outlier:", total_without)

df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
print(df[["Customer", "Sales", "Profit", "Profit Margin"]])

# 5. I would retain Vikram's record.

# 6. Insight 1: Vikram has exceptionally high Sales of ₹300,000. Insight 2: The outlier significantly increases average Sales from ₹44,285.71 to ₹76,250, Insight 3:Vikram's 20% Profit Margin is not obviously abnormal

