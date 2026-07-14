# # 1. Sum
import numpy as np
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.sum())

# # 2. Mean (Average)
import numpy as np 
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.mean())

# # 3. Median 
import numpy as np
marks = np.array([45, 60, 72, 80, 95])
print(np.median(marks))

# # 4. Maximum and Minimum
import numpy as np
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.max())
print(sales.min())

# # 5. Standard Deviation 
import numpy as np
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.std())

# # 6. Variance 
import numpy as np
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.var())

# # 7. argmax() and argmin() - largest or lowest sales at which index
import numpy as np 
sales = np.array([1200, 2500, 3000, 4500, 5000])
print(sales.argmax())
print(sales.argmin())

# # 8. Cumulative Sum - running total 
import numpy as np 
sales = np.array([100, 200, 300, 400])
print(sales.cumsum())

# # 9. Cumulative Product
import numpy as np 
numbers = np.array([2, 3, 4])
print(numbers.cumprod())

# # Industry Example 
# # Employee Salaries
# # salary = np.array([
# # 35000,
# # 42000,
# # 50000,
# # 62000,
# # 71000,
# # 48000
# # ])
import numpy as np 
salary = np.array([
35000,
42000,
50000,
62000,
71000,
48000
])
print("Average:", salary.mean())
print("Highest:", salary.max())
print("Lowest:", salary.min())
print("Median:", np.median(salary))
print("Standard Deviation:", salary.std())
print("Variance:", salary.var())
