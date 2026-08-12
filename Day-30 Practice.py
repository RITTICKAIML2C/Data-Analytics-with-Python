import numpy as np
# # 1. Data Inspection
# # Display : Original data, Shape, Number of dimensions, Total number of elements, Overall average, Highest score, Lowest score
data = np.array([
    [78, 85, 91, 67],
    [88, 92, 76, 81],
    [65, 72, 90, 95],
    [84, 79, 88, 93],
    [91, 86, 94, 89]
])
print("Original Data:", data)
print("Shape:", data.shape)
print("Number of Dimensions:", data.ndim)
print("Total Number of Elements:", data.size)
print("Overall Average:", data.mean())
print("Highest Score:", data.max())
# print("Lowest Score:", data.min())

# # 2. Boolean Analytics 
# # Display: Scores ≥ 90, Scores < 70, Scores between 70 and 89, Number of scores ≥ 90, Number of scores < 70, Number of scores between 70 and 89
data = np.array([
    [78, 85, 91, 67],
    [88, 92, 76, 81],
    [65, 72, 90, 95],
    [84, 79, 88, 93],
    [91, 86, 94, 89]
])
print("Score ≥ 90:", data[data >= 90])
print("Score < 70:", data[data < 70])
print("Scores between 70 and 89:", data[(data >= 70) & (data <= 89)])
print("Number of scores ≥ 90:", np.sum(data >= 90))
print("Number of scores < 70:", np.sum(data < 70))
print("Number of scores between 70 and 89:", np.sum((data >= 70) & (data <= 89)))

# # 3. Row & Column Analytics 
# # Calculate : Average score of every employee, Average score of every test, Highest score of every employee, Lowest score of every employee, Highest score of every test, Lowest score of every test
data = np.array([
    [78, 85, 91, 67],
    [88, 92, 76, 81],
    [65, 72, 90, 95],
    [84, 79, 88, 93],
    [91, 86, 94, 89]
])
print("Average score of every employee:", data.mean(axis = 1))
print("Average score of every test:", data.mean(axis = 0))
print("Highest score of every employee:", data.max(axis = 1))
print("Lowest score of every employee:", data.min(axis = 1))
print("Highest score of every test:", data.max(axis = 0))
print("Lowest score of every test:", data.min(axis = 0))

# # 4. Ranking 
# # Find : Marks from highest → lowest, Ranking indices, Student IDs ranked by marks, Top 3 student IDs, Top 3 marks, Bottom 3 student IDs, Bottom 3 marks
marks = np.array([78, 92, 65, 88, 95, 71, 84, 90])
student_id = np.array([101,102,103,104,105,106,107,108])
ranking_indices = np.argsort(marks)[::-1]
print("Marks from highest - lowest:", marks[ranking_indices])
print("Ranking Indices:", ranking_indices)
print("Student IDs ranked by marks:", student_id[ranking_indices])
print("Top 3 student IDs:", student_id[ranking_indices[:3]])
print("Top 3 marks:", marks[ranking_indices[:3]])
print("Bottom 3 student IDs:", student_id[ranking_indices[-3:]])
print("Bottom 3 marks:", marks[ranking_indices[-3:]])

# # 5. Missing Data 
# # Find : Number of missing salaries Mean salary ignoring NaN, Median salary ignoring NaN, Highest salary, Lowest salary, Replace NaN with 50000, Average of cleaned salary
salary = np.array([
    35000,
    42000,
    np.nan,
    55000,
    62000,
    np.nan,
    71000,
    48000
])
print("Number of missing salaries:", np.sum(np.isnan(salary)))
print("Mean Salary ignoring NaN:", np.nanmean(salary))
print("Median Salary ignoring NaN:", np.nanmedian(salary))
print("Highest Salary:", np.nanmax(salary))
print("Lowest Salary:", np.nanmin(salary))
cleaned_salary = np.nan_to_num(salary, nan = 50000)
print("Replace NaN with 50000:", cleaned_salary)
print("Average of cleaned salary:", cleaned_salary.mean())

# # 6. Relationship Analysis 
# # Calculate : Mean experience, Mean performance, Correlation, Covariance
experience = np.array([1, 2, 3, 4, 5, 6])
performance = np.array([55, 60, 68, 75, 85, 91])
print("Mean Experience:", np.mean(experience))
print("Mean Performance:", np.mean(performance))
print("Correlation:", np.corrcoef(experience, performance)[0, 1])
print("Covariance:", np.cov(experience, performance)[0, 1])

# # Industry Practice - Employee Analytics System
# # Employee Overview : Employee IDs, Salaries, Performance, Experience
# # Salary Analysis : Average salary, Highest salary, Lowest salary, Employees earning > $50,000, Top 3 salaries, Top 3 employee IDs
# # Performance Analysis : Average performance, Highest performance, Lowest performance, Employees scoring ≥ 85, Employees scoring < 70, Number of employees scoring ≥ 85
# # Experience Analysis : Average experience, Highest experience, Lowest experience
# # Relationship Analysis : Correlation between experience and performance, Covariance between experience and performance, Ranking
# # Rank employees from highest performance → lowest performance while keeping the employee IDs correctly matched
employee_id = np.array([101,102,103,104,105,106,107,108])
salary = np.array([
    35000,
    42000,
    51000,
    62000,
    71000,
    48000,
    55000,
    68000
])
performance = np.array([
    65,
    78,
    91,
    88,
    95,
    72,
    84,
    90
])
experience = np.array([
    1,
    2,
    5,
    4,
    7,
    3,
    4,
    6
])

# # Employee Overview 
print("Employee IDs:", employee_id)
print("Salaries:", salary)
print("Performance:", performance)
print("Experience:", experience)

# # Salary Analysis 
print("Average Salary:", salary.mean())
print("Highest Salary:", salary.max())
print("Lowest Salary:", salary.min())
print("Employees earning > 50000:", salary[salary > 50000])
salary_rank = np.argsort(salary)[::-1]
print("Top 3 salaries:", salary[salary_rank[:3]])
print("Top 3 employee IDs:", employee_id[salary_rank[:3]])

# # Performance Analysis 
print("Average Performance:", performance.mean())
print("Highest Performance:", performance.max())
print("Lowest Performance:", performance.min())
print("Employees scoring ≥ 85:", employee_id[performance >= 85])
print("Employees scoring < 70", employee_id[performance < 70])
print("Number of employees scoring ≥ 85:", np.sum(performance >= 85))

# # Experience Analysis 
print("Average experience:", experience.mean())
print("Highest experience:", experience.max())
print("Lowest experience:", experience.min())

# # Relationship Analysis 
print("Correlation between experience and performance:", np.corrcoef(experience, performance)[0, 1])
print("Covariance between experience and performance:", np.cov(experience, performance)[0, 1])

# # Ranking
performance_rank = np.argsort(performance)[::-1]
print(employee_id[performance_rank])
print(performance[performance_rank])
