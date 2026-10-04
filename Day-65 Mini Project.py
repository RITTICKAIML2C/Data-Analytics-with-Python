# # MINI PROJECT — Employee Analytics Visualization Dashboard
# # 📊 Step 1 — Department Comparison Create a bar chart for: Average Salary by Department Average Performance by Department Average Training Hours by Department
# # 🔗 Step 2 — Relationship Analysis Create scatter plots for: Experience vs Salary Training Hours vs Performance
# # 📦 Step 3 — Distribution Analysis Create histograms for: Salary Performance
# # 🥧 Step 4 — Workforce Distribution Create a pie chart showing: Employee distribution by Department
# # 🏆 Step 5 — Top Employees Create a bar chart showing the Top 5 employees by Performance. Hint: top_5 = df.nlargest(5, "Performance")
# # 💼 Step 6 — Business Insights After looking at your charts, answer:
# # Which department appears to have the highest average salary?, Which department has the strongest average performance?, Does experience appear related to salary?, Does training appear related to performance?, How is employee salary distributed?, Which department has the largest workforce?, Who are the top-performing employees?
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Employee": [
        "Amit", "Rahul", "Priya", "Sneha",
        "Arjun", "Neha", "Rohan", "Ananya",
        "Vikas", "Karan", "Meera", "Riya"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "HR", "Marketing",
        "IT", "Finance", "HR", "IT"
    ],

    "Salary": [
        95000, 55000, 85000, 70000,
        120000, 65000, 80000, 90000,
        60000, 110000, 75000, 100000
    ],

    "Performance": [
        94, 72, 91, 68,
        97, 78, 88, 95,
        59, 93, 85, 90
    ],

    "Experience": [
        7, 3, 6, 4,
        10, 2, 5, 8,
        2, 9, 6, 7
    ],

    "Training_Hours": [
        40, 20, 35, 25,
        50, 30, 32, 45,
        18, 48, 35, 42
    ]
})
department_avg = df.groupby("Department").agg({
    "Salary": "mean",
    "Performance": "mean",
    "Training_Hours": "mean"
})
print(department_avg)

plt.figure(figsize=(8, 5))
department_avg["Salary"].plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

plt.figure(figsize=(8, 5))
department_avg["Performance"].plot(kind="bar")
plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance")
plt.show()

plt.figure(figsize=(8, 5))
department_avg["Training_Hours"].plot(kind="bar")
plt.title("Average Training Hours by Department")
plt.xlabel("Department")
plt.ylabel("Average Training Hours")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Experience"],
    df["Salary"]
)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Training_Hours"],
    df["Performance"]
)
plt.title("Training Hours vs Performance")
plt.xlabel("Training Hours")
plt.ylabel("Performance")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Performance"], bins=5)
plt.title("Performance Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Number of Employees")
plt.show()

department_count = df["Department"].value_counts()
print(department_count)
plt.figure(figsize=(7, 7))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)
plt.title("Employee Distribution by Department")
plt.show()

top_5 = df.nlargest(5, "Performance")
print(top_5[["Employee", "Performance"]])
plt.figure(figsize=(8, 5))
plt.bar(
    top_5["Employee"],
    top_5["Performance"]
)
plt.title("Top 5 Employees by Performance")
plt.xlabel("Employee")
plt.ylabel("Performance Score")
plt.show()

# IT has the highest average salary.
# Finance has the strongest average performance
# Yes
# Yes
# The salaries are distributed from approximately ₹55,000 to ₹120,000.
# IT has the largest workforce.
# Arjun — 97, Ananya — 95, 🥉 Amit — 94, Karan — 93, Priya — 91
