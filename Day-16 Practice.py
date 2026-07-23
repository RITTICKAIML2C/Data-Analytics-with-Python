import numpy as np
# # 1. Create : arr = np.array([45, 12, 89, 23, 67, 10])
# # Print : Original Array, Ascending Array, Descending Array
arr = np.array([45,12,89,23,67,10])
print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])

# # 2. Using the same array print:
# # Indexes that sort the array (argsort), Index of minimum value, Index of Minimum Value
arr = np.array([45,12,89,23,67,10])
print("Indexes that sort the array:", np.argsort(arr))
print("Index of Maximun Value:", np.argmax(arr))
print("Index of Minimum Value:", np.argmin(arr))

# # 3. Create : marks = np.array([78,85,92,78,90,85,95,92])
# # Print : unique marks, sorted marks, highest marks, lowest marks
marks = np.array([78,85,92,78,90,85,95,92])
print("Unique Marks:", np.unique(marks))
print("Sorted Marks:", np.sort(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# # 4. Create : sales = np.array([1200,4500,800,6000,3000,7200,1500])
# # Print : Sales greater than 3000 using np.where(), their indices, Higher sales index, Lowest Sales Index
sales = np.array([1200,4500,800,6000,3000,7200,1500])
print("Sales greater than Rs3000:", np.where(sales > 3000))
print("Sales greater than Rs3000:", np.where(sales > 3000)[0])
print("Highest Sales Index:", np.argmax(sales))
print("Lowest Sales Index:", np.argmin(sales))

# # 5. Create :  values = np.array([0,5,8,0,12,15,0,20])
# Print : Non-zero indices, Non-zero values
values = np.array([0, 5, 8, 0, 12, 15, 0, 20])
non_zero_indices = np.nonzero(values)
print("Non-zero indices:", non_zero_indices[0])
print("Non-zero values:", values[non_zero_indices])

# # 6. Create : employees = np.array([45000, 52000, 48000, 61000, 71000, 52000, 45000])
# # Print : sorted salaries, unique salaries, Highest Salary, Lowest Salary
employees = np.array([
45000,
52000,
48000,
61000,
71000,
52000,
45000
])
print("Sorted Salaries:", np.sort(employees))
print("Unique Salaries:", np.unique(employees))
print("Highest Salary:", np.max(employees))
print("Lowest Salary:", np.min(employees))

# # Industry Practice 
# # Create : purchases = np.array([1200, 5000, 2500, 8000, 5000, 1200, 9000, 3000, 4500, 8000])
# # Original Purchases, Sorted purchases Unique purchase values Purchase values above ₹4000 Their indices (np.where)
# # Highest purchase, Lowest purchase, Index of highest purchase, Index of lowest purchase
purchases = np.array([
1200,
5000,
2500,
8000,
5000,
1200,
9000,
3000,
4500,
8000
])
print("Original Purchases:", purchases)
print("Sorted Purchases:", np.sort(purchases))
print("Unique Purchase Value:", np.unique(purchases))
print("Purchase Values above Rs4000:", np.where(purchases > 4000))
print("Purchase Values above Rs4000 Indices:", np.where(purchases > 4000)[0])
print("Highest Purchase:", np.max(purchases))
print("Lowest Purchase:", np.min(purchases))
print("Index of Highest Purchase:", np.argmax(purchases))
print("Index of Lowest Purchase:", np.argmin(purchases))
