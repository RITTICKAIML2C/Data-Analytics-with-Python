# # 1. Create : arr = np.array([5,10,15,20,25])
# # Print : Add 5, Subtract 2, Multiply by 3, Divide by 5, Square every element
import numpy as np 
arr = np.array([5, 10, 15, 20, 25])
print("Sum:", arr + 5)
print("Difference:", arr - 2)
print("Multipy:", arr * 3)
print("Division:", arr / 5)
print("Square:", arr ** 2)

# # 2. Create: a = np.array([2,4,6,8]), b = np.array([1,2,3,4])
# # Print: a + b, a - b, a * b, a / b
import numpy as np 
a = np.array([2,4,6,8])
b = np.array([1,2,3,4])
print("Sum:", a + b)
print("Difference:", a - b)
print("Multiply:", a * b)
print("Division:", a / b)

# # 3. Create: 
# # salary = np.array([
# # 35000,
# # 42000,
# # 50000,
# # 62000,
# # 71000
# # ])
# # Calculate : Salary after ₹5000 increment, Salary after 10% bonus, Salary after 5% tax deduction
import numpy as np 
salary = np.array([
35000,
42000,
50000,
62000,
71000
])
print("Salary after Rs5000 increment:", salary + 5000)
print("Salary after 10% bonus:", salary * 1.10)
print("Salary after 5% tax deduction:", salary * 0.95)

# # 4. Create: 
# # prices = np.array([
# # 120,
# # 250,
# # 400,
# # 600,
# # 900
# # ])
# # Calculate: Prices after 18% GST, Prices after 20% discount, Prices after adding ₹50 delivery charge
import numpy as np 
prices = np.array([
120,
250,
400,
600,
900
])
print("Price after 18% GST:", prices * 1.18)
print("Price after 20% discount:", prices * 0.80)
print("Price after adding Rs50 delivery charge:", prices + 50)

# # 5. Create: 
# # marks = np.array([
# # 78,
# # 85,
# # 92,
# # 67,
# # 88
# # ])
# # Print : Sum, Mean, Maximum, Minimum, Product
import numpy as np 
marks = np.array([
78,
85,
92,
67,
88
])
print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Product:", marks.prod())

# # 6. Create: 
# # sales = np.array([
# # 1200,
# # 2500,
# # 3000,
# # 4500,
# # 5000
# # ])
# # Calculate: Sales after 12% growth, Sales after ₹500 cashback, Sales after 5% reduction
import numpy as np 
sales = np.array([
1200,
2500,
3000,
4500,
5000
])
print("Sales after 12% growth:", sales * 1.12)
print("Sales after Rs500 cashback:", sales - 500)
print("Sales after %5 reduction:", sales * 0.95)

# # 7. Industry Practice
# # Employee Bonus Calculator 
# # Create: 
# # salary = np.array([
# # 35000,
# # 42000,
# # 50000,
# # 62000,
# # 71000,
# # 48000
# # ])
# # Display: Original salary, Salary after 12% annual increment, Salary after ₹3000 bonus, Salary after 10% performance bonus
import numpy as np 
salary = np.array([
35000,
42000,
50000,
62000,
71000,
48000
])
print("Original Salary:", salary)
print("Salary after 12% annual increment:", salary * 1.12)
print("Salary after Rs3000 bonus:", salary + 3000)
print("Salary after 10% performance bonus:", salary * 1.10)
