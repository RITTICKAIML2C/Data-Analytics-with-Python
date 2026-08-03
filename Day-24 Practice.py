import numpy as np
# # 1. marks = np.array([75, np.nan, 82, 90, np.nan, 68, 88])
# # print : original array, mean, median, maximum, minimum
marks = np.array([75, np.nan, 82, 90, np.nan, 68, 88])
print("Original Array:", marks)
print("Mean:", np.nanmean(marks))
print("Median:", np.nanmedian(marks))
print("Maximum:", np.nanmax(marks))
print("Minimum:", np.nanmin(marks))

# # 2. sales = np.array([1200, 1800, np.nan, 2500, 3000, np.nan])
sales = np.array([1200, 1800, np.nan, 2500, 3000, np.nan])
print("NaN values replaced to 2000:", np.nan_to_num(sales, nan = 2000))

# # 3. A = np.array([15, 25, 35, 45, 55]), B = np.array([20, 20, 40, 40, 60])
# # Print : Element Wise Maximum, Element Wise Minimum
A = np.array([15, 25, 35, 45, 55])
B = np.array([20, 20, 40, 40, 60])
print("Element Wise Maximum:", np.maximum(A, B))
print("Element Wise Minimum:", np.minimum(A, B))

# # 4. salary = np.array([35000, 42000, np.nan, 55000, 62000, np.nan])
# # Print : Mean, Standard deviation, Variance, Highest Salary, Lowest Salary
salary = np.array([35000, 42000, np.nan, 55000, 62000, np.nan])
print("Mean:", np.nanmean(salary))
print("Standard Deviation:", np.nanstd(salary))
print("Variance:", np.nanvar(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.nanmin(salary))

# # 5. temperature = np.array([31, np.nan, 35, 37, 30, np.nan, 33])
# # Print : Replace NaN with 32 and print : clean array, average temperature, maximum temperature
import numpy as np
temperature = np.array([31, np.nan, 35, 37, 30, np.nan, 33])
clean_array = np.nan_to_num(temperature, nan=32)
print("Clean Array:", clean_array)
print("Average Temperature:", clean_array.mean())
print("Maximum Temperature:", clean_array.max())

# # 6. profit = np.array([120000, 145000, np.nan, 160000, 175000, np.nan, 180000])
# # Mean, Median, Variance, Standard Deviation, Replace NaN with 150000, Print clean array
profit = np.array([120000, 145000, np.nan, 160000, 175000, np.nan, 180000])
print("Mean:", np.nanmean(profit))
print("Median:", np.nanmedian(profit))
print("Variance:", np.nanvar(profit))
print("Standard Deviation:", np.nanstd(profit))
print("Replaced NaN with 150000:", np.nan_to_num(profit, nan = 150000))
print("Cleaned Array:", np.nan_to_num(profit, nan = 150000))

# # Industry Practice 
# # Employee Salary Cleaning Dashboard 
# # Display : Original Salary, Mean Salary, Median Salary, Highest Salary, Lowest Salary, Standard Deviation, Variance, Replace mssing salaries by 50000, Print clear array, Average cleaned array
salary = np.array([
    35000,
    42000,
    np.nan,
    51000,
    60000,
    np.nan,
    72000,
    68000,
    55000,
    np.nan
])
print("Original Salary:", salary)
print("Mean Salary:", np.nanmean(salary))
print("Median Salary:", np.nanmedian(salary))
print("Highest Salary:", np.nanmax(salary))
print("Lowest Salary:", np.nanmin(salary))
print("Standard Deviation:", np.nanstd(salary))
print("Variance:", np.nanvar(salary))
clean_salary = np.nan_to_num(salary, nan=50000)
print("Cleaned Salary Array:", clean_salary)
print("Average Cleaned Salary:", clean_salary.mean())
