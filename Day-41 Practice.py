import pandas as pd
import matplotlib.pyplot as plt

# # 1. Experience vs Salary 
# # Find : Correlation between Experience and Salary, Determine whether the relationship is positive or negative, Determine whether it is weak, moderate, or strong
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Experience": [1, 2, 3, 5, 7, 9],
    "Salary": [30000, 35000, 42000, 52000, 68000, 80000]
})
correlation = df["Experience"].corr(df["Salary"])
print(correlation)
# positive relationship
# very strong 

# # 2. Study Analysis 
# # Find : Correlation between Study_Hours and Exam_Score, Interpret the result, Create a scatter plot of Study Hours → Exam Score
# # Include : Title, X-axis, Y-axis, Grid 
df = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7],
    "Exam_Score": [45, 50, 55, 63, 70, 78, 85]
})
correlation = df["Study_Hours"].corr(df["Exam_Score"])
print(correlation)

plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()
plt.show()

# # 3. Industrial Practice
# # Calculate : Advertising ↔ Sales correlation, Advertising ↔ Customers correlation, Sales ↔ Customers correlation
# # Determine : Which relationship is strongest?, Are the relationships positive or negative?
# # Visualization : Create two scatter plots: Advertising → Sales, Advertising → Customers, Title, X-axis label, Y-axis label, Grid
# # Business question : Based on the data: Does higher advertising spending generally correspond with higher sales?
df = pd.DataFrame({
    "Advertising": [10, 15, 20, 25, 30, 35, 40, 45],
    "Sales": [50, 55, 65, 72, 80, 88, 95, 105],
    "Customers": [100, 120, 135, 150, 170, 185, 200, 220]
})
print(df["Advertising"].corr(df["Sales"]))
print(df["Advertising"].corr(df["Customers"]))
print(df["Sales"].corr(df["Customers"]))

# Adversting & Customers is the strongest 
# All positive 

plt.scatter(df["Advertising"], df["Sales"])
plt.title("Advertising vs Sales")
plt.xlabel("Advertising")
plt.ylabel("Sales")
plt.grid()
plt.show()
plt.scatter(df["Advertising"], df["Customers"])
plt.title("Advertising vs Customers")
plt.xlabel("Advertising")
plt.ylabel("Customers")
plt.grid()
plt.show()
Yes 
