print("Hello World")
print("*" * 10)

x = 1
y = 2
unit_price = 3

print("Hello World!")

# Fundamentals in Python
students_count = 1000
rating = 4.99 
is_published = True
course_name = "Python Programming"

course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

course = "Python \nProgramming"
print(course)

first = "Rittick"
last = "Raj"
full = f"{len(first)} {2 + 2}"
print(full)

course = "  python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

import math

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Fundamentals of Computer Programming
temperature = 14
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

high_income = False
good_credit = True
student = True

if high_income or good_credit or not student:
    print("Eligible")

age should be between 18 and 65
age = 22 
if 18 <= age < 65:
    print("Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

for number in range(1, 10, 2):
    print("Attempt", number, (number + 1) * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterable 
for item in shopping_cart:
    print(item)

number = 100
while number > 0:
    print(number)
    number //= 2

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

# Functions 
def greet():
    print("Hi there")
    print("Welcome aboard")
greet()

# Argumments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
greet("Rittick", "Raj")
greet("John", "Smith")

# Function Types
def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
file = open("context.txt", "w")
file.write(message)

def greet(name):
    print(f"Hi {name}")
print(greet("Mosh"))

# Keyword Arguments
def increement(number, by):
    return number + by
print(increement(2, by=1))

# Default Arguments
def increment(number, by=1):
    return number + by
print(increment(2, 5))

# *Args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4, 5))

