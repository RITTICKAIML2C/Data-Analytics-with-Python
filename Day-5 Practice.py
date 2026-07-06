# # 1. Create a list of squares from 1 to 10 using list comprehension.
squares = [i ** 2 for i in range(1, 11)]
print(squares)

# # 2. From: numbers = [12, 25, 18, 41, 50, 63]. Create a list containing only even numbers
numbers = [12, 25, 18, 41, 50, 63]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# # 3. From: marks = [35, 80, 60, 25, 90]. Create a list that contains "Pass" or "Fail".
marks = [35, 80, 60, 25, 90]
result = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print(result)

# # 4. Convert: names = ["ritick", "rahul", "priya", "amit"]. into uppercase using list comprehension.
names = ["ritick", "rahul", "priya", "amit"]
new_names = [name.upper() for name in names]
print(new_names)

# # 5. Given: prices = [100, 250, 500, 750]. Increase every price by 18% GST.
prices = [100, 250, 500, 750]
increased_price = [price * 1.18 for price in prices]
print(increased_price)

# # 6. Remove all negative numbers: numbers = [-5, 10, -3, 20, -1, 15]
numbers = [-5, 10, -3, 20, -1, 15]
new_numbers = [num for num in numbers if num > 0]
print(new_numbers)

# # Industry Practice
# # Employee Salary Analysis
# # Given: 
# # employees = [
# #     {"name": "Aman", "salary": 45000},
# #     {"name": "Rahul", "salary": 70000},
# #     {"name": "Priya", "salary": 55000},
# #     {"name": "Riya", "salary": 80000}
# # ]
# # Using list comprehensions: Create a list of employee names. Create a list of salaries. Find employees earning more than ₹60,000. Increase every salary by 10%.
employees = [
    {"name": "Aman", "salary": 45000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Priya", "salary": 55000},
    {"name": "Riya", "salary": 80000}
]
names = [employee["name"] for employee in employees]
print("Employee Names:", names)
salaries = [employee["salary"] for employee in employees]
print("Salaries:", salaries)
high_salary = [employee["name"] for employee in employees if employee["salary"] > 60000]
print("Employees earning more than ₹60,000:", high_salary)
new_salaries = [employee["salary"] * 1.10 for employee in employees]
print("Salaries after 10% increase:", new_salaries)
