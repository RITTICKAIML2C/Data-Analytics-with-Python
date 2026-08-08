import numpy as np
# # 1. marks = np.array([78,85,91,67,88])
# # Save as marks.npy, Load it back, Print loaded array
marks = np.array([78,85,91,67,88])
np.save("marks.npy", marks)
print(np.load("marks.npy"))

# # 2. sales = np.array([1200,1500,1800,2200])
# # Save as sales.txt, Load it back, Print loaded data
sales = np.array([1200,1500,1800,2200])
np.savetxt("sales.txt", sales)
print(np.loadtxt("sales.txt"))

# # 3. salary = np.array([35000,42000,51000,62000])
# # Save as salary.csv, Use comma delimiter, Load the CSV, Print it
salary = np.array([35000,42000,51000,62000])
np.savetxt("salary.csv", salary, delimiter=",")
print(np.loadtxt("salary.csv", delimiter=","))

# # 4. prices = np.array([10.456, 20.987, 30.123, 40.765])
# # Save with only 2 decimal places, Load it, Print 
prices = np.array([10.456,20.987,30.123,40.765])
np.savetxt("prices.txt", prices, fmt="%.2f")
print(np.loadtxt("prices.txt"))

# # 5. matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
# # Save as CSV, Load it, Print original shape,Print loaded shape
matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
np.savetxt("matrix.csv", matrix, delimiter=",", fmt="%d")
loaded = np.loadtxt("matrix.csv", delimiter=",")
print(matrix.shape)
print(loaded.shape)
print(loaded)

# # 6. attendance = np.array([90,85,88,92,80])
# # Save as TXT using integer format (fmt="%d"), Load it, Print loaded array
attendance = np.array([90,85,88,92,80])
np.savetxt("attendance.txt", attendance, fmt="%d")
print(np.loadtxt("attendance.txt", dtype=int))

# # Industry Practice 
# # Employee Salary Report 
# # Display : Employee table Save as employee_report.csv Load it back Print loaded table Print shape Print average salary
employee_id = np.array([101,102,103,104,105])
salary = np.array([35000,42000,51000,62000,70000])
table = np.column_stack((employee_id, salary))
print(table)
np.savetxt("employee_report.csv", table, delimiter=",", fmt="%d")
loaded = np.loadtxt("employee_report.csv", delimiter=",", dtype=int)
print(loaded)
print(loaded.shape)
print(np.mean(loaded[:,1]))
