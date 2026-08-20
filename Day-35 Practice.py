import pandas as pd 
# # 1. Basic Pivot Table
# # Create a DataFrame with: Employee_ID Department Salary
# # Print: Average salary by department, Highest salary by department, Employee count by department
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [40000, 60000, 45000, 50000, 70000, 55000]
})
avg_salary = df.pivot_table(values="Salary", index="Department", aggfunc="mean")
print(avg_salary)

max_salary = df.pivot_table(values="Salary", index="Department", aggfunc="max")
print(max_salary)

emp_count = df.pivot_table(values="Salary", index="Department", aggfunc="count")
print(emp_count)

# # 2. Multiple Aggregation 
# # Using the same DataFrame, display: Mean salary, Median salary, Maximum salary, Minimum salary, Employee count
# # using one pivot_table().
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [40000, 60000, 45000, 50000, 70000, 55000]
})
summary = df.pivot_table(values="Salary", index="Department", aggfunc=["mean", "median", "max", "min", "count"])
print(summary)

# # 3. Multiple Values 
# # Create : Department, Salary, Performance
# # Display department-wise: average salary, average performance
df = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [40000, 60000, 45000, 50000, 70000, 55000],
    "Performance": [80, 90, 85, 75, 95, 88]
})
result = df.pivot_table(values=["Salary", "Performance"], index="Department", aggfunc="mean")
print(result)

# # 4. Pivot with Columns 
# # Create: Department, Gender, Salary
# # Display : Average Salary by Department X Gender 
df = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"],
    "Salary": [40000, 60000, 45000, 50000, 70000, 55000]
})
result = df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="mean")
print(result)

# # 5. Fill Missing Values 
# # fill_value=0
df = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"],
    "Salary": [40000, 60000, 45000, 50000, 70000, 55000]
})
result = df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="mean", fill_value=0)
print(result)

# # 6. Crosstab
# # Create : Department, Gender 
# # Display : Counts, Percentage Distribution
df = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
})
counts = pd.crosstab(df["Department"], df["Gender"])
print(counts)
percentage = pd.crosstab(df["Department"], df["Gender"], normalize="index")
print(percentage)

# # Industry Practice - HR Analytics Dashboard 
# # Create a DataFrame with: Employee_ID, Name, Dept, Gender, Salary, Performance, experience
# # Generate the following reports: 
# # Employee Analytics : Average salary by department, Average performance by department, Employee count by department, Highest salary by department, Highest performance by departmen
# # Gender Analytics : Male/Female count per department, Percentage distribution
# # Salary Analytics : Average salary by Gender × Department, Maximum salary by Gender × Department
# # Business Insights : Department with highest average salary, Department with highest average performance, Gender earning the highest average salary, Department with the largest workforce
df = pd.DataFrame({
    "Employee_ID": [101,102,103,104,105,106,107,108],
    "Name": ["Aman","Riya","Rahul","Neha","Arjun","Sneha","Karan","Priya"],
    "Department": ["HR","IT","HR","Finance","IT","Finance","HR","IT"],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Salary": [40000,60000,45000,50000,70000,55000,48000,65000],
    "Performance": [80,90,85,75,95,88,82,91],
    "Experience": [2,4,3,5,6,4,2,5]
})
print(df.pivot_table(values="Salary", index="Department", aggfunc="mean"))
print(df.pivot_table(values="Performance", index="Department", aggfunc="mean"))
print(df.pivot_table(values="Employee_ID", index="Department", aggfunc="count"))
print(df.pivot_table(values="Salary", index="Department", aggfunc="max"))
print(df.pivot_table(values="Performance", index="Department", aggfunc="max"))

print(pd.crosstab(df["Department"], df["Gender"]))
print(pd.crosstab(df["Department"], df["Gender"], normalize="index") * 100)

print(df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="mean"))
print(df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="max"))

print("Highest Avg Salary Department:", df.groupby("Department")["Salary"].mean().idxmax())
print("Highest Avg Performance Department:", df.groupby("Department")["Performance"].mean().idxmax())
print("Highest Avg Salary Gender:", df.groupby("Gender")["Salary"].mean().idxmax())
print("Largest Workforce Department:", df["Department"].value_counts().idxmax())

