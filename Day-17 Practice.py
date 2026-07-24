import numpy as np
# # 1. Create : arr = np.array([15, 30, 45, 60, 75])
# # Print : Values greater than 40, Values less than 50
arr = np.array([15, 30, 45, 60, 75])
print("Value greater than 40:", arr[arr > 40])
print("Value less than 50:", arr[arr < 50])

# # 2. Create : marks = np.array([35, 60, 80, 25, 90])
# # Using np.where(), print: "Pass" if marks greater than equal to 40, "Fail" otherwise
marks = np.array([35, 60, 80, 25, 90])
print("Result:", np.where(marks >= 40, "Pass", "Fail"))

# # 3. Create : prices = np.array([120, 250, 1500, 800, 3500])
# # Use np.clip() to limit prices between 200 and 2000
prices = np.array([120, 250, 1500, 800, 3500])
print("Original Prices:", prices)
print("Clipped Prices:", np.clip(prices, 200, 2000))

# # 4. Create : arr = np.array([15, np.nan, 28, np.nan, 50])
# # Print : missing values, number of missing values
arr = np.array([15, np.nan, 28, np.nan, 50])
print("Missing Values:", np.isnan(arr))
print("Number of Missing Values:", np.isnan(arr).sum())

# # 5. Create : numbers = np.array([20, np.inf, 45, np.nan, -np.inf, 60])
# # Print : infinite values mask, finite values mask 
numbers = np.array([20, np.inf, 45, np.nan, -np.inf, 60])
print("Finite Numbers:", np.isfinite(numbers))
print("Infinite Numbers:", np.isinf(numbers))

# # 6. Create : sales = np.array([1200, 4500, 8000, 3200])
# # Print : Is any sale greater than Rs7000, Are all sales greater than Rs1000
sales = np.array([1200, 4500, 8000, 3200])
print("IS any salary greater than Rs7000 ?:", np.any(sales > 7000))
print("Are all sales greater than Rs1000?:", np.all(sales > 1000))

# # Industry Practice 
# # Emplooyee Salary Validation 
# # Create : salary = np.array([35000, 42000, -5000, 65000, np.nan, 52000, 90000])
# # Display: Original salary array Missing values mask Negative salaries Replace negative salaries with 0 using np.where() Check if all salaries are positive Count missing values
salary = np.array([
35000,
42000,
-5000,
65000,
np.nan,
52000,
90000
])
print("Original Salary:", salary)
print("Missing Values Mask:", np.isnan(salary))
print("Negative Salaries:", salary[salary < 0])
print("Salary after replacing Negative Values:", np.where(salary < 0, 0, salary))
print("Are all salaries positive:", np.all(salary > 0))
print("Number of Missing Values:", np.isnan(salary).sum())
