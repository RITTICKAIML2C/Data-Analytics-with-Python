# # 1. dropna() 
import pandas as pd
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [50000, None, 70000, None, 80000],
    "Sales": [1000, None, 5000, 3000, 10000],
    "Performance": [85, 90, None, 75, None]
})
print(df)

# # a. Find Missing Values - 
print(df.isna().sum())

# # b. Remove rows containing any missing values 
print(df.dropna()) # removes rows where at least one value is missing 

# # c. how="all" - removes a row only if every value in that row is missing.
print(df.dropna(how="all"))

# # d. Remove rows based on specific columns 
print(df.dropna(subset=["Salary"])) # removes employees whose salary is missing 

# # e. You can use multiple columns 
print(df.dropna(subset=["Salary", "Performance"])) # keeps only employees who have both salary and performance available 

# # 2. Advanced fillna() - df["Salary"].fillna(df["Salary"].emdian())
# # a. Fill with a fixed value 
df["Performance"] = df["Performance"].fillna(0)

# # b. Fill Multiple Columns differently 
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
print(df)

# # 3. Forward Dill & Backward Fill 
# # a. Forward Fill - a missing value gets the previous available value
df["Sales"] = df["Sales"].ffill() 

# # b. Backward Fill - the missing value gets the next available value 
df["Sales"] = df["Sales"].bfill()
print(df)

# # 4. Duplicate Data - real datasets frequently contains duplicate records 
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Priya", "Priya", "Sneha", "Arjun"],
    "Salary": [50000, 60000, 70000, 70000, 55000, 80000]
})

# # a. Detect Duplicate 
print(df.duplicated())

# # b. Show duplicate rows 
print(df[df.duplicated()])

# # c. Remove duplicates 
df = df.drop_duplicates()
print(df)

# # d. Duplicate based on a specific column 
print(df[df.duplicated("Employee_ID", keep=False)]) # keep = False marks all occurences of duplicates as True 

# # 5. Data Validation 
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Salary": [50000, -60000, 70000, 8000000, 55000],
    "Performance": [85, 92, 110, 78, -5],
    "Experience": [3, 5, -2, 4, 50]
})

# # a. Invalid Salary 
print(df[df["Salary"] <= 0])

# # b. Suspiciously high salary 
print(df[df["Salary"]> 1000000])

# # c. Invalid Performance - if performance is supposed to be between 0 and 100
print(df[(df["Performance"] < 0) | (df["Performance"] > 100)])

# # d. Invalid Experience 
print(df[(df["Experience"] < 0) | (df["Experience"] > 40)])
print(df)
