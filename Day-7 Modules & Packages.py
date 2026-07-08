# # Importing a Module 
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

# # Import specific functions
from math import sqrt, pi
print(sqrt(49))
print(pi)

# # Import with Alias
import math as m 
print(m.sqrt(81))

# # The randon Module - useful for generating sample data and testing
import random
print(random.randint(1, 100))

# # The datetime Module - you'll use this for timestamps in reports.
from datetime import datetime
today = datetime.now()
print(today)

# # The os Module - tells you the current working directory.
import os 
print(os.getcwd()) 

# # Creating your own module
# # File 1 : 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# # File 2: 
import calculator
print(calculator.add(10, 20))

# # CSV Module - Bridge to Pandas
import csv
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
