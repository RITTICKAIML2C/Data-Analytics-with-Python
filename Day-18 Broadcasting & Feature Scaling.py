# # 1. Boradcasting - Broadcasting allows NumPy to perform arithmetic operations between arrays of different shapes without writing loops.
import numpy as np 
arr = np.array([10, 20, 30, 40])
print(arr + 5)

# # 2. Broadcasting with Two Arrays
import numpy as np 
A = np.array([10, 20, 30])
B = np.array([1, 2, 3])
print(A + B)

# # 3. Broadcasting a Row Vector
import numpy as np
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix + np.array([1, 2, 3]))

# # 4. Broadcasting a Column Vector
import numpy as np
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix + np.array([
    [1],
    [2]
]))

# # 5. Min-Max Normalization
# max(x)−min(x) / x−min(x)​
import numpy as np
data = np.array([10, 20, 30, 40, 50])
print((data-data.min()) / (data.max() - data.min()))

# # 6. Standardization (Z-score)
# # Formula : x−μ / σ
import numpy as np 
data = np.array([10, 20, 30, 40, 50])
print((data - data.mean()) / data.std())

# # 7. Why Feature Scaling ? - Machine learning algorithms can become biased toward larger values
# # Suppose one feature is: Salary = 900000
# # Another feature: Experience = 2
