# # Mini Project — Department Performance Dashboard
# # Create a DataFrame with: Employee_ID Name Department Salary Performance Experience
# # Then build a dashboard that prints:
# # 📊 Department Analytics Average salary Median salary Highest salary Lowest salary Employee count Average performance Highest performance Average experience
# # 📈 Multiple Aggregation
# # Use: groupby().agg() to display: mean salary max salary min salary mean performance max performance employee count
# # 🏆 Business Insights Find: Department with highest average salary Department with highest average performance Department with most employees Employees earning above their department average Employees whose performance is above their department average
# # ⭐ Bonus : Add a new column: Salary_Level using: High Medium Low
# # based on salary ranges, then display the count of each salary level within each department using groupby().

import pandas as pd
df = pd.DataFrame({
    "Employee_ID":[101,102,103,104,105,106,107,108],
    "Name":["Amit","Priya","Rahul","Neha","Karan","Anjali","Riya","Vikas"],
    "Department":["IT","HR","Finance","IT","HR","Finance","IT","Finance"],
    "Salary":[60000,45000,70000,65000,48000,72000,62000,75000],
    "Performance":[8.5,7.8,9.2,8.9,8.0,9.5,8.7,9.3],
    "Experience":[3,2,6,4,3,7,5,8]
})
print("Average Salary\n", df.groupby("Department")["Salary"].mean(), "\n")
print("Median Salary\n", df.groupby("Department")["Salary"].median(), "\n")
print("Highest Salary\n", df.groupby("Department")["Salary"].max(), "\n")
print("Lowest Salary\n", df.groupby("Department")["Salary"].min(), "\n")
print("Employee Count\n", df.groupby("Department")["Employee_ID"].count(), "\n")
print("Average Performance\n", df.groupby("Department")["Performance"].mean(), "\n")
print("Highest Performance\n", df.groupby("Department")["Performance"].max(), "\n")
print("Average Experience\n", df.groupby("Department")["Experience"].mean(), "\n")

summary = df.groupby("Department").agg({
    "Salary":["mean","max","min"],
    "Performance":["mean","max"],
    "Employee_ID":"count"
})
print(summary)

print("Highest Avg Salary:",
      df.groupby("Department")["Salary"].mean().idxmax())

print("Highest Avg Performance:",
      df.groupby("Department")["Performance"].mean().idxmax())

print("Most Employees:",
      df["Department"].value_counts().idxmax())

print("\nEmployees Above Department Avg Salary")
print(df[df["Salary"] >
         df.groupby("Department")["Salary"].transform("mean")])

print("\nEmployees Above Department Avg Performance")
print(df[df["Performance"] >
         df.groupby("Department")["Performance"].transform("mean")])

def level(s):
    if s >= 70000:
        return "High"
    elif s >= 55000:
        return "Medium"
    else:
        return "Low"

df["Salary_Level"] = df["Salary"].apply(level)

print("\nSalary Level Count")
print(df.groupby(["Department","Salary_Level"]).size())

print(df.grouby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].median())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Performance"].mean())
print(df.groupby("Department")["Performance"].max())
print(df.groupby("Department")["Experience"].mean())

print()
