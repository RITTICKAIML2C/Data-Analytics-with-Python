import numpy as np 
import pandas as pd 
# # 1. Performance Level 
# # Create: Performance_Level
# # Rules: Performance >= 90 → Excellent, Performance >= 75 → Good, Performance >= 60 → Average, Performance < 60  → Poor. Use np.select().
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan", "Neha"],
    "Performance": [95, 82, 68, 55, 90, 73]
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
df["Performance_Level"] = np.select(conditions, choices, default="Unknown")
print(df)

# # 2. Employee Level 
# # Create: Employee_Level
# # Rules: Experience >= 8 → Senior, Experience >= 5 → Mid-Level, Experience < 5  → Junior. Use np.select().
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    "Experience": [
        10, 6, 3, 8, 2, 5
    ]
})
conditions = [
    df["Experience"] >= 8, 
    df["Experience"] >= 5, 
    df["Experience"] < 5
]
choices = [
    "Senior", 
    "Mid-Level", 
    "Junior"
]
df["Employee_Level"] = np.select(conditions, choices, default="Other")
print(df)

# # 3. Salary Brand 
# # Create: Salary_Band
# # Rules: Annual Salary >= 1,200,000 → Premium, Annual Salary >= 900,000   → High, Annual Salary >= 700,000   → Medium, Annual Salary < 700,000    → Low. Use np.select().
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul",
        "Priya", "Karan", "Neha"
    ],
    "Annual_Salary": [
        1200000, 850000, 650000,
        1500000, 550000, 950000
    ]
})
conditions = [
    df["Annual_Salary"] >= 1200000,
    df["Annual_Salary"] >= 900000, 
    df["Annual_Salary"] >= 700000, 
    df["Annual_Salary"] < 700000
]
choices = [
    "Premium", 
    "High",
    "Medium", 
    "Low"
]
df["Salary_Band"] = np.select(conditions, choices, default="Other")
print(df)

# # 4. Business Classification 
# # Create : Employee_Category
# # Use these rules:Performance >= 90 AND Experience >= 8 → "Star Employee", Performance >= 90 AND Experience < 8 → "High Performer", Performance >= 75 AND Experience >= 5 → "Reliable Employee", Performance >= 60 → "Average Employee", Performance < 60 → "Needs Improvement"
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
    (df["Performance"] >= 90) & (df["Experience"] >= 8), 
    (df["Performance"] >= 90) & (df["Experience"] < 8),
    (df["Performance"] >= 75) & (df["Experience"] >= 5),
    (df["Performance"] >= 60),
    (df["Performance"] < 60)
]
choices = [
    "Star Employee", 
    "High Performer",
    "Reliable Payment", 
    "Average Employee", 
    "Needs Improvement"
]
df["Employee_Category"] = np.select(conditions, choices, default="Other")
print(df)
