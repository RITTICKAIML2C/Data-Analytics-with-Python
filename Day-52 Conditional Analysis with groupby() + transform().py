# # 1. Department Average
import pandas as pd 
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [60000, 80000, 45000, 55000]
})
print(df.groupby("Department")["Salary"].mean())
df["Department_Avg"] = (df.groupby("Department")["Salary"].transform("mean"))
print(df)
print(df[df["Salary"] > df["Department_Avg"]])

