# # 1. Generate: 20 random integers between 100 and 500
# # Print: Complete Array, Highest Value, Lowest Value
import numpy as np 
array = np.random.randint(100, 500, 20)
print("Complete Array:", array)
print("Highest Value:", array.max())
print("Lowest Value:", array.min())

# # 2. Generate : np.random.rand(10)
# # Print : Mean, Maximum, Minimum
arr = np.random.rand(10)
print("Array:", arr)
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())

# # 3. Generate: np.random.randn(15)
# # Print : mean, standard deviation
array = np.random.randn(15)
print("Array:", array)
print("Mean:", array.mean())
print("Standard Deviation:", array.std())

# # 4. Create : cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"]
# # Randomly select 12 cities
cities = [
"Delhi",
"Mumbai",
"Kolkata",
"Chennai",
"Bengaluru"
]
select = np.random.choice(cities, size = 12)
print("Random Select:", select)

# # 5. Use : np.random.seed(100)
# # Generate : 10 random integers from 1- 100 
np.random.seed(100)
arr = np.random.randint(1, 101, 10)
print(arr)

# # Industry Practice
# # Customer Data Generator:
# # Generate: Customers IDs 1001-1100. Generate 20 random IDs.
# # Generate Customers Purchases : 500-10000. Generate 20 purchaes 
# # Randomly assign : Gold, Silver, Bronze to each customer.
# # Display : IDs, Purchases, Membership Type
np.random.seed(100)
customer_ids = np.random.choice(np.arange(1001, 1101), 20)
print("Customer IDs:", customer_ids)
purchases = np.random.randint(500, 10001, 20)
print("Purchases:", purchases)
membership = np.random.choice(["Gold", "Silver", "Bronze"], 20)
print("Membership:", membership)
