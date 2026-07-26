import numpy as np 
# # 1. Create : arr = np.array([5,10,15,20,25])
# # Print : Add 10, Multiply by 2
arr = np.array([5,10,15,20,25])
print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)

# # 2. Create : 
# # A = np.array([10,20,30]), B = np.array([2,4,6])
# # Print : Addition, Multiplication
A = np.array([10,20,30])
B = np.array([2,4,6])
print("Addition:", A + B)
print("Multiplication:", A * B)

# # 3. Create : 
# # matrix = np.array([
# #     [10,20,30],
# #     [40,50,60]
# # ])
# # row = np.array([1,2,3])
matrix = np.array([
    [10,20,30],
    [40,50,60]
])
print("New Matrix:", matrix + np.array([1, 2, 3]))

# # 4. Create : matrix = np.array([[10 20], [30, 40]])
# # Boradcast the column
matrix = np.array([
    [10,20],
    [30,40]
])
print("New Matrix:", matrix + np.array([
    [100], 
    [200]
]))

# # 5. Create : marks = np.array([50, 60, 70, 80, 90])
# # Print : Min-Max normalized values
marks = np.array([
50,
60,
70,
80,
90
])
print("Min-Max Value:", (marks - marks.min()) / marks.max() - marks.min())

# # 6. Create : salary = np.array([35000, 42000, 50000, 62000, 71000])
# # Print : Standarized Values
salary = np.array([
35000,
42000,
50000,
62000,
71000
])
print("Standardized Values:", (salary - salary.mean()) / salary.std())

# # 7. Industry Practice
# # Employee Salary Scaling 
# # Create : salary = np.array([35000, 42000, 50000, 62000, 71000, 48000, 55000])
# # Display : Original salary, Salary after ₹5000 increment, Salary after 10% bonus, Normalized salary, Standardized salary
salary = np.array([
35000,
42000,
50000,
62000,
71000,
48000,
55000
])
print("Original Salary:", salary)
print("Salary after Rs5000 increment:", salary + 5000)
print("Salary after 10% bonus:", salary * 1.10)
print("Normalized Value:", (salary - salary.min()) / salary.max() - salary.min())
print("Standardized Salary:", (salary - salary.min()) / salary.std())
