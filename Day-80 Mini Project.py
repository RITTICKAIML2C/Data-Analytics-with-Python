# # 💼 Mini Project — Sales Distribution Analyzer
# # Create a small analysis that: Displays Sales.describe(). Calculates mean, median and standard deviation. Calculates Q1 and Q3. Calculates skewness.
# # Calculates coefficient of variation. Finds the customer with maximum Sales. Prints 3 business insights from your results.
import pandas as pd
df = pd.DataFrame({
    "Customer":["Amit","Riya","Rahul","Priya","Karan","Neha","Vikram","Anu"],
    "Sales":[50000,60000,55000,65000,70000,52000,300000,58000],
    "Profit":[10000,12000,11000,13000,14000,10500,60000,11500]
})
print("=== Sales Descriptive Statistics ===")
print(df["Sales"].describe())

mean_sales = df["Sales"].mean()
median_sales = df["Sales"].median()
std_sales = df["Sales"].std()
print("Mean:", mean_sales)
print("Median:", median_sales)
print("Standard Deviation:", std_sales)

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
print("Q1:", Q1)
print("Q3:", Q3)

skewness = df["Sales"].skew()
print("Skewness:", skewness)

CV = (std_sales / mean_sales) * 100
print("CV:", CV, "%")

max_customer = df.loc[df["Sales"].idxmax(), "Customer"]
max_sales = df["Sales"].max()
print("Customer:", max_customer)
print("Sales:", max_sales)

# 1. Sales are strongly right-skewed because one customer has exceptionally high sales
# 2. Sales show high variability, as the coefficient of variation is approximately 94.69%.
# 3. Vikram is the highest-value customer with sales of ₹300,000, so this customer has a major impact on overall sales statistics.
