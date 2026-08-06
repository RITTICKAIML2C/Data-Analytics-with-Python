# # 1. reshape() - change the dimensions without changing the data
import numpy as np
arr = np.arange(1, 13)
print(arr.reshape(3, 4))

# # 2. reshape(-1, n) - NumPy automatically calculates one dimensions.
import numpy as np
arr = np.arange(1, 13)
print(arr.reshape(-1, 3))
print(arr.reshape(2, -1))

# # 3. flatten() - coverts any array into a 1D copy.
import numpy as np
matrix = np.array([
    [10, 20], 
    [30, 40]
])
print(matrix.flatten())

# # 4. ravel() - Also coverts to 1D.
import numpy as np
matrix = np.array([
    [10, 20],
    [30, 40]
])
print(matrix.ravel())

# # 5. resize() - changes array size.
import numpy as np
arr = np.array([1, 2, 3, 4])
print(np.resize(arr, 8))

# # 6. expand_dims() - adds a new dimension.
import numpy as np 
arr = np.array([10, 20, 30])
print(np.expand_dims(arr, axis = 0))
# # Column vector
print(np.expand_dims(arr, axis = 1))

# # 7. squeeze() - removes dimensions of size 1
import numpy as np 
arr = np.array([10, 20, 30])
print(np.squeeze(arr))

# # 8. Advanced transpose() - swaps rows and columns 
import numpy as np 
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix.T)

