# # 1. Percentiles 
import numpy as np 
marks = np.array([40, 50, 60, 70, 80, 90, 100])
print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))

# # 2. Quantiles - same as percentiles 
import numpy as np
marks = np.array([40,50,60,70,80,90,100])
print(np.quantile(marks, 0.25))
print(np.quantile(marks, 0.50))
print(np.quantile(marks, 0.75))

# # 3. Covariance - measures how two variables move together 
import numpy as np
hours = np.array([2, 4, 6, 8, 10])
marks = np.array([30, 45, 60, 75, 90])
print(np.cov(hours, marks))

# # 4. Correlation - correlation tells strength of relationship
import numpy as np 
hours = np.array([2, 4, 6, 8, 10])
marks = np.array([30, 45, 60, 75, 90])
print(np.corrcoef(hours, marks))
