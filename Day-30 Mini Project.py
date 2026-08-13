# # MINI PROJECT - Employee Performance & Salary Analytics Dashboard
# # 🔹 Basic Statistics : Original employee data, Shape, Average salary, Average performance, Average experience, Highest salary, Lowest salary, Highest performance, Lowest performance
# # 🔹 Salary Segmentation : Classify employees: High Salary → ≥ 60000, Medium Salary → 40000–59999, Low Salary → < 40000, Use np.select(), Display: Salary categories, Number of employees in each category, Average salary of each category
# # 🔹 Performance Segmentation : Classify: Excellent → ≥ 85, Pass → 70–84, Needs Improvement → < 70, Use np.select(). Display: Performance labels, Number in each category
# # 🔹 Ranking : Using np.argsort(): Employees ranked by salary, Employees ranked by performance, Top 3 highest-paid employees, Top 3 performers, Bottom 3 performers
# # 🔹 Statistical Analysis : Calculate: Salary median, Salary standard deviation, Performance median, Performance standard deviation, 25th percentile of salary, 75th percentile of salary
# # 🔹 Relationship Analysis : Calculate:, Correlation between experience and salary, Correlation between experience and performance, Covariance between experience and salary, Covariance between experience and performance
# # ⭐ Bonus : Find: Which employee has the highest combination of performance and experience?, And: Which employee has the highest average salary + performance ranking?

# # 1. Basic Statistics
import numpy as np
employee_id = np.array([
    101,102,103,104,105,106,107,108,109,110
])
salary = np.array([
    35000,42000,51000,62000,71000,
    48000,55000,68000,59000,80000
])
performance = np.array([
    68,75,91,88,95,72,84,90,79,97
])
experience = np.array([
    1,2,5,4,7,3,4,6,3,8
])
print("========== BASIC STATISTICS ==========")
print("Employee IDs:", employee_id)
print("Salary:", salary)
print("Performance:", performance)
print("Experience:", experience)
print("Shape:", employee_id.shape)
print("Average Salary:", np.mean(salary))
print("Average Performance:", np.mean(performance))
print("Average Experience:", np.mean(experience))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))
print("Highest Performance:", np.max(performance))
print("Lowest Performance:", np.min(performance))

# # 2. Salary Segmentation
# # Create categories using np.select()
salary_conditions = [
    salary >= 60000,
    (salary >= 40000) & (salary <= 59999),
    salary < 40000
]
salary_categories = np.select(
    salary_conditions,
    ["High Salary", "Medium Salary", "Low Salary"],
    default="Unknown"
)
print("Salary Categories:")
print(salary_categories)

# # Number of employees in each category
for category in ["High Salary", "Medium Salary", "Low Salary"]:
    count = np.sum(salary_categories == category)
    print(category, ":", count)

# # Average salary of each category
for category in ["High Salary", "Medium Salary", "Low Salary"]:
    mask = salary_categories == category
    print(category, "Average:", np.mean(salary[mask]))

# # 3. Performance Segmentation
performance_conditions = [
    performance >= 85,
    (performance >= 70) & (performance <= 84),
    performance < 70
]
performance_labels = np.select(
    performance_conditions,
    ["Excellent", "Pass", "Needs Improvement"],
    default="Unknown"
)
print("Performance Labels:")
print(performance_labels)

# # Number in each categor
for category in ["Excellent", "Pass", "Needs Improvement"]:
    count = np.sum(performance_labels == category)
    print(category, ":", count)

# # 4. Ranking
# # Employees ranked by salary
salary_rank = np.argsort(salary)[::-1]
print(employee_id[salary_rank])
print(salary[salary_rank])

# # Employees ranked by performance
performance_rank = np.argsort(performance)[::-1]
print(employee_id[performance_rank])
print(performance[performance_rank])

# # Top 3 highest-paid employees
print(employee_id[salary_rank[:3]])

# # Top 3 performers
print(employee_id[performance_rank[:3]])

# # Bottom 3 performers
print(employee_id[performance_rank[-3:]])

# # 5. Statistical Analysis
# # Salary median
print(np.median(salary))

# # Salary standard deviation
print(np.std(salary))

# # Performance median
print(np.median(performance))

# # Performance standard deviation
print(np.std(performance))

# # 25th percentile of salary
print(np.percentile(salary, 25))

# # 75th percentile of salary
print(np.percentile(salary, 75))

# # 6. Relationship Analysis
# # Experience vs Salary
corr_exp_salary = np.corrcoef(experience, salary)[0, 1]
cov_exp_salary = np.cov(experience, salary)[0, 1]
print("Correlation:", corr_exp_salary)
print("Covariance:", cov_exp_salary)

# # Experience vs Performance
corr_exp_performance = np.corrcoef(
    experience,
    performance
)[0, 1]
cov_exp_performance = np.cov(
    experience,
    performance
)[0, 1]
print("Correlation:", corr_exp_performance)
print("Covariance:", cov_exp_performance)

# # 7. Bonus — Highest Combination of Performance + Experience
combined_score = performance + experience
best_index = np.argmax(combined_score)
print("Employee:", employee_id[best_index])
print("Performance:", performance[best_index])
print("Experience:", experience[best_index])
print("Combined Score:", combined_score[best_index])

# # 8. Bonus — Highest Average Salary + Performance Ranking
salary_rank = np.argsort(salary)[::-1]
performance_rank = np.argsort(performance)[::-1]
salary_position = np.empty(len(salary), dtype=int)
performance_position = np.empty(len(performance), dtype=int)
salary_position[salary_rank] = np.arange(1, len(salary) + 1)
performance_position[performance_rank] = np.arange(1, len(performance) + 1)
average_rank = (
    salary_position + performance_position
) / 2
best_index = np.argmin(average_rank)
print("Employee:", employee_id[best_index])
print("Salary Rank:", salary_position[best_index])
print("Performance Rank:", performance_position[best_index])
print("Average Rank:", average_rank[best_index])
