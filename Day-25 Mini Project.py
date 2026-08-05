# # Mini Project
# # Student Database Builder 
# # Your program should display: Student database using column_stack() Vertical stack of marks and attendance Horizontal stack of marks and attendance
# # Shape of student database Split student database into: First 2 students Last 3 students Highest mark Average attendance
import numpy as np 
student_id = np.array([101,102,103,104,105])
marks = np.array([78,85,91,67,88])
attendance = np.array([90,95,85,80,92])
student_database = np.column_stack((student_id, marks, attendance))
print("Student database using column_stack():", student_database)
print("Vertical Stack of Marks and Attendance:", np.vstack((marks, attendance)))
print("Horizontal Stack of Marks and Attendance:", np.hstack((marks, attendance)))
print("Shape of Student Database:", student_database.shape)
print("First 2 Students:", student_database[:2])
print("Last 3 Students:", student_database[2:])
print("Highest Marks:", np.max(marks))
print("Average Attendance:", np.mean(attendance))
