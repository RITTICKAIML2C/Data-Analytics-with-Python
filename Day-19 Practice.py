import numpy as np 
# # 1. Create : arr = np.array([10,20,30,40,50,60,70,80])
# # Print: Values greater than 30 and less than 70, Values less than 20 or greater than 60
arr = np.array([10,20,30,40,50,60,70,80])
print("Value greater than 30 and less than 70:", np.logical_and(arr > 30, arr < 70))
print("Values less than 20 or greater than 60:", np.logical_or(arr < 20, arr > 60))

# # 2. Create : marks = np.array([35,48,72,90,66,28,81])
# # Using : np.where()
# # Print : "Pass" if marks ≥ 40, "Distinction" if marks ≥ 75, "Fail" otherwise
marks = np.array([35,48,72,90,66,28,81])
print(np.where(marks >= 75, "Distinction", np.where(marks >= 40, "Pass", "Fail")))

# # 3. Create : salary = np.array([35000, 42000, 52000, 61000, 72000, 46000])
# # Print : Salaries between ₹45,000 and ₹65,000, Salaries above ₹60,000, Salaries below ₹40,000
salary = np.array([35000,42000,52000,61000,72000,46000])
print("45k–65k:", salary[(salary >= 45000) & (salary <= 65000)])
print("Above 60k:", salary[salary > 60000])
print("Below 40k:", salary[salary < 40000])

# # 4. Create : sales = np.array([1200,4500,6200,3000,9800,1500,7100])
# # Print : logical_and(sales > 2000, sales < 8000), logical_or(sales < 2000, sales > 7000), logical_not(sales > 5000)
sales = np.array([1200,4500,6200,3000,9800,1500,7100])
print(np.logical_and(sales > 2000, sales < 8000))
print(np.logical_or(sales < 2000, sales > 7000))
print(np.logical_not(sales > 5000))

# # 5. Create : temperature = np.array([28,31,35,39,42,30,26])
# # Replace: Above 40 → 40. Below 30 → 30, using np.where().
temperature = np.array([28,31,35,39,42,30,26])
temperature = np.where(temperature > 40, 40,
              np.where(temperature < 30, 30, temperature))
print(temperature)

# # 6. Create : prices = np.array([120,450,800,1500,2500,4000])
# # Print : Premium (>2000), Budget (<500), Mid-range (500–2000)
prices = np.array([120,450,800,1500,2500,4000])
print("Premium:", prices[prices > 2000])
print("Budget:", prices[prices < 500])
print("Mid-range:", prices[(prices >= 500) & (prices <= 2000)])

# # 7. Industry Practice
# # Customer Segmentation
# # Create : purchase = np.array([1200,8500,4200,600,15000,7800,2500,950])
# # Display: Premium Customers (> ₹8000)Regular Customers (₹2000–₹8000)Low Customers (< ₹2000)Label each customer:"Premium""Regular""Low" using np.where().
purchase = np.array([1200,8500,4200,600,15000,7800,2500,950])
print("Premium:", purchase[purchase > 8000])
print("Regular:", purchase[(purchase >= 2000) & (purchase <= 8000)])
print("Low:", purchase[purchase < 2000])
labels = np.where(purchase > 8000, "Premium",
         np.where(purchase >= 2000, "Regular", "Low"))
print(labels)

