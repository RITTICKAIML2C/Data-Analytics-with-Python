# # Practice 
# # Question 1 — Create Performance Category
# # Create: Excellent → Performance ≥ 90, Good → Performance ≥ 75, Average → Performance ≥ 60, Poor Otherwise. Use np.select().
# # Question 2 — Salary Pivot
# # Create a Pivot Table showing: Rows → Department, Columns → Performance_Category, Values → Salary, Aggregation → Average Salary
# # Question 3 — Department Dashboard
# # Create a Pivot Table showing: Rows → Department, Values → Salary. Calculate: Average Salary, Maximum Salary, Minimum Salary
# # Question 4 — Crosstab Create a Crosstab showing: Rows → Department, Columns → Performance_Category. This should count the number of employees in each category.
# # Question 5 — Advanced Pivot, Create a Pivot Table showing:
# # Rows → Department, Columns → Performance_Category, Values → Experience, Aggregation → Average Experience
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul", "Priya",
        "Karan", "Neha", "Vikas", "Anjali",
        "Rohan", "Sneha"
    ],

    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "Finance",
        "Marketing", "Marketing"
    ],

    "Salary": [
        85000, 60000, 75000, 95000,
        55000, 90000, 80000, 110000,
        70000, 65000
    ],

    "Performance": [
        95, 82, 88, 92,
        65, 94, 85, 98,
        78, 72
    ],

    "Experience": [
        8, 4, 6, 10,
        2, 7, 5, 12,
        3, 4
    ]
})
df["Performance_Category"] = np.select([df["Performance"] >= 90, df["Performance"] >= 75, df["Performance"] >= 60], ["Excellent", "Good", "Average"], default="Poor")
print(df)
print(pd.pivot_table(df, index="Department", columns="Performance_Category", values="Salary", aggfunc="mean"))
print(pd.pivot_table(df, index="Department", values="Salary", aggfunc=["mean", "max", "min"]))
print(pd.crosstab(df["Department"], df["Performance_Category"]))
print(pd.pivot_table(df, index="Department", columns="Performance_Category", values="Experience", aggfunc="mean"))
