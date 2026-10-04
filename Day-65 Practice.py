# # Practice 
# # Q1 — Bar Chart 📊 Create a bar chart of average Salary by Department.
# # Q2 — Bar Chart Create a bar chart of average Performance by Department.
# # Q3 — Scatter Plot Create a scatter plot: Experience vs Salary
# # Q4 — Scatter Plot Create a scatter plot: Performance vs Salary
# # Q5 — Histogram : Create a histogram showing the distribution of: Salary
# # Q6 — Pie Chart Create a pie chart showing the percentage of employees in each department.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul", "Priya",
        "Karan", "Neha", "Vikas", "Anjali",
        "Rohan", "Sneha"
    ],

    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "Finance",
        "Marketing", "Marketing"
    ],

    "Salary": [
        85000, 60000, 75000, 95000,
        55000, 90000, 80000, 110000,
        70000, 65000
    ],

    "Performance": [
        95, 82, 88, 92,
        65, 94, 85, 98,
        78, 72
    ],

    "Experience": [
        8, 4, 6, 10,
        2, 7, 5, 12,
        3, 4
    ]
})
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()

df.groupby("Department")["Performance"].mean().plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Performance")
plt.title("Average Performance by Department")
plt.show()

df.plot(x="Experience", y="Salary", kind="scatter")
plt.show()

df.plot(x="Performance", y="Salary", kind="scatter")
plt.show()

df["Salary"].plot(kind="hist")
plt.xlabel("Salary")
plt.title("Salary Distribution")
plt.show()

df["Department"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.show()
