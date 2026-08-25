# # 🚀 Mini Project — Employee Performance Dashboard
# # Create a DataFrame with 10 employees: Employee_ID, Department, Experience, Salary, Performance
# # Use departments: IT, HR, Finance, Marketing
# # Your dashboard should calculate:
# # 📊 Analysis : Average Salary, Average Performance, Highest Salary, Highest Performance
# # 📈 Visualization : Create two scatter plots: 1. Experience vs Salary, 2. Salary vs Performance
# # Each plot should contain: Title, X-axis, Y-axis, Grid
# # ⭐ Business Insights : Find: Highest-paid employee, Highest-performing employee, Department with highest average salary 

import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108,
                    109, 110, 111, 112],
    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing"
    ],
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 6, 7],
    "Salary": [
        32000, 35000, 42000, 40000,
        55000, 48000, 68000, 62000,
        85000, 45000, 72000, 70000
    ],
    "Performance": [
        65, 70, 78, 74,
        86, 82, 91, 88,
        96, 79, 94, 92
    ]
})
print(df)
print(df["Salary"].mean())
print(df["Performance"].mean())
print(df["Salary"].max())
print(df["Performance"].max())

plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid()
plt.show()

plt.scatter(df["Salary"], df["Performance"])
plt.title("Salary vs Performance")
plt.xlabel("Salary")
plt.ylabel("Performance")
plt.grid()
plt.show()

print(df.loc[df["Salary"].idxmax(), "Employee_ID"])
print(df.loc[df["Performance"].idxmax(), "Employee_ID"])

department_salary = df.groupby("Department")["Salary"].mean()
highest_salary_department = department_salary.idxmax()
highest_department_average = department_salary.max()
print(highest_salary_department, highest_department_average)
