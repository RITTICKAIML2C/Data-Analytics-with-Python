# # 1. pivot_table() 
df.groupby("Department")["Salary"].mean()

pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Employee_Status",
    aggfunc="mean"
)

# # Example Dataset
import pandas as pd

df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul", "Priya",
        "Karan", "Neha", "Vikas", "Anjali"
    ],

    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "Finance"
    ],

    "Salary": [
        85000, 60000, 75000, 95000,
        55000, 90000, 80000, 110000
    ],

    "Performance_Category": [
        "Excellent", "Good", "Good", "Excellent",
        "Poor", "Excellent", "Good", "Excellent"
    ]
})
salary_pivot = pd.pivot_table(
    df, 
    values="Salary",
    index="Department", 
    columns="Performance_Category",
    aggfunc="mean"
)
print(salary_pivot)

# # 2. Multiple Aggregations 
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc=["mean", "max", "min"]
)

# # 3. pd.crosstab() - counts combinations between categories 
pd.crosstab(
    df["Department"],
    df["Performance_Category"]
)

