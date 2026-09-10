import pandas as pd 
# # 1. Basic Practice 
# # Create : Find: Number of employees in each department, Department with the most employees, Number of employees in IT
# # Use: df["Department"].value_counts() and appropriate indexing.
df = pd.DataFrame({
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT"
    ]
})
print(df["Department"].value_counts())
print(df["Department"].value_counts().index[0])
print(df["Department"].value_counts()["IT"])

# # 2. Sales Category Analysis 
# # Number of orders in each category, Most common category, Least common category
df = pd.DataFrame({
    "Product_Category": [
        "Electronics", "Clothing", "Electronics",
        "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing", "Electronics", "IT"
    ]
})
print(df["Product_Category"].value_counts())
print(df["Product_Category"].value_counts().index[0])
print(df["Product_Category"].value_counts().index[-1])

# # 3. Value_counts() with percentage
# # 1. 1. Department counts df["Department"].value_counts()
# # 2. Department percentageS df["Department"].value_counts(normalize=True)
# # Then convert it into percentages: df["Department"].value_counts(normalize=True) * 100
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "HR", "Finance",
        "IT", "HR", "Marketing", "Finance",
        "IT", "Marketing"
    ]
})
print(df["Department"].value_counts())
print(df["Department"].value_counts(normalize=True))
print(df["Department"].value_counts(normalize=True) * 100)
