import numpy as np
# # 1. Create : A = np.array([[10, 20], [30, 40]]), B = np.array([5, 15], [25, 35])
# # Print : A + B, A - B, A X B (element-wise)
A = np.array([
    [10,20],
    [30,40]
])
B = np.array([
    [5,15],
    [25,35]
])
print("Addition:", A + B)
print("Substraction:", A - B)
print("Element-Wise:", A * B)

# # 2. Using the same matrix 
# # np.dot(A,B) and A @ B
A = np.array([
    [10,20],
    [30,40]
])
B = np.array([
    [5,15],
    [25,35]
])
print(np.dot(A, B))
print(A @ B)

# # 3. Create : matrix = np.array([[2, 4, 6], [8, 10, 12]])
# # Print : Shape, Number of Dimension, Tranpose 
matrix = np.array([
    [2,4,6],
    [8,10,12]
])
print("Shape:", matrix.shape)
print("Dimension:", matrix.ndim)
print("Transpose:", matrix.T)

# # 4. Create : 
# # Print Identity Matrix 
print("Identity Matrix:", np.eye(4))

# # 5. Create : sales = np.array([[1200, 1500], [1800, 2000]]), growth = np.array([200, 300], [400, 500])
# # Print : New sales after growth, Difference, Element-Wise Multiplication 
sales = np.array([
    [1200,1500],
    [1800,2000]
])
growth = np.array([
    [200,300],
    [400,500]
])
print("New Sales after Growth:", sales + growth)
print("Difference:", sales - growth)
print("Element-Wise Multiplication:", sales * growth)

# # 6. Create : marks = np.array([[78, 85], [92, 88]]), bonus = np.array([[2, 5], [3, 2]])
# # Print : Updated Marks, Matrix Multiplcation, Transpose 
marks = np.array([
    [78,85],
    [92,88]
])
bonus = np.array([
    [2,5],
    [3,2]
])
print("Updated Marks:", marks + bonus)
print("Matrix Multiplication:", np.dot(marks, bonus))
print("Transpose:", marks.T, bonus.T)

# # Industry Practice 
# # Company Branch Revenue Analysis
# # Create : revenue = np.array([[120000, 150000], [180000, 170000]]), expenses = np.array([[50000,60000],[70000,65000]])
# # Display: Total revenue (revenue + expenses), Profit (revenue - expenses), Element-wise multiplication, Matrix multiplication, Revenue transpose
revenue = np.array([
    [120000,150000],
    [180000,170000]
])
expenses = np.array([
    [50000,60000],
    [70000,65000]
])
print("Total Revenue:", revenue + expenses)
print("Profit:", revenue - expenses)
print("Element-Wise Multiplication:", revenue * expenses)
print("Matrix Multiplication:", np.dot(revenue, expenses))
print("Revenue Transpose:", revenue.T, expenses.T)

