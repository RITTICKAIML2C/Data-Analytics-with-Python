# # 🚀 Mini Project — Employee Promotion Analysis
# # Step 1 — Department Code Use .map(): IT → 101, HR → 102, Finance → 103, Marketing → 104
# # Step 2 — Performance Flag, Create: High_Performer, Rules: Performance >= 90 → True, Otherwise → False
# # Step 3 — Experience Flag, Create: Experienced_Employee, Rules: Experience >= 5 → True, Otherwise → False
# # Step 4 — Salary Flag, Create: High_Salary. Rules: Salary >= 80000 → True, Otherwise → False
# # Step 5 — Promotion Eligibility, Create: Promotion_Eligible, Rules: Performance >= 90 AND Experience >= 5
# # 📊 Business Analysis : After creating the features, find: 1. Number of high performers, 2. Number of experienced employees, 3. Number of high-salary employees, 4. Number of promotion-eligible employees, 5. List all promotion-eligible employees, 6. Department with the most promotion-eligible employees
# # ⭐ Bonus Challenge : Find employees who satisfy all three: High Performer + High Salary + Experienced Employee
# # Then answer in words: Which employees are strong candidates for promotion based on performance, salary level and experience?
import pandas as pd 
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Arjun",
             "Neha", "Rohan", "Ananya", "Vikas", "Karan"],
    "Department": ["IT", "HR", "Finance", "Marketing", "IT",
                    "Finance", "HR", "Marketing", "IT", "Finance"],
    "Salary": [85000, 65000, 90000, 75000, 95000,
               70000, 82000, 88000, 60000, 100000],
    "Performance": [92, 85, 95, 88, 91,
                     78, 93, 96, 82, 94],
    "Experience": [6, 4, 7, 3, 8,
                   2, 5, 6, 4, 9]
}

df = pd.DataFrame(data)

# Step 1: Department Code
df["Department_Code"] = df["Department"].map({
    "IT": 101,
    "HR": 102,
    "Finance": 103,
    "Marketing": 104
})

# Step 2: High Performer
df["High_Performer"] = df["Performance"] >= 90

# Step 3: Experienced Employee
df["Experienced_Employee"] = df["Experience"] >= 5

# Step 4: High Salary
df["High_Salary"] = df["Salary"] >= 80000

# Step 5: Promotion Eligible
df["Promotion_Eligible"] = (
    (df["Performance"] >= 90) &
    (df["Experience"] >= 5)
)

print(df)

# 1. Number of high performers
print(df["High_Performer"].sum())

# 2. Number of experienced employees
print(df["Experienced_Employee"].sum())

# 3. Number of high-salary employees
print(df["High_Salary"].sum())

# 4. Number of promotion-eligible employees
print(df["Promotion_Eligible"].sum())

# 5. Promotion-eligible employees
print(df[df["Promotion_Eligible"]])

# 6. Department with most promotion-eligible employees
print(df[df["Promotion_Eligible"]].groupby("Department").size())

strong = df[
    (df["High_Performer"]) &
    (df["High_Salary"]) &
    (df["Experienced_Employee"])
]

print(strong)

# The strong promotion candidates are:

# Amit, Priya, Arjun, Rohan, Ananya, and Karan.

# They meet all three conditions: high performance + high salary + 5 or more years of experience
