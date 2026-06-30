# # Mini Project - 1
# # Student Marks Analyzer
# # Use:
# # marks = [78, 65, 90, 88, 76]
# # Your program should display:
# # Total marks
# # Average marks
# # Highest marks
# # Lowest marks
# # Number of students
# # Pass percentage (Assume pass marks = 40)

marks = [78, 65, 90, 88, 76]

# # Total Marks
total = sum(marks)

# # Average Marks 
average = total / len(marks)

# # Highest Marks
highest = max(marks)

# # Lowest Marks 
lowest = min(marks)

# # Number of students
students = len(marks)

# # Pass Percentage (Pass Marks = 40)
passed = 0
for mark in marks:
    if mark >= 40:
        passed += 1

pass_percentage = (passed / students) * 100

# # Display Result 
print("Total Marks =", total)
print("Average Marks =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Number of Students =", students)
print("Pass Percentage =", pass_percentage, "%")
