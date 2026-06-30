# # Lists
# # Create a list of 10 numbers.
# # Find the sum.
# # Find the average.
# # Find the maximum.
# # Find the minimum.
# # Sort the list in ascending and descending order.

# # Create a list of 10 numbers.
numbers = [40, 20, 50, 10, 30, 70, 80, 60, 90, 100]

# # Find the sum
print("Sum =", sum(numbers))

# # Find the average
print("Average =", sum(numbers) / len(numbers))

# # Find the maximum
print("Maximum =", max(numbers))

# # Find the minimum
print("Minimum =", min(numbers))

# # Sort the list in ascending order
print("Ascending Order =", sorted(numbers))

# # Sort the list in descending order
print("Descending Order =", sorted(numbers, reverse=True))

# # Dictionaries 
student = {
    "name": "Your Name",
    "age": 20,
    "course": "Data Analytics"
}

# # Print all keys
print("Keys:", student.keys())

# # Print all values
print("Values:", student.values())

# # Add "coty"
student["city"] = "Kolkata"
print("After adding city:", student)

# # Update "age"
student["age"] = 21
print("After updating age:", student)

# # Delete "city"
del student["city"]
print("After deleting city:", student)

# # Loops
# # Print:
# # Even numbers
# # Odd numbers
# # Squares of each number
numbers = [12, 15, 20, 35, 42, 50]

# # Print Even numbers
print("Even Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)

# # Print Odd numbers
print("Odd Numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number)

# # Print Square of each number
print("\nSquares of each number:")
for number in numbers:
    print(number ** 2)

# # Functions
# # Write functions to:
# # Calculate total marks
# # Calculate average
# # Find the maximum value
marks = [78, 85, 92, 67, 88]

# # Function to calculate total marks
def total_marks(marks):
    return sum(marks)

# # Function to calculate average marks
def average_marks(marks):
    return sum(marks) / len(marks)

# # Function to find maximum marks
def maximum_marks(marks):
    return max(marks)

# # Function calls
print("Marks:", marks)
print("Total Marks =", total_marks(marks))
print("Average Marks =", average_marks(marks))
print("Maximum Marks =", maximum_marks(marks))

