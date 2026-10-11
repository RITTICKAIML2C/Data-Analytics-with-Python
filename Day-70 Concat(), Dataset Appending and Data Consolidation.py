# 1. pd.concat() 
import pandas as pd 
df1 = pd.DataFrame({
    "Employee": ["Amit", "Riya"],
    "Salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "Employee": ["Rahul", "Priya"],
    "Salary": [55000, 65000]
})
combined = pd.concat([df1, df2])
print(combined)

# 2. ingore_index = True
combined = pd.concat([df1, df2], ignore_index=True)

# 3. Concatenating Rows 
print(pd.concat([df1, df2], axis=0))

# 4. Concatenating Columns 
print(pd.concat([df1, df2], axis=1))

# 5. Different Columns 
import pandas as pd 
df1 = pd.DataFrame({
    "Employee": ["Amit", "Riya"],
    "Salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "Employee": ["Rahul", "Priya"],
    "Department": ["IT", "HR"]
})
print(pd.concat([df1, df2], ignore_index=True))

# 6. join="inner"
print(pd.concat([df1, df2], ignore_index=True, join="inner"))

# 7. Adding a Source Column 
north["Branch"] = "North"
south["Branch"] = "South"
combined = pd.concat([north, south], ignore_index=True)
print(combined)

# 8. keys= 
combined = pd.concat([df1, df2], keys=["January", "February"])
print(combined)


