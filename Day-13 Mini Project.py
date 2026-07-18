# # Mini Project 
# # Sales Data Simulator 
# # Create a program that generates: Sales : Generate 30 randoms sales, between 1000-20000
# # Randomly assign a product: Laptop, Phone, Tablet, Monitor, Keyboard
# # Randomly assign a city: Delhi, Mumbai, Kolkata, Hyderabad, Pune
# # Display: Sales, Products, Cities
# # Then print: Highest sale, Lowest sale, Average sale, Total sales
import numpy as np 
sales = np.random.randint(1000, 20001, 30)
print("Sales:", sales)
products = np.random.choice(["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"], 30)
print("Products:", products)
cities = np.random.choice(["Delhi", "Mumbai", "Kolkata", "Hyderabad", "Pune"], 30)
print("Cities:", cities)
print("Highest Sales:", sales.max())
print("Lowest Sales:", sales.min())
print("Average Sales:", sales.mean())
print("Total Sales:", sales.sum())
