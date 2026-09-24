# 1. Dataset Inspection - 
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()

# 2. nunique() - tells you how many unique values exist
df["Department"].nunique()
For example, our dataset has: IT, HR, Finance, Marketing
So: df["Department"].nunique() returns: 4
You can also use: df.nunique() to inspect every column.

# 3. Statistical EDA
# Calculate: 1. Average salary
df["Salary"].mean()

# 2. Median salary
df["Salary"].median()

# 3. Average performance
df["Performance"].mean()

# 4. Median performance
df["Performance"].median()

# 5. Salary standard deviation
df["Salary"].std()

# 6. Performance standard deviation
df["Performance"].std()

# 4. Department EDA 
# 1. Average salary by department
df.groupby("Department")["Salary"].mean()

# 2. Average performance by department
df.groupby("Department")["Performance"].mean()

# 3. Average experience by department
df.groupby("Department")["Experience"].mean()

# 4. Employee count by department
df["Department"].value_counts()

