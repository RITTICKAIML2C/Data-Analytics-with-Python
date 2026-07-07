# # Lambda Functions - a short anonymous function

# # without lambda function
def square(x):
    return x * x

# # with lambda function 
squares = lambda x: x * x
print(squares(5))

# # Lamba with Multiple Parameters
add = lambda a, b: a + b
print(add(10, 20))

# # map() in Python - apply this operation to every item.
# # Suppose you want to increase every salary by 10%.
salaries = [30000, 40000, 50000]
new_salaries = list(map(lambda salary: salary * 1.10, salaries))
print(new_salaries)

# # Filter() in Python - leeps only the items that satisfy a condition.
# # filter employees earning more than 50,000.
salaries = [30000, 45000, 60000, 80000]
high_salary = list(filter(lambda salary: salary > 50000, salaries))
print(high_salary)

# # sorted() in Python 
# # Sort employee by salary
employees = [
    {"name": "Aman", "salary": 45000}, 
    {"name": "Rahul", "salary": 70000},
    {"name": "Priya", "salary": 55000}
]
sorted_employees = sorted(employees, key = lambda employee: employee["salary"])
print(sorted_employees)
