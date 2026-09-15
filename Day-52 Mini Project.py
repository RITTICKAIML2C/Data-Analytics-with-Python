# # Mini Project — Employee Performance Analysis
# # 📊 Analysis
# # Calculate: Average salary by department. Average performance by department.
# # Add: Department_Avg_Salary using transform().
# # Add: Department_Avg_Performance using transform().
# # 🔥 Conditional Analysis Find employees who: A. Earn more than their department's average salary, B. Have performance higher than their department's average performance, C. Satisfy both conditions: Salary > Department Average Salary AND Performance > Department Average Performance
# # ⭐ Business Insights : Which department has the highest average salary?, Which department has the highest average performance?, Who is the highest-paid employee?
# # Who is the highest-performing employee?, Which employees are above their department's salary AND performance averages?
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Employee_ID": [
        101, 102, 103,
        104, 105, 106,
        107, 108, 109,
        110, 111, 112
    ],

    "Name": [
        "Aarav", "Riya", "Karan",
        "Neha", "Arjun", "Priya",
        "Rahul", "Sneha", "Vikram",
        "Ananya", "Rohan", "Meera"
    ],

    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR",
        "Finance", "Finance", "Finance",
        "Marketing", "Marketing", "Marketing"
    ],

    "Salary": [
        85000, 70000, 95000,
        60000, 65000, 55000,
        90000, 75000, 82000,
        70000, 78000, 68000
    ],

    "Performance": [
        92, 78, 88,
        85, 90, 72,
        95, 82, 87,
        80, 93, 75
    ],

    "Experience": [
        5, 3, 7,
        4, 5, 2,
        8, 4, 6,
        3, 6, 2
    ]
})
avg_salary = df.groupby("Department")["Salary"].mean()
avg_performance = df.groupby("Department")["Performance"].mean()
df["Department_Avg_Salary"] = (
    df.groupby("Department")["Salary"].transform("mean")
)
df["Department_Avg_Performance"] = (
    df.groupby("Department")["Performance"].transform("mean")
)
above_salary = df[
    df["Salary"] > df["Department_Avg_Salary"]
]
above_performance = df[
    df["Performance"] > df["Department_Avg_Performance"]
]
above_both = df[
    (df["Salary"] > df["Department_Avg_Salary"]) &
    (df["Performance"] > df["Department_Avg_Performance"])
]
highest_salary_department = avg_salary.idxmax()
highest_performance_department = avg_performance.idxmax()
highest_paid_employee = df.loc[
    df["Salary"].idxmax(), "Name"
]
highest_performing_employee = df.loc[
    df["Performance"].idxmax(), "Name"
]
print("Average Salary:")
print(avg_salary)
print("Average Performance:")
print(avg_performance)
print("Employees Above Salary Average:")
print(above_salary)
print("Employees Above Performance Average:")
print(above_performance)
print("Employees Above Both Averages:")
print(above_both)
print("Highest Average Salary Department:",
      highest_salary_department)
print("Highest Average Performance Department:",
      highest_performance_department)
print("Highest Paid Employee:",
      highest_paid_employee)
print("Highest Performing Employee:",
      highest_performing_employee)
