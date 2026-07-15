# # 1. Create :
# # marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])
# # Print : sum, mean, median, max, mim, standard deviation, variance
import numpy as np
marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])
print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Median:", np.median(marks))
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Standard Deviation:", marks.std())
print("Variance:", marks.var())

# # 2. Create:
# # sales = np.array([1200, 3500, 8000, 4500, 600, 9800, 2500, 7200])
# # Print: Highest sale, lowest sale, index of highest sale, index of lowest sale
import numpy as np 
sales = np.array([1200, 3500, 8000, 4500, 600, 9800, 2500, 7200])
print("Highest Sale:", sales.max())
print("Lowest Sale:", sales.min())
print("Index of Highest Sale:", sales.argmax())
print("Index of Lowest Sale:", sales.argmin())

# # 3. Create 
# # salary = np.array([35000, 42000, 50000, 62000, 71000, 48000, 55000])
# # Print: Average salary, Median Salary, Standard Deviation, Variance 
import numpy as np 
salary = np.array([35000, 42000, 50000, 62000, 71000, 48000, 55000])
print("Average Salary:", salary.mean())
print("Median Salary:", np.median(salary))
print("Standard Deviation:", salary.std())
print("Variance:", salary.var())

# # 4. Create:
# # revenue = np.array([1000, 1200, 1500, 1700, 2000])
# # Print : Cumulative Sum, Cumulative Product
import numpy as np 
revenue = np.array([1000, 1200, 1500, 1700, 2000])
print("Cumulative Sum:", revenue.cumsum())
print("Cumulative Product:", revenue.cumprod())

# # 5. Create:
# # temperature = np.array([31, 33, 35, 36, 34, 32, 30])
# # Print: Highest temperature, Lowest temperature, Average temperature, Median temperature
import numpy as np 
temperature = np.array([31, 33, 35, 36, 34, 32, 30])
print("Highest Temperature:", temperature.max())
print("Lowest Temperature:", temperature.min())
print("Average Temperature:", temperature.mean())
print("Median Temperature:", np.median(temperature))

# # 6. Create:
# # expenses = np.array([12000, 15000, 18000, 22000, 17000, 16000])
# # Print: Total expenses, Average expenses, Highest Expense, Lowest Expense, Standard Deviation
import numpy as np
expenses = np.array([12000, 15000, 18000, 22000, 17000, 16000])
print("Total Expenses:", expenses.sum())
print("Average Expenses:", expenses.mean())
print("Highest Expense:", expenses.max())
print("Lowest Expense:", expenses.min())
print("Standard Deviation:", expenses.std())

# # Industry Practice
# # Comapany Performance Analysis
# # Create : 
# # profit = np.array([120000, 135000, 150000, 142000, 160000, 175000, 180000, 165000])
# # Display : Total profit, Average profit, Median profit, Highest profi, Lowest profit
# # Profit variance, Profit standard deviation, Month with highest profit (using argmax()), Month with lowest profit (using argmin())
import numpy as np
profit = np.array([120000, 135000, 150000, 142000, 160000, 175000, 180000, 165000])
print("Total Profit:", profit.sum())
print("Average Profit:", profit.mean())
print("Median Profit:", np.median(profit))
print("Highest Profit:", profit.max())
print("Lowest Profit:", profit.min())
print("Profit Variance:", profit.var())
print("Profit Standard Deviation:", profit.std())
print("Month with highest profit:", profit.argmax())
print("Month with lowest profit:", profit.argmin())
