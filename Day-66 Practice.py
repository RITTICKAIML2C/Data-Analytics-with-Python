# # Practice
# # Q1 — String Cleaning : Convert all employee names to: uppercase + remove extra spaces
# # Q2 — Duplicate Analysis, Find: Number of duplicate rows. Then remove the duplicates.
# # Q3 — Date Analysis : Convert Joining_Date to datetime and create: Year, Month, Day_Name
# # Q4 — Salary Outliers : Use the IQR method to identify salary outliers. Don't delete them.
# # Q5 — Business Analysis : Find: Average salary by department, Number of employees by department, Earliest joining date, Latest joining da
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee": [
        " Aman ", "RIYA", "Rahul", "Priya",
        "Karan", "Neha", "Rahul"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "Marketing", "IT"
    ],
    "Salary": [
        85000, 60000, 75000, 95000,
        55000, 50000, 75000
    ],
    "Joining_Date": [
        "2022-01-10", "2023-03-15", "2021-07-20",
        "2020-05-12", "2024-01-05", "2023-09-10",
        "2021-07-20"
    ]
})
df["Employee"] = df["Employee"].str.strip().str.upper()
print(df["Employee"])

print(df.duplicated().sum())

df = df.drop_duplicates()
print(df)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
df["Year"] = df["Joining_Date"].dt.year
df["Month"] = df["Joining_Date"].dt.month
df["Day_Name"] = df["Joining_Date"].dt.day_name()
print(df)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]
print(outliers)

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

employee_count = df.groupby("Department")["Employee"].count()
print(employee_count)

earliest_date = df["Joining_Date"].min()
print(earliest_date)

latest_date = df["Joining_Date"].max()
print(latest_date)

