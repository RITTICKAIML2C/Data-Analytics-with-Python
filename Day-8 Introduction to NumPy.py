# # 1. Sotre it as Numpy Array
import numpy as np
marks = np.array([75, 82, 90, 68, 95])
print(marks)

# # 2. To increase every sale by 10%, you'd write:
sales = np.array([100, 200, 300])
new_sales = sales * 1.10
print(new_sales)

# # 3. Installing Numpy
# Install - pip install numpy

# # Checking if installed
import numpy as np
print(np.__version__)

# # 4. Creating Arrays
# # a. From a list 
import numpy as np 
numbers = np.array([10, 20, 30, 40])
print(numbers)

# # b. 2D Arrays
import numpy as np
matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])
print(matrix)

# # 5. Special Arrays
# # a. Zeroes
zero = np.zeros(5)
print(zero)

# # b. Ones 
one = np.ones(4)
print(one)

# # c. Range
range = np.arange(1, 11)
print(range)

# # d. Even Numbers
even_numbers = np.arange(2, 21, 2)
print(even_numbers)

# # e. Equally Sapced Numbers
equally_spaced = np.linspace(0, 100, 5)
print(equally_spaced)

# # 6. Array Attributes
arr = np.array([10, 20, 30, 40])
# a. Shape
print(arr.shape)

# # b. Number of Dimnesions
print(arr.ndim)

# # c. Size 
print(arr.size)

# # d. Data Type
print(arr.dtype)

# # 7. Indexing 
marks = np.array([75, 82, 90, 68, 95])

# # a. First Element
print(marks[0])

# # b. Last Element 
print(marks[-1])

# # c. Third Element
print(marks[2])

