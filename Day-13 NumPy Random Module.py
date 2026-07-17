# # 1. np.random.randint()
# # Syntax = np.random.randint(start, stop, step)
import numpy as np 
sales = np.random.randint(1000, 5000, size = 10)
print(sales)

# # 2. np.random.rand() - generates random decimal number from 0 to 1
import numpy as np 
score = np.random.rand(5)
print(score)

# # 3. np.random.randn() - generate number from a normal (Gaussian) distribution.
import numpy as np 
data = np.random.randn(10)
print(data)

# # 4. np.random.choice() - randomly selects values from a list.
import numpy as np 
departments = ["HR", "Sales", "Finance", "Analytics"]
print(np.random.choice(departments, size = 8))

# # 5. np.random.seed() - normally every run gives different random numbers
import numpy as np
np.random.seed(42)
print(np.random.randint(1, 100, 5))

# # Industry Example 
# # Generate Employee data:
import numpy as np 
np.random.seed(1)
salary = np.random.randint(30000, 80000, 10)
department = np.random.choice(["HR", "Sales", "Finance", "Analytics"], size = 10)
print(salary)
print(department)
