import numpy as np
# # 1. Create : arr = np.array([12, 24, 36, 48, 60])
# # Print : normal for, np.nditer()
marks = np.array([35, 55, 70, 90, 25])
# # a. normal for
for i in marks:
    print(i)
# # b. npnditer()
for i in np.nditer(marks):
    print(i)

# # 2. Create : matrix = np.array([[10, 20, 30], [40, 50, 60]])
# # Print : every row, every individual elements
matrix = np.array([
[10,20,30],
[40,50,60]
])
# # a. every row
for row in matrix:
    print(row)
# # b. every individual element 
for row in matrix:
    for value in row:
        print(value)

# # 3. Create : marks = np.array([35, 78, 82, 45, 91, 27, 68, 83])
# # Print : Passed Marks, Failed Marks, Average of passed students, Avergae of Failed Students, Number of Passed Students, Number of Failed Students
marks = np.array([
35,
78,
82,
45,
91,
27,
68,
88
])
print("Passed Marks:", marks[marks >= 40])
print("Failed Marks:", marks[marks < 40])
print("Average of Passed Students:", marks[marks >= 40].mean())
print("Average of Failed Students:", marks[marks < 40].mean())
print("Number of Passed Students:", len(marks[marks >= 40]))
print("Number of Failed Students:", len(marks[marks < 40]))

# # 4. Create : salary = np.array([35000, 42000, 52000, 61000, 71000, 48000, 55000])
# # Print : Salaries above Rs50000, Their Average, Highest Salary among them, Count of Salaries above Rs50000
salary = np.array([
35000,
42000,
52000,
61000,
71000,
48000,
55000
])
print("Salaries above Rs50000:", salary[salary > 50000])
print("Their Average:", salary[salary > 50000].mean())
print("Highest Salary:", salary[salary > 50000].max())
print("Salaries above Rs50000:", len(salary[salary > 50000]))

# # 5. Create : sales = np.array([1200, 4500, 6200, 3000, 9800, 1500, 7100, 5200])
# # Print : Sales above Rs5000, Total of sales, Average, Count
sales = np.array([
1200,
4500,
6200,
3000,
9800,
1500,
7100,
5200
])
print("Sales above Rs5000:", sales[sales > 5000])
print("Total of those sales:", sales[sales > 5000].sum())
print("Average:", sales[sales > 5000].mean())
print("Count:", len(sales[sales > 5000]))

# # 6. Create : temperature = np.array([28, 31, 35, 39, 42, 30, 26, 37])
# # Print : Temperature above 35, Average Hot Temperature, Number of Hot Days
temperature = np.array([
28,
31,
35,
39,
42,
30,
26,
37
])
print("Temperature above 35:", temperature[temperature > 35])
print("Avergae Hot Temperature:", (temperature[temperature > 35]).mean())
print("Number of Hot Dsys:", len(temperature[temperature > 35]))

# # 7. Industry Practice
# # Sales Performance Analyzer 
# # Create : sales = np.array([1200, 8500, 4200, 600, 15000, 7800, 2500, 950, 6700, 11000])
# # Display : Premium sales (>₹8000), Regular sales (₹2000–₹8000), Low sales (<₹2000)
# # Then Calculate : Average premium sale, Average regular sale, Average low sale, Count in each category
sales = np.array([
1200,
8500,
4200,
600,
15000,
7800,
2500,
950,
6700,
11000
])
premium = sales[sales > 8000]
regular = sales[(sales >= 2000) & (sales <= 8000)]
low = sales[sales < 2000]
print("Premium Sales (>8000):", premium)
print("Regular Sales (2000–8000):", regular)
print("Low Sales (<2000):", low)
print("Average Premium Sale:", np.mean(premium))
print("Average Regular Sale:", np.mean(regular))
print("Average Low Sale:", np.mean(low))
print("Premium Count:", len(premium))
print("Regular Count:", len(regular))
print("Low Count:", len(low))
