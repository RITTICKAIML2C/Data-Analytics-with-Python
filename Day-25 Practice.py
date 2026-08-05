import numpy as np 
# # 1. A = np.array([10,20,30]), B = np.array([40,50,60])
# # Print : vertical stack, horizontal stack
A = np.array([10,20,30])
B = np.array([40,50,60])
print("Vertical Stack:", np.vstack((A, B)))
print("Horizontal Stack:", np.hstack((A, B)))

# # 2. id = np.array([101,102,103,104]), salary = np.array([35000,42000,50000,61000])
# # Print : Column stack, Row Stack
id = np.array([101,102,103,104])
salary = np.array([35000,42000,50000,61000])
print("Column Stack:", np.column_stack((id, salary)))
print("Row Stack:", np.row_stack((id, salary)))
print("Row Stack:", np.vstack((id, salary)))

# # 3. arr = np.arange(1,17)
# # Print : split into 4 parts, split into 2 parts
arr = np.arange(1,17)
print("Split into 4 equal parts:", np.split(arr, 4))
print("Split into 2 equal parts:", np.split(arr, 2))

# # 4. matrix = np.arange(1,17).reshape(4,4)
# # Print : Vertical split into 2 parts, Horizontal split into 2 parts
matrix = np.arange(1,17).reshape(4,4)
print("Vertical split into 2 parts:", np.vsplit(matrix, 2))
print("Horizontal split into 2 parts:", np.hsplit(matrix, 2))

# # 5. A = np.array([[10,20],[30,40]]), B = np.array([[50,60],[70,80]])
# # Print : dstack, vstack, hstack
A = np.array([[10,20],[30,40]])
B = np.array([[50,60],[70,80]])
print("Dstack:", np.dstack((A, B)))
print("Vstack:", np.vstack((A, B)))
print("Hstack:", np.hstack((A, B)))

# # 6. name = np.array(["A","B","C","D"]), marks = np.array([78,85,91,67]), age = np.array([18,19,18,20])
# # Print : Coulmn Stack of all three arrays, shape of the result
name = np.array(["A","B","C","D"])
marks = np.array([78,85,91,67])
age = np.array([18,19,18,20])
result = np.column_stack((name, marks, age))
print("Column Stack of all three arrays:", result)
print("Shape Result:", result.shape)

# # Industry Practice
# # Employee Data Manager 
# # Display :Employee table using column_stack(), Vertical stack of salary and experience, Horizontal stack of salary and experience, Shape of employee table
# # Split employee table into: First 3 employees, Last 2 employees
emp_id = np.array([101,102,103,104,105])
salary = np.array([35000,42000,51000,62000,70000])
experience = np.array([2,3,5,6,8])
result = np.column_stack((emp_id, salary, experience))
print("Employee table using column_stack():", result)
print("Vertical Stack of Salary and Experience:", np.vstack((salary, experience)))
print("Horizontal Stack of Salary and Experience:", np.hstack((salary, experience)))
print("Shape of Employee Table:", result.shape)
print("Split First 3 Employee:", result[:3])
print("Split Last 2 Employee:", result[3:])
