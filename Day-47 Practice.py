import pandas as pd
# # 1. Basic Pivot Table 
# # Your task : Create a pivot table showing:
# # Department → Month → Total Sales
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics",
        "Furniture", "Furniture",
        "Clothing", "Clothing"
    ],
    "Month": [
        "Jan", "Feb",
        "Jan", "Feb",
        "Jan", "Feb"
    ],
    "Sales": [
        50000, 65000,
        40000, 55000,
        30000, 45000
    ]
})
print(pd.pivot_table(df, values="Department", index="Month", columns="Sales", aggfunc="sum"))

# # 2. Average Sales 
# # Using the same DataFrame, create a pivot table showing:
# # Department → Month → Average Sales
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics",
        "Furniture", "Furniture",
        "Clothing", "Clothing"
    ],
    "Month": [
        "Jan", "Feb",
        "Jan", "Feb",
        "Jan", "Feb"
    ],
    "Sales": [
        50000, 65000,
        40000, 55000,
        30000, 45000
    ]
})
print(pd.pivot_table(df, values="Sales", index="Department", columns="Month", aggfunc="mean"))

# # Industrial Practice 
df = pd.DataFrame({
    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing"
    ],
    "Month": [
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar"
    ],
    "Sales": [
        50000, 65000, 70000,
        40000, 55000, 60000,
        30000, 45000, 50000
    ],
    "Profit": [
        8000, 10000, 12000,
        6000, 9000, 11000,
        4000, 7000, 8500
    ]
})
print(pd.pivot_table(df, values="Sales", index="Department", columns="Month", aggfunc="sum"))
print(pd.pivot_table(df, values="Profit", index="Department", columns="Month", aggfunc="sum"))
# 1. Electronics — ₹185,000
# 2. Electronics — ₹30,000
# 3. March has the highest overall sales — ₹180,000.
