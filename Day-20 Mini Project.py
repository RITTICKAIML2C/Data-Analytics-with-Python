# # Mini Project
# # Student Result Analytics Dashboard 
# # Create : marks = np.array([78, 45, 91, 66, 82, 39, 55, 97, 71, 28, 88, 63])
# # Display : Original marks Passed marks Failed marks Excellent marks (≥85) Average marks (40–84)
# # Calculate : Average of passed students, Average of failed students, Average of excellent students, Count of each category, Pass percentage, Highest mark, Lowest mark, Overall average
import numpy as np
marks = np.array([
    78,
    45,
    91,
    66,
    82,
    39,
    55,
    97,
    71,
    28,
    88,
    63
])
passed = marks[marks >= 40]
failed = marks[marks < 40]
excellent = marks[marks >= 85]
average = marks[(marks >= 40) & (marks <= 84)]
print("Original Marks:", marks)
print("Passed Marks:", passed)
print("Failed Marks:", failed)
print("Excellent Marks (>=85):", excellent)
print("Average Marks (40-84):", average)
print("Average of Passed Students:", np.mean(passed))
print("Average of Failed Students:", np.mean(failed))
print("Average of Excellent Students:", np.mean(excellent))
print("Count of Passed Students:", len(passed))
print("Count of Failed Students:", len(failed))
print("Count of Excellent Students:", len(excellent))
print("Count of Average Students:", len(average))
print("Pass Percentage:", (len(passed) / len(marks)) * 100, "%")
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Overall Average:", np.mean(marks))
