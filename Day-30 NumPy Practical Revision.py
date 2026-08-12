# # 1. Array Creation 
import numpy as np 
arr = np.array([10, 20, 30])
# Useful:
np.arange()
np.zeros()
np.ones()
np.full()

# # 2. Shape & Reshaping 
arr.shape
arr.reshape(3, 4)
arr.flatten()
arr.ravel()

# # 3. Indexing & Slicing 
arr[2]
arr[1:5]
matrix[1, 2]
matrix[:, 0]     # first column
matrix[0, :]     # first row

# # Fancy Indexing:
arr[[1, 3, 5]]

# # 4. Boolean Filtering 
salary[salary > 50000]

# # Multiple Conditions:
salary[(salary > 40000) & (salary < 70000)]

# # 5. Conditional Transformation
np.where(salary > 50000, "High", "Low")

# # Multiple categories:
np.select(
    [condition1, condition2],
    ["Category 1", "Category 2"],
    default="Other"
)

# # 6. Statistical Analysis
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.min(arr)
np.max(arr)
np.percentile(arr, 25)
np.percentile(arr, 50)
np.percentile(arr, 75)

# # For missing data:
np.nanmean()
np.nanmedian()
np.nanstd()
np.nanvar()
np.nanmin()
np.nanmax()

# # 7. Correlation & Covariance 
np.corrcoef(x, y)
np.cov(x, y)

# # 8. Axis Operations - This is one of the most important concepts for Data Analytics.
# # Column-Wise 
np.sum(data, axis=0)

# # Row=Wise
np.sum(data, axis=1)

# # Same concept applies to:
np.mean()
np.max()
np.min()
np.std()

# # 9. Ranking 
np.sort(arr)
np.argsort(arr)
np.argmax(arr)
np.argmin(arr)

# # TOp 3:
arr[np.argsort(arr)[-3:][::-1]]

# # 10. Missing Values
np.isnan(arr)

# # Replace missing values:
np.nan_to_num(arr, nan=50000)

