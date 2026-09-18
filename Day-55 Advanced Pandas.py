# # 1. apply()
import pandas as pd 
def salary_category(salary):
    if salary >= 80000:
        return "High"
    elif salary >= 60000:
        return "Medium"
    else:
        return "Low"
df["Salary_Category"] = df["Salary"].apply(salary_category)

# # 2. np.select()
import pandas as pd
conditions = [
    df["Performance"] >= 90,
    df["Performance"] >= 75,
    df["Performance"] >= 60
]

choices = [
    "Excellent",
    "Good",
    "Average"
]

df["Performance_Category"] = np.select(
    conditions,
    choices,
    default="Poor"
)

# # 3. Feature Engineering
df["Annual_Salary"] = df["Monthly_Salary"] * 12

df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100
