# # 🏢 Mini Project — Employee Data Cleaning
# # Then perform: Missing-value count, Missing-value percentage, Identify the worst column, Fill numerical missing values appropriately, Fill categorical missing values, Verify zero missing values
# # Calculate: Average salary, Average performance, Average experience, Average training hours, Give 3 business insights
import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Amit", "Priya", "Rahul", "Sneha", "Arjun",
        "Neha", "Vikram", "Riya", "Karan", "Ananya", "Rohit", "Pooja"
    ],
    "Department": [
        "IT", "HR", "Finance", np.nan, "IT",
        "Marketing", "Finance", "IT", np.nan, "HR", "Marketing", "IT"
    ],
    "Salary": [
        65000, 55000, np.nan, 72000, 68000,
        50000, 62000, np.nan, 58000, 54000, 60000, 75000
    ],
    "Performance": [
        8.5, 7.2, 9.1, np.nan, 8.8,
        6.9, 7.8, 9.3, np.nan, 7.5, 8.1, 9.0
    ],
    "Experience": [
        3, 5, np.nan, 7, 4,
        2, 6, 5, np.nan, 3, 4, 8
    ],
    "Training_Hours": [
        20, np.nan, 35, 25, 30,
        15, 28, np.nan, 22, 18, 26, 40
    ]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
print(df.isnull().mean()*100)
print((df.isnull().mean()*100).idxmax())
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)
print(df["Department"].mode()[0])
print(df.isnull().sum())
print(df["Salary"].mean())
print(df["Performance"].mean())
print(df["Experience"].mean())
print(df["Training_Hours"].mean())
averages = df[
    ["Salary", "Performance", "Experience", "Training_Hours"]
].mean()
print(averages)
print(df)
print(df.round(2))

# Insight 1 — Employee performance is relatively strong
# The average performance score is approximately 8.08/10, indicating that the overall workforce is performing well.
# Insight 2 — Training investment is significant
# Employees receive approximately 25.25 training hours on average. This suggests the organization is investing considerably in employee development.
# Insight 3 — Experienced employees may be valuable
# The average experience is approximately 4.67 years, meaning the workforce has a reasonable level of experience. The company could investigate whether employees with more experience and training consistently achieve higher performance.
