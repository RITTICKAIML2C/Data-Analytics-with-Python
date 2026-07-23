# # 1. Boolean Arrays - a comparison on a NumPy array returns a Boolean array.
import numpy as np 
arr = np.array([10, 20, 30, 40])
print(arr > 20)
print(arr[arr > 20])

# # 2. np.where() - can replace values based on a condition
import numpy as np 
marks = np.array([35, 60, 80, 25, 90])
print(np.where(marks >= 40, "Pass", "Fail"))

# # 3. np.clip() - limit values to a given range
import numpy as np 
marks = np.array([20, 45, 78, 110])
print(np.clip(marks, 0, 100))

# # 4. np.isnan() - checks whether values are missing (NaN)
import numpy as np 
arr = np.array([10, np.nan, 25, np.nan])
print(np.isnan(arr))

# # 5. np.isfinite() - checks if values are finite numbers.
import numpy as np
arr = np.array([10, np.inf, -np.inf, np.nan, 25])
print(np.isfinite(arr))

# # 6. np.isinf() - checks infinite values
import numpy as np 
arr = np.array([10, np.inf, -np.inf])
print(np.isinf(arr))

# # 7. np.any() - returns True if at least one element satisfies the conditon
import numpy as np 
arr = np.array([10, 20, 30])
print(np.any(arr > 25))

# # 8. np.all() - return True only if every element satisfies the condition.
import numpy as np 
arr = np.array([10, 20, 30])
print(np.all(arr > 5))

