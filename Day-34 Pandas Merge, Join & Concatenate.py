# # 1. pd.merge()
# pd.merge(left_df, right_df, on="Common_Column")
import pandas as pd 
employees = pd.DataFrame({
    "Employee_ID":[101,102,103],
    "Name":["Aman","Riya","Rahul"]
})
salary = pd.DataFrame({
    "Employee_ID":[101,102,103],
    "Salary":[50000,60000,70000]
})
result = pd.merge(employees, salary, on="Employee_ID")
print(result)

# # 2. Type of Merge 
# # (a) Inner Merge (Default) : Returns only matching records.
pd.merge(df1, df2, on="Employee_ID", how="inner")

# # (b) Left Merge : Keeps all rows from the left DataFrame.
pd.merge(df1, df2, on="Employee_ID", how="left")

# # (c) Right Merge : Keep all rows from the right DataFrame
how="right"

# # (d) Outer Merge : Keeps Everything 
how="outer"

# # 3. Merge on Different Column Names. Sometimes the common columns have different names.
pd.merge(employees, salary, left_on="Employee_ID", right_on="ID")

# # 4. Multiple Key Merge 
pd.merge(df1, df2, on=["Department", "Year"])

# # 5. concat() - used for stacking DataFrames
# # a. Vertical - rows are added 
pd.concat([df1, df2])

# # b. Horizontal - columns are added
pd.concat([df1, df2], axis=1)

# # 6. join() - works mainly with indexes.
df1.join(df2)

# # 7. Important Paramters 
# # a. common column : on= 
# # b. Merge type : how=
# # c. Different Column Names : left_on=
# # d. Rename Duplicate Column Names: suffixes=
