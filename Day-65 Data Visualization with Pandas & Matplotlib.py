import pandas as pd 
import matplotlib.pyplot as plt
# # 1. Bar Chart - Best for comparing categories
# # Average salary by department
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()

# # 2. Line Chart - Best for showing a trend or change over time.
df.plot(x="Month", y="Sales", kind="line")
plt.show()

# # 3. Scatter Plot - Best for examining relationships between two numerical variables.
# # Experience vs Salary
df.plot(x="Experience", y="Salary", kind="scatter")
plt.show()

# # 4. Pie Chart - Best for showing proportions 
df["Department"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.show()

# # 5. Histogram - Best for understanding the distribution of numerical data.
# df["Salary"].plot(kind="hist")
# plt.xlabel("Salary")
# plt.title("Salary Distributions")
# plt.show()

