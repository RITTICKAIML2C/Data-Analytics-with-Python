# # 1. Create a lambda function to calculate cube of a number.
cube = lambda x: x ** 3
print(cube(2))

# # 2. Create a lamba function that returns the maximum of two number.
maximum = lambda a,b: max(a, b)
print(maximum(10, 20))

# # 3. Using map() convert: numbers = [2, 4, 6, 8] into their squares.
numbers = [2, 4, 6, 8]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# # 4. Using filter(), keep only numbers greater than 20. 
# # numbers = [5, 18, 22, 35, 12, 40]
numbers = [5, 18, 22, 35, 12, 40]
new_numbers = list(filter(lambda number: number > 20, numbers))
print(new_numbers) 

# # 5. Using sorted() and lambda sort: 
# # students = [
# #     {"name": "Aman", "marks": 78},
# #     {"name": "Rahul", "marks": 92},
# #     {"name": "Priya", "marks": 85}
# # ]
# # Sort by marks in ascending order 
students = [
    {"name": "Aman", "marks": 78},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 85}
]
sorted_marks = sorted(students, key = lambda student: student["marks"])
print(sorted_marks)

# # 6. Using map(), add 18% GST to:
# # prices = [100, 250, 500, 1000]
prices = [100, 250, 500, 1000]
new_price = list(map(lambda price: price * 1.18, prices))
print(new_price)

# # 7. Industry Practice
# # Customer Transaction Analysis
# # Given:
# # transactions = [
# #     {"customer": "Aman", "amount": 1200},
# #     {"customer": "Rahul", "amount": 8500},
# #    {"customer": "Priya", "amount": 4500},
# #     {"customer": "Riya", "amount": 11000}
# # ]
# # Using lambda, map(), filter(), and sorted():
# # Find transactions above ₹5000, Add 18% GST to every transaction, Sort transactions by amount (highest first), Extract only customer names.

transactions = [
    {"customer": "Aman", "amount": 1200},
    {"customer": "Rahul", "amount": 8500},
    {"customer": "Priya", "amount": 4500},
    {"customer": "Riya", "amount": 11000}
]
high_transactions = list(filter(lambda transaction: transaction["amount"] > 5000, transactions))
print(high_transactions)
gst_transactions = list(map(lambda transaction: transaction["amount"] * 1.18, transactions))
print(gst_transactions)
sorted_transactions = sorted(transactions, key = lambda transaction:  transaction["amount"], reverse = True)
print(sorted_transactions)
customer_names = list(map(lambda name: name["customer"], transactions))
print(customer_names)
