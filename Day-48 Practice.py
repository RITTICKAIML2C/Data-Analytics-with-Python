import pandas as pd 
# # 1. Basic Crosstab
# # Create a crosstab:
# pd.crosstab(df["Department"], df["Status"])
# Then answer: How many Fast orders are in IT?, How many Delayed orders are in HR?, Which department has the most Fast orders?
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR",
        "Finance", "Finance"
    ],
    "Status": [
        "Fast", "Normal", "Fast",
        "Delayed", "Fast", "Normal",
        "Fast", "Delayed"
    ]
})
print(pd.crosstab(df["Department"], df["Status"]))

# 1. 2
# 2. 1
# 3. IT - 2 Fast Orders 

# # 2. Sales Delivery Analysis 
# # Then identify: Department with the most Fast deliveries, Department with the most Delayed deliveries
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing", "Clothing"
    ],
    "Delivery_Status": [
        "Fast", "Normal", "Delayed",
        "Fast", "Fast", "Normal",
        "Delayed", "Normal", "Fast", "Delayed"
    ]
})
print(pd.crosstab(
    df["Department"],
    df["Delivery_Status"]
))

# 1. Furniture - 2 fast deliveries
# 2. Clothing - 2 Delayed deliveries 
