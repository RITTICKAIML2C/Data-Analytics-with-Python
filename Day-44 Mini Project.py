# # Mini Project — Employee Performance Ranking
# # Create a DataFrame with 10 employees: Employee_ID Name Departmentm Salary Performance Experience
# # Use: IT HR Finance Marketing
# # 📊 Employee Ranking Create: Salary_Rank, Performance_Rank
# # Then display: Top 3 highest-paid employees, Top 3 performers, Bottom 3 salaries, Bottom 3 performers
# # 🏢 Department Sorting : Sort the complete DataFrame by: Department → Performance, with the highest-performing employee appearing first within each department.
# # ⭐ Business Insights Find:
# # Highest-paid employee Highest-performing employee Employee with the most experience Department containing the highest-paid employee Department containing the highest-performing employee
# # 🔥 Bonus : Find the top-performing employee in each department
import pandas as pd
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rahul", "Priya", "Amit", "Sneha", "Vikash",
        "Anjali", "Rohan", "Neha", "Arjun", "Pooja"
    ],
    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "HR", "Finance", "Marketing", "IT", "Finance"
    ],
    "Salary": [
        75000, 52000, 85000, 60000, 90000,
        48000, 78000, 65000, 82000, 70000
    ],
    "Performance": [
        92, 85, 95, 78, 88,
        90, 86, 82, 96, 91
    ],
    "Experience": [
        5, 3, 7, 4, 8,
        2, 6, 5, 9, 4
    ]
})
df["Salary_Rank"] = df["Salary"].rank(ascending=False)
df["Performance_Rank"] = df["Performance"].rank(ascending=False)
print(df.nlargest(3, "Salary"))
print(df.nlargest(3, "Performance"))
print(df.nsmallest(3, "Salary"))
print(df.nsmallest(3, "Performance"))
print(df.sort_values(["Department", "Performance"], ascending=[True, False]))

print(df.loc[df["Salary"].idxmax()])
print(df.loc[df["Performance"].idxmax()])
print(df.loc[df["Experience"].idxmax()])
print(df.loc[df["Salary"].idxmax(), "Department"])
print(df.loc[df["Performance"].idxmax(), "Department"])

print(df.loc[df.groupby("Department")["Performance"].idxmax()])

