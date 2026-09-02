import pandas as pd 
# # 1. Employee Ranking 
# # Tasks : Sort employees by salary from highest → lowest, Display the top 3 highest-paid employees, Display the bottom 3 lowest-paid employees, Create Salary_Rank, Create Performance_Rank, Display the employee with rank 1 in salary, Display the employee with rank 1 in performance.
df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance"],
    "Salary": [60000, 45000, 75000, 70000, 52000, 68000],
    "Performance": [85, 78, 92, 90, 80, 88]
})
print(df.sort_values("Salary", ascending=False))
print(df.nlargest(3, "Salary"))
print(df.nsmallest(3, "Salary"))
df["Salary_Rank"] = df["Salary"].rank(ascending=False)
df["Performance_Rank"] = df["Performance"].rank(ascending=False)
print(df)
print(df.nlargest(1, "Salary"))
print(df.nlargest(1, "Performance"))

# # Industrial Practice — Sales Ranking
# # 📊 Sales Ranking : Find: Top 3 products by Sales. Top 3 products by Profit. Lowest 2 products by Sales. Create Sales_Rank. Create Profit_Rank.
# # 🏢 Department Analysis : Sort the products by: Department → Sales with sales descending within each department.
# # ⭐ Business Insights : Answer:
# # Which product has the highest sales? Which product has the highest profit? Which product has the lowest sales? Is the highest-selling product also the highest-profit product?
df = pd.DataFrame({
    "Product": [
        "Laptop", "Phone", "Tablet", "Monitor",
        "Keyboard", "Mouse", "Headphones", "Printer"
    ],
    "Department": [
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories", "Accessories", "Office"
    ],
    "Sales": [
        85000, 120000, 65000, 70000,
        30000, 25000, 45000, 55000
    ],
    "Profit": [
        15000, 22000, 12000, 14000,
        7000, 5000, 9000, 11000
    ]
})
print(df.nlargest(3, "Sales"))
print(df.nlargest(3, "Profit"))
print(df.nsmallest(2, "Sales"))
print(df["Sales"].rank(ascending=False))
print(df["Profit"].rank(ascending=False))
print(df.sort_values(["Department", "Sales"], ascending=[True, False]))
print(df.loc[df["Sales"].idxmax()])
print(df.loc[df["Profit"].idxmax()])
print(df.loc["Sales"].idxmax())
Yes 
