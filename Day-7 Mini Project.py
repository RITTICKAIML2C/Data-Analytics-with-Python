# # Mini Project
# # Sales Report Generator
# # Create a CSV file: Product,Sales, Laptop,50000, Phone,30000, Tablet,20000m, Monitor,15000, Keyboard,5000
# # Your program should: Read the CSV file, Display all products, Calculate total sales, Calculate average sales.
# # Find the highest-selling product, Find the lowest-selling product, Display a professional summary.

import csv
total = 0
products = []
with open("sales.csv", "r") as file:
    reader = csv. reader(file)
    next(reader)
    for row in reader:
        print(row)
        total += int(row[1])
        products.append(row)
average = total / len(products)
highest = max(products, key = lambda product: int[product[1]])
lowest = min(products, key = lambda product: int[product[1]])
print("Total Sales:", total)
print("Average Sales:", average)
print("Highest Selling Product:", highest[0], highest[1])
print("Lowest Selling Product:", lowest[0], lowest[1])
