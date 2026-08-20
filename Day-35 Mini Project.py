# # Mini Project — Company HR Summary Dashboard
# # Create a DataFrame with 12 employees and these columns: Employee_ID Name Department Gender Salary Performance Experience
# # Build a dashboard that prints:
# # 📊 Employee Overview : Shape, Columns, Data types
# # 💰 Salary Dashboard : Average salary by department, Median salary by department, Maximum salary by department, Minimum salary by departmentm, Employee count by department (using one pivot_table())
# # 📈 Performance Dashboard : Average performance by department, Maximum performance by department, Average experience by department
# # 👥 Gender Dashboard : Using pd.crosstab() display: Employee count, Percentage distribution
# # 💼 Salary Matrix : Using pivot_table() display: Average salary by Department × Gender, Highest salary by Department × Gender
# # ⭐ Business Insights : Find: Highest-paid employee, Highest-performing employee, Department with highest average salary, Department with highest average performance, Employees earning above their department average, Employees performing above their department average
# # 🚀 Bonus : Create a new column: Salary_Level : High, Medium, Low
# # Then display:
# # pd.crosstab(
# #     df["Department"],
# #     df["Salary_Level"]
# # )

import pandas as pd 
df = pd.DataFrame({
    "Employee_ID": [101,102,103,104,105,106,107,108,109,110,111,112],
    "Name": ["Aman","Riya","Rahul","Neha","Arjun","Sneha",
             "Karan","Priya","Rohit","Anjali","Vikas","Pooja"],
    "Department": ["HR","IT","Finance","HR","IT","Finance",
                   "Marketing","IT","HR","Marketing","Finance","IT"],
    "Gender": ["Male","Female","Male","Female","Male","Female",
               "Male","Female","Male","Female","Male","Female"],
    "Salary": [40000,65000,55000,45000,70000,60000,
               50000,72000,48000,53000,62000,68000],
    "Performance": [80,92,85,88,95,90,
                    78,96,84,87,91,89],
    "Experience": [2,5,4,3,6,5,
                   2,7,3,4,6,5]
})
print(df.shape)
print(df.columns)
print(df.dtypes)

salary_dashboard = df.pivot_table(values="Salary", index="Department", aggfunc=["mean", "median", "max", "min", "count"])
print(salary_dashboard)

performance_dashboard = df.pivot_table(values=["Performance", "Experience"], index="Department", aggfunc={"Performance": ["mean", "max"], "Experience": "mean"})
print(performance_dashboard)

print(pd.crosstab(df["Department"], df["Gender"]))

print(pd.crosstab(df["Department"], df["Gender"], normalize="index") * 100)

print(df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="mean", fill_value=0))

print(df.pivot_table(values="Salary", index="Department", columns="Gender", aggfunc="max", fill_value=0))

print(df.loc[df["Salary"].idxmax()])

print(df.loc[df["Performance"].idxmax()])

print(df.groupby("Department")["Salary"].mean().idxmax())

print(df.groupby("Department")["Performance"].mean().idxmax())

dept_avg_salary = df.groupby("Department")["Salary"].transform("mean")
print(df[df["Salary"] > dept_avg_salary][
    ["Name", "Department", "Salary"]
])

dept_avg_perf = df.groupby("Department")["Performance"].transform("mean")
print(df[df["Performance"] > dept_avg_perf][
    ["Name", "Department", "Performance"]
])

def salary_level(salary):
    if salary >= 65000:
        return "High"
    elif salary >= 50000:
        return "Medium"
    else:
        return "Low"

df["Salary_Level"] = df["Salary"].apply(salary_level)
print(pd.crosstab(
    df["Department"],
    df["Salary_Level"]
))

print("\nShape:")
print(df.shape)

print("\nColumn:")
print(df.columns)

print("\nDatatype:")
print(df.dtypes)
