# # Mini Project
# # Sales Performance Analyzer
# # Create:
# # sales = np.array([
# # 1200,
# # 3500,
# # 8000,
# # 4500,
# # 600,
# # 9800,
# # 2500,
# # 7200,
# # 1500,
# # 5100
# # ])
# # Your program should display: Original sales, Top sales (> ₹5000), Low sales (< ₹2000), Medium sales (₹2000–₹5000 inclusive), Every alternate sale, Reverse order of sales
# # First five sales, Last three sales
# # Print each result with clear labels.

import numpy as np 
sales = np.array([
1200,
3500,
8000,
4500,
600,
9800,
2500,
7200,
1500,
5100
])
print("Original Sales:", sales)
print("Top Sales (> Rs5000):", sales[sales > 5000])
print("Low Sales (< Rs2000):", sales[sales < 2000])
print("Medium Sales (Rs2000 - Rs5000 inclusive):", sales[(sales >= 2000) & (sales <= 5000)])
print("Every Alternate Sale:", sales[::2])
print("Reverse Order Of Sales:", sales[::-1])
print("First Five Sales:", sales[0:5])
print("Last Three Sales:", sales[-3:])
