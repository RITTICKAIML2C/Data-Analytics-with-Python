# # Practice 
# # Q1 — Missing Values : Find the number of missing values in every column.
# # Q2 — Missing Percentage : Calculate the missing-value percentage for every column.
# # Q3 — Remove Missing Data : Create a dataset where rows with missing Salary are removed.
# # Q4 — Fill Missing Data : Fill Salary using median, Fill Performance using mean, Fill Department using mode, Fill Experience using median
# # Q5 — Business Check : After cleaning: df.isna().sum(). Confirm that there are no missing values.
import pandas as pd
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan", "Neha"],
    "Department": ["IT", "HR", None, "Finance", "IT", None],
    "Salary": [85000, None, 75000, 95000, None, 60000],
    "Performance": [95, 82, None, 92, 65, None],
    "Experience": [8, 4, 6, None, 2, 3]
})
print(df.isna().sum())
print(df.isna().mean() * 100)
print(df.dropna(subset= ["Salary"]))
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Experience"] = df["Experience"].fillna(df["Experience"].median())
print(df)
print(df.isna().sum())

