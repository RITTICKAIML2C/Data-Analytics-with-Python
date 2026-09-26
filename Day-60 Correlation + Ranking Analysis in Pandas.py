# # 1. Correlation
df["Column1"].corr(df["Column2"])
df["Salary"].corr(df["Experience"])

# # Range : Correlation	Meaning
# Close to +1	Strong positive relationship
# Close to 0	Weak or no linear relationship
# Close to -1	Strong negative relationship

# # 2. Correlation Matrix 
# print(df.corr(numeric_only=True))

# # 3. nlargest() & nsmallest()
# # a. Top 3 salaries - df.nlargest(3, "Salary")
# # b. Top 2 performer - df.nlargest(2, "Performance")
# # c. Lowest 3 salaries - df.nsmallest(3, "Salary")
