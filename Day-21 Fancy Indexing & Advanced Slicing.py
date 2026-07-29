# # 1. Fancy Indexing (1D Array)
import numpy as np 
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[[0, 2, 5]])

# # 2. Fancy Indexing (2D Array)
import numpy as np
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix[[0, 2]])

# # 3. Row & Column Selection
import numpy as np 
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix[:, 1])
print(matrix[1, :])

# # 4. Slice Rows and Columns 
import numpy as np 
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[1:4, 2:5])

# # 5. Reverse Rows and Columns 
import numpy as np
matrix = np.arange(1, 10).reshape(3, 3)
print(matrix[::-1])
print(matrix[:, ::-1])

# # 6. Boolean + Fancy Indexing 
import numpy as np 
marks = np.array([78, 85, 92, 67, 88, 95])
print(marks[[0, 2, 5]])
print(marks[marks > 80])


