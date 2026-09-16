# # Mini Project - Employee Data Cleaning 
# # 📊 Step 1 — Data Quality Find: Missing values per column, Total missing values, Employees with missing Salary, Employees with missing Performance, Employees with missing Experience
# # 🧹 Step 2 — Cleaning Use: Median Salary → fill missing Salary, Mean Performance → fill missing Performance, Median Experience → fill missing Experience
# # Then verify: df.isna().sum() should show zero missing values for those columns.
# # 📈 Step 3 — Analysis After cleaning, calculate: Average salary by department, Average performance by department, Highest-paid employee, Highest-performing employee, Department with highest average salary, Department with highest average performance
# # ⭐ Step 4 — Business Insights Answer in words: Which department has the highest average salary?, Which department has the highest average performance?, Who is the highest-paid employee?, Who is the highest-performing employee?, How many values were missing before cleaning?, Why did you use median for Salary?, Why did you use mean for Performance?
import pandas as pd

df = pd.DataFrame({

    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],

    "Name": [
        "Amit", "Rahul", "Priya", "Sneha",
        "Arjun", "Neha", "Vikash", "Anjali",
        "Rohan", "Pooja", "Karan", "Meera"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing",
        "IT", "HR", "Finance", "Marketing"
    ],

    "Salary": [
        70000, 55000, None, 65000,
        85000, 60000, 75000, None,
        90000, 58000, 80000, 72000
    ],

    "Performance": [
        85, None, 90, 78,
        95, 88, None, 82,
        92, 75, 89, None
    ],

    "Experience": [
        3, 2, None, 4,
        6, 3, 5, None,
        7, 2, 6, 4
    ]
})


# =========================
# STEP 1 — DATA QUALITY
# =========================

print(df.isna().sum())

print(df.isna().sum().sum())

# Missing Salary
print(df.loc[df["Salary"].isna(), "Name"])

# Missing Performance
print(df.loc[df["Performance"].isna(), "Name"])

# Missing Experience
print(df.loc[df["Experience"].isna(), "Name"])

# Salary NOT missing
print(df.loc[df["Salary"].notna(), "Name"])


# =========================
# STEP 2 — CLEANING
# =========================

print(df["Salary"].median())

print(df["Performance"].mean())

print(df["Experience"].median())


df["Salary"] = df["Salary"].fillna(df["Salary"].median())

df["Performance"] = df["Performance"].fillna(
    df["Performance"].mean()
)

df["Experience"] = df["Experience"].fillna(
    df["Experience"].median()
)


# Verify
print(df.isna().sum())


# =========================
# STEP 3 — ANALYSIS
# =========================

# Average Salary by Department
print(df.groupby("Department")["Salary"].mean())

# Average Performance by Department
print(df.groupby("Department")["Performance"].mean())

# Using agg()
print(
    df.groupby("Department").agg({
        "Salary": "mean",
        "Performance": "mean"
    })
)

# Using transform()
print(
    df.groupby("Department")["Salary"].transform("mean")
)

print(
    df.groupby("Department")["Performance"].transform("mean")
)

# Highest-paid employee
print(df.loc[df["Salary"].idxmax()])

# Highest-performing employee
print(df.loc[df["Performance"].idxmax()])

# Highest average salary department
print(
    df.groupby("Department")["Salary"].mean().idxmax()
)

# Highest average performance department
print(
    df.groupby("Department")["Performance"].mean().idxmax()
)


# =========================
# DROPNA PRACTICE
# =========================

print(df.copy().dropna())
