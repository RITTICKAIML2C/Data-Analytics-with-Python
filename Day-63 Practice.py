# # Question 1 — Sorting
# # Sort the DataFrame by: Salary from highest to lowest. Performance from highest to lowest. Experience from highest to lowest. Department alphabetically and then Salary from highest to lowest.
# # Question 2 — Ranking, Create these columns: Salary_Rank Performance_Rank Experience_Rank. All should have Rank 1 as the highest value.Use: method="dense"
# # Question 3 — Top and Bottom Employees. Find: Top 3 highest-paid employees. Top 3 highest-performing employees. Top 3 most experienced employees. Bottom 3 employees by salary. Bottom 3 employees by performance. Return only the employee name and relevant value.
# # Question 4 — Business Leaderboard. Create a new DataFrame containing: Employee Department Salary Performance Experience Salary Rank Performance Rank
# # Then sort it by: Performance Rank, Salary Rank
# # Both from smallest to largest.
import pandas as pd

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
print(df.sort_values("Salary", ascending=False))
print(df.sort_values("Salary", ascending=False))
print(df.sort_values("Salary", ascending=False))
print(df.sort_values(["Department", "Salary"], ascending=[True, False]))

df["Salary_Rank"] = df["Salary"].rank(ascending=False, method="dense")
df["Performance_Rank"] = df["Performance"].rank(ascending=False, method="dense")
df["Experience_Rank"] = df["Experience"].rank(ascending=False, method="dense")
print(df)

print(df.nlargest(3, "Salary"))
print(df.nlargest(3, "Performance"))
print(df.nlargest(3, "Experience"))
print(df.nsmallest(3, "Salary"))
print(df.nsmallest(3, "Performance"))

leaderboard = df[["Employee", "Department", "Salary", "Performance", "Experience", "Salary_Rank", "Performance_Rank"]].sort_values(["Performance_Rank", "Salary_Rank"])
