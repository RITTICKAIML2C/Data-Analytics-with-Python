import pandas as pd 
# # 1. Dataset Exploration
# # How many employees are there? How many columns? What is the average salary? What is the minimum salary? What is the maximum salary?
# # What is the average performance What is the minimum experience What is the maximum experience? 
df = pd.DataFrame({
    "Employee_ID": range(101, 111),

    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha", "Arjun",
        "Neha", "Rohan", "Ananya", "Vikas", "Karan"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "HR", "Marketing", "IT", "Finance"
    ],

    "Salary": [
        95000, 55000, 85000, 70000, 120000,
        65000, 80000, 90000, 60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ]
})
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# How many employees? → 10
# How many columns? → 6
# Average salary? → ₹83,000
# Minimum salary? → ₹55,000
# Maximum salary? → ₹1,20,000
# Average performance? → 83.5
# Minimum experience? → 2 years
# Maximum experience? → 10 years

# # 2. Uniqueness Analysis, Using the same DataFrame:
# # Find: A. Number of unique departments, B. Number of unique salaries, C. Number of unique performance scores, D. Number of unique experience values, E. Unique departments themselves: df["Department"].unique()
# # Business Question : Which column appears to have the greatest variety of values?
df = pd.DataFrame({
    "Employee_ID": range(101, 111),

    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha", "Arjun",
        "Neha", "Rohan", "Ananya", "Vikas", "Karan"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "HR", "Marketing", "IT", "Finance"
    ],

    "Salary": [
        95000, 55000, 85000, 70000, 120000,
        65000, 80000, 90000, 60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ]
})
print(df["Department"].nunique())
print(df["Salary"].nunique())          
print(df["Performance"].nunique())       
print(df["Experience"].nunique())       
print(df["Department"].unique())

# Greatest variety: Salary and Performance — both have 10 unique values.

# # 3. Compare Mean vs Median, Find: average_salary = df["Salary"].mean() median_salary = df["Salary"].median()
# # print("Average Salary:", average_salary, print("Median Salary:", median_salary)
# # Then answer: Is the average salary higher or lower than the median salary? And more importantly: What might this tell you about the salary distribution?
df = pd.DataFrame({
    "Employee_ID": range(101, 111),

    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha", "Arjun",
        "Neha", "Rohan", "Ananya", "Vikas", "Karan"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "HR", "Marketing", "IT", "Finance"
    ],

    "Salary": [
        95000, 55000, 85000, 70000, 120000,
        65000, 80000, 90000, 60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ]
})
average_salary = df["Salary"].mean()
median_salary = df["Salary"].median()
print("Average Salary:", average_salary)
print("Median Salary:", median_salary)

# Average salary is higher than the median salary.

# # 4. Department EDA
# # Now we're going to combine everything you've learned. Calculate: 1. Average salary by department, 2. Average performance by department, 3. Average experience by department, 4. Employee count by department
# # Find: A. Department with the highest average salary, B. Department with the lowest average salary, C. Department with the highest average performance, D. Department with the lowest average performance, E. Department with the most employees, F. Department with the highest average experience.
# # Use: .idxmax() and .idxmin() where appropriate.
df = pd.DataFrame({
    "Employee_ID": range(101, 111),

    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha", "Arjun",
        "Neha", "Rohan", "Ananya", "Vikas", "Karan"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "HR", "Marketing", "IT", "Finance"
    ],

    "Salary": [
        95000, 55000, 85000, 70000, 120000,
        65000, 80000, 90000, 60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ]
})
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Performance"].mean())
print(df.groupby("Department")["Experience"].mean())
print(df["Department"].value_counts())
print(df.groupby("Department")["Salary"].mean().idxmax())
print(df.groupby("Department")["Salary"].mean().idxmin())
print(df.groupby("Department")["Performance"].mean().idxmax())
print(df.groupby("Department")["Performance"].mean().idxmin())
print(df["Department"].value_counts().idxmax())
print(df.groupby("Department")["Experience"].mean().idxmax())
