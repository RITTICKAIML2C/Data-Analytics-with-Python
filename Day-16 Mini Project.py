# # Mini Project 
# # Sales Data Quality Dashboard 
# # Create: sales = np.array([1200,4500,3200,5100,800,6500,7200,2800,3900,10000,4500,3200,7200])
# # Print : Original sales Sorted sales (ascending) Sorted sales (descending) Unique sales values Sales greater than ₹5000 Their indices Highest sale Lowest sale
# # Index of highest sale Index of lowest sale Non-zero values Non-zero indices
import numpy as np
sales = np.array([
1200,
4500,
3200,
5100,
800,
6500,
7200,
2800,
3900,
10000,
4500,
3200,
7200
])
print("Original Sales:", sales)
print("Sorted Sales (ascending):", np.sort(sales))
print("Sorted Sales (descemding):", np.sort(sales)[::-1])
print("Unqiue Sales Values:", np.unique(sales))
print("Sales greater than Rs5000:", np.where(sales > 5000))
print("Sales greater than Rs5000:", np.where(sales > 5000)[0])
print("Highest Sales:", np.max(sales))
print("Highest Sales Index:", np.argmax(sales))
print("Lowest Sales:", np.min(sales))
print("Lowest Sales Index:", np.argmin(sales))
print("Non-Zero Values:", np.nonzero(sales))
print("Non-Zero Indices:", np.nonzero(sales)[0])
