# # 1. Create a file named notes.txt and write your name and college into it.
with open("notes.txt", "w") as file:
    file.write("Your Name\n")
    file.write("Your College Name\n")

# # 2. Read the contents of notes.txt and print them
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

# # 3. Append the following line to the file: Learning Data Analytics, Read the file again.
with open("notes.txt", "a") as file:
    file.write("Learning Data Analytics\n")
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

# # 4. Create a file containing five student names, one per line. Read all names and print them using a loop.
with open("student.txt", "w") as file:
    file.write("Aman\n")
    file.write("Sammer\n")
    file.write("Fuddi\n")
    file.write("Bhuvan\n")
    file.write("Bencho\n")
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

# # 5. Create a CSV file named employees.csv with the following data: Name,Department,Salary, Rittick,Analytics,50000, Rahul,Sales,45000, Priya,HR,55000
# # Read the file and print every line.
with open("employees.csv", "w") as file:
    file.write("Name,Department,Salary\n")
    file.write("Rittick,Analytics,50000\n")
    file.write("Rahul,Sales,45000\n")
    file.write("Priya,HR,55000\n")
with open("employees.csv", "r") as file:
    for line in file:
        print(line.strip())

# # 6. Industry Practice: Employee Salary Report, Create a program that: Takes employee details., Saves them in employees.txt., Reads the file., Displays all employees., This simulates maintaining employee records
with open("employees.txt", "w") as file:
    for i in range(3):
        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = input("Enter salary: ")
        file.write(name + "," + dept + "," + salary + "\n")
with open("employees.txt", "r") as file:
    print("\nEmployee Records:")
    for line in file:
        print(line.strip())
