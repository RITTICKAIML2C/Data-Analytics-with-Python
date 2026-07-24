# # Mini Project 
# # Sales Data Cleaning Dashboard 
# # Create : sales = np.array([1200, 4500, -800, 6500, np.nan, 7200, 1500, -200, 9800, 5000])
# # Your program should display: Original sales Missing values Count of missing values Negative sales Replace negative values with 0
# # Replace missing values with 0 (hint: use np.where(np.isnan(...), 0, sales)) Sales greater than ₹5000 Is any sale greater than ₹9000? Are all sales non-negative after cleaning?
# # Cleaned sales array Total cleaned sales Average cleaned sales
import numpy as np 
sales = np.array([
1200,
4500,
-800,
6500,
np.nan,
7200,
1500,
-200,
9800,
5000
])
print("Original Sales:", sales)
print("Missing Values:", np.isnan(sales))
print("Total Missing Values:", np.isnan(sales).sum())
print("Negative Sales:", sales[sales < 0])
print("Negative Values replaced with 0:", np.where(sales < 0, 0, sales))
print("Missing Replaced:", np.where(np.isnan(sales), 0, sales))
print("Sales > Rs5000:", sales[sales > 5000])
print("Any Sale > Rs9000:", np.any(sales > 9000))
print("All Non-Negative After Cleaning:", np.all(np.where(np.isnan(np.where(sales < 0, 0, sales)), 0, np.where(sales < 0, 0, sales)) >= 0))
print("Cleaned Sales:", np.where(np.isnan(np.where(sales < 0, 0, sales)), 0, np.where(sales < 0, 0, sales)))
print("Total Cleaned Sales:", np.sum(np.where(np.isnan(np.where(sales < 0, 0, sales)), 0, np.where(sales < 0, 0, sales))))
print("Average Cleaned Sales:", np.mean(np.where(np.isnan(np.where(sales < 0, 0, sales)), 0, np.where(sales < 0, 0, sales))))
