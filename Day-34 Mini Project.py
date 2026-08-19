import pandas as pd
# # Create four DataFrames : Employees, Employee_ID, Name, Department_ID, Departments, Department_ID, Department, Performance, Employee_ID, Performance, Salary, Employee_ID, Salary
# # Step 1 — Merge
# # Create one final DataFrame containing: Employee_ID, Name, Department, Salary, Performance
# # Step 2 — Dashboard Display: Employee Overview Complete merged DataFrame Shape Columns Data types Salary Analytics Average salary Median salary Highest salary Lowest salary
# # Top 3 salaries, Bottom 3 salaries, Performance Analytics, Average performance, Highest performance, Lowest performance, Top 3 performers, Department Analytics
# # Using groupby(): Average salary, Average performancel, Employee count, Highest salary, Highest performance, Business Insights
# # Find: Highest-paid employee, Highest-performing employee, Department with highest average salary, Department with highest average performance, Employees earning above their department average salary, Employees performing above their department average performance
# # ⭐ Bonus : Create a new column:,Performance_Level, using:, Excellent (≥90), Good (80–89), Average (70–79), Needs Improvement (<70)
# # Then display: groupby(["Department", "Performance_Level"]).size() to see the distribution of performance levels within each department
employees = pd.DataFrame({
    "Employee_ID":[101,102,103,104,105],
    "Name":["Aman","Riya","Rahul","Neha","Karan"],
    "Department_ID":[1,2,1,3,2]
})

departments = pd.DataFrame({
    "Department_ID":[1,2,3],
    "Department":["HR","IT","Finance"]
})

performance = pd.DataFrame({
    "Employee_ID":[101,102,103,104,105],
    "Performance":[85,92,78,95,88]
})

salary = pd.DataFrame({
    "Employee_ID":[101,102,103,104,105],
    "Salary":[50000,70000,55000,80000,65000]
})

df = pd.merge(employees, departments, on="Department_ID")
df = pd.merge(df, salary, on="Employee_ID")
df = pd.merge(df, performance, on="Employee_ID")
df = df[["Employee_ID","Name","Department","Salary","Performance"]]
print(df)

print(df.shape)
print(df.columns)
print(df.dtypes)

print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].max())
print(df["Salary"].min())
print(df.sort_values("Salary", ascending=False).head(3))
print(df.sort_values("Salary", ascending=False).tail(3))

print(df["Performance"].mean())
print(df["Performance"].max())
print(df["Performance"].min())
print(df.sort_values("Performance", ascending=False).head(3))

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Performance"].mean())
print(df.groupby("Department").size())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Performance"].max())

print(df.loc[df["Salary"].idxmax()])
print(df.loc[df["Performance"].idxmax()])
print(df.groupby("Department")["Salary"].mean().idxmax())
print(df.groupby("Department")["Performance"].mean().idxmax())

avg_salary = df.groupby("Department")["Salary"].transform("mean")
print(df[df["Salary"] > avg_salary])

avg_perf = df.groupby("Department")["Performance"].transform("mean")
print(df[df["Performance"] > avg_perf])

df["Performance_Level"] = df["Performance"].apply(
    lambda x: "Excellent" if x >= 90
    else "Good" if x >= 80
    else "Average" if x >= 70
    else "Needs Improvement"
)
print(df[["Name", "Performance", "Performance_Level"]])
