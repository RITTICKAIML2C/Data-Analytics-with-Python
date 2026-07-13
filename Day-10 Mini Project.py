# # Mini Project 
# # Product Pricing System
# # Create: 
# # products = np.array([
# # 500,
# # 1200,
# # 2500,
# # 800,
# # 3000,
# # 4500,
# # 600
# # ])
# # Your program should display: Original prices, Prices after 18% GST, Prices after 15% discount, Prices after adding ₹100 shipping, Total price, Average price, Highest price, Lowest price
# # Print everything with proper labels

import numpy as np 
products = np.array([
500,
1200,
2500,
800,
3000,
4500,
600
])
print("Original Price:", products)
print("Price after 18% GST:", products * 1.18)
print("Prices after 15% discount:", products * 0.85)
print("Prices after adding ₹100 shipping", products + 100)
print("Total Price:", products.sum())
print("Average Price:", products.mean())
print("Highest Price:", products.max())
print("Lowest Price:", products.min())
