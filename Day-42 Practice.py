import pandas as pd
import matplotlib.pyplot as plt
# # 1. Correlation Matrix 
# # Tasks : Print the correlation matrix.
# # Find : Study Hours ↔ Exam Score, Attendance ↔ Exam Score, Assignment Score ↔ Exam Score, Identify which relationship is strongest.
# # State whether the strongest relationship is positive or negative.
# # Create a scatter plot: Study_Hours → Exam_Score, Title, X-axis, Y-axis, Grid
df = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 72, 78, 82, 88, 92],
    "Assignment_Score": [55, 60, 65, 70, 75, 80, 86, 90],
    "Exam_Score": [45, 50, 55, 62, 68, 75, 82, 88]
})
print(df.corr())
print(df["Study_Hours"].corr(df["Exam_Score"]))
print(df["Attendance"].corr(df["Exam_Score"]))
print(df["Assignment_Score"].corr(df["Exam_Score"]))
Assignment Score ↔ Exam Score
Positive 
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()
plt.show()

# # Industrial Practice — Business Correlation Analysis
# # 📊 Correlation Analysis : Calculate the correlation matrix.
# # Then specifically calculate: Advertising ↔ Website Visits, Advertising ↔ Customers, Advertising ↔ Sales, Website Visits ↔ Customers, Website Visits ↔ Sales, Customers ↔ Sales
# # Business Analysis : Which relationship is strongest? ,Which relationship is weakest?, Are all relationships positive or negative?, Does advertising appear to be associated with higher sales?, Does having more website visitors appear to be associated with higher sales?
# # Visualization - Advertising → Sales, Website Visits → Sales
df = pd.DataFrame({
    "Advertising": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    "Website_Visits": [1000, 1200, 1350, 1500, 1750, 1900, 2200, 2400, 2600, 2900],
    "Customers": [100, 115, 130, 145, 165, 180, 205, 225, 250, 275],
    "Sales": [50000, 56000, 63000, 70000, 78000, 85000, 94000, 105000, 115000, 128000]
})
print(df.corr())
print(df["Advertising"].corr(df["Website_Visits"]))
print(df["Advertising"].corr(df["Customers"]))
print(df["Advertising"].corr(df["Sales"]))
print(df["Website_Visits"].corr(df["Customers"]))
print(df["Website_Visits"].corr(df["Sales"]))
print(df["Customers"].corr(df["Sales"]))

# Customers ↔ Sales
# Advertising ↔ Sales
# Yes, Positive 
# Yes
# Yes 

plt.scatter(df["Advertising"], df["Sales"])
plt.title("Advertising vs Sales")
plt.xlabel("Advertising")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.scatter(df["Website_Visits"], df["Sales"])
plt.title("Website Visits vs Sales")
plt.xlabel("Website Visits")
plt.ylabel("Sales")
plt.grid()
plt.show()
