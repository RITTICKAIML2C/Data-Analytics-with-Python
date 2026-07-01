# 1. Create a function that return square of a number.
def squareofanumber(n):
    return n ** 2
print("Square:", squareofanumber(4))

# 2. Create a function that returns the larger of two numbers
def largestoftwonumbers(a, b):
    if a > b:
        return "a is largest"
    else:
        return "b is largest"
print(largestoftwonumbers(10, 20))

# 3. Create a function that returns whether a number is even or odd.
def evenorodd(number):
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"
print(evenorodd(10))

# 4. Create a function that calculates the average of a list of numbers.
def averageofnumbers(num):
    return sum(num) / len(num)
print("Avergae is:", averageofnumbers([10, 20, 30, 40, 50]))

# 5. Create a function that returns highest marks from a list
def highestmarks(marks):
    return max(marks)
print("Highest Marks:", highestmarks([98, 97, 96, 99, 100]))

# 6. Create a function with default parameter : greet(), greet("Rittick")
def greet(name = "Guest"):
    print("Hello,", name)
greet()
greet("Rittick")

# 7. Employee Salary Calculator
# Create functions to:
# Calculate monthly salary
# Calculate annual salary
# Calculate bonus
# Calculate tax
# Calculate final salary
# Call these functions with sample employee data.
def monthly_salary(basic_salary):
    return basic_salary
def annual_salary(monthly):
    return monthly*12
def calculate_bonus(annual):
    return annual*0.10
def calculate_tax(tax):
    return annual * 0.05
def final_salary(annual, bonus, tax):
    return annual + bonus - tax
employee_name = "Rittick"
basic_salary = 50000
monthly = monthly_salary(basic_salary)
annual = annual_salary(monthly)
bonus = calculate_bonus(annual)
tax = calculate_tax(annual)
final = final_salary(annual, bonus, tax)

print("Employee Name :", employee_name)
print("Monthly Salary :", monthly)
print("Annual Salary  :", annual)
print("Bonus (10%)    :", bonus)
print("Tax (5%)       :", tax)
print("Final Salary   :", final)
