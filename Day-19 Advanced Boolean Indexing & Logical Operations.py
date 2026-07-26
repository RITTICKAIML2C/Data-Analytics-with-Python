# # 1. Boolean Arrays - A comparison on a NumPy array returns a Boolean array.
import numpy as np 
arr = np.array([10, 25, 40, 55, 70])
print(arr > 30)

# # 2. Multiple Conditions
import numpy as np 
arr = np.array([10, 25, 40, 55, 70])
print([arr > 20] & (arr < 60))

# # 3. np.logical_and() - equivalent to &
import numpy as np
arr = np.array([10, 25, 40, 55, 70])
print(np.logical_and(arr > 20, arr < 60))

# # 4. np.logical_or() - equivalent to |
import numpy as np
arr = np.array([10, 25, 40, 55, 70])
print(np.logical_or(arr < 20, arr > 60))

# # 5. np.logical_not() - equivalent to ~
import numpy as np
arr = np.array([10, 25, 40, 55, 70])
print(np.logical_not(arr > 30))

# # 6. Replacing values conditionally
import numpy as np
arr = np.array([10, 25, 40, 55, 70])
print(np.where(arr > 50, 100, arr))

