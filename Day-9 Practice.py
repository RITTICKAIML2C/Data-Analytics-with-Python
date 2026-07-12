# # 1. Create : arr = np.array([5,10,15,20,25,30,35,40])
# # Print : First four elements, Last three elements, Every second element, Reverse the array
import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
print("First Four Element:", arr[0:4])
print("Last Three Elements:", arr[-3:])
print("Every Second Element:", arr[::2])
print("Reversed Array:", arr[::-1])

# # 2. Create: 
# # matrix = np.array([
# #     [11,12,13],
# #     [21,22,23],
# #     [31,32,33]
# # ])
# # Print: First row, Last row, Second column, First two columns
import numpy as np
matrix = np.array([
    [11,12,13],
    [21,22,23],
    [31,32,33]
])
print("First Row:", matrix[0])
print("Last Row:", matrix[-1])
print("Second Column:", matrix[:,1])
print("First Two Column:", matrix[:, :2])

# # 3. Given : marks = np.array([35,78,90,42,66,25,88,95])
# # Using Boolean masking, print: Marks greater than 50, Marks less than 40, Marks between 40 and 80 (inclusive)
import numpy as np
marks = np.array([35, 78, 90, 42, 66, 25, 88, 95])
print("Marks greater than 50:", marks[marks > 50])
print("Marks less than 40:", marks[marks < 40])
print("Marks between 40 and 80 (inclusive):", marks[(marks >= 40) & (marks <= 80)])

# # 4. Given: prices = np.array([100,250,500,750,1000,1250])
# # Using fancy indexing, print: First, third and last prices, Second and fourth prices
import numpy as np 
prices = np.array([100,250,500,750,1000,1250])
print("First, Third and Last Price:", prices[[0, 2, -1]])
print("Second and Fourth Price:", prices[[1, 3]])

# # 5. Given: 
# # employees = np.array([
# #     ["Aman","Analytics"],
# #     ["Rahul","Sales"],
# #     ["Priya","HR"],
# #     ["Riya","Finance"]
# # ])
# # Print: All employee names, All departments, First two employees
import numpy as np 
employees = np.array([
    ["Aman","Analytics"],
    ["Rahul","Sales"],
    ["Priya","HR"],
    ["Riya","Finance"]
])
print("All Employees Names:", employees[:,0])
print("All Departments:", employees[:,1])
print("First Two Employees:", employees[:2])

# # 6. Given: sales = np.array([1200,4500,800,6000,3000,7200,1500])
# # Print: Sales above ₹3000, Sales below ₹2000, Sales between ₹2000 and ₹6000 (inclusive)
import numpy as np
sales = np.array([1200,4500,800,6000,3000,7200,1500])
print("Sales above Rs3000:", sales[sales > 3000])
print("Sales below Rs2000:", sales[sales < 2000])
print("Sales between Rs2000 and Rs6000 (inclusive):", sales[(sales >= 2000) & (sales <= 6000)])

# # 7. Industry Practice
# # Employee Salary Filter
# # Create : salary = np.array([
# # 35000,
# # 42000,
# # 50000,
# # 62000,
# # 71000,
# # 48000,
# # 55000
# # ])
# # Display: Salaries above ₹50,000, Salaries below ₹45,000, Salaries between ₹45,000 and ₹60,000, Highest salary (using indexing after sorting is not required yet)
import numpy as np 
salary = np.array([
35000,
42000,
50000,
62000,
71000,
48000,
55000
])
print("Salaries above Rs50000:", salary[salary > 50000])
print("Salaries below Rs45000:", salary[salary < 45000])
print("Salaries between Rs45000 and Rs60000:", salary[(salary >= 45000) & (salary <= 60000)])
print("Highest Salary:", max(salary))
