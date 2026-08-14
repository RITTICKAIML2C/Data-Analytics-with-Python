import pandas as pd
# # 1. Create a series : 78, 85, 91, 67, 88 with Indexes : A, B, C, D, E
series = pd.Series(
    [78, 85, 91, 67, 88],
    index = ["A", "B", "C", "D", "E"]
)
print("Series:\n", series)
print("Values:", series.values)
print("Index:", series.index)
print("DataType:", series.dtype)
print("Shape:", series.shape)
print("Number of Elements:", series.size)

# # 2. Create an Employee DataFrame. Print the DataFrame
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df)

# # 3. DataFrame Inspection 
# # Using the DataFrame from Q2, display: First 3 rows, Last 2 rows, Shape, Columns
# # Index, Data types, info(), describe()
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# # 4. Column Selection
# # Display: Employee IDs, Salaries, Salary + Performance, Name + Experience + Salary
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df[[]"Employee_ID"]])
print(df["[Salary"]])
print(df[["Salary", "Performance"]])
print(df[["Name", "Experience", "Salary"]])

# # 5. loc Practice
# # Using the employee DataFrame: Select first employee, Select first 3 employees
# # Select salary of employee at index 2, Select Name and Salary for indexes 1–3
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df.loc[0])
print(df.loc[0:2])
print(df.loc[2]["Salary"])
print(df.loc[1:3, ["Name", "Salary"]])

# # 6. iloc Practice 
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[:, 0:2])
print(df.iloc[1:4, 2:4])

# # 7. Filtering 
# # Find employees: earning > $50,000, earning ≥ $60,000, earning < $50,000
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df[df["Salary"] > 50000])
print(df[df["Salary"] >= 60000])
print(df[df["Salary"] < 50000])

# # 8. Peformance Filtering 
# # Find: Performance ≥ 85, Performance < 80, Performance between 70 and 90
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df[df["Performance"] >= 85])
print(df[df["Performance"] < 80])
print(df[(df["Performance"] >= 70) & (df["Performance"] <= 90)])

# # 9. Multiple Conditions
# #  Find employees who: earn more than $50,000 AND have performance ≥ 85.
# # Then find employees who: earn more than $60,000 OR have performance ≥ 90.
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df[(df["Salary"] > 50000) & (df["Performance"] >= 85)])
print(df[(df["Salary"] > 60000) & (df["Performance"] >= 90)])

# # 10. Business Questions 
# # Find all employees with: Experience ≥ 4 AND Performance ≥ 85
data = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Aman","Riya","Rahul","Neha","Arjun"], 
    "Salary" : [35000,45000,52000,68000,75000], 
    "Performance" : [72,85,91,88,95], 
    "Experience" : [1,3,5,4,7]
}
df = pd.DataFrame(data)
print(df.loc[
    (df["Experience"] >= 4) &
    (df["Performance"] >= 85),
    ["Employee_ID", "Name", "Performance", "Experience"]
])

# # Industry Practice - Employee Data Inspection System
# # Create this DataFrame
# # Employee Overview : Complete DataFrame, First 5 employees, Last 3 employees, Shape, Column names, Data types
# # Salary Analysis : Average salary, Highest salary, Lowest salary, Employees earning > $50,000, Employees earning ≥ $60,000
# # Performance Analysis : Average performance, Highest performance, Lowest performance, Employees with performance ≥ 85, Employees with performance < 70
# # Experience Analysis : Average experience, Employees with experience ≥ 5 years
# # Combined Analysis : Find employees who: Salary > $50,000 AND Performance >= 85 AND Experience >= 4, Display: Employee_ID, Name, Salary, Performance, Experience
import pandas as pd
data = {
    "Employee_ID": [101,102,103,104,105,106,107,108],
    "Name": [
        "Aman", "Riya", "Rahul", "Neha",
        "Arjun", "Priya", "Karan", "Sneha"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT"
    ],
    "Salary": [
        35000, 45000, 52000, 68000,
        75000, 48000, 62000, 58000
    ],
    "Performance": [
        68, 75, 91, 88,
        95, 72, 84, 90
    ],
    "Experience": [
        1, 2, 5, 4,
        7, 3, 4, 6
    ]
}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)

print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print(df.loc[df["Salary"] > 50000])
print(df.loc[df["Salary"] >= 60000])

print("Average Performance:", df["Performance"].mean())
print("Highest Performance:", df["Performance"].max())
print("Lowest Performance:", df["Performance"].min())
print(df.loc[df["Performance"] >= 85])
print(df.loc[df["Performance"] < 70])

print("Average Experience:", df["Experience"].mean())
print(df.loc[df["Experience"] >= 5])

print(df.loc[
    (df["Salary"] > 50000) &
    (df["Performance"] >= 85) & 
    (df["Experience"] >= 4), 
    ["Employee_ID", "Name", "Salary", "Performance", "Experience"]
])
