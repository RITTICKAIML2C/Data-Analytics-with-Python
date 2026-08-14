# # Mini Project - Employee Data Exploration Dashboard
# # 🔹 1. Dataset Overview : Original DataFrame, First 5 rows, Last 3 rows, Shape, Columns, Data types, info(), describe()
# # 🔹 2. Salary Analytics Calculate: Average salary Median salary Highest salary Lowest salary Employees earning > $50,000 Employees earning > $60,000
# # 🔹 3. Performance Analytics Calculate: Average performance Highest performance Lowest performance Employees scoring ≥ 85 Employees scoring < 70
# # 🔹 4. Experience Analytics Find: Average experience Highest experience Employees with ≥ 5 years experience
# # 🔹 5. Advanced Filtering Find employees who satisfy: Salary > $50,000 AND Performance >= 85 Then: Experience >= 5 OR Performance >= 90
# # 🔹 6. Column Selection Display only: Name Department Salary Performance for employees earning more than $50,000.
# # ⭐ Bonus Using loc and iloc, manually retrieve: First employee Last employee Salary of the 5th employee Name + Salary of employees 3–7
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
print(df.info())
print(df.describe())

print("Average Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print(df.loc[df["Salary"] > 50000])
print(df.loc[df["Salary"] > 60000])

print("Average Performance:", df["Performance"].mean())
print("Highest Performance:", df["Performance"].max())
print("Lowest Performance:", df["Performance"].min())
print(df[df["Performance"] >= 85])
print(df[df["Performance"] < 70])

print("Average Experience:", df["Experience"].mean())
print("Highest Experience:", df["Experience"].max())
print(df[df["Experience"] >= 5])

print(df.loc[
    (df["Salary"] > 50000) &
    (df["Performance"] >= 85)
])
print(df.loc[
    (df["Experience"] >= 5) |
    (df["Performance"] >= 90)
])

print(df.loc[
    df["Salary"] > 50000,
    ["Name", "Department", "Salary", "Performance"]
])

print(df.loc[0])
print(df.loc[7])
print(df.loc[4, "Salary"])
print(df.loc[2:6, ["Name", "Salary"]])

print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[4, 3])
print(df.iloc[2:7, [1, 3]])
