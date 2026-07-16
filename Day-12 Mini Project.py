# # Mini Project 
# # Monthly Sales Report Generator
# # Create : sales = np.array([1200, 1500, 1800, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200])
# # Your program should: Display original sales, Reshape into 4×3, Reshape into 3×4, Display transpose
# # Flatten the array, Split into 4 equal months, Split into 2 half-year reports, Print every result with proper labels
import numpy as np 
sales = np.array([
1200,
1500,
1800,
2200,
2500,
2700,
3000,
3200,
3500,
3700,
4000,
4200
])
print("Original Sales:", sales)
print("4X3:", sales.reshape(3, 4))
print("3X4:", sales.reshape(4, 3))
matrix = sales.reshape(4, 3)
print("Transpose:", matrix.T)
print("Flatten:", sales.flatten())
print("Split into 4 equal monts:", np.split(sales, 4))
print("Split into 2 half-year reports:", np.split(sales, 2))
