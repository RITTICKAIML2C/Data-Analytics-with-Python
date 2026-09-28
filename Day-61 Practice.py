# # Practice 
# # Question 1 Calculate the following for every department: Average salary, Maximum salary, Minimum salary, Average performance, Average experience, Employee count
# # Use one .groupby().agg().
# # Question 2 Find the department with: Highest average salary Highest average performance Highest average experience Most employees
# # Question 3 Create this summary: Department Average_Salary, Average_Performance, Average_Experience, Employee_Count. Use named aggregation.
# # Question 4 — Business Filtering Find employees who satisfy: Performance >= 90 AND Experience >= 7 AND Salary >= 85000 
# # Question 5 — Ranking Find: Top 3 salaries, Top 3 performances, Top 3 most experienced employees
# # Return only the employee name and relevant value.
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

    "Performance": [
        95, 82, 88, 92,
        65, 94, 85, 98
    ],

    "Experience": [
        8, 4, 6, 10,
        2, 7, 5, 12
    ]
})
department_stats = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Average_Performance=("Performance", "mean"),
    Average_Experience=("Experience", "mean"),
    Employee_Count=("Employee", "count")
)
print(department_stats)

print(department_stats["Average_Salary"].idxmax())
print(department_stats["Average_Performance"].idxmax())
print(department_stats["Average_Experience"].idxmax())
print(department_stats["Employee_Count"].idxmax())

summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Average_Performance=("Performance", "mean"),
    Average_Experience=("Experience", "mean"),
    Employee_Count=("Employee", "count")
)
print(summary)

filtered_employees = df[
    (df["Performance"] >= 90)
    & (df["Experience"] >= 7)
    & (df["Salary"] >= 85000)
]
print(filtered_employees)

top_salary = df.nlargest(3, "Salary")[["Employee", "Salary"]]
print(top_salary)
top_performance = df.nlargest(3, "Performance")[
    ["Employee", "Performance"]
]
print(top_performance)
top_experience = df.nlargest(3, "Experience")[
    ["Employee", "Experience"]
]
print(top_experience)
