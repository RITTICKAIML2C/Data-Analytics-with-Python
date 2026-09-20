import pandas as pd 
# # 1. Department Mapping
# # Create : Department_Code
# # Using : IT → 101, HR → 102, Finance → 103, Marketing → 104. Use .map() 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan", "Neha"],
    "Department": [
        "IT", "HR", "Finance", "IT", "Marketing", "Finance"
    ]
})
df["Department_Code"] = df["Department"].map({
    "IT" : 101, 
    "HR" : 102, 
    "Finance" : 103,
    "Marketing" : 104
})
print(df)

# # 2. Department Replacement
# # Using Same DataFrame replace
# # IT → Information Technology, HR → Human Resources, Finance → Finance Department, Marketing → Marketing Department. Use .replace()
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya", "Karan", "Neha"],
    "Department": [
        "IT", "HR", "Finance", "IT", "Marketing", "Finance"
    ]
})
df["Department"] = df["Department"].replace({
    "IT" : "Information Technology", 
    "HR" : "Human Resources",
    "Finance" : "Finance Department",
    "Marketing" : "Marketing Department"
})
print(df)

# # 3. Employee Business Flags 
# # Create these Boolean columns: High_Performer Performance >= 90, Experienced_Employee : Experience >= 5, High_Salary : Salary >= 80000
# # Promotion_Eligible : Employee must have: Performance >= 90 AND Experience >= 5
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
df["High_Performer"] = df["Performance"] >= 90
df["Experienced_Employee"] = df["Experience"] >=5 
df["High_Salary"] = df["Salary"] >= 80000
df["Promotion_Eligible"] = (
    (df["Performance"] >= 90) & 
    (df["Experience"] >= 5)
)
print(df)
