# # 1. Basic Correlation Matrix 
df.corr(numeric_only = True)

import pandas as pd 
df = pd.DataFrame({
    "Experience": [1, 2, 3, 5, 7, 9],
    "Salary": [30000, 35000, 42000, 52000, 68000, 80000],
    "Performance": [60, 65, 70, 78, 88, 94]
})
print(df.corr())
