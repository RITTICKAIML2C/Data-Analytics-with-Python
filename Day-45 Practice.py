import pandas as pd 
# # 1. Employee + Department 
# # Create two dataframes : Employee Data, Columns: Employee_ID Name Department_ID Salary
# # Use 6 employees. Department Data, Columns: Department_ID Department_Name Location
# # Use 4 departments. Then perform:
# # A. Inner merge using: Department_ID
# # B. Left merge.
# # C. Outer merge.
# # D. Answer: How many employees have matching departments? Which employees don't have department information? Which departments don't have employees?
employees = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohit", "Ananya"],
    "Department_ID": [1, 2, 3, 5, 2, 4],
    "Salary": [50000, 60000, 55000, 45000, 65000, 70000]
}
departments = {
    "Department_ID": [1, 2, 3, 4],
    "Department_Name": ["HR", "IT", "Finance", "Marketing"],
    "Location": ["Delhi", "Bangalore", "Mumbai", "Kolkata"]
}
inner_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="inner"
)
print(inner_merge)

left_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="left"
)
print(left_merge)

outer_merge = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="outer",
    indicator=True
)
print(outer_merge)

matching_employees = inner_merge["Employee_ID"].nunique()
print("Employees with matching departments:", matching_employees)

employees_without_department = left_merge[
    left_merge["Department_Name"].isna()
]
print(employees_without_department[["Employee_ID", "Name", "Department_ID"]])

# Department_ID = 6
# Department_Name = "Operations"
# Location = "Pune"
