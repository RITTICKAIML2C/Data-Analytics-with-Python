# # Industry Practice - Employee Analytics 
import numpy as np
salary = np.array([
    35000,
    42000,
    50000,
    62000,
    71000,
    48000,
    55000,
    68000
])
print("Top Employees:", salary[[3,4,7]])
print("Employees >50000:", salary[salary > 50000])
print("First Five Employees:", salary[:5])
print("Last Three Employees:", salary[-3:])
print("Middle Employees:", salary[2:6])
