# # 🚀 Mini Project — Employee Salary Distribution
# # Create a DataFrame with 10–12 employees: Employee_ID, Department, Salary, Performance
# # Use departments: IT, HR, Finance, Marketing
# # 📊 Analysis : Calculate: Average Salary, Median Salary, Highest Salary, Lowest Salary, Average Performance
# # 📈 Visualization : Create exactly 2 charts: Chart 1 — Salary Distribution plt.hist(...)
# # Chart 2 — Performance Distribution : plt.hist(...)
# # Each chart should have: Title, X-axis label, Y-axis label, Appropriate bins
# # ⭐ Business Insight : From your charts, determine:, Where salaries are mainly concentrated, Where performance scores are mainly concentrated.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    
    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "HR", "Marketing"
    ],
    
    "Salary": [
        32000, 38000, 45000, 42000,
        52000, 48000, 60000, 55000,
        68000, 72000, 50000, 80000
    ],
    
    "Performance": [
        65, 72, 78, 75,
        84, 80, 88, 86,
        92, 95, 82, 90
    ]
})
print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Performance"].mean())

plt.hist(df["Salary"], bins = 5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

plt.hist(df["Performance"], bins = 5)
plt.title("Performance Distribution")
plt.xlabel("Performance")
plt.ylabel("Number of Employees")
plt.show()

# Salary concentration : Salaries are mainly concentrated in the middle range, particularly around ₹42,000–₹60,000. There are fewer employees at the very low and very high salary levels.
# Performance concentration : Performance scores are mainly concentrated in the high range, especially around 80–95. The average performance of approximately 83.92 supports this observation.
