# # 🚀 MINI PROJECT — Employee Development & Compensation Analysis
# # 🔎 Step 1 — Dataset Analysis
# # Find: Number of employees, Number of departments, Average salary, Average performance, Average experience, Average training hours, Highest salary, Highest performance
# # 🔗 Step 2 — Correlation Analysis Find the correlation between: Salary and Performance Salary and Experience, Performance and Experience, Training Hours and Performance, Training Hours and Experience
# # Also print: df.corr(numeric_only=True)
# # 🏆 Step 3 — Employee Rankings Find: Top 3 highest-paid employees, Top 3 highest performers, Top 3 most experienced employees, Top 3 employees with the highest training hours, Bottom 3 employees by salary
# # 📊 Step 4 — Department Analysis Calculate: Average salary by department, Average performance by department, Average experience by department, Average training hours by department ,Employee count by department
# # Then find: Department with the highest average salary, Department with the highest average performance, Department with the highest average experience, Department with the highest average training hours, Department with the most employees
# # ⭐ Step 5 — Business Insights Write actual conclusions for: Does experience appear related to salary?, Does training appear related to performance?, Which department has the strongest employee performance?, Which department invests the most in training?, Who appears to be the strongest overall employee?. Who appears to be the most experienced high performer?, Which employees might be strong candidates for leadership?
import pandas as pd

df = pd.DataFrame({
    "Employee_ID": range(101, 113),

    "Employee": [
        "Aman", "Riya", "Rahul", "Priya",
        "Karan", "Neha", "Vikas", "Anjali",
        "Rohan", "Sneha", "Arjun", "Meera"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "HR", "Marketing",
        "IT", "Finance", "HR", "IT"
    ],

    "Salary": [
        85000, 60000, 70000, 95000,
        55000, 90000, 75000, 110000,
        80000, 65000, 120000, 88000
    ],

    "Performance": [
        95, 82, 76, 92,
        65, 94, 85, 98,
        88, 72, 97, 90
    ],

    "Experience": [
        8, 4, 5, 10,
        2, 7, 6, 12,
        5, 3, 11, 9
    ],

    "Training_Hours": [
        45, 22, 30, 48,
        15, 42, 35, 55,
        32, 20, 60, 46
    ]
})
# Number of employees
print("Number of employees:", df["Employee"].count())

# Number of departments
print("Number of departments:", df["Department"].nunique())

# Average salary
print("Average salary:", df["Salary"].mean())

# Average performance
print("Average performance:", df["Performance"].mean())

# Average experience
print("Average experience:", df["Experience"].mean())

# Average training hours
print("Average training hours:", df["Training_Hours"].mean())

# Highest salary
print("Highest salary:", df["Salary"].max())

# Highest performance
print("Highest performance:", df["Performance"].max())

print("Salary ↔ Performance:",
      df["Salary"].corr(df["Performance"]))

print("Salary ↔ Experience:",
      df["Salary"].corr(df["Experience"]))

print("Performance ↔ Experience:",
      df["Performance"].corr(df["Experience"]))

print("Training Hours ↔ Performance:",
      df["Training_Hours"].corr(df["Performance"]))

print("Training Hours ↔ Experience:",
      df["Training_Hours"].corr(df["Experience"]))

print("\nFull Correlation Matrix:")
print(df.corr(numeric_only=True))

print(df.nlargest(3, "Salary")[["Employee", "Salary"]])

print(df.nlargest(3, "Performance")[["Employee", "Performance"]])

print(df.nlargest(3, "Experience")[["Employee", "Experience"]])

print(df.nlargest(3, "Training_Hours")[["Employee", "Training_Hours"]])

print(df.nsmallest(3, "Salary")[["Employee", "Salary"]])

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Performance"].mean())

print(df.groupby("Department")["Experience"].mean())

print(df.groupby("Department")["Training_Hours"].mean())

print(df.groupby("Department")["Employee"].count())

# 1. Yes
# 2. Yes, Strongly 
# 3. Marketing 
# 4. Marketing 
# 5. Anjali 
# 6. Anjali 
# 7. Anjali, Arjun, Priya
