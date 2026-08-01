# # Industry Practice - Employee Performance Classification
import numpy as np 
performance = np.array([
    35,
    48,
    72,
    90,
    66,
    28,
    81,
    95
])
conditions = [
    performance >= 85,
    performance >= 40
]
choices = [
    "Excellent",
    "Pass"
]
labels = np.select(conditions, choices, default = "Fail")
print("Performance Scores:", performance)
print("Labels:", labels)
print("Excellent Employees:", performance[performance >= 85])
print("Passed Employees:", performance[(performance >= 40) & (performance < 85)])
print("Failed Employees:", performance[performance < 40])
print("Number of Excellent:", np.sum(performance >= 85))
print("Number of Passed:", np.sum((performance >= 40) & (performance < 85)))
print("Number of Failed:", np.sum(performance < 40))
