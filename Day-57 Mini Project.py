# # 🚀 Mini Project — Employee Business Classification System
# # Step 1 — Performance Category Create: Performance_Category, Rules: >= 90 → Excellent, >= 75 → Good, >= 60 → Average, < 60  → Poor. Use np.select().
# # Step 2 — Experience Category Create: Experience_Category, Rules: >= 8 → Senior, >= 4 → Mid-Level, < 4  → Junior, Step 3 — Salary Category. Create: Salary_Category, Rules: Salary >= 100000 → High, Salary >= 70000  → Medium, Salary < 70000   → Low
# # ⭐ Step 4 — Overall Employee Status: Create: Employee_Status Use these business rules:
# # 🥇 Star Employee: Performance >= 90 AND Experience >= 8 AND Salary >= 100000 🟢 High Potential Performance >= 90 AND Experience >= 5 🔵 Solid Performer Performance >= 75 AND Experience >= 4 🟡 Developing Performance >= 60 🔴 Needs Improvement Performance < 60 Use np.select().
# # 📊 Step 5 — Business Analysis After creating all the features, find: 1. Number of employees in each Performance Category, 2. Number of employees in each Experience Category, 3. Number of employees in each Salary Category. 4. Number of employees in each Employee Status
# # 🏢 Step 6 — Department Analysis Find: Average salary by Employee Status, Average performance by Employee Status, Employee count by Department + Status
# # ⭐ Step 7 — Business Insights: Answer in actual sentences: Which employee status is the most common?, Which department has the most Star Employees? Which department has the most High Potential employees?, Which employee has the highest salary?, Which employee has the highest performance?, What percentage of employees are Excellent performers?, What percentage of employees are Star Employees?
# # 🔥 Bonus Challenge : Find employees who are: Excellent AND Senior AND High Salary
# # Then answer: Which employees are the strongest candidates for leadership or promotion?
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha",
        "Vikas", "Anjali"
    ],
    "Salary": [
        95000, 65000, 55000, 110000,
        50000, 85000, 75000, 120000
    ],
    "Performance": [
        95, 82, 65, 92,
        58, 88, 76, 97
    ],
    "Experience": [
        8, 5, 3, 10,
        2, 6, 4, 12
    ]
})

conditions = [
    df["Performance"] >= 90,
    df["Performance"] >= 75,
    df["Performance"] >= 60,
    df["Performance"] < 60
]

choices = [
    "Excellent",
    "Good",
    "Average",
    "Poor"
]

df["Performance_Category"] = np.select(
    conditions, choices, default="Unknown"
)

conditions = [
    df["Experience"] >= 8,
    df["Experience"] >= 4,
    df["Experience"] < 4
]

choices = [
    "Senior",
    "Mid-Level",
    "Junior"
]

df["Experience_Category"] = np.select(
    conditions, choices, default="Unknown"
)

conditions = [
    df["Salary"] >= 100000,
    df["Salary"] >= 70000,
    df["Salary"] < 70000
]

choices = [
    "High",
    "Medium",
    "Low"
]

df["Salary_Category"] = np.select(
    conditions, choices, default="Unknown"
)

conditions = [
    (df["Performance"] >= 90) &
    (df["Experience"] >= 8) &
    (df["Salary"] >= 100000),

    (df["Performance"] >= 90) &
    (df["Experience"] >= 5),

    (df["Performance"] >= 75) &
    (df["Experience"] >= 4),

    df["Performance"] >= 60,

    df["Performance"] < 60
]

choices = [
    "Star Employee",
    "High Potential",
    "Solid Performer",
    "Developing",
    "Needs Improvement"
]

df["Employee_Status"] = np.select(
    conditions, choices, default="Unknown"
)

print(df)

# 1. Performance Category
print(df["Performance_Category"].value_counts())

# 2. Experience Category
print(df["Experience_Category"].value_counts())

# 3. Salary Category
print(df["Salary_Category"].value_counts())

# 4. Employee Status
print(df["Employee_Status"].value_counts())

# Average salary by status
print(df.groupby("Employee_Status")["Salary"].mean())

# Average performance by status
print(df.groupby("Employee_Status")["Performance"].mean())

# Department + Status
print(df.groupby(["Department", "Employee_Status"]).size())

1. Most common employee status

Solid Performer and Developing are tied as the most common, with 2 employees each.

2. Department with most Star Employees

Cannot determine because the current DataFrame has no Department column.

3. Department with most High Potential employees

Cannot determine for the same reason.

4. Highest salary

Anjali — ₹120,000

5. Highest performance

Anjali — 97

6. Percentage of Excellent performers

There are 3 Excellent performers:

# Aman
# Priya
# Anjali
# 3 / 8 × 100 = 37.5%

# Answer: 37.5%

# 7. Percentage of Star Employees

# Star Employees:

# Anjali
# 1 / 8 × 100 = 12.5%

# Answer: 12.5%

strong_candidates = df[
    (df["Performance_Category"] == "Excellent") &
    (df["Experience_Category"] == "Senior") &
    (df["Salary_Category"] == "High")
]

print(strong_candidates)
# ✅ Result

# Anjali is the strongest leadership/promotion candidate because she has:

# 97 Performance → Excellent
# 12 years Experience → Senior
# ₹120,000 Salary → High

# So the answer is:

# Anjali is the strongest candidate for leadership or promotion based on excellent performance, senior-level experience, and high salary.
