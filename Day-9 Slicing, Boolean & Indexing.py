# # 1. Array Slicing
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])

# # a. First Three Elements
print(arr[:3])

# # b. Last Three Elements 
print(arr[-3:])

# # c. Every Second Element
print(arr[::2])

# # d. Reverse an Array
print(arr[::-1])

# # 2. Slicing a 2D Array
import numpy as np
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# # a. First Row
print(matrix[0])

# # b. Second Column
print(matrix[:,1])

# # c. Last Row
print(matrix[-1])

# # d. First Two Rows
print(matrix[:2])

# # e. First Two Columns
print(matrix[:, :2])

# # 3. Boolean Masking
# # Suppose: sales = np.array([1200, 4500, 800, 6000, 3000])
import numpy as np
sales = np.array([1200, 4500, 800, 6000, 3000])

# # a. Find Sales greater than Rs3000
print(sales > 3000)

# # b. Filter the data
print(sales[sales > 3000])

# # c. Sales less than Rs2000
print(sales[sales < 2000])

# # d. Sales Between Rs2000 and Rs 5000
print(sales[(sales >= 2000) & (sales <= 5000)])

# # 4. Fancy Indexing - lets you select multipe elements by index
import numpy as np 
arr = np.array([10, 20, 30, 40, 50, 60])

# # a. 1st, 3rd and 5th element:
print(arr[[0, 2, 4]])

# # 5. Real Business Example
# # Suppose employee salaries are: salary = np.array([35000,42000,50000,62000,71000])
import numpy as np 
salary = np.array([35000,42000,50000,62000,71000])

# # a. Employees earning above Rs50000
print(salary[salary > 50000])

