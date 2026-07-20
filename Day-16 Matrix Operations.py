# # What is a matrix ?
import numpy as np 
A = np.array([
    [1. 2],
    [3, 4]
])
Rows = 2, Column = 2, Shape = (2, 2)

# # 1. Matrix Operations
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# # a. Addition
print(A + B)

# # b. Substraction
print(A - B)

# # c. Element-Wise Multiplication
print(A * B)

# # d. Matrix Multiplication (Dot Product)
print(np.dot(A, B))

# # e. Transpose 
print(A.T)
print(B.T)

# # f. Identity Matrix - it has 1 on the diagonal and 0 elsewhere 
print(np.eye(3))

# # g. Matrix Shape
print(A.shape)
print(B.shape)

# # h. Matrix Dimensions 
print(A.ndim)
print(B.ndim)
