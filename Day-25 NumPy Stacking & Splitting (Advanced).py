# # 1. np.vstack() - stack arrays vertically (row-wise),
import numpy as np 
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(np.vstack((A, B)))

# # 2. np.hstack() - stack arrays horizontally (column-wise for 1D arrays)
import numpy as np 
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(np.hstack((A, B)))

# # 3. np.coulmn_stack() - coverts 1D arrays into columns and joins them
import numpy as np
name_id = np.array([101,102,103])
salary = np.array([40000,50000,60000])
print(np.column_stack((name_id, salary)))

# # 4. np.row_stack() - works like vstack()
import numpy as np 
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(np.row_stack((A, B)))
print(np.vstack((A, B))) - alternative 

# # 5. np.dstack() - stacks arrays along the third dimensions.
import numpy as np 
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dstack((A, B)))

# # 6. np.split() - splits a 1D Array into equal parts
import numpy as np 
arr = np.arange(12)
print(np.split(arr, 3))

# # 7. np.hsplit() - split columns 
import numpy as np 
matrix = np.arange(16).reshape(4, 4)
print(np.hsplit(matrix, 2))

# # 8. np.vsplit() - splits rows
import numpy as np 
matrix = np.arange(16).reshape(4, 4)
print(np.vsplit(matrix, 2))

