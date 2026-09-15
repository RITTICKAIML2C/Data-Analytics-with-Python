# # 1. Detect Missing Values
# df.isna() - gives True if a value is missing 
# df.isna().sum() or df.isnull().sum() - number of missing values per column (both are same)
import pandas as pd 
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [50000, None, 70000, 60000, None],
    "Performance": [80, 85, None, 90, 75]
})
print(df)
print(df.isna().sum())

# # 2. Find Rows with Missing values
# # a. Find Employee whose salary is missing : 
df[df["Salary"].isna()]

# # b. Find Employee whose salary is not missing : 
df[df["Salary"].notna()]

# # 3. Filling Missing Values 
# # a. Suppose salary has missing values You can replace them with a specific value: 
df["Salary"] = df["Salary"].fillna(50000)

# # b. For numerical data, we often use: 
Mean : df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
Median : df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# # 4. Drop Missing Values - to remove rows containing missing values : df.dropna()
TO remove rows only when salary is missing : df.dropna(subset = ["Salary"])
