import numpy as np
# # 1. Create : arr = np.arange(1,13)
# # Print : Original array, Shape, Reshape(3, 4), Reshape(2, 6)
arr = np.arange(1,13)
print("Original Array:", arr)
print("Shape:", np.shape(arr))
print("Reshape into (3,4):", arr.reshape(3, 4))
print("Reshape into (2, 6):", arr.reshape(2, 6))

# # 2. Using the same array : arr = np.arange(1,13)
# # Print : Reshape(-1, 3), Reshape(4, -1)
arr = np.arange(1,13)
print("Reshape(-1, 3):", arr.reshape(-1, 3))
print("Reshape(4, -1):", arr.reshape(4, -1))

# # 3. Create : matrix = np.array([[10, 20], [30, 40]])
# # Print : flatten, ravel, shape after flatten
matrix = np.array([
    [10,20],
    [30,40]
])
flatten_matrix = matrix.flatten()
print("Flatten Matrix:", flatten_matrix)
print("Shape after Flatten:", np.shape(flatten_matrix))
print("Ravel:", np.ravel(matrix))

# # 4. Create : arr = np.array([5,10,15,20])
# # Resize it to : 6 elements, 8 elements
arr = np.array([5,10,15,20])
print(np.resize(arr, 6))
print(np.resize(arr, 8))

# # 5. Create : marks = np.array([78,85,91,67])
# # Print : Original Array, Expand Dimension(axis = 0), Expand dimension(axis = 1), Squeexe back to 1D
marks = np.array([78,85,91,67])
print("Original Array:", marks)
print("Expanded Dimension (axis = 0):", np.expand_dims(marks, axis = 0))
print("Expanded Dimension (axis = 1):", np.expand_dims(marks, axis = 1))
print("Squeeze back to 1D:", np.squeeze(marks))

# # 6. Create : sales = np.arange(100,112)
# # Print : Original Array, Reshape(3, 4), Transpose, Flatten
sales = np.arange(100,112)
print("Original Array:", sales)
print("Reshape into (3, 4):", sales.reshape(3, 4))
print("Transpose:", sales.T)
print("Flatten:", sales.flatten())

# Industry Practice
# # Employee Attendance Formatter
# # Display : Original Array, Shape, Reshape into (3,4), Transpose, Flatten, Expand dimension (axis = 0), Expand Dimension (axis = 1), Squeezed Array
employee_hours = np.array([
8,9,7,8,
6,8,9,7,
8,8,7,9
])
print("Original Array:", employee_hours)
print("Shape:", np.shape(employee_hours))
print("Reshape into (3, 4):", employee_hours.reshape(3, 4))
print("Transpose:", employee_hours.T)
print("Flatten:", employee_hours.flatten())
print("Expanded Dimension (axis = 0):", np.expand_dims(employee_hours, axis = 0))
print("Expanded Dimension (axis = 1):", np.expand_dims(employee_hours, axis = 1))
print("Squeezed Array:", np.squeeze(employee_hours))
