# 1. Check Duplicates 
df.duplicated().sum()

# Remove Duplicates
df = df.drop_duplicates()

# 2. Check Missing Valyes 
df.isna().sum()

# Missing Percentage
df.isna().mean() * 100

# 3. Check Invalid Values 
df[df["Sales"] < 0]

# 4. Check Unique Values 
df["Category"].unique()
df["Category"].value_counts()

