# # Mini Project 
# # Employee Analytics Dashboard Create a DataFrame with 8–10 employees: Employee_ID, Department, Salary, Performance, Experience
# # Use departments: IT, HR, Finance, Marketing
# # 📊 Analysis : Calculate: Average Salary, Average Performance, Highest Salary, Highest Performance
# # 📈 Dashboard : Create 2 charts in one figure: Chart 1: Experience → Salary → Scatter plot
# # Chart 2: Salary → Performanc → Scatter plot
# # Each chart should contain: Title, X-axis label, Y-axis label, Grid
# # ⭐ Business Insights : Find Highest-paid employee, Highest-performing employee, Department with highest average salary
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Employee_ID": ["E101", "E102", "E103", "E104", "E105",
                    "E106", "E107", "E108", "E109", "E110"],

    "Department": ["IT", "HR", "Finance", "Marketing", "IT",
                   "Finance", "HR", "Marketing", "IT", "Finance"],

    "Salary": [75000, 52000, 68000, 60000, 82000,
               72000, 55000, 63000, 90000, 78000],

    "Performance": [85, 78, 82, 80, 92,
                    88, 75, 84, 95, 90],

    "Experience": [3, 2, 4, 3, 6,
                   5, 2, 4, 8, 7]
})
average_salary = df["Salary"].mean()
average_performance = df["Performance"].mean()
highest_salary = df["Salary"].max()
highest_performance = df["Performance"].max()
print("Average Salary:", average_salary)
print("Average Performance:", average_performance)
print("Highest Salary:", highest_salary)
print("Highest Performance:", highest_performance)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid()

plt.subplot(1, 2, 2)
plt.scatter(df["Salary"], df["Performance"])
plt.title("Salary vs Performance")
plt.xlabel("Salary")
plt.ylabel("Performance")
plt.grid()
plt.tight_layout()
plt.show()

highest_paid_employee = df.loc[df["Salary"].idxmax(), "Employee_ID"]
highest_performing_employee = df.loc[df["Performance"].idxmax(), "Employee_ID"]
highest_salary_department = df.groupby("Department")["Salary"].mean().idxmax()
print("Highest-paid employee:", highest_paid_employee)
print("Highest-performing employee:", highest_performing_employee)
print("Department with highest average salary:", highest_salary_department)
