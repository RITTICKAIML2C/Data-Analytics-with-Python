# # Mini Project
# # Student Performance Statistical Dashboard 
# # Your program should display: Original marks, Mean, Median, Standard deviation, Variance, 25th percentile, 50th percentile, 75th percentile, Highest mark, Lowest mark
# # Correlation between study hours and marks, Covariance between study hours and marks
import numpy as np 
marks = np.array([
65,
72,
81,
95,
88,
74,
69,
91,
85,
77,
83,
98
])

study_hours = np.array([
2,
3,
4,
6,
5,
3,
2,
6,
5,
4,
5,
7
])
print("Original Marks:", marks)
print("Mean:", np.mean(marks))
print("Median:", np.quantile(marks, 0.5))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("25th Percentile:", np.quantile(marks, 0.25))
print("50th Percentile:", np.quantile(marks, 0.5))
print("75th Percentile:", np.quantile(marks, 0.75))
print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())
print("Correlation betweem study hours and marks:", np.corrcoef(study_hours, marks))
print("Covariance between study hours and marks:", np.cov(study_hours, marks))
