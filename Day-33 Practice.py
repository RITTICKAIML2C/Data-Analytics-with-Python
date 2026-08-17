import pandas as pd 
# # 1. Basic GroupBy
# # Print: Average salary by department, Maximum salary by department, Minimum salary by department, Total salary by department
df = pd.DataFrame({
    "Department": [
        "IT","HR","IT","Finance",
        "HR","Finance","IT"
    ],
    "Salary":[
        50000,45000,65000,
        70000,48000,72000,60000
    ]
})
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].sum())

# # 2. Multiple Aggregations 
# # Using agg(), display for each department: mean salary, max salary, min salary, count of employees
df = pd.DataFrame({
    "Department":[
        "IT","HR","IT",
        "Finance","HR","Finance","IT"
    ],
    "Salary":[
        50000,45000,65000,
        70000,48000,72000,60000
    ]
})
result = df.groupby("Department").agg(
    Mean_Salary=("Salary", "mean"),
    Max_Salary=("Salary", "max"),
    Min_Salary=("Salary", "min"),
    Employee_Count=("Salary", "count")
)
print(result)

# # 3. Group Performance 
# # Print: Average performance, Highest performance, Lowest performance, department-wise
df = pd.DataFrame({
    "Department":[
        "IT","HR","IT",
        "Finance","HR",
        "Finance","IT"
    ],
    "Performance":[
        82,75,91,
        88,80,95,86
    ]
})
print(df.groupby("Department")["Performance"].mean())
print(df.groupby("Department")["Performance"].max())
print(df.groupby("Department")["Performance"].min())

# # 4. Multiple Columns GroupBy
# # Find average salary grouped by Department & Gender
df = pd.DataFrame({
    "Department":[
        "IT","IT","HR","HR",
        "Finance","Finance"
    ],
    "Gender":[
        "M","F","M","F","M","F"
    ],
    "Salary":[
        60000,65000,
        45000,48000,
        70000,72000
    ]
})
print(df.groupby(["Department", "Gender"])["Salary"].mean())

# # 5. reset_index()
# # Group by Department Calculate average salary, Convert result back into, a normal DataFrame using reset_index()
df = pd.DataFrame({
    "Department":[
        "IT","HR","Finance",
        "IT","Finance"
    ],
    "Salary":[
        50000,45000,
        70000,65000,72000
    ]
})
print(df.groupby("Department")["Salary"].mean().reset_index())

# # Industry Practice
# # Average salary by departmentAverage performance by department Maximum salary by department Minimum salary by department Employee count by department Multiple aggregation using agg()
# # Average experience by department Department with highest average salary Department with highest average performance
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Department": [
        "IT", "HR", "Finance", "IT",
        "HR", "Finance", "IT", "Finance"
    ],
    "Salary": [
        60000, 45000, 70000, 65000,
        48000, 72000, 62000, 75000
    ],
    "Performance": [
        8.5, 7.8, 9.2, 8.9,
        8.0, 9.5, 8.7, 9.3
    ],
    "Experience": [
        3, 2, 6, 4,
        3, 7, 5, 8
    ]
})
avg_salary = df.groupby("Department")["Salary"].mean().reset_index()
print("Average Salary by Department")
print(avg_salary)

avg_performance = df.groupby("Department")["Performance"].mean().reset_index()
print("\nAverage Performance by Department")
print(avg_performance)

max_salary = df.groupby("Department")["Salary"].max().reset_index()
print("\nMaximum Salary by Department")
print(max_salary)

min_salary = df.groupby("Department")["Salary"].min().reset_index()
print("\nMinimum Salary by Department")
print(min_salary)

employee_count = df.groupby("Department")["Employee_ID"].count().reset_index()
employee_count.rename(columns={"Employee_ID": "Employee_Count"}, inplace=True)
print("\nEmployee Count by Department")
print(employee_count)

summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Average_Performance=("Performance", "mean"),
    Average_Experience=("Experience", "mean"),
    Employee_Count=("Employee_ID", "count")
).reset_index()
print("\nDepartment Summary")
print(summary)

avg_experience = df.groupby("Department")["Experience"].mean().reset_index()
print("\nAverage Experience by Department")
print(avg_experience)

highest_salary = (
    df.groupby("Department")["Salary"]
      .mean()
      .idxmax()
)
print("\nDepartment with Highest Average Salary:")
print(highest_salary)

highest_performance = (
    df.groupby("Department")["Performance"]
      .mean()
      .idxmax()
)
print("\nDepartment with Highest Average Performance:")
print(highest_performance)
