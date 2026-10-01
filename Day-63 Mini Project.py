# # 🚀 MINI PROJECT — Employee Ranking & Performance Leaderboard
# # Step 1 — Create Global Rankings Create: Salary_Rank Performance_Rank Experience_Rank Training_Rank. Highest value = Rank 1.
# # Step 2 — Department Rankings, Create a rank for each employee within their department. Salary rank within department. Now create: Department_Performance_Rank Department_Experience_Rank
# # Step 3 — Overall Employee Score 🏆. Create an Overall_Score using: Performance × 0.5, Experience × 0.2, Training_Hours × 0.2, Salary_Rank × -0.1, Since a lower salary rank is better, multiplying it by -0.1 rewards employees with a better salary ranking. Highest overall score should receive Rank 1.
# # Step 4 — Top Performers, Find: Top 5 employees by Overall_Score. Top 3 employees by Salary, Top 3 employees by Performance, Top 3 employees by Experience, Top 3 employees by Training Hours.
# # Step 5 — Department Leaders. For each department, find the employee with: Highest salary. Highest performance, Highest experience.
# # 💡 You can use sorting + groupby() or idxmax().
# # Step 6 — Business Insights. After completing the analysis, answer: Who is the strongest overall employee according to the scoring system? Who is the highest-paid employee? Who is the highest-performing employee? hich employees are the strongest performers within their departments? Which department has the strongest combination of performance, experience, and training? Does the highest-paid employee necessarily have the highest overall score? Which employees appear to be strong candidates for leadership?
import pandas as pd

df = pd.DataFrame({
    "Employee_ID": range(101, 113),

    "Employee": [
        "Aman", "Riya", "Rahul", "Priya",
        "Karan", "Neha", "Vikas", "Anjali",
        "Rohan", "Sneha", "Arjun", "Meera"
    ],

    "Department": [
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "HR", "Marketing",
        "IT", "Finance", "HR", "IT"
    ],

    "Salary": [
        85000, 60000, 70000, 95000,
        55000, 90000, 75000, 110000,
        80000, 65000, 120000, 88000
    ],

    "Performance": [
        95, 82, 76, 92,
        65, 94, 85, 98,
        88, 72, 97, 90
    ],

    "Experience": [
        8, 4, 5, 10,
        2, 7, 6, 12,
        5, 3, 11, 9
    ],

    "Training_Hours": [
        45, 22, 30, 48,
        15, 42, 35, 55,
        32, 20, 60, 46
    ]
})
df["Salary_Rank"] = df["Salary"].rank(ascending=False, method="dense")
df["Performance_Rank"] = df["Performance"].rank(ascending=False, method="dense")
df["Experience_Rank"] = df["Experience"].rank(ascending=False, method="dense")
df["Training_Rank"] = df["Training_Hours"].rank(ascending=False, method="dense")

df["Department_Salary_Rank"] = (df.groupby("Department")["Salary"].rank(ascending=False, method="dense"))
df["Department_Performance_Rank"] = (df.groupby("Department")["Performance"].rank(ascending=False, method="dense"))
df["Department_Experience_Rank"] = (df.groupby("Department")["Experience"].rank(ascending=False, method="dense"))

df["Overall_Score"] = (df["Performance"] * 0.5 + df["Experience"] * 0.2 + df["Training_Hours"] * 0.2 + df["Salary_Rank"] * -0.1)
df["Overall_Rank"] = (df["Overall_Score"].rank(ascending=False, method="dense"))

print(df.nlargest(5, "Overall_Score")[["Employee", "Overall_Score"]])
print(df.nlargest(3, "Salary")[["Employee", "Salary"]])
print(df.nlargest(3, "Performance")[["Employee", "Performance"]])
print(df.nlargest(3, "Experience")[["Employee", "Experience"]])
print(df.nlargest(3, "Training_Hours")[["Employee", "Training_Hours"]])

print(
    df.loc[
        df.groupby("Department")["Salary"].idxmax(),
        ["Department", "Employee", "Salary"]
    ]
)
print(
    df.loc[
        df.groupby("Department")["Performance"].idxmax(),
        ["Department", "Employee", "Performance"]
    ]
)
print(
    df.loc[
        df.groupby("Department")["Experience"].idxmax(),
        ["Department", "Employee", "Experience"]
    ]
)

print("\n--- STRONGEST OVERALL EMPLOYEE ---")
print(
    df.loc[
        df["Overall_Score"].idxmax(),
        ["Employee", "Overall_Score"]
    ]
)


print("\n--- HIGHEST-PAID EMPLOYEE ---")
print(
    df.loc[
        df["Salary"].idxmax(),
        ["Employee", "Salary"]
    ]
)


print("\n--- HIGHEST-PERFORMING EMPLOYEE ---")
print(
    df.loc[
        df["Performance"].idxmax(),
        ["Employee", "Performance"]
    ]
)


print("\n--- DEPARTMENT PERFORMANCE LEADERS ---")
print(
    df.loc[
        df.groupby("Department")["Performance"].idxmax(),
        ["Department", "Employee", "Performance"]
    ]
)


print("\n--- DEPARTMENT AVERAGES ---")
department_stats = (
    df.groupby("Department")
      [["Performance", "Experience", "Training_Hours"]]
      .mean()
)

print(department_stats)


print("\n--- DEPARTMENT COMBINED SCORE ---")
department_score = (
    df.groupby("Department")
      [["Performance", "Experience", "Training_Hours"]]
      .mean()
      .mean(axis=1)
      .sort_values(ascending=False)
)

print(department_score)


print("\n--- LEADERSHIP CANDIDATES ---")
print(
    df.nlargest(
        5,
        ["Performance", "Experience", "Training_Hours"]
    )[[
        "Employee",
        "Department",
        "Performance",
        "Experience",
        "Training_Hours",
        "Overall_Score"
    ]]
)


print(
    df.sort_values("Overall_Rank")[[
        "Employee_ID",
        "Employee",
        "Department",
        "Salary",
        "Performance",
        "Experience",
        "Training_Hours",
        "Salary_Rank",
        "Performance_Rank",
        "Experience_Rank",
        "Training_Rank",
        "Department_Salary_Rank",
        "Department_Performance_Rank",
        "Department_Experience_Rank",
        "Overall_Score",
        "Overall_Rank"
    ]]
)
