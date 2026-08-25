# # 1. Histogram 
# # Syntax = plt.hist(data)
import matplotlib.pyplot as plt 
salary = [30000, 35000, 40000, 45000, 50000, 52000,
          55000, 60000, 65000, 70000, 75000, 80000]
plt.hist(salary)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

# # 2. Understadning bins = more bins -> more detailed distributions
plt.hist(salary, bins=5)

