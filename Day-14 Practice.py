import numpy as np
# # 1. Create : arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# # print : Total sum, mean, maximum, minimum
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("Total sum:", arr.sum())
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())

# # 2. Using the same array print:
# # Rows sum, Column sum, Row mean, Column mean
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("Row Sums:", arr.sum(axis = 1))
print("Column Sums:", arr.sum(axis = 0))
print("Row Means:", arr.mean(axis = 1))
print("Column Means:", arr.mean(axis = 0))

# # 3. Create : numbers = np.array([25, 36, 49, 64, 81])
# # Print: Square Root, Square, Sum
numbers = np.array([25,36,49,64,81])
print("Square Root:", np.sqrt(numbers))
print("Square:", np.square(numbers))
print("Sum:", np.sum(numbers))

# # 4. Create : values = np.array([-5,-10,15,-20,25])
# # Print: Absolute Values, Maximum, Minimum
values = np.array([-5,-10,15,-20,25])
print("Absolute:", np.abs(values))
print("Maximum:", np.max(values))
print("Minimum:", np.min(values))

# # 5. Create : prices = np.array([99.45, 150.89, 201.12, 450.67, 999.99]) 
# # Print : Rounded Values, Ceil Values, Floor Values
prices = np.array([
99.45,
150.89,
201.12,
450.67,
999.99
])
print("Rounded Values:", np.round(prices))
print("Ceil Values:", np.ceil(prices))
print("Floor Values:", np.floor(prices))

# # 6. Create : sales = np.array([[1200, 1800, 2500], [2200, 3100, 2800], [1500, 2600, 3300]])
# # Print : Total sales, Sales per month (column-wise), Sales per product (row-wise), Average Sales per month
sales = np.array([
[1200,1800,2500],
[2200,3100,2800],
[1500,2600,3300]
])
print("Total Sales:", sales.sum())
print("Sales per Month (column-wise):", sales.sum(axis = 0))
print("Sales per Product:", sales.sum(axis = 1))
print("Average Sales per Month:", sales.mean(axis = 0))

# # Industry Practice
# # Company Performance Dashboard 
# # Create : 
# # profit = np.array([
# # [120000,130000,125000],
# # [150000,145000,160000],
# # [170000,165000,180000],
# # [155000,150000,158000]
# # ])
# # Display : Overall profit, Profit by quarter (row-wise sum), Profit by department (column-wise sum)
# # Average quarterly profit, Highest profit, Lowest profit
profit = np.array([
[120000,130000,125000],
[150000,145000,160000],
[170000,165000,180000],
[155000,150000,158000]
])
print("Overall Profit:", profit.sum())
print("Profit by Quarter (row-wise sum):", profit.sum(axis = 1))
print("Profit by Department (column-wise sum):", profit.sum(axis = 0))
print("Average Quarterly Profit:", profit.mean())
print("Highest Profit:", profit.max())
print("Lowest Profit:", profit.min())

