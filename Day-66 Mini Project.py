# # 🏢 MINI PROJECT — REAL-WORLD EMPLOYEE EDA
# # Your tasks: 1. Data Cleaning Clean employee names Handle missing values, Remove duplicates, Convert dates
# # 2. Feature Engineering Create: Joining_Year, Joining_Month, Experience_Category
# # 3. Outlier Analysis Use IQR to identify salary outliers.
# # 4. EDA Calculate: Average salary by department Average performance by department Employee count by department, Average salary by city, Employees with salary > ₹80,000, Top 5 performers
# # 5. Visualization Create: Salary by department → Bar chart Performance by department → Bar chart Salary distribution → Histogram Experience vs Salary → Scatter plot
# # 6. Business Insights Give at least 5 insights based on your analysis.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dataset
df = pd.DataFrame({
    "Employee": [
        " Aman ", "RIYA", "Rahul", " Priya", "Karan ",
        "neha", "VIKAS", "Sneha", " Arjun", "Pooja",
        "rahul", "Meera", "Aman", "Rohit", "Kavya",
        "Dev", "Simran", "Aman "
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "IT",
        "Marketing", "Finance", "HR", "IT", "Sales",
        "IT", "Finance", "IT", "Sales", "Marketing",
        "IT", "HR", "IT"
    ],
    "Salary": [
        85000, 60000, 75000, 95000, 55000,
        50000, 90000, 72000, np.nan, 88000,
        75000, 500000, 85000, 92000, 52000,
        78000, 68000, 85000
    ],
    "Performance": [
        88, 75, 82, 91, 68,
        72, 89, 84, 79, 90,
        82, np.nan, 88, 86, 74,
        81, 77, 88
    ],
    "Experience": [
        3, 2, 4, 6, 1,
        2, 5, 3, 4, 5,
        4, 8, 3, 7, 2,
        4, 3, 3
    ],
    "Joining_Date": [
        "2022-01-10", "2023-03-15", "2021-07-20",
        "2020-05-12", "2024-01-05", "2023-09-10",
        "2019-06-11", "2022-08-25", "2021-11-30",
        "2020-02-14", "2021-07-20", "2018-04-16",
        "2022-01-10", "2019-10-21", "2023-05-19",
        "2021-03-08", "2022-06-17", "2022-01-10"
    ],
    "City": [
        "Delhi", "Mumbai", "Bangalore", "Pune", "Delhi",
        "Kolkata", "Mumbai", "Delhi", np.nan, "Pune",
        "Bangalore", "Mumbai", "Delhi", "Kolkata", "Kolkata",
        "Pune", "Delhi", "Delhi"
    ]
})
df["Employee"] = df["Employee"].str.strip().str.upper()
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
df["City"] = df["City"].fillna("Unknown")

print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()
df = df.reset_index(drop=True)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
df["Joining_Year"] = df["Joining_Date"].dt.year
df["Joining_Month"] = df["Joining_Date"].dt.month
df["Experience_Category"] = pd.cut(
    df["Experience"],
    bins=[-1, 2, 5, np.inf],
    labels=["Junior", "Mid-Level", "Senior"]
)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print(outliers[["Employee", "Salary"]])


print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Performance"].mean())

print(df.groupby("Department")["Employee"].count())

print(df.groupby("City")["Salary"].mean())

print(df[df["Salary"] > 80000][
    ["Employee", "Department", "Salary"]
])

print(df.nlargest(5, "Performance")[
    ["Employee", "Performance"]
])

df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

df.groupby("Department")["Performance"].mean().plot(kind="bar")
plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Performance")
plt.show()

df["Salary"].plot(kind="hist", bins=8)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.show()

df.plot(kind="scatter", x="Experience", y="Salary")
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
