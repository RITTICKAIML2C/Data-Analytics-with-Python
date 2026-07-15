# # Mini Project 
# # Sales Analytics Dashboard (NumPy Version)
# # Create : sales = np.array([1200, 4500, 3200, 5100, 800, 6500, 7200, 2800, 3900, 10000])
# # Your program should display:
# # Original sales, total sales, Average sales, Median sales, Highest sale, Lowest sale
# # Index of highest sale, Index of lowest sale, Standard deviation, Variance, Cumulative sales

import numpy as np 
sales = np.array([1200, 4500, 3200, 5100, 800, 6500, 7200, 2800, 3900, 10000])
print("Original Sales:", sales)
print("Total Sales:", sales.sum())
print("Average Sales:", sales.mean())
print("Median Sales:", np.median(sales))
print("Highest Sales:", sales.max())
print("Lowest Sales:", sales.min())
print("Index with highest sale:", sales.argmax())
print("Sales with lowest sale:", sales.argmin())
print("Standar Deviation:", sales.std())
print("Variance:", sales.var())
print("Cumulative Sales:", sales.cumsum())
