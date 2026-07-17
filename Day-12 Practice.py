# # 1. Create: arr = np.arange(1,13)
# # Print : Original array, Reshape into 3×4, Reshape into 2×6
import numpy as np 
arr = np.arange(1,13)
print("Original Array:", arr)
print("Array 3X4:", arr.reshape(3, 4))
print("Array 2X6:", arr.reshape(2, 6))

# # 2. Create:
# # matrix = np.array([
# # [10,20,30],
# # [40,50,60]
# # ])
# # Print : flatten, ravel, transpose
import numpy as np 
matrix = np.array([
[10,20,30],
[40,50,60]
])
print("Flatten Matrix:", matrix.flatten())
print("Ravel Array:", matrix.ravel())
print("Transpose Matrix:", matrix.T)

# # 3. Create : 
# # a = np.array([1,2,3]), b = np.array([4,5,6])
# # Print : concatenate, vertical, horizontal stack
import numpy as np 
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Concatenate:", np.concatenate((a,b)))
print("Vertical Stack:", np.vstack((a, b)))
print("Horizontal Stack:", np.hstack((a, b)))

# # 4. Create : arr = np.arange(1,17)
# # Split it into : 4 equal arrays, 2 equal arrays
import numpy as np 
arr = np.arange(1,17)
print("4 Equal Arrays:", np.split(arr, 4))
print("2 Equal Arrays:", np.split(arr, 2))

# # 5. Create: matrix = np.arange(1,17).reshape(4,4)
# # Split : Vertically into 2 parts, Horizontally into 2 parts
import numpy as np 
matrix = np.arange(1,17).reshape(4,4)
print("Vertically into 2 parts:", np.vsplit(matrix, 2))
print("Horizontal into 2 parts:", np.hsplit(matrix, 2))

# # Industry Practice
# # Employee Data Organizer
# # Create : employees = np.array([35000,42000,50000,62000,71000,48000,55000,68000])
# # Task : Reshape into 4×2, Reshape into 2×4, Flatten it, Split into 4 equal parts, Print transpose
import numpy as np
employees = np.array([
35000,
42000,
50000,
62000,
71000,
48000,
55000,
68000
])
print("4X2:", employees.reshape(4, 2))
print("2X4:", employees.reshape(2, 4))
print("Flatten:", employees.flatten())
print("Split into 4 equal parts:", np.split(employees, 4))
print
