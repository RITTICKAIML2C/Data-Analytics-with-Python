# # Mini Project 
# # Student Analytics Dashboard 
# # Create : 
# # marks = np.array([
# # [78,85,90],
# # [88,76,91],
# # [67,72,80],
# # [95,89,94],
# # [81,84,79]
# # ])
# # Your program should display: Original marks Total marks Overall average Subject-wise totals (axis=0) Student-wise totals (axis=1)
# # Subject-wise averages Student-wise averages Highest mark Lowest mark Square of every mark Square root of every mark
import numpy as np 
marks = np.array([
[78,85,90],
[88,76,91],
[67,72,80],
[95,89,94],
[81,84,79]
])
print("Original Marks:", marks)
print("Total Marks:", marks.sum())
print("Overall Average:", marks.mean())
print("Subject Wise Totals (axis = 0):", marks.sum(axis = 0))
print("Student Wise Totals (aixs = 1):", marks.sum(axis = 1))
print("Subject Wise Average:", marks.mean(axis = 0))
print("Student Wise Average:", marks.mean(axis = 1))
print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())
print("Square of every marks:", np.square(marks))
print("Square Root of every marks:", np.sqrt(marks))
