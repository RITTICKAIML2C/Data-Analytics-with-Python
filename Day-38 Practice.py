import pandas as pd
import matplotlib.pyplot as plt
# # 1. Create this Dataframe
# # a. Display DataFrame
# # b. Create a scatter plot : Experience -> Salary, Requirements: Title, X-label, Y-label, grid
# # c. Find : Highest Salary, Lowest Salary, Average Salary
# # d. Find employee with the highest salary
df = pd.DataFrame({
    "Employee":["Aman", "Riya", "Rahul", "Neha", "Arjun", "Priya"],
    "Experience": [1, 2, 3, 5, 7, 8],
    "Salary": [30000, 35000, 42000, 52000, 68000, 75000]
})
print(df)
plt.scatter(df["Experience"], df["Salary"])
plt.title("Exeprience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid()
plt.show()
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].mean())
print(df.loc[df["Salary"].idxmax(), "Employee"])

# # Industrial Practice 
# # a. Employee Analysis - Average Salary, Average Performance, Highest Salary, Highest Performance
# # b. Visualization - Experience vs Salary them Experience vs Performance. Both should have Title, Axis Labels, Grid
# # c. Business Insight - Does salary generally increase as experience increases ? and Does performance generally increases as experience increases ?
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Department": [
        "IT", "HR", "Finance", "IT",
        "Finance", "HR", "IT", "Finance"
    ],
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [32000, 36000, 42000, 50000, 57000, 62000, 70000, 78000],
    "Performance": [65, 72, 78, 84, 88, 91, 94, 96]
})
print(df)
print(df["Salary"].mean())
print(df["Performance"].mean())
print(df["Salary"].max())
print(df["Performance"].max())
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid()
plt.show()
plt.scatter(df["Experience"], df["Performance"])
plt.title("Experience vs Performance")
plt.xlabel("Experience")
plt.ylabel("Performance")
plt.grid()
plt.show()
Yes, Yes 
