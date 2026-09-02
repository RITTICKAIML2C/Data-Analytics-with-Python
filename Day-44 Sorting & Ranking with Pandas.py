# # 1. sort_values()
# # a. lowest -> highest 
df.sort_values("Salary")

# # b. highest -> lowest 
df.sort_values("Salary", ascending = False)

import pandas as pd 
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Rahul", "Neha", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [60000, 45000, 75000, 70000, 52000]
})
print(df.sort_values("Salary", ascending = False))

# # 2. Sorting by Multiple Columns
df.sort_values(
    ["Department", "Salary"], 
    ascending = [True, False]
)

# # 3. rank() - gvies every row a ranking 
df["Salary_Rank"] = df["Salary"].rank(ascending = False)

# # 4. Top N Records 
df.nlargest(3, "Salary")      # Give the top 3 salaries
df,nsmallest(3, "Salary")     # Give the botto 3 salaries 
