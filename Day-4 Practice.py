# # 1. Ask user for a number. Handle: ValueError, ZeroDivisionError. Print the result of 100 / number.
try:
    number = float(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Error: Plese enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# # 2. Create a list: numbers = [10, 20, 30]. Ask user for an index. Handle IndexError
numbers = [10, 20, 30]
try:
    index = int(input("Enter the index: "))
    print("Element:", numbers[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")

# # 3. Create: student = {
# #     "name": "Rittick",
# #     "course": "Data Analytics"
# # }. Ask the user for a key. Handle KeyError.
student = {
    "name" : "Rittick", 
    "course" : "Data Analytics"
}
try:
    key = input("Enter the key: ")
    print("value:", student[key])
except KeyError:
    print("Error: Key not found.")

# # 4. Open: sales. txt. Handle FileNotFoundError.
try:
    with open("sales.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: sales.txt file not found.")

# # 5. Use:try, except, else and finally in one complete example.
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Program execution completed")

# # 6. Industry Practice - Safe Employee Salary Calculator. Create a salary calculator that:
# # Accepts salary from the user, Rejects invalid inputs, Prevents division by zero, Displays a professional error message instead of crashing.
try:
    salary = float(input("Enter employee salary: "))
    employees = int(input("Enter number of employees: "))
    average_salary = salary / employees
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Number of employees cannot be zero.")
else:
    print("Average Salary per Employee:", average_salary)
finally:
    print("Salary Calculation Completed.")
