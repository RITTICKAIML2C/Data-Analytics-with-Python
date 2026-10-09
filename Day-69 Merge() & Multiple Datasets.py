# 1. Merge() 
pd.merge(customers, orders, on="Customer_ID")

# 2. Types of Joins 
# a. Inner Join - matching records 
pd.merge(left, right, on="Customer_ID", how="inner")

# b. Left Join - Keep all records from the left DataFrame:
pd.merge(left, right, on="Customer_ID", how="left")

# c. Right Join - Keep all records from the right DataFrame:
pd.merge(left, right, on="Customer_ID", how="right")

# d. Outer Join - Keep everything:
pd.merge(left, right, on="Customer_ID", how="outer")

# 3. Merge using Different Column Names 
pd.merge(
    orders,
    customers,
    left_on="Customer_ID",
    right_on="ID"
)

# 4. Duplicate Columns After Merge 
pd.merge(
    df1,
    df2,
    on="ID",
    suffixes=("_left", "_right")
)

# 5. Validate Your Merge 
pd.merge(
    orders,
    customers,
    on="Customer_ID",
    validate="many_to_one"
)

