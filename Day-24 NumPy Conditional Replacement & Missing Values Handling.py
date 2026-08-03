# # 1. np.maximum() - Returns the element-wise maximum of two arrays.
import numpy as np
A = np.array([10, 50, 30])
B = np.array([20, 40, 35])
print(np.maximum(A, B))

# # 2. np.minimum() - Returns the element-wise minimum.
import numpy as np
A = np.array([10, 50, 30])
B = np.array([20, 40, 35])
print(np.minimum(A, B))

# # 3. Missing Values (NaN)
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(sales.mean())

# # 4. np.nanmean() - ignores NaN values
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanmean(sales))

# # 5. np.nanmedian() 
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanmedian(sales))

# # 6. np.nanstd()
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanstd(sales))

# # 7. np.nanvar()
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanvar(sales))

# # 8. np.nanmax() 
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanmax(sales))

# # 9. np.nanmin()
import numpy as np 
sales = np.array([1200, 1500, np.nan, 2500, 3000])
print(np.nanmin(sales))

# # 10. np.nan_to_num() - replaces missing values
import numpy as np 
sales = np.array([1200, np.nan, 2500])
print(np.nan_to_num(sales))
print(np.nan_to_num(sales, nan = 2000))

