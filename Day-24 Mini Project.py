# # Mini Project
# # Sales Data Cleaning & Analytics Dashboard
# # Your program should display: Original sales Mean (ignoring NaN) Median Standard deviation Variance Highest sale Lowest sale Replace NaN with 4000 Cleaned sales Average cleaned sales Highest cleaned sale Lowest cleaned sale
import numpy as np
sales = np.array([
1200,
2500,
np.nan,
4200,
3800,
np.nan,
5100,
6200,
7100,
np.nan,
4800,
3500
])
print("Original Sales:", sales)
print("Mean:", np.nanmean(sales))
print("Median:", np.nanmedian(sales))
print("Standard Deviation:", np.nanstd(sales))
print("Variance:", np.nanvar(sales))
print("Highest Sales:", np.nanmax(sales))
print("Lowest Sales:", np.nanmin(sales))
clean_sales = np.nan_to_num(sales, nan=4000)
print("Cleaned Sales:", clean_sales)
print("Average Cleaned Sales:", clean_sales.mean())
print("Highest Cleaned Sale:", clean_sales.max())
print("Lowest Cleaned Sale:", clean_sales.min())
