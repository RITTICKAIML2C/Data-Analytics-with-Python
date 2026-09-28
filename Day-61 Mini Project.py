# # 🚀 MINI PROJECT — Employee Department Performance Dashboard
# # Step 1 — Department Dashboard Create one aggregated DataFrame containing: Average Salary, Maximum Salary, Average Performance, Maximum Performance, Average Experience, Average Training Hours, Employee Count
# # Step 2 — Department Leaders Find: Department with highest average salary, Department with highest average performance, Department with highest average experience, Department with highest average training hours, Department with the most employees
# # Step 3 — Employee Rankings Find: Highest-paid employee, Highest-performing employee, Most experienced employee, Employee with the most training hours, Top 3 employees by salary, Top 3 employees by performance
# # Step 4 — High-Potential Employees Create: High_Potential, Performance >= 90 AND Experience >= 7 AND Training_Hours >= 40
# # Then find: Number of high-potential employees, Names of high-potential employees
# # Step 5 — Department Performance Create a department summary and determine: Which department appears strongest when considering performance + experience + training?, Don't simply use idxmax(). Look at the three metrics together and explain your reasoning.
# # 💼 Step 6 — Business Insights After completing the analysis, write actual conclusions such as: "The IT department has strong employee performance and substantial training investment." "Employees with higher experience and training appear to form a strong high-potential group." But base your conclusions on your actual output.
# # Analyst Question 1 If two departments have similar average performance, but one has significantly higher average training hours, what could that indicate?
# # Analyst Question 2 Why is .agg() more useful than performing five separate groupby() operations?
# # Analyst Question 3 Why should an analyst avoid deciding which department is "best" using only salary?
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
department_dashboard = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Average_Performance=("Performance", "mean"),
    Maximum_Performance=("Performance", "max"),
    Average_Experience=("Experience", "mean"),
    Average_Training_Hours=("Training_Hours", "mean"),
    Employee_Count=("Employee", "count")
)

# Step 2 — Department Leaders
print("Highest Average Salary:", department_dashboard["Average_Salary"].idxmax())
print("Highest Average Performance:", department_dashboard["Average_Performance"].idxmax())
print("Highest Average Experience:", department_dashboard["Average_Experience"].idxmax())
print("Highest Average Training Hours:", department_dashboard["Average_Training_Hours"].idxmax())
print("Most Employees:", department_dashboard["Employee_Count"].idxmax())

# Step 3 — Employee Rankings
print("Highest Paid:", df.loc[df["Salary"].idxmax(), "Employee"])
print("Highest Performing:", df.loc[df["Performance"].idxmax(), "Employee"])
print("Most Experienced:", df.loc[df["Experience"].idxmax(), "Employee"])
print("Most Training Hours:", df.loc[df["Training_Hours"].idxmax(), "Employee"])
print("\nTop 3 by Salary:\n", df.nlargest(3, "Salary")[["Employee", "Salary"]])
print("\nTop 3 by Performance:\n", df.nlargest(3, "Performance")[["Employee", "Performance"]])

# Step 4 — High-Potential Employees
df["High_Potential"] = (
    (df["Performance"] >= 90) &
    (df["Experience"] >= 7) &
    (df["Training_Hours"] >= 40)
)

print("\nHigh-Potential Employee Count:", df["High_Potential"].sum())
print("High-Potential Employees:", df.loc[df["High_Potential"], "Employee"].tolist())

# Step 5 — Department Performance Summary
performance_summary = df.groupby("Department").agg(
    Average_Performance=("Performance", "mean"),
    Average_Experience=("Experience", "mean"),
    Average_Training_Hours=("Training_Hours", "mean")
)

print("\nDepartment Dashboard:\n", department_dashboard)
print("\nDepartment Performance Summary:\n", performance_summary)

# Step 6 — Business Insights
print("\nBusiness Insights:")
print("Marketing appears strongest overall because it performs strongly across performance, experience, and training.")
print("HR has the highest average salary.")
print("High-potential employees have strong performance, significant experience, and substantial training investment.")

# Analyst Question 1 : Higher training hours could indicate greater investment in employee development, which may support better future performance even if current performance is similar.
# Analyst Question 2 : .agg() is more useful because it calculates multiple metrics in one groupby() operation, making the code shorter, cleaner, and easier to analyze.
# Analyst Question 3 : Salary alone doesn't measure department quality. An analyst should also consider performance, experience, productivity, training, and other business metrics.
