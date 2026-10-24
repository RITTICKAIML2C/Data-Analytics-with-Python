# # 💼 Mini Project — Data Quality Audit
# # Using the same dataset: Check duplicates Check missing values Check negative Sales/Profit Check inconsistent Category names Remove duplicate rows.
# # Fix "electronics" → "Electronics" Remove rows with invalid negative Sales/Profit Fill missing numeric values using an appropriate method Recheck the dataset Write 3 data-quality/business insights.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Order_ID": [1001,1002,1003,1003,1005,1006,1007],
    "Category": ["Electronics","Furniture","electronics",
                 "Furniture","Clothing","Clothing","Clothing"],
    "Sales": [85000,60000,-5000,60000,45000,np.nan,30000],
    "Profit": [18000,12000,-1000,12000,9000,8000,np.nan]
})
print(df.duplicated().sum())

print(df.isnull().sum())

print(df[(df["Sales"] < 0) | (df["Profit"] < 0)])

print(df["Category"].unique())

df = df.drop_duplicates()

df["Category"] = df["Category"].replace("electronics", "Electronics")

df = df[(df["Sales"] >= 0) & (df["Profit"] >= 0)]

df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

print(df)

print(df.isnull().sum())

print(df[(df["Sales"] < 0) | (df["Profit"] < 0)])

print(df["Category"].unique())
