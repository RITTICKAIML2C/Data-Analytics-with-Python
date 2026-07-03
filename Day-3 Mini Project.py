# # Mini Project
# # 📂 Step 5: Mini Project
# # Student Record Management System
# # Create a menu-driven program:
# # 1. Add Student
# # 2. View Students
# # 3. Search Student
# # 4. Exit
# # Requirements:
# # Store records in students.txt.
# # Add new students.
# # Display all students.
# # Search for a student by name.
# # This is your first file-based application.

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")
    # 1. Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        with open("students.txt", "a") as file:
            file.write(name + "," + age + "," + course + "\n")
        print("Student added successfully!")
    # 2. View Students
    elif choice == "2":
        print("\n--- Student List ---")
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())
    # 3. Search Student
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        with open("students.txt", "r") as file:
            for line in file:
                if search.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True
        if not found:
            print("Student not found!")
    # 4. Exit
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
