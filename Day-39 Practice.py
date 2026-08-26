import pandas as pd
import matplotlib.pyplot as plt
# # 1. Create this dataframe:
# # a. Display the Data Frame
# # b. Create a histogram of salary. Requirements : Title, X-axis label, Y-axis labels
# # c. Create a histogram of Performance
# # d. Calculate :  Average Salary, Average Performance, Highest Salary, Lowest Salary
df = pd.DataFrame({
    "Employee": [
        "Aman", "Riya", "Rahul", "Neha",
        "Arjun", "Priya", "Karan", "Sneha"
    ],
    "Salary": [
        32000, 35000, 42000, 48000,
        55000, 62000, 70000, 78000
    ],
    "Performance": [
        65, 70, 78, 82,
        86, 90, 94, 96
    ]
})
print(df)

plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

plt.hist(df["Performance"])
plt.title("Performance Analysis")
plt.xlabel("Performance")
plt.ylabel("Number of Employees")
plt.show()

print(df["Salary"].mean())
print(df["Performance"].mean())
print(df["Salary"].max())
print(df["Salary"].min())

# # 🏭 Industrial Practice, Now work with this employee dataset:
# # a. Salary distribution - Create a histogram showing salary distribution.
# # b. Performance distribution - Create a histogram showing performance distribution
# # c. Analysis - Average Salary, Median Salary, Avg Performance, Highest Salary, Lowest Salary
# # d. Business Insight - Are salaries concentrated more toward the lower, middle, or higher range? and Are employee performances mostly low, middle, or high?
df = pd.DataFrame({
    "Employee_ID": [101,102,103,104,105,106,107,108,109,110],
    "Department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "Marketing", "Finance", "Marketing"
    ],
    "Salary": [
        32000, 38000, 45000, 52000, 48000,
        60000, 68000, 55000, 72000, 80000
    ],
    "Performance": [
        65, 72, 78, 84, 80,
        88, 92, 86, 95, 90
    ]
})
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

plt.hist(df["Performance"])
plt.title("Performance Distribution")
plt.xlabel("Performance")
plt.ylabel("Number of Employees")
plt.show()

print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Performance"].mean())
print(df["Salary"].max())
print(df["Salary"].min())

# Salary distribution: Salaries are concentrated more toward the middle-to-higher range. The dataset has several employees earning between ₹52,000 and ₹80,000, while only two employees are below ₹40,000.
# Performance distribution: Employee performance is clearly concentrated toward the higher range. Most employees have performance scores of 80 or above, with an average performance of 83.
