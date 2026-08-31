# # Mini Project — Employee Correlation Dashboard
# # Keep this one small. Create a DataFrame with 10 employees:
# # Employee_ID, Experience, Training_Hours, Salary, Performance
# # Use realistic numerical values.
# # 📊 Analysis : Calculate: Full correlation matrix, Experience ↔ Salary, Experience ↔ Performance, Training Hours ↔ Performance, Salary ↔ Performance
# # 📈 Visualization : Create 2 scatter plots: Experience → Salary, Training_Hours → Performance
# # ⭐ Business Insights : Which pair has the strongest relationship? Is it positive or negative?, Does experience appear related to salary?, Does training appear related to performance?, Does higher salary appear associated with higher performance?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Employee_ID": ["E001", "E002", "E003", "E004", "E005",
                    "E006", "E007", "E008", "E009", "E010"],

    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 10, 12],

    "Training_Hours": [10, 12, 15, 18, 20, 24, 26, 30, 34, 38],

    "Salary": [32000, 35000, 39000, 44000, 50000,
               55000, 61000, 67000, 76000, 85000],

    "Performance": [62, 65, 69, 72, 75, 79, 82, 86, 89, 93]
})
print("Full Correlation Matrix:")
print(df.corr(numeric_only=True).round(3))
print("Individual Correlations:")
print("Experience ↔ Salary:", round(df["Experience"].corr(df["Salary"]), 3))
print("Experience ↔ Performance:", round(df["Experience"].corr(df["Performance"]), 3))
print("Training Hours ↔ Performance:", round(df["Training_Hours"].corr(df["Performance"]), 3))
print("Salary ↔ Performance:", round(df["Salary"].corr(df["Performance"]), 3))
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

plt.scatter(df["Training_Hours"], df["Performance"])
plt.title("Training Hours vs Performance")
plt.xlabel("Training Hours")
plt.ylabel("Performance Score")
plt.grid(True)
plt.show()

# 1. Experience ↔ Salary
# 2. Positive
# 3. Yes, very strongly.
# 4. Yes
# 5. Yes
