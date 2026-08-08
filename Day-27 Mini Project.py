# # Mini Project 
# # Student Result Report Generator 
# # Your program should: Display the student report Save it as student_report.csv Load it back Print loaded report Print shape
# # Print average marks Print highest marks Print average attendance
import numpy as np
student_id = np.array([101,102,103,104,105])
marks = np.array([78,85,91,67,88])
attendance = np.array([90,95,85,80,92])
report = np.column_stack((student_id, marks, attendance))
print("Student Report:", report)
np.savetxt("student_report.csv", report, delimiter=",", fmt="%d")
loaded = np.loadtxt("student_report.csv", delimiter=",", dtype=int)
print("Loaded Report:", loaded)
print("Shape:", loaded.shape)
print("Average Marks:", np.mean(loaded[:,1]))
print("Highest Marks:", np.max(loaded[:,1]))
print("Average Attendance:", np.mean(loaded[:,2]))
