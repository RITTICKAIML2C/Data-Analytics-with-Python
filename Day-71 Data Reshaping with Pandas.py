# 1. pivot() - turns unique row values into columns 
df.pivot(index="Month", column="Category", values="Sales")

# 2. pivot_table() 
df.pivot_table(index="Month", columns="Category", values="Sales", aggfunc="sum")

# 3 melt() - converts wide to long format 
df.melt(id_vars=["Month"], var_name="Category", values_name="Sales")

# 4. stack() / unstack() 
# a. columns to rows
df.stack()

# b. rows to columns
df.unstack()

