# # 1. Array Functions
import numpy as np
arr = np.array([45, 12, 89, 23, 67])
# a. Sort in Ascending Order.
print(np.sort(arr))

# # b. Sort in Descending Order
# # Use slicing: 
print(np.sort(arr)[::-1])

# # c. argsort() - instead of returning the sorted values, it return the indices that would sort the array.
arr = np.array([45, 12, 89, 23])
print(np.argsort(arr))

# # d. unique() - return only unique values
arr = np.array([10, 20, 20, 30, 30, 30, 40])
print(np.unique(arr))

# # e. where() - used to find indices matching a condition
arr = np.array([10, 25, 40, 18, 60])
print(np.where(arr > 20))

# # f. argmax() - return the index of largest value
arr = np.array([20, 45, 15, 90, 55])
print(arr.argmax())

# # g. argmin() - return the index of smallest value.
arr = np.array([20, 40, 15, 90, 55])
print(arr.argmin())

# # h. nonzero() - return indices of non-zero values
arr = np.array([0, 5, 0, 8, 10])
print(np.nonzero(arr))
