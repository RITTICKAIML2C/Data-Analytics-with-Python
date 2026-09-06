# # 1. pivot_table()
pd.pivot_table(
    df, 
    values="Sales", 
    index="Department", 
    columns="Month", 
    aggfunc="sum"
)

Think of it as:

Rows → index
Columns → columns
What to calculate → values
How to calculate → aggfunc
