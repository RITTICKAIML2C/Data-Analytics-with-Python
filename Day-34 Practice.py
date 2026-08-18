import pandas as pd
# # 1. Basic Merge 
# # Merge both DataFrames and Display complete result
employees = pd.DataFrame({
    "Employee_ID":[101,102,103,104],
    "Name":["Aman","Riya","Rahul","Neha"]
})

salary = pd.DataFrame({
    "Employee_ID":[101,102,103,104],
    "Salary":[50000,65000,72000,58000]
})
print(pd.merge(employees, salary, on="Employee_ID"))

# # 2. Left Merge
# # Perform LEFT merge and Display result
employees = pd.DataFrame({
    "Employee_ID":[101,102,103,104,105],
    "Name":["Aman","Riya","Rahul","Neha","Arjun"]
})

salary = pd.DataFrame({
    "Employee_ID":[101,102,104],
    "Salary":[50000,65000,58000]
})
print(pd.merge(employees, salary, on="Employee_ID", how="left")


# # 3. Outer Merge
# # Perform OUTER merge
employees = pd.DataFrame({
    "Employee_ID":[101,102,103]
})

salary = pd.DataFrame({
    "Employee_ID":[102,103,104],
    "Salary":[60000,70000,80000]
})
print(pd.merge(employees, salary, on="Employee_ID", how="outer"))

# # 4. Different Column Names 
# # Merge using : left_on, right_on
employees = pd.DataFrame({
    "Employee_ID":[101,102,103],
    "Name":["Aman","Riya","Rahul"]
})

salary = pd.DataFrame({
    "ID":[101,102,103],
    "Salary":[50000,65000,70000]
})
print(pd.merge(employees, salary, left_on="Employee_ID", right_on="ID"))

# # 5. Concatenation
# # Concatenate Vertically, Concatenate Horizontally 
df1 = pd.DataFrame({
    "Name":["Aman","Riya"]
})
df2 = pd.DataFrame({
    "Name":["Rahul","Neha"]
})
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis = 1))

# # Industry Practice - Employee HR System 
# # Employees : Employee_ID, Name, Department_ID
# # Departments : Department_ID, Department_Name
# # Salaries : Employee_ID, Salary, Bonus
# # Merge Employees + Departments, Merge result with Salaries, Show complete employee report, Average salary by department
# # Highest-paid employee, Employees without salary information, Employees without department information, Department with highest average salary
employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Department_ID": [1, 2, 1, None]
})
departments = pd.DataFrame({
    "Department_ID": [1, 2, 3],
    "Department_Name": ["HR", "IT", "Finance"]
})
salaries = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Salary": [50000, 65000, 70000],
    "Bonus": [5000, 7000, 6000]
})
emp_dept = pd.merge(employees, departments, on="Department_ID", how="left")
print(emp_dept)

emp_report = pd.merge(emp_dept, salaries, on="Employee_ID", how="left")
print(emp_report)

avg_salary = emp_report.groupby("Department_Name")["Salary"].mean()
print(avg_salary)

highest_paid = emp_report.loc[emp_report["Salary"].idxmax()]
print(highest_paid)

no_salary = emp_report[emp_report["Salary"].isna()]
print(no_salary)

no_department = emp_report[emp_report["Department_Name"].isna()]
print(no_department)

highest_avg_dept = avg_salary.idxmax()
highest_avg_salary = avg_salary.max()

# print(highest_avg_dept, highest_avg_salary)
