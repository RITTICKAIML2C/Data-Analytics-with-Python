# # Mini Project
# # Mini Project
# # Student Result Calculator. The program should:
# # Ask for the number of students.
# # Take marks as input.
# # Handle invalid marks (non-numeric input).
# # Calculate: Average, Highest, Lowest
# # Handle cases where no valid marks are entered.
# # Display results without crashing.

marks = []
try:
    n = int(input("Enter the number of students: "))
    for i in range(n):
        try:
            mark = float(input(f"Enter marks of students {i + 1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid marks! This student's marks were skipped.")
    if len(marks) == 0:
        print("No valid marks are entered.")
    else:
        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)
        print("\nStudent Result")
        print("Average Marks:", average)
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
except ValueError:
    print("Invalid input! Please enter a valid number of students.")
finally:
    print("Program finished.")
