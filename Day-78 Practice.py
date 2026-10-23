# # Practice 
# # Q1 Find the number of duplicate rows.
# # Q2 Find missing values in each column.
# # Q3 Find orders with negative Sales or Profit.
# # Q4 Find inconsistent Category values.
# # Q5 Find the total number of valid orders after removing duplicates and invalid sales/profit records.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Order_ID": [1001,1002,1003,1003,1005,1006,1007],
    "Category": ["Electronics","Furniture","electronics",
                 "Furniture","Clothing","Clothing","Clothing"],
    "Sales": [85000,60000,-5000,60000,45000,np.nan,30000],
    "Profit": [18000,12000,-1000,12000,9000,8000,np.nan]
})
duplicate_count = df.duplicated().sum()
print(duplicate_count)

missing_values = df.isnull().sum()
print(missing_values)

negative_orders = df[(df["Sales"] < 0) | (df["Profit"] < 0)]
print(negative_orders)

print(df["Category"].unique())

valid_orders = df[
    (df["Sales"].notnull()) &
    (df["Profit"].notnull()) &
    (df["Sales"] >= 0) &
    (df["Profit"] >= 0)
]
print(valid_orders)
print("Total valid orders:", len(valid_orders))
