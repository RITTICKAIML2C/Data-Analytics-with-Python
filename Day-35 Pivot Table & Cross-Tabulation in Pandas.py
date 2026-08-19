# # Pivot Table Index 
pd.pivot_table(df, values="Salary", index="Department",aggfunc="mean")

# # Example : 
import pandas as pd
pivot = pd.pivot_table(df, values="Salary", index="Department", aggfunc="mean")
print(pivot)

# # Multiple Aggregations 
pd.pivot_table(df, values="Salary", index="Department", aggfunc=["mean","max","min","count"])

# # Multiple Values 
pd.pivot_table(df, values=["Salary","Performance"], index="Department", aggfunc="mean")

# # Using Columns 
pd.pivot_table(df, values="Salary", index="Department", columns="Gender", aggfunc="mean")

# # Filling Missing Values
pd.pivot_table(df, values="Salary", index="Department", columns="Gender", aggfunc="mean", fill_value=0)

# # Margins (Totals) - Adds an All row
pd.pivot_table(df, values="salary", index="Department", aggfunc="mean", margins=True)

# # Crosstab - counts occurrences 
pd.crosstab(df["Department"], df["Gender"])

# # Normalize - To get percentages
pd.crosstab(df["Department"], df["Gender"], normalize="index")

