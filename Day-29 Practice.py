import numpy as np 
# # 1. Basic Sorting 
# # Print: Original marks Ascending marks Descending marks
# # argsort() indices Highest mark Lowest mark
marks = np.array([78, 45, 91, 67, 88, 95, 72])
print("Original Marks:", marks)
print("Ascending Marks:", np.sort(marks))
print("Descending Marks:", np.sort(marks)[::-1])
print("Argsort() indices:", np.argsort(marks))
print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())

# # 2. Row-wise & Column-wise Sorting
# # Print: Original matrix Each row sorted Each column sorted Each row sorted in descending order
marks = np.array([
    [78, 91, 65],
    [88, 72, 95],
    [61, 84, 79]
])
print("Original Matrix:", marks)
print("Each Row Sorted:", np.sort(marks, axis = 1))
print("Each Column Sorted:", np.sort(marks, axis = 0))
print("Each Row Sorted in Descending Order:", np.sort(marks, axis = 1)[:, ::-1])

# # 3. Employee Salary Ranking 
# # Find: Salaries in ascending order Salaries in descending order Ranking indices using argsort()
# # Highest salary Lowest salary Top 3 salaries Indices of top 3 salaries
salary = np.array([
    35000,
    52000,
    48000,
    71000,
    62000,
    45000,
    80000
])
print("Salaries in Ascending Order:", np.sort(salary))
print("Salaries in Descending Order:", np.sort(salary)[::-1])
print("Ranking indices using argsort():", np.argsort(salary))
print("Highest Salary:", salary.max())
print("Lowest Salary:", salary.min())
print("Top 3 salaries:", np.sort(salary)[-3:])
print("Indices of top 3 salaries:", np.argsort(salary)[-3:])

# # 4. Student Ranking 
# # Find: Highest 3 marks Lowest 3 marks Indices of highest 3 marks
# # Indices of lowest 3 marks Complete ranking from highest to lowest
marks = np.array([
    78,
    92,
    65,
    88,
    95,
    71,
    84
])
print("Highest 3 Marks:", np.sort(marks)[-3:][::-1])
print("Lowest 3 Marks:", np.sort(marks)[:3])
print("Indices of highest 3 marks:", np.argsort(marks)[-3:][::-1])
print("Indices of lowest 3 marks:", np.argsort(marks)[:3])
print("Complete ranking from highest to lowest:", np.argsort(marks)[::-1])

# # 5. Sales Ranking 
# # Find: Top 3 sales Bottom 3 sales Indices of top 3 sales
# # Indices of bottom 3 sales Sales sorted from highest to lowest
sales = np.array([
    1200,
    8500,
    4200,
    15000,
    6200,
    9800,
    3500,
    12000
])
print("Top 3 sales:", np.sort(sales)[-3:][::-1])
print("Bottom 3 sales:", np.sort(sales)[:3])
print("Indices of top 3 sales:", np.argsort(sales)[-3:][::-1])
print("Indices of bottom 3 sales:", np.argsort(sales)[:3])
print("Sales Sorted from highest to lowest:", np.argsort(sales)[::-1])

# # Industry Practice 
# # Employee Salary Ranking 
# # Your program should display:
# # Salary Analysis Original employee IDs Original salaries Salaries ascending Salaries descending Salary ranking indices
# # Employee Ranking: Display: Highest-paid employee ID Highest salary Lowest-paid employee ID Lowest salary Top 3 employee IDs Top 3 salaries
employee_id = np.array([
    101, 102, 103, 104, 105, 106, 107
])
salary = np.array([
    45000,
    72000,
    51000,
    90000,
    62000,
    58000,
    80000
])
print("Original employee IDs:")
print(employee_id)
print("Original salaries:")
print(salary)
sort_indices = np.argsort(salary)
salaries_ascending = salary[sort_indices]
print("Salaries ascending:")
print(salaries_ascending)
descending_indices = sort_indices[::-1]
salaries_descending = salary[descending_indices]
print("Salaries descending:")
print(salaries_descending)
print("Salary ranking indices:")
print(descending_indices)
employee_ranking = employee_id[descending_indices]
print("Employee Ranking:")
print(employee_ranking)
highest_index = np.argmax(salary)
print("Highest-paid employee ID:", employee_id[highest_index])
print("Highest salary:", salary[highest_index])
lowest_index = np.argmin(salary)
print("Lowest-paid employee ID:", employee_id[lowest_index])
print("Lowest salary:", salary[lowest_index])
top_3_indices = np.argsort(salary)[-3:][::-1]
print("Top 3 employee IDs:")
print(employee_id[top_3_indices])
print("Top 3 salaries:")
print(salary[top_3_indices])
