# # 1. map() - is useful when you want to convert values from oen category into another value 
import pandas as pd 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"]
})
df["Department_Code"] = df["Department"].map({
    "IT" : 101, 
    "HR" : 102, 
    "Finance" : 103
})
print(df)

# # 2. replace() - is useful when you want to rename or substitute existing values.
import pandas as pd 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"]
})
df["Department"] = df["Department"].replace({
    "IT" : "Information Technology", 
    "HR" : "Human Resources", 
    "Finance" : "Finance Department"
})
print(df)

# # 3. Boolean Features - True / False
import pandas as pd 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"]
})
df["High_Performer"] = df["Performance"] >= 90

# # 4. Business Flags 
df["Salary_Above_Average"] = (df["Salary"] > df["Department_Avg_Salary"])

# # 5. Promotion Eligibility 
df["Promotion_Eligible"] = (
    (df["Performnce"] >= 90) &
    (df["Experience"] >= 5)
)


