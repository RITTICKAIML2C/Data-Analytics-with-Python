# # 1. Filter Even and Odd Numbers
import numpy as np
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print("Even Numbers:", arr[arr % 2 == 0])
print("Odd Numbers:", arr[arr % 2 != 0])

# # 2. Filter Using Multiple Conditions 
import numpy as np 
marks = np.array([35, 48, 72, 90, 66, 28, 81])
print("Marks between 50 and 80:", marks[(marks >= 50) & (marks <= 80)])

# # 3. Replace Values Using np.where()
import numpy as np 
salary = np.array([35000, 42000, 52000, 61000, 72000])
print(np.where(salary < 50000, salary + 5000, salary))

# # 4. Multiple Conditions Using np.select()
import numpy as np
marks = np.array([35, 55, 72, 91, 83, 28])
conditions = [
    marks >= 85, 
    marks >= 40
]
choices = [
    "Excellent", 
    "Pass"
]
print(np.select(conditions, choices, default = "Fail"))

# # 5. Count Values Satisfying a Condition
import numpy as np
sales = np.array([1200, 4500, 6200, 3000, 9800, 1500])
print("Sales > Rs5000:", np.sum(sales > 5000))
print("Sales <= Rs5000:", np.sum(sales <= 5000))

# # 6. Find Indices Matching a Condition
import numpy as np 
temperature = np.array([28, 31, 35, 39, 42, 30, 26])
print(np.where(temperature > 35)[0])
