# # Mini Project - Sales Report Extractor 
# # Write a program for the following dataset:
# # sales = np.array([
# #     [1200,1500,1800,2000],
# #    [2200,2500,2800,3000],
# #    [3200,3500,3800,4000],
# #    [4200,4500,4800,5000]
# #])
# # Your program should display:
# # Original sales matrix First row Last row First column Last column Middle 2×2 block First and third rows (using fancy indexing) Sales greater than ₹3000
# # Highest sale Lowest sale Average sale

import numpy as np 
sales = np.array([
    [1200,1500,1800,2000],
    [2200,2500,2800,3000],
    [3200,3500,3800,4000],
    [4200,4500,4800,5000]
])
print("Original Sales Matrix:", sales)
print("First Row:", sales[0])
print("Last Row:", sales[-1])
print("First Column:", sales[:, 0])
print("Last Column:", sales[:, -1])
print("Middle 2x2 block:", sales[1:3, 1:3])
print("First and Third Row:", sales[[0, 2]])
print("Sales greater than Rs3000:", sales[sales > 3000])
print("Highest Sales:", sales.max())
print("Lowest Sales:", sales.min())
print("Average Sales:", sales.mean())
