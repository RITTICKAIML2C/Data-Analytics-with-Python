# # Mini Project
# # Student Marks Array
# # Create a NumPy Array: [78, 85, 92, 67, 88, 95, 73, 81]
# # Display: Complete Array, Shape, Number of Dimensions, Size, DataType, First Mark, Last Marks, Middle Marks
import numpy as np
marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])
print("Complete Array:", marks)
print("Shape:", marks.shape)
print("Number of Dimensions:", marks.ndim)
print("Size:", marks.size)
print("DataType:", marks.dtype)
print("First Marks:", marks[0])
print("Last Marks:", marks[-1])
print("Middle Marks:", marks[len(marks) // 2 -1 : len(marks) // 2 + 1])
