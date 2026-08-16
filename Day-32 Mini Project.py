# # Mini Project
# # Original DataFrame, Shape, Data Types
# # Missing values per column, Total missing values, Duplicate rows, Number of duplicate
# # Remove duplicates, Fix inconsistent departments, Fill missing Salary, Fill missing Performance
# # Annual Salary, Bonus, Performance Level
# # Average Salary, Median Salary, Highest Salary, Lowest Salary, Average Performance, Average Experience, Department Counts
# # Top 3 Salaries, Top 3 Performers
# # Salary > 50000 AND Performance >= 85, Experience >= 5 OR Performance >= 90
# # Average salary by department, Highest-paid employee, Highest-performing employee, Department with the highest average salary

import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 103, 104, 105, 106, 107],
    "Name": ["Aman", "Riya", "Rahul", "Rahul", "Neha", "Arjun", "Priya", "Karan"],
    "Department": ["IT", "HR", "IT ", "IT ", "Finance", "IT", "HR", "Finance"],
    "Salary": [35000, np.nan, 52000, 52000, 68000, 75000, np.nan, 62000],
    "Performance": [72, 85, np.nan, np.nan, 88, 95, 72, 84],
    "Experience": [1, 2, 5, 5, 4, 7, 3, 4]
})
print(df)
print(df.shape)
print(df.dtypes)

print(df.isna().sum())
print(df.isna().sum().sum())
print(df[df.duplicated()])
print(df.duplicated().sum())

df = df.drop_duplicates()
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
print(df)                               

df["Annual_Salary"] = df["Salary"] * 12
df["Bonus"] = df["Annual_Salary"] * 0.10
df["Performance_Level"] = df["Performance"].apply(
    lambda x: "Excellent" if x >= 85
    else "Pass" if x >= 70
    else "Needs Improvement"
)
print(df)

print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Performance"].mean())
print(df["Experience"].mean())
print(df["Department"].value_counts())

print(df.sort_values("Salary", ascending=False).head(3))
print(df.sort_values("Performance", ascending=False).head(3))

print(df[(df["Salary"] > 50000) & (df["Performance"] >= 85)])
print(df[(df["Experience"] >= 5 | (df["Performance"] >= 90))])

print(df.groupby("Department")["Salary"].mean())
highest_salary = df["Salary"].max()
print(df[df["Salary"] == highest_salary])

highest_performance = df["Performance"].max()
print(df[df["Performance"] == highest_performance])

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary.sort_values(ascending=False).head(1))

