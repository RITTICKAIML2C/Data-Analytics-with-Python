# # Mini Project — Company Employee Dashboard
# # Create two DataFrames. employees
# # Columns: Employee_ID Name Department_ID Salary Performance
# # Create 8 employees. departments
# # Columns: Department_ID Department Manager Location
# # Create 4 departments. Then:
# # 📊 Step 1 — Merge : Perform a left merge.
# # 💰 Step 2 — Analysis : After merging, calculate: Average salary by department Maximum salary by department Average performance by department Employee count by department
# # ⭐ Step 3 — Business Insights Find: Department with highest average salary Department with highest average performance Highest-paid employee Highest-performing employee
# # 🔥 Bonus : Find employees whose: Salary > department average salary
import pandas as pd 
employees = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit", "Ananya", "Vikash", "Neha"],
    "Department_ID": [1, 2, 3, 2, 1, 4, 3, 4],
    "Salary": [50000, 65000, 55000, 70000, 60000, 75000, 58000, 68000],
    "Performance": [82, 91, 78, 95, 88, 93, 85, 89]
}
departments = {
    "Department_ID": [1, 2, 3, 4],
    "Department": ["HR", "IT", "Finance", "Marketing"],
    "Manager": ["Raj", "Arjun", "Meera", "Karan"],
    "Location": ["Delhi", "Bangalore", "Mumbai", "Kolkata"]
}
merged_df = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="left"
)
print(merged_df)

avg_salary = merged_df.groupby("Department")["Salary"].mean()
print(avg_salary)

max_salary = merged_df.groupby("Department")["Salary"].max()
print(max_salary)

avg_performance = merged_df.groupby("Department")["Performance"].mean()
print(avg_performance)

employee_count = merged_df.groupby("Department")["Employee_ID"].count()
print(employee_count)

highest_avg_salary_department = (
    merged_df.groupby("Department")["Salary"]
    .mean()
    .idxmax()
)
print("Department with highest average salary:",
      highest_avg_salary_department)

highest_avg_performance_department = (
    merged_df.groupby("Department")["Performance"]
    .mean()
    .idxmax()
)
print("Department with highest average performance:",
      highest_avg_performance_department)

highest_paid_employee = merged_df.loc[
    merged_df["Salary"].idxmax()
]
print(highest_paid_employee)

highest_performing_employee = merged_df.loc[
    merged_df["Performance"].idxmax()
]
print(highest_performing_employee)

department_avg_salary = merged_df.groupby("Department")["Salary"].transform("mean")
print(department_avg_salary)
merged_df["Department_Avg_Salary"] = department_avg_salary

above_department_average = merged_df[
    merged_df["Salary"] > merged_df["Department_Avg_Salary"]
]
print(
    above_department_average[
        ["Employee_ID", "Name", "Department", "Salary", "Department_Avg_Salary"]
    ]
)
