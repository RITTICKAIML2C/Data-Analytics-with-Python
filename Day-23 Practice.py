import numpy as np 
# # 1. marks = np.array([55,62,70,80,90,95,85,60,73,88])
# # Print : 25th percentile, 50th percentile, 75th percentile
marks = np.array([55,62,70,80,90,95,85,60,73,88])
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

# # 2. salary = np.array([25000,30000,35000,40000,45000,50000])
# # Print : Q1, Median, Q3 using quantile()
salary = np.array([25000,30000,35000,40000,45000,50000])
print("Median:", np.quantile(salary, 0.5))
print("Q1:", np.quantile(salary, 0.25))
print("Q3:", np.quantile(salary, 0.75))

# # 3. sales = np.array([1200,1500,1800,2200,2600,3000,3500,4000])
# # Print : 10th percentile, 90th percentile, Mean, Std Deviation
sales = np.array([1200,1500,1800,2200,2600,3000,3500,4000])
print("10th Percentile:", np.percentile(sales, 10))
print("90th Percentile:", np.percentile(sales, 90))
print("Mean:", np.mean(sales))
print("Standard Deviation:", sales.std())

# # 4. hours = np.array([1,2,3,4,5]), marks = np.array([35,45,55,70,90])
# # Print : Covariance, Coorelation matrix
hours = np.array([1,2,3,4,5])
marks = np.array([35,45,55,70,90])
print("Covariance:", np.cov(hours, marks))
print("Coorelation Matrix:", np.corrcoef(hours, marks))

# # 5. temperature = np.array([20,22,24,26,28]), icecream_sales = np.array([100,150,200,280,350])
# # Print : Covariance, Correlation
temperature = np.array([20,22,24,26,28])
icecream_sales = np.array([100,150,200,280,350])
print("Covariance:", np.cov(temperature, icecream_sales))
print("Correlation:", np.corrcoef(temperature, icecream_sales))

# # 6. income = np.array([25000,30000,40000,45000,60000]), expenses = np.array([18000,22000,26000,30000,38000])
income = np.array([25000,30000,40000,45000,60000])
expenses = np.array([18000,22000,26000,30000,38000])
print("Correlation:", np.corrcoef(income, expenses))
print("Covariance:", np.cov(income, expenses))

# # Industry Practice 
# # Employee Performance Analysis
# # Display : Mean performance, Median performance, Standard deviation, Variance, 25th percentile, 75th percentile, Correlation between experience and performance, Covariance between experience and performance
performance = np.array([
72,
81,
65,
90,
88,
95,
78,
84,
69,
91
])
experience = np.array([
1,
2,
1,
5,
4,
6,
3,
4,
2,
5
])
print("Mean Performance:", performance.mean())
print("Median Performance:", np.quantile(performance, 0.5))
print("Standard Deviation:", np.std(performance))
print("Variance:", np.var(performance))
print("25th Percentile:", np.percentile(performance, 25))
print("75th Percentile:", np.percentile(performance, 75))
print("Correlation:", np.corrcoef(experience, performance))
print("Covariance:", np.cov(experience, performance))
