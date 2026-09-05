# # 1. Row-wise Concatenation 
import pandas as pd 
jan = pd.DataFrame({
    "Order_ID": [101, 102, 103],
    "Sales": [5000, 7000, 6000]
})
feb = pd.DataFrame({
    "Order_ID": [104, 105, 106],
    "Sales": [8000, 9000, 7500]
})
result = pd.concat([jan, feb])
print(result)

# # 2. ignore_index=True 
print(pd.concat([jan, feb], ignore_index=True))

# # 3. Column-wise Concatenation 
import pandas as pd 
employee = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit"],
    "Department": ["IT", "HR", "Finance"]
})
performance = pd.DataFrame({
    "Performance": [90, 85, 88],
    "Experience": [5, 3, 4]
})
print(pd.concat([employee, performance], axis=1))
