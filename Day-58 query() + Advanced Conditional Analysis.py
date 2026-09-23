# # 1. DataFrame.query()
# Insted of : df[df["Salary"] > 80000]
You can write : df.query("Salary > 80000")

# # For multiple conditions: 
df.query("Salary > 80000 anbd Performance >= 90")

