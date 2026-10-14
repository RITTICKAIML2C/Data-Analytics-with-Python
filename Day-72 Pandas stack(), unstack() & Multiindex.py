# 1. stack() - move columns to row 
stacked = df.stack()

# 2. unstack() - rows to columns 
unstacked = stacked.unstack()

# 3. Multiindex - a groupby() can create multiple index level 
result = df.groupby(["Month", "Category"])["Sales"].sum()

