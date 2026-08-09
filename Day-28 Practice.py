import numpy as np 
# # 1. Basic Axis Operations
# # Print : Total Sum, Column-wise Sum, Row-wise sum, Column-wise mean, Row-wise mean
data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("Total Sum:", np.sum(data))
print("Column-Wise Sum:", np.sum(data, axis = 0))
print("Row-Wise Sum:", np.sum(data, axis = 1))
print("Column-Wise Mean:", np.mean(data, axis = 0))
print("Row-Wise Mean:", np.mean(data, axis = 1))

# # 2. Maximum & Minimum 
# # Print: Highest mark overall, Lowest mark overall, Highest mark in each column, Highest mark in each row
# # Lowest mark in each column, Lowest mark in each row
marks = np.array([
    [78,85,91],
    [67,88,95],
    [72,90,84]
])
print("Highest Marks Overall:", np.max(marks))
print("Lowest Marks Overall:", np.min(marks))
print("Highest Marks in Each Column:", np.max(marks, axis = 0))
print("Highest Marks in Each Row:", np.max(marks, axis = 1))
print("Lowest Marks in Each Column:", np.min(marks, axis = 0))
print("Lowest Marks in Each Row:", np.min(marks, axis = 1))

# # 3. Index Analysis 
# # Find : Index of maximum value in each column, Index of maximum value in each row, Index of minimum value in each column, Index of minimum value in each row
sales = np.array([
    [1200,2500,1800],
    [3200,4500,2800],
    [5100,6200,4000]
])
print("Index of maximum value in each column:", np.argmax(sales, axis = 0))
print("Index of maximum value in each row:", np.argmax(sales, axis = 1))
print("Index of minimum value in each column:", np.argmin(sales, axis = 0))
print("Index of minimum value in each row:", np.argmin(sales, axis = 1))

# # 4. Counting with Conditions 
# # Find : Number of scores ≥ 80, Number of scores < 50, Number of scores between 50 and 80, Number of scores ≥ 70 in each row
scores = np.array([
    [45,78,91],
    [32,85,67],
    [90,55,88]
])
print("Number of scores ≥ 80:", np.sum(scores >= 80))
print("Number of scores < 50:", np.sum(scores < 50))
print("Number of scores between 50 and 80:", np.sum((scores >= 50) & (scores <= 80)))
print("Number of scores ≥ 70 in each row:", np.sum(scores >= 70, axis = 1))

# # 5. Employee Analytics 
# # Calculate: Total salary Average salary Average salary per column Average salary per row Highest salary per column Highest salary per row
salary = np.array([
    [35000,42000,50000],
    [45000,55000,62000],
    [48000,60000,71000]
])
print("Total Salary:", np.sum(salary))
print("Average Salary:", np.mean(salary))
print("Average Salary per column:", np.mean(salary, axis = 0))
print("Average Salary per row:", np.mean(salary, axis = 1))
print("Highest Salary per column:", np.max(salary, axis = 0))
print("Highest Salary per row:", np.max(salary, axis = 1))

# # Industry Practice 
# # Monthly Sales Analytics 
# # Build a small analytics report displaying: Total sales Average sales Total sales per row Total sales per column Average sales per row Average sales per column Highest sale in each row Highest sale in each column Lowest sale in each row
# # Lowest sale in each column
# # Number of sales greater than ₹3000
# # Number of sales greater than ₹4000
sales = np.array([
    [1200,1500,1800,2000],
    [2200,2500,2800,3000],
    [3200,3500,3800,4000],
    [4200,4500,4800,5000]
])
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Total Sales per row:", np.sum(sales, axis = 1))
print("Total Sales per column:", np.sum(sales, axis = 0))
print("Average sales per row:", np.mean(sales, axis = 1))
print("Average sales per column:", np.mean(sales, axis = 0))
print("Highest sales in each row:", np.max(sales, axis = 1))
print("Highest sales in each column:", np.max(sales, axis = 0))
print("Lowest sales in each row:", np.min(sales, axis = 1))
print("Lowest sales in each column:", np.min(sales, axis = 0))
print("Number of sales greater than Rs3000:", np.sum(sales > 3000))
print("Number of sales greater than Rs4000:", np.sum(sales > 5000))
