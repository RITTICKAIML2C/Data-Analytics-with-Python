# # 1. Use the math module to print: square root of 144, value of pi, factorial of 6.
import math
print(math.sqrt(144))
print(math.pi)
print(math.factorial(6))

# # 2. Use the random module to generate: 
# # A random integer between 1 and 50, A random choice from : ["Python", "SQL", "Power BI", "Excel"]
import random
print(random.randint(1, 50))
skills = ["Python", "SQL", "Power BI", "Excel"]
print(random.choice(skills))

# # 3. Use the datetime module to print: Current date, current time
from datetime import datetime
today = datetime.now()
print(today.date())
print(today.time())

# # 4. Create your own module: calculator.py
# # File 1: 
def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

# # File 2: 
import calculator
a = 20 
b = 5
print(calculator.add(a, b))
print(calculator.substract(a, b))
print(calculator.multiply(a, b))
print(calculator.divide(a, b))

# # 6. Create: employees.csv
# # Read and print every row using the csv module. 
# # Name,Department,Salary
# # Rittick,Analytics,50000
# # Rahul,Sales,45000
# # Priya,HR,60000
import csv
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# # 7. Industry Practice 
# # Employee Report Generator 
# # employees = [
# #     ["Aman", "Analytics", 50000],
# #     ["Rahul", "Sales", 45000],
# #     ["Priya", "HR", 60000]
# # ]
# # Your program should: Save the data to a CSV file, Read the CSV file, Display all employee records, Calculate the average salary, Display the highest salary.
import csv
employees = [
    ["Aman", "Analytics", 50000],
    ["Rahul", "Sales", 45000],
    ["Priya", "HR", 60000]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Department", "Salary"])
    writer.writerows(employees)
salary = []
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        print(row)
        salary.append(int(row[2]))
print("Average Salary:", sum(salary) / len(salary))
print("Highest Salary:", max(salary))
