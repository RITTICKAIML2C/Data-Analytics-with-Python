# # Mini Project 
# # Student Attendance Matrix Dashboard 
# # Your program should display: Original attendance array Shape Reshape into 4 × 3 Transpose Flatten array Ravel array Expand dimension (axis=0) Expand dimension (axis=1)
# # Squeezed array Reshape into 2 × 6 Reshape using (-1, 2)
import numpy as np 
attendance = np.array([
90,85,88,
95,80,84,
75,89,91,
87,92,86
])
print("Original Attendance Array:", attendance)
print("Shape:", np.shape(attendance))
print("Reshape into 4x3:", attendance.reshape(4, 3))
print("Transpose:", attendance.T)
print("Flatten:", attendance.flatten())
print("Ravel:", attendance.ravel())
print("Exapnd Dimension (axis = 0):", np.expand_dims(attendance, axis = 0))
print("Exapnd Dimension (axis = 1):", np.expand_dims(attendance, axis = 1))
print("Squeezed Array:", np.squeeze(attendance))
print("Reshape into 2x6:", attendance.reshape(2, 6))
print("Reshape using (-1, 2):", attendance.reshape(-1, 2))
