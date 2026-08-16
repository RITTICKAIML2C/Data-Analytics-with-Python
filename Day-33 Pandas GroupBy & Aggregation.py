# # 1. GroupBy + Aggregation 
# # a. Average Salary in each department 
df.groupby("Department")["Salary"].mean()

# # b. Highest Salary in each department
df.grouby("Department")["Salary"].max()

# # c. How many employees are in each department
df.groupby("Department")["Employee_ID"].count()

# # d. Combine Multiple Choices 
df.groupby("Department")["Salary"].agg(["count", "mean", "min", "max"])
