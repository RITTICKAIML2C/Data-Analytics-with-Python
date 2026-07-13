# # 1. Arithemtic Operations 
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# # a. Addition
print(arr + 10)

# # b. Substraction
print(arr - 5)

# # c. Multiplication
print(arr * 2)

# # d. Division
print(arr / 2)

# # e. Exponents 
print(arr ** 2)

# # 2. Operations between Arrays
# import numpy as np 
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# # a. Addition
print(a + b)

# # b. Substraction
print(a - b)

# # c. Multiplication 
print(a * b)

# # d. Division
print(a / b)

# # 3. Vectorization  - done in one line without writting explicit loops
import numpy as np 
prices = np.array([100, 250, 500])
gst_price = prices * 1.18
print(gst_price)

# # 4. Broadcasting - automatically adds to every element
import numpy as np 
salary = np.array([35000, 42000, 50000])
salaries = salary + 500
print(salaries)

# import numpy as np
marks = np.array([70, 80, 90])
mark = marks * 1.05
print(mark)

# # 5. Useful NumPy Math Functions 
import numpy as np 
numbers = np.array([10, 20, 30, 40, 50, 60])

# # a. Total 
print(numbers.sum())

# # b. Average
print(numbers.mean())

# # c. Maximum
print(numbers.max())

# # d. Minimum 
print(numbers.min())

# # e. Product
print(numbers.prod())

# # Industry Example 
# # A company has product prices:
import numpy as np
prices = np.array([1000, 1500, 2000, 2500])
print("Gst Price:", prices * 1.18)
print("Discount:", prices * 0.90)
