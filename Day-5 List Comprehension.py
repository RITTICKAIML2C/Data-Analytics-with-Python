# # List Comprehension

# # Increase in sale without list comprehension
sales = [100, 200, 300, 400]
new_sales = []
for sale in sales:
    new_sales.append(sale * 1.10)
print(new_sales)

# # Increase in sale with list comprehension
sales = [100, 200, 300, 400]
new_sales = [sale * 1.10 for sale in sales]
print(new_sales)

# # Basic List Comprehension 
number = [i for i in range(5)]
print(number)

# # Square of numbers
squares = [i ** 2 for i in range(1, 6)]
print(squares)

# # Filtering Data
numbers = [10, 15, 20, 25, 30]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# # COnditional Expression 
marks = [45, 70, 30, 90]
result = ["Pass" if marks >= 40 else "Fail" for marks in marks]
print(result)

# # String Operations 
names = ["rittick", "rahul", "soumya"]
upper_names = [name.upper() for name in names]
print(upper_names)

# # Real Data Analytics Example
sales = [1200, 3500, 900, 4500, 2500]
high_sales = [sale for sale in sales if sale > 2000]
print(high_sales)
