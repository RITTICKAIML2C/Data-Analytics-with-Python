# # 1. reshape() - changes the shape of an array without changing its data.
import numpy as np
arr = np.arange(1, 13)
print(arr)
print(arr.reshape(3,4)) # converting a long list into a table

# # 2. flatten() - converts it back into one dimension
import numpy as np 
matrix = np.array([
    [10, 20, 30], 
    [40, 50, 60]
])
print(matrix)
print(matrix.flatten())

# # 3. ravel() - return a view when possible, making it more memeory efficient
import numpy as np 
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix)
print(matrix.ravel())

# # 4. transpose() - rows becomes columns
import numpy as np 
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix)
print(matrix.T)

# # 5. concatenate() - combines arrays
import numpy as np 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))

# # 6. vstack() - vertical stacking 
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))

# # 7. hstack() - horizontal stacking
import numpy as np 
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack((a,b)))

# # 8. split() 
import numpy as np 
arr = np.arange(1, 13)
print(np.split(arr,3))

# # 9. vsplit() - split vertically
import numpy as np 
matrix = np.arange(1, 13).reshape(4, 3)
print(np.vsplit(matrix,2))

# # 10. hsplit() - split columns
import numpy as np 
matrix = np.arange(1, 13).reshape(3, 4)
print(np.hsplit(matrix,2))

# # Industry Example 
# # Suppose a company has two month of sales
# # Jan : jan = np.array([1200,1500,1800])
# # Feb : feb = np.array([1700,2000,2100])
# # 1. Comnbine them 
import numpy as np 
jan = np.array([1200,1500,1800])
feb = np.array([1700,2000,2100])
sales = np.concatenate((jan, feb))
print(sales.reshape(2, 3))
