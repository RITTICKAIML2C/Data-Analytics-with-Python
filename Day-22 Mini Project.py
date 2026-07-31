# # Mini Project - Customer Purchase Classification Dashboard 
import numpy as np

# Customer purchase amounts
customers = np.array([
    1200,
    4500,
    8200,
    15000,
    700,
    6200,
    9800,
    3500,
    18000,
    2500
])
print("Original Purchase Amounts:")
print(customers)
premium = customers >= 10000
regular = (customers >= 5000) & (customers < 10000)
basic = customers < 5000
print("\nPremium Customers (≥ ₹10,000):")
print(customers[premium])
print("\nRegular Customers (₹5,000–₹9,999):")
print(customers[regular])
print("\nBasic Customers (< ₹5,000):")
print(customers[basic])
conditions = [premium, regular, basic]
labels = ["Premium", "Regular", "Basic"]
customer_labels = np.select(
    conditions,
    labels,
    default="Unknown"
)
print("\nCustomer Labels:")
print(customer_labels)
print("\nNumber of Premium Customers:", np.sum(premium))
print("Number of Regular Customers:", np.sum(regular))
print("Number of Basic Customers:", np.sum(basic))
print("\nAverage Purchase Amount: ₹", np.mean(customers))
print("Highest Purchase Amount: ₹", np.max(customers))
print("Lowest Purchase Amount: ₹", np.min(customers))
