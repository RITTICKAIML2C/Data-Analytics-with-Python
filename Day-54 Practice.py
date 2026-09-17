 # # 🏭 Industrial Practice — Employee Data Quality
# # 🔎 Step 1 — Data Quality Find: Missing values in every column, Total missing values, Duplicate rows, Duplicate Employee IDs, Employees with missing Salary, Employees with missing Performance, Employees with missing Experience
# # 🧹 Step 2 — Data Validation Find: Employees with salary <= 0, Employees with salary suspiciously above 1,000,000, Employees with Performance < 0, Employees with Performance > 100, Employees with Experience < 0, Employees with Experience > 40. Don't modify the data yet. Just identify the problems.
# # 🛠️ Step 3 — Clean the Dataset You decide the appropriate strategy. Requirements: Remove the duplicate record. Handle missing Salary, Handle missing Performance, Handle missing Experience, Handle invalid Salary, Handle invalid Performance, Handle invalid Experience. Then verify: print(df.isna().sum()) and confirm that your cleaned dataset contains no invalid values.
# # 📊 Step 4 — Business Analysis : After cleaning, calculate: Department analysis, Average Salary by Department, Average Performance by Department, Employee Count by Department
# # Find: Highest average salary department, Highest average performance department, Highest-paid employee, Highest-performing employee, Department with the most employees
# # ⭐ Step 5 — Business Insights : Don't just print Pandas output. Write actual conclusions such as: "IT has the highest average salary among the departments.", "The highest-performing employee belongs to the Finance department."
import pandas as pd

df = pd.DataFrame({
    "Employee_ID": [
        101, 102, 103, 103, 104,
        105, 106, 107, 108, 109
    ],

    "Name": [
        "Amit", "Rahul", "Priya", "Priya", "Sneha",
        "Arjun", "Neha", "Vikash", "Rohan", "Pooja"
    ],

    "Department": [
        "IT", "HR", "Finance", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing", "IT"
    ],

    "Salary": [
        70000, None, 85000, 85000, -5000,
        90000, 60000, None, 75000, 8000000
    ],

    "Performance": [
        85, 90, None, None, 78,
        95, 88, 82, 105, -10
    ],

    "Experience": [
        3, 5, 7, 7, 4,
        6, None, 5, 50, 2
    ]
})
print(df)
print(df.isna().sum())
print(df.isna().sum().sum())
print(df[df.duplicated()])
print(df[df["Employee_ID"].duplicated(keep=False)])
print(df[df["Salary"].isna()])
print(df[df["Performance"].isna()])
print(df[df["Experience"].isna()])

print(df[df["Salary"] <= 0])
print(df[df["Salary"] > 1000000])
print(df[df["Performance"] < 0])
print(df[df["Performance"] > 100])
print(df[df["Experience"] < 0])
print(df[df["Experience"] > 40])

df = df.drop_duplicates()
df.loc[df["Salary"] <= 0, "Salary"] = None
df.loc[df["Salary"] > 1000000, "Salary"] = None
df.loc[(df["Performance"] < 0) | (df["Performance"] > 100), "Performance"] = None
df.loc[(df["Experience"] < 0) | (df["Experience"] > 40), "Experience"] = None
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].median())
df["Experience"] = df["Experience"].fillna(df["Experience"].median())
print(df.isna().sum())

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Performance"].mean())
print(df["Department"].value_counts())
print(df.loc[df["Salary"].idxmax()])       
print(df.loc[df["Performance"].idxmax()])  

# Highest average salary: IT.
# Highest average performance: Finance.
# Highest-paid employee: Arjun (₹90,000).
# Highest-performing employee: Arjun (95).
# Most employees: IT and Finance are tied with 3 employees each.
# No missing or invalid values remain after cleaning.
