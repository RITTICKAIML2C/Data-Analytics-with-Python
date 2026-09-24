# # 🏭 Industrial Practice — Employee Risk Analysis
# # Step 1 — Create Performance_Category, Use np.select(): >= 90 → Excellent, >= 75 → Good, >= 60 → Average, < 60 → Poor
# # Step 2 — Create Risk_Flag Use these rules: Performance < 60        → "High Risk", Performance < 75        → "Medium Risk", Performance >= 75        → "Low Risk". Use np.select().
# # Step 3 — Create Promotion_Ready - An employee is promotion-ready if: Performance >= 90 AND Experience >= 5 AND Salary >= 80000
# # Create a Boolean column: Promotion_Ready
# # 📊 Step 4 — Business Analysis Find: 1. Number of employees in each Performance_Category, 2. Number of employees in each Risk_Flag, 3. Number of promotion-ready employees, 4. List all promotion-ready employees, 5. Highest-performing employee, 6. Highest-paid employee, 7. Department with the highest average performance, 8. Department with the highest average salary.
# # 🔥 Step 5 — Advanced Filtering, Using .query(), find: A. Excellent performers earning more than ₹80,000, B. Employees with: Performance < 75 AND Experience < 5, C. Employees with: Salary >= 100000 OR Performance >= 95, D. Employees who are not promotion-ready.
# # 💼 Step 6 — Analyst Questions: Don't just print the Pandas output. Write actual conclusions: Which employee is the strongest promotion candidate? Which employees require performance development? Which department appears strongest based on average performance? Which department has the highest average salary? How many employees are at high risk? What percentage of employees are promotion-ready?. For percentage: (df["Promotion_Ready"].sum() / len(df)) * 100
# # ⭐ Bonus Challenge ; Create a new column:
# # Employee_Segment with these rules: Performance >= 90 AND Experience >= 8 → "Leadership Ready", Performance >= 90 AND Experience >= 5→ "High Potential", Performance >= 75 AND Experience >= 4 → "Strong Performer", Performance >= 60 → "Developing", Performance < 60 → "Needs Improvement". Important: Put the most specific condition first. This is the exact concept you've been practicing with np.select().
import numpy as np 
import pandas as pd 

df = pd.DataFrame({
    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha",
        "Arjun", "Neha", "Rohan", "Ananya",
        "Vikas", "Karan"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "HR", "Marketing",
        "IT", "Finance"
    ],

    "Salary": [
        95000, 55000, 85000, 70000,
        120000, 65000, 80000, 90000,
        60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ]
})
conditions = [df["Performance"] >= 90, df["Performance"] >= 75, df["Performance"] >= 60]
choices = ["Excellent", "Good", "Average"]
df["Performance_Category"] = np.select(conditions, choices, default="Poor")

conditions = [df["Performance"] < 60, df["Performance"] < 75]
choices = ["High Risk", "Medium Risk"]
df["Risk_Flag"] = np.select(conditions, choices, default="Low Risk")

df["Promotion_Ready"] = (df["Performance"] >= 90) & (df["Experience"] >= 5) & (df["Salary"] >= 80000)

# 1
df["Performance_Category"].value_counts()

# 2
df["Risk_Flag"].value_counts()

# 3
df["Promotion_Ready"].sum()

# 4
df.query("Promotion_Ready")["Employee"]

# 5
df.loc[df["Performance"].idxmax(), "Employee"]

# 6
df.loc[df["Salary"].idxmax(), "Employee"]

# 7
df.groupby("Department")["Performance"].mean().idxmax()

# 8
df.groupby("Department")["Salary"].mean().idxmax()

# A
df.query('Performance_Category == "Excellent" and Salary > 80000')

# B
df.query("Performance < 75 and Experience < 5")

# C
df.query("Salary >= 100000 or Performance >= 95")

# D
df.query("not Promotion_Ready")

# 1
df.loc[df["Promotion_Ready"], "Employee"]

# 2
df.query("Performance < 75")["Employee"]

# 3
df.groupby("Department")["Performance"].mean().idxmax()

# 4
df.groupby("Department")["Salary"].mean().idxmax()

# 5
df.query('Risk_Flag == "High Risk"').shape[0]

# 6
(df["Promotion_Ready"].sum() / len(df)) * 100

conditions = [
    (df["Performance"] >= 90) & (df["Experience"] >= 8),
    (df["Performance"] >= 90) & (df["Experience"] >= 5),
    (df["Performance"] >= 75) & (df["Experience"] >= 4),
    df["Performance"] >= 60
]

choices = ["Leadership Ready", "High Potential", "Strong Performer", "Developing"]

df["Employee_Segment"] = np.select(conditions, choices, default="Needs Improvement")
