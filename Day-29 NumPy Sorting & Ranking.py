# # 1. np.sort() - sort values in ascending order.
import numpy as np
arr = np.array([50, 20, 80, 10, 40])
print(np.sort(arr))

# # 2. Sorting a 2D array with axis
import numpy as np 
data = np.array([
    [50, 20, 80],
    [30, 90, 40],
    [70, 10, 60]
])
# # a. Sort each row 
print(np.sort(data, axis = 1))

# # b. Sort each column
print(np.sort(data, axis = 0))

# # 3. np.argsort() - gives you the indices that would produce the sorted values.
import numpy as np 
marks = np.array([78, 91, 65, 88])
print(np.argsort(marks)) # - [2 0 3 1]
print(marks[np.argsort(marks)]) # - [65 78 88 91]

# # 4. Finding Top N Values 
import numpy as np 
sales = np.array([1200, 5000, 3200, 9000, 4500, 7800])
sorted_sales = np.sort(sales)
# a. To find the top 3:
print(sorted_sales[-3:])

# # b. For descending order:
print(np.sort(sales)[::-1][:3])

# # 5. Top N Employees using argsort()
import numpy as np 
salary = np.array([35000, 52000, 48000, 71000, 62000])
# # a. Get indices in ascending order:
print(np.argsort(salary))

# # b. Top 3 employee indices:
print(salary[-3:][::-1])

# # 6. np.partition() - When you only care about the top/bottom values and don't need the entire array sorted, np.partition() can be useful:
import numpy as np 
arr = np.array([50, 10, 90, 30, 70, 20])
print(np.partition(arr, -3)[-3:])

