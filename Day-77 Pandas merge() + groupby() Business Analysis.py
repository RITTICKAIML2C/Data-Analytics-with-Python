# 1. Merge Datasets
merged = orders.merge(customers, on="Customer_ID", how="left")

# 2. Validate the relationship 
merged = orders.merge(
    customers, 
    on="Customer_ID", 
    how="left",
    validate="many_to_one"
)

# 3. Analyze the merged data 
city_sales = merged.groupby("City")["Sales"].sum()

# 4. Find Unmatched Records 
merged[merged["Customers"].isna()]

