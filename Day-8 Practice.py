# # 1. Create a Numpy array: [10, 20, 30, 40, 50]
# # Print: Array, Shape, Size, Data type
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("DataType:", arr.dtype)

# # 2. Create : [5, 10, 15, 20, 25]
# # Print : First Element, Third Element, Last Element 
import numpy as np 
arr = np.array([5, 10, 15, 20, 25])
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Last Element:", arr[-1])

# # 3. Create: np.zeros(10), np.ones(8)
import numpy as np 
zero = np.zeros(10)
print("Zeroes:", zero)
ones = np.ones(8)
print("Ones:", ones)

# # 4. Using np.range() create: 
# # Numbers from 1–20, Even numbers from 2–30, Multiples of 5 from 5–50
import numpy as np 
numbers = np.arange(1,21)
print("Numbers from 1-20:", numbers)
even_numbers = np.arange(2, 31, 2)
print("Even Numbers from 2-30:", even_numbers)
multiples = np.arange(0, 51, 5)
print("Multiples of 5 from 5-50:", multiples)

# # 5. Using np.linspace() create: 
# # 10 equally spaced numbers from 0 to 100
import numpy as np
equally_spaced = np.linspace(0, 100, 10)
print("Equally Spaced Number from 0 to 100:", (equally_spaced))

# # 6. Create this 2D Array:
# # [[10,20,30],
# #  [40,50,60],
# #  [70,80,90]]
# # Print : Shape, Number of Dimensions, Size
import numpy as np
matrix = np.array([
    [10, 20, 30], 
    [40, 50, 60],
    [70, 80, 90]
])
print("2D Array:", matrix)
print("Shape:", matrix.shape)
print("Number of Dimensions:", matrix.ndim)
print("Size:", matrix.size)

# # 7. Industry Practice 
# # Employee Salary Analysis
# # Create : [35000, 42000, 50000, 62000, 71000]
# # Print : Shape, Size, DataType, First Salary, Last Salary
import numpy as np
employees_salary = np.array([35000, 42000, 50000, 62000, 71000])
print("Shape:", employees_salary.shape)
print("Size", employees_salary.size)
print("DataType:", employees_salary.dtype)
print("First Salary:", employees_salary[0])
print("Last Salary:", employees_salary[-1])
