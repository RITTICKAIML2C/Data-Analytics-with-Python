# # Mini Project - Employee Relationship Analysis
# # 📊 Analysis : Calculate: Experience ↔ Salary correlation, Experience ↔ Performance correlation, Salary ↔ Performance correlation
# # 📈 Visualization : Create 2 scatter plots: Experience -> Salary, Salary -> Performance 
# # ⭐ Business Insights : Which pair has the strongest relationship?, Is the strongest relationship positive or negative?, Does experience appear to be related to salary?, Does higher salary appear to be associated with higher performance?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Employee_ID": ["E001", "E002", "E003", "E004", "E005",
                    "E006", "E007", "E008", "E009", "E010"],

    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 10, 12],

    "Salary": [32000, 35000, 40000, 45000, 50000,
               56000, 62000, 68000, 76000, 85000],

    "Performance": [65, 68, 72, 70, 78, 82, 80, 88, 91, 94]
})
print(df)
experience_salary = df["Experience"].corr(df["Salary"])
experience_performance = df["Experience"].corr(df["Performance"])
salary_performance = df["Salary"].corr(df["Performance"])
print("Correlation Results:")
print("Experience ↔ Salary:", experience_salary)
print("Experience ↔ Performance:", experience_performance)
print("Salary ↔ Performance:", salary_performance)
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
plt.scatter(df["Salary"], df["Performance"])
plt.title("Salary vs Performance")
plt.xlabel("Salary")
plt.ylabel("Performance Score")
plt.grid(True)
plt.show()

# 1. +0.999
# 2. Positive 
# 3. Yes, very strongly
# 4. Yes 
