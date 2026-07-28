# # 1. Iterating Through Arrays
import numpy as np 
arr = np.array([10, 20, 30])
for x in arr:
    print(x)

# # 2. 2D Array
import numpy as np 
matrix = np.array([
    [10, 20], 
    [30, 40]
])
# # a. Row matrix
for row in matrix:
    print(row)

# # b. Iterate Every Element
for row in matrix:
    for value in row:
        print(value)

# # c. np.nditer() - professional way to iterate through arrays of any dimension
for x in np.nditer(matrix):
    print(x)

# # 3. Conditional Statistics - Instead of calculating statistics for the whole array, calculate them for filtered values.
import numpy as np 
marks = np.array([35, 55, 70, 90, 25])
print(marks[marks >= 40].mean())

# # 4. Counting Values - count how many values satisfy a condition.
import numpy as np 
marks = np.array([35, 55, 70, 90, 25])
print(np.sum(marks >= 40))

# # 5. Percentage
import numpy as np 
marks = np.array([35, 55, 70, 90, 25])
print("Percentage:", np.sum(marks >= 40) / len(marks) * 100)
