# # 1. String Operations 
df["Name"].str.upper()
df["Name"].str.lower()
df["Name"].str.strip()

# # Useful methods 
.str.contains()
.str.startswith()
.str.endswith()
.str.replace()
.str.len()

# # Example 
df[df["Department"].str.contains("IT", na=False)]
na=False prevents missing values from causing problems

# # 2. Duplicates 
# # a. Find Duplicates
df.duplicated()

# # b. Count duplicates 
df.duplicated().sum()

# # c. Remove Duplicates 
df = df.drop_duplicates()

# # d. For specific columns 
df = df.drop_duplicates(subset=["Employee"])

# # 3. Outliers - is an unusually high or low observation 
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[
    (df["Salary"] < lower) |
    (df["Salary"] > upper)
]

# # 4. Date & Time Analysis 
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()

