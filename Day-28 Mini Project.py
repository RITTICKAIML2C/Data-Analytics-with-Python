# # Mini Project 
# # Employee Performance Dashboard 
# # Your program should display:
# # Basic Statistics - Original performance matrix Overall average Overall highest score Overall lowest score
# # Row-wise Analysis - Average performance of each employee Highest score of each employee Lowest score of each employee
# # Column-wise Analysis - Average performance of each test Highest score in each test Lowest score in each test
# # Conditional Analysis - Number of scores ≥ 90 Number of scores < 70 Number of scores between 70 and 89 Number of scores ≥ 80 in each employee row
# # ⭐ Bonus - Find the employee index with the highest average performance.
import numpy as np 
performance = np.array([
    [78,85,91,67],
    [88,92,76,81],
    [65,72,90,95],
    [84,79,88,93],
    [91,86,94,89]
])
# Basic Statistics
print("Original Performance Matrix:", performance)
print("Overall Average:", np.mean(performance))
print("Overall Highest Score:", np.max(performance))
print("Overall Lowest Score:", np.min(performance))
# Row-wise Analysis
print("Average Performance of each employee:", np.mean(performance, axis = 1))
print("Highest Score of each employee:", np.max(performance, axis = 1))
print("Lowest Score of each employee:", np.min(performance, axis = 1))
# Column-wise Analysis
print("Average Performance of each test:", np.mean(performance, axis = 0))
print("Highest Score of each test:", np.max(performance, axis = 0))
print("Lowest Score of each test:", np.min(performance, axis = 0))
# Conditional Analysis
print("Number of scores ≥ 90:", np.sum(performance >= 90))
print("Number of scores < 70:", np.sum(performance < 70))
print("Number of scores between 70 and 89:", np.sum((performance >= 70) & (performance < 90)))
print("Number of scores ≥ 80 in each employee row:", np.sum(performance >= 80, axis = 1))
# Bonus
employee_avg = np.mean(performance, axis=1)
print("Employee index with highest average:", np.argmax(employee_avg))
