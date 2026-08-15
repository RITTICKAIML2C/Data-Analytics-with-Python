import pandas as pd
import numpy as np

# # 1. Missing Values 
# # Display: DataFrame, Missing-value matrix, Missing values per column, Total missing values, Rows without missing Salary 
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Arjun"],
    "Salary": [35000, np.nan, 52000, np.nan, 75000],
    "Performance": [72, 85, np.nan, 88, 95]
})
print(df)
print(df.isna())
print(df.isna().sum())
print(df.isna().isna())
print(df[df["Salary"].notna()])

# # 2. Fill Missing Values 
# # Using the same DataFrame: Fill missing Salary with the mean Salary, Fill missing Performance with the median Performance, Display the cleaned DataFrame
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

df["Performance"] = df["Performance"].fillna(df["Performance"].median())
print(df["Performance"])

print(df)

# # 3. Drop Missing Values 
# # Find: Rows containing missing values DataFrame after dropna() DataFrame after dropping rows where only Salary is missing
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
print(df[df.isna().any(axis = 1)])
print(df.dropna())
print(df.dropna(subset = ["Salary"]))

# # 4. Duplicates 
# # Display: Duplicate rows Number of duplicates DataFrame after removing duplicates
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 103, 104, 105, 105],
    "Name": ["Aman", "Riya", "Rahul", "Rahul", "Neha", "Arjun", "Arjun"],
    "Salary": [35000, 45000, 52000, 52000, 68000, 75000, 75000]
})
print(df[df.duplicated()])
print(df.duplicated().sum())
print(df.drop_duplicates())

# # 5. Create New Columns 
# # Create : Bonus, Annual Salary, where : Bonus = 10% of Salary, Annual Salary = Salary × 12
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, 45000, 52000, 68000]
})
df["Bonus"] = df["Salary"] * 0.10
print(df)

df["Annual Salary"] = df["Salary"] * 12
print(df)

# # 6. apply() 
# # Create a new column: Performance_Level 
# # Performance >= 85 → Excellent, Performance >= 70 → Pass, Performance < 70  → Needs Improvement
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Arjun"],
    "Performance": [68, 75, 91, 88, 95]
})
df["Performance_LeveL"] = df["Performance"].apply(lambda x: "Excellent" if x >= 85 else "Pass" if x >= 70 else "Needs Improvement")
print(df)

# # 7. Sorting 
# # Find : Employees sorted by salary ascending Employees sorted by salary descending Employees sorted by performance descending Top 3 highest-paid employees
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Arjun"],
    "Salary": [35000, 75000, 52000, 68000, 45000],
    "Performance": [72, 95, 91, 88, 85]
})
print(df.sort_values("Salary"))
print(df.sort_values("Salary", ascending = False))
print(df.sort_values("Performance", ascending = False))
print(df.sort_values("Salary", ascending = False).head(3))

# # 8. Categorical Analysis
# # Find : Unique departments, Number of unique departments, Number of employees in each department
# # Use : unique(), nunique(), value_counts()
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Arjun", "Priya"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"]
})
print(df["Department"].unique())
print(df["Department"].nunique())
print(df["Department"].value_counts())

# # Industry Practice - Employee Data Cleaning System
# # Your program should perform:
# # 1️⃣ Inspect : DataFrame, Shape, Data types, Missing values, Duplicate rows
# # 2️⃣ Clean : Remove duplicate rows, Fix "IT " → "IT", Fill missing Salary with median salary, Fill missing Performance with mean performance
# # 3️⃣ Transform : Create:, Annual_Salary, Bonus, Performance_Level
# # 4️⃣ Analyze : Find: Average salary, Median salary, Highest salary, Lowest salary, Department counts, Average salary by department, Top 3 employees by salary, Top 3 employees by performance
# # 5️⃣ Filter : Find employees satisfying: Salary > 50,000 AND Performance >= 85, Then: Experience >= 5 OR Performance >= 90

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 103, 104, 105, 106, 107],
    "Name": ["Aman", "Riya", "Rahul", "Rahul", "Neha", "Arjun", "Priya", "Karan"],
    "Department": ["IT", "HR", "IT ", "IT ", "Finance", "IT", "HR", "Finance"],
    "Salary": [35000, np.nan, 52000, 52000, 68000, 75000, np.nan, 62000],
    "Performance": [72, 85, np.nan, np.nan, 88, 95, 72, 84],
    "Experience": [1, 2, 5, 5, 4, 7, 3, 4]
})
print(df)
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df[df.duplicated()])

df = df.drop_duplicates()
df["Department"] = df["Department"].replace("IT ", "IT")
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
print(df)

df["Annual_Salary"] = df["Salary"] * 12
df["Bonus"] = df["Annual_Salary"] * 0.10
df["Performance_Level"] = df["Performance"].apply(lambda x: "Excellent" if x >= 85 else "Pass" if x >= 70 else "Need Improvement")
print(df)

print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Department"].value_counts())
print(df.sort_values("Salary", ascending=False).head(3))
print(df.sort_values("Performance", ascending=False).head(3))

print(df[df["Salary"] > 50000] * (df["Performance"] >= 85))
print(df[df["Experience"] >=5 | (df["Performance"] >= 90)])

