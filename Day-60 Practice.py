import pandas as pd 
# # 1. Basic Correlation 
# # Find : 1. Correlation between Salary and Performance, 2. Correlation between Salary and Experience, 3. Correlation between Performance and Experience
# # Then tell me: Which relationship appears strongest? Are Salary and Experience positively or negatively related?
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    
    "Salary": [
        85000, 60000, 75000,
        95000, 55000, 90000
    ],
    
    "Performance": [
        95, 82, 88,
        92, 65, 94
    ],
    
    "Experience": [
        8, 4, 6,
        10, 2, 7
    ]
})
print(df["Salary"].corr(df["Performance"]))
print(df["Salary"].corr(df["Experience"]))
print(df["Performance"].corr(df["Experience"]))

# 1. Strongest - Salary with Experience
# 2. Positively Related

# # 2. Correlation Matrix 
# # Then answer: Which two variables have the strongest relationship, Which relationship is the weakest?, Is experience more strongly related to salary or performance?
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    
    "Salary": [
        85000, 60000, 75000,
        95000, 55000, 90000
    ],
    
    "Performance": [
        95, 82, 88,
        92, 65, 94
    ],
    
    "Experience": [
        8, 4, 6,
        10, 2, 7
    ]
})
print(df.corr(numeric_only=True))
# 1. Salary & Experience
# 2. 0.8755
# 3. Experience is more strongly related to salary 

# # 3. Ranking Analysis 
# # A. Top 3 highest-paid employees, B. Top 3 performers, C. Top 2 most experienced employees, D. Lowest-paid employee, E. Employee with the lowest performance
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    
    "Salary": [
        85000, 60000, 75000,
        95000, 55000, 90000
    ],
    
    "Performance": [
        95, 82, 88,
        92, 65, 94
    ],
    
    "Experience": [
        8, 4, 6,
        10, 2, 7
    ]
})
print(df.nlargest(3, "Salary"))
print(df.nlargest(3, "Performance"))
print(df.nlargest(2, "Experience"))
print(df.nsmallest(1, "Salary"))
print(df.nsmallest(1, "Performance"))

# # Industrial Practice - Employee Relationship Analysis
# # 📊 Step 1 — Correlation Analysis. Find: Salary ↔ Performance correlation, Salary ↔ Experience correlation, Performance ↔ Experience correlation, Training Hours ↔ Performance correlation, Training Hours ↔ Salary correlation
# # Then print the complete correlation matrix: df.corr(numeric_only=True)
# # 📈 Step 2 — Ranking Analysis Find: Top 3 highest-paid employees, Top 3 highest-performing employees, Top 3 most experienced employees, Top 3 employees with the most training hours, Bottom 3 salaries
# # 💼 Step 3 — Business Questions Answer: Which employee has the highest salary?, Which employee has the highest performance? Which employee has the most experience? Which employee has the most training hours? Does experience appear positively related to salary? Does training appear positively related to performance?
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
        95000, 55000, 85000, 70000, 120000,
        65000, 80000, 90000, 60000, 110000
    ],

    "Performance": [
        94, 72, 91, 68, 97,
        78, 88, 95, 59, 93
    ],

    "Experience": [
        7, 3, 6, 4, 10,
        2, 5, 8, 2, 9
    ],

    "Training_Hours": [
        40, 20, 35, 25, 50,
        30, 32, 45, 18, 48
    ]
})
print(df["Salary"].corr(df["Performance"]))
print(df["Salary"].corr(df["Experience"]))
print(df["Performance"].corr(df["Experience"]))
print(df["Training_Hours"].corr(df["Performance"]))
print(df["Training_Hours"].corr(df["Salary"]))
print(df.corr(numeric_only=True))

print(df.nlargest(3, "Salary"))
print(df.nlargest(3, "Performance"))
print(df.nlargest(3, "Experience"))
print(df.nlargest(3, "Training_Hours"))
print(df.nsmallest(3, "Salary"))

# 1. Arjun
# 2. Arjun
# 3. Arjun
# 4. Arjun
# 5. Yes
# 6. Yes
