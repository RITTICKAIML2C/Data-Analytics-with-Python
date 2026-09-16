import pandas as pd 
# # 1. Basic Missing Data 
# # Task : Display the DataFrame, Find the number of missing values in every column, Find employees with missing salary, Find employees with missing performance, Find employees whose salary is not missingl, Calculate the average salary ignoring missing values.
# # Calculate the median performance ignoring missing values, Fill missing Salary values with the average salary, Fill missing Performance values with the median performance, Display the cleaned DataFrame.
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, None, 75000, 55000, None, 80000],
    "Performance": [85, 90, None, 78, 88, None]
})
print(df)
print(df.isna().sum())
print(df[df["Employee"].isna()])
print(df[df["Performance"].isna()])
print(df[df["Salary"].notna()])
print(df["Salary"].mean())
print(df["Performance"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Performance"] = df["Performance"].fillna(df["Performance"].median())
print(df)

# # 2. Industrial Data Cleaning 
# # Task : Find missing values in each column, Find the total number of missing Sales values, Find the total number of missing Profit values, Find products with missing Sales, Find products with missing Profit.
# # Data Cleaning : Calculate average Sales, Calculate median Sales, Fill missing Sales using the median Sales, Fill missing Profit using the mean Profit, Verify that there are no missing values remaining.
# # Business Analysis : Find the department with the highest average Sales after cleaning, Find the product with the highest Sales after cleaning, Calculate total Sales, Calculate total Profit.
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Furniture",
        "Furniture", "Clothing", "Clothing",
        "IT", "IT"
    ],
    "Product": [
        "Laptop", "Phone", "Chair", "Table",
        "Shirt", "Jeans", "Server", "Software"
    ],
    "Sales": [
        120000, None, 55000, 70000,
        None, 45000, 150000, None
    ],
    "Profit": [
        18000, 15000, None, 10000,
        7000, None, 30000, 25000
    ]
})
print(df.isna().sum())
print(df["Sales"].isna().sum())
print(df["Profit"].isna().sum())
print(df["Product"].isna())
print(df.loc[df["Sales"].isna(), "Product"])
print(df.loc[df["Profit"].isna(), "Product"])

print(df["Sales"].mean())
print(df["Sales"].median())
print(df["Sales"].fillna(df["Sales"].median()))
print(df["Profit"].fillna(df["Profit"].mean()))
print(df.isna().sum())

print(df.groupby("Department")["Sales"].mean().idxmax())
print(df.loc[df["Sales"].idxmax(), "Product"])
print(df["Sales"].sum())
print(df["Profit"].sum())
print(df)
