# # 1. Missing Values
import pandas as pd 
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul"],
    "Salary": [50000, None, 70000]
})

# # 2. Detect Missing Values 
# # a. isna() / isnull()
print(df.isna())
print(df.isnull())

# # b. count missing values
print(df.isna().sum)

# # c. Percentage of Missing Values
print(df.isna().mean() * 100)

# # 3. Find Non-Missing Values 
print(df.notna())

# # 4. Removing Missing Data 
# # a. Remove rows containing any missing values 
print(df.dropna())

# # b. Remove row where a specific column is missing 
print(df.dropna(subset=["Salary"]))

# # c. Remove columns containing missing values 
print(df.dropna(axis=1))

# # d. Remove only completely empty rows 
print(df.dropna(how="all"))

# # 5. Filling Missing Values 
# # a. Fill with a fixed values 
df["Salary"] = df["Salary"].fillna(0)
print(df)

# # b. Mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

# # c. Median 
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df)

# # d. Mode 
df["Salary"] = df["Salary"].fillna(df["Salary"].mode()[0])
print(df)

# # 6. Forward Fill / Backward Fill
# # a. Forward Fill
df["Salary"] = df["Salary"].ffill()
print(df)

# # b. Backward Fill
df["Salary"] = df["Salary"].bfill()
print(df)
