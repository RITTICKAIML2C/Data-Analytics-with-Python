# # For a 2D array:
import numpy as np 
data = np.array([
    [10, 20, 30], 
    [40, 50, 60], 
    [70, 80, 90]
])

# # 1. np.sum() 
print(np.sum(data))
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))

# # 2. np.mean() 
print(np.mean(data, axis = 0))
print(np.mean(data, axis = 1))

# # 3. np.max() / np.min() 
print(np.max(data, axis = 0))
print(np.min(data, axis = 1))

# # 4. np.argmax(), np.argmin() - return the index of the maximum / minimum 
print(np.argmax(data, axis = 0))
print(np.argmin(data, axis = 1))

# # 5. np.sum(condition) - very useful for counting.
sales = np.array([1200, 5000, 8000, 3000])
print(np.sum(sales > 4000))     # because two values are greater than 4000
