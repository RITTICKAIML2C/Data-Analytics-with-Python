# # Mini Project — Employee Analytics Report
# # Create : Employee_ID, Department, Salary, Performance, Experience
# # IT, HR, Finance, Marketing
# # 📊 Build ONE department summary using groupby().agg()
# # Calculate: Average Salary, Median Salary, Maximum Salary, Minimum Salary, Average Performance, Maximum Performance, Average Experience, Employee Count
# # ⭐ Business Insights : Find: Department with the highest average salary Department with the highest average performance Department with the most employees Department with the highest average experience
# # 🔥 Bonus : Find employees whose: Salary > their department's average salary
import pandas as pd
df = pd.DataFrame({
    "Employee_ID": range(1, 11),
    "Department": [
        "IT", "IT",
        "HR", "HR",
        "Finance", "Finance",
        "Marketing", "Marketing",
        "IT", "Finance"
    ],
    "Salary": [
        70000, 80000,
        45000, 50000,
        65000, 75000,
        55000, 60000,
        90000, 85000
    ],
    "Performance": [
        85, 90,
        78, 82,
        88, 92,
        80, 86,
        95, 89
    ],
    "Experience": [
        3, 5,
        2, 4,
        5, 7,
        3, 6,
        8, 6
    ]
})
print(df)
summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Average_Performance=("Performance", "mean"),
    Maximum_Performance=("Performance", "max"),
    Average_Experience=("Experience", "mean"),
    Employee_Count=("Employee_ID", "count")
)
print(summary)

print(summary["Average_Salary"].idxmax())
print(summary["Average_Performance"].idxmax())
print(summary["Employee_Count"].idxmax())
print(summary["Average_Experience"].idxmax())

df["Department_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
above_average = df[df["Salary"] > df["Department_Avg_Salary"]]
print(above_average)
