# # 1. Axis in NumPy
# # For a 2D array:
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
# # 1. Axis 
print(arr.sum(axis = 0))
print(arr.sum(axis = 1))

# # 2. Sum
print(arr.sum())

# # 3. Mean
print(arr.mean())

# # 4. Maximum 
print(arr.max())

# # 5. Minimum 
print(arr.min())

# # 6. Row-wise Operations 
print(arr.sum(axis = 1))
print(arr.mean(axis = 1))
print(arr.max(axis = 1))
print(arr.min(axis = 1))

# # 7. Column Wise Operations 
print(arr.sum(axis = 0))
print(arr.mean(axis = 0))
print(arr.max(axis = 0))
print(arr.min(axis = 0))

# # 8. Useful functions 
print(np.sqrt(arr))
print(np.square(arr))
print(np.abs(arr))
print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))


