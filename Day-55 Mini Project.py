# # Mini Project — Employee Feature Engineering
# # 1. Annual Salary, Monthly_Salary × 12
# # 2. Salary Category, Annual Salary >= 1,000,000 → High, Annual Salary >= 700,000   → Medium, Otherwise → Low
# # 3. Performance Category : >= 90 → Excellent, >= 75 → Good, >= 60 → Average, < 60 → Poor
# # 4. Experience Category : >= 8 → Senior, >= 4 → Mid-Level, < 4 → Junior
# # 5. Salary Per Experience : Create: Annual_Salary / Experience
# # 6. Business Analysis : Find: Highest annual salary, Highest salary-per-experience employee, Department with highest average annual salary, Number of Excellent performers, Number of Senior employees, Average annual salary by performance category
# # ⭐ Bonus : Find employees who are: Excellent performers AND High salary AND Senior
import pandas as pd 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Monthly_Salary": [85000, 60000, 50000, 75000, 55000, 95000],
    "Performance": [95, 82, 68, 91, 55, 94],
    "Experience": [9, 5, 3, 8, 2, 10]
})
df["Annual_Salary"] = df["Monthly_Salary"] * 12 

df["Salary_Category"] = df["Annual_Salary"].apply(
    lambda salary: "High" if salary >= 1000000
    else "Medium" if salary >= 700000
    else "Low"
)

df["Performance_Category"] = df["Performance"].apply(
    lambda performance: "Excellent" if performance >= 90
    else "Good" if performance >= 75
    else "Average" if performance >= 60
    else "Poor"
)

df["Experience_Category"] = df["Experience"].apply(
    lambda experience: "Senior" if experience >= 8
    else "Mid-Level" if experience >= 4
    else "Junior"
)

df["Salary_Per_Experience"] = (
    df["Annual_Salary"] / df["Experience"]
)

print(df["Annual_Salary"].max())
print(df.loc[df["Salary_Per_Experience"].idxmax(), "Employee"])
print(df.groupby("Department")["Annual_Salary"].mean())
print(df.groupby("Department")["Annual_Salary"].mean().idxmax())
print((df["Performance_Category"] == "Excellent").sum())
print((df["Experience_Category"] == "Senior").mean())

bonus_employees = df[
    (df["Performance_Category"] == "Excellent") &
    (df["Salary_Category"] == "High") &
    (df["Experience_Category"] == "Senior")
]
print(bonus_employees)

df["Annual_Salary"] = df["Monthly_Salary"] * 12
print(df["Annual_Salary"].max())

print(df.loc[
    df["Salary_Per_Experience"].idxmax(),
    "Employee"
])

index = df["Salary_Per_Experience"].idxmax()
print(df.loc[index, "Employee"])

print((df.groupby("Department")["Annual_Salary"].mean().idxmax()))

print((df["Performance_Category"] == "Excellent").sum())

print(df.groupby("Performance_Category")["Annual_Salary"].mean())

bonus_employees = df[
    (df["Performance_Category"] == "Excellent") &
    (df["Salary_Category"] == "High") &
    (df["Experience_Category"] == "Senior")
]
print(bonus_employees)
