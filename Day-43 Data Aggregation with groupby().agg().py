# # 1. What is agg() ?
df.groupby("Department")["Salary"].mean()

df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Employee_Count=("Salary", "count")
)

# # 2. Multiple Columns 
summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Average_Performance=("Performance", "mean"),
    Maximum_Salary=("Salary", "max"),
    Maximum_Performance=("Performance", "max"),
    Employee_Count=("Employee_ID", "count")
)
print(summary)

# # 3. Example 
import pandas as pd 
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Salary": [60000, 70000, 45000, 50000, 65000, 75000],
    "Performance": [85, 92, 78, 84, 88, 95]
})
summary = df.groupby("Department").agg(
    Average_Salary = ("Salary", "mean"), 
    Maximum_Salary = ("Salary", "max"), 
    Average_Performance=("Performance", "mean"),
    Maximum_Performance=("Performance", "max"),
    Employee_Count=("Salary", "count")
)
print(summary)
