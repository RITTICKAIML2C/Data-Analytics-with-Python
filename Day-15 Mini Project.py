# # Mini Project
# # Product Sales Matrix Dashboard
# # Create : products = np.array([[1200,1500,1800],[2200,2500,2800],[3200,3500,3800]]), growth = np.array([[100,150,200], [200,250,300],[300,350,400]])
# # Your program should display: Original product sales Growth matrix Updated sales (products + growth) Difference (products - growth) Element-wise multiplication Matrix multiplication (np.dot) Transpose of product sales
# # Shape Number of dimensions Identity matrix of size 3 × 3
import numpy as np 
products = np.array([
    [1200,1500,1800],
    [2200,2500,2800],
    [3200,3500,3800]
])
growth = np.array([
    [100,150,200],
    [200,250,300],
    [300,350,400]
])
print("Original Product Sales:", products)
print("Growth Matrix:", growth)
print("Updated Sales:", products + growth)
print("Difference:", products - growth)
print("Element-Wise Multiplication:", products * growth)
print("Matrix Multiplication:", np.dot(products, growth))
print("Transpose of Product Sales:", products.T)
print("Shape:", products.shape, growth.shape)
print("Number of dimensions:", products.ndim, growth.ndim)
print("Identity Matrix:", np.eye(3, dtype = int))
