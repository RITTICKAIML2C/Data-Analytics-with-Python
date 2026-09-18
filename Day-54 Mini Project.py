# # 🔥Mini Challenge
# # After completing everything above, create a final Data Quality Report containing: Original rows: Duplicate rows removed: Missing values before cleaning: Missing values after cleaning: Invalid salary records: Invalid performance records: Invalid experience records: Final number of employees:
# # Then answer:
# # 💼 Analyst Question : Would you perform business analysis on the original dataset before cleaning it? Why or why not?
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

# Original rows: 10
# Duplicate rows removed: 1
# Missing values before cleaning: 5
# Missing values after cleaning: 0
# Invalid salary records: 2
# Invalid performance records: 2
# Invalid experience records: 1
# Final number of employees: 9

# No. I would clean and validate the dataset first, because missing values, duplicate employees, negative salary, performance above 100, and unrealistic experience could produce incorrect averages, employee rankings, and business conclusions.
