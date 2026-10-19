# # Practice 
# # Q1 Using query(), find customers with Sales > ₹100,000.
# # Q2 Find customers with Sales > ₹60,000 AND Profit > ₹10,000.
# # Q3 Find Electronics customers with Sales > ₹100,000.
# # Q4 Use eval() to create: Profit_Margin
# # Q5 Using query(), find customers with Profit_Margin > 20%.
import pandas as pd

df = pd.DataFrame({
    "Customer": ["Amit","Riya","Rahul","Priya","Karan","Neha"],
    "Category": ["Electronics","Furniture","Clothing",
                 "Electronics","Furniture","Clothing"],
    "Sales": [120000,75000,45000,150000,65000,30000],
    "Profit": [30000,12000,9000,40000,10000,5000]
})
df.query("Sales > 100000")

# Q2
df.query("Sales > 60000 and Profit > 10000")

# Q3
df.query("Category == 'Electronics' and Sales > 100000")

# Q4
df.eval("Profit_Margin = (Profit / Sales) * 100", inplace=True)

# Q5
df.query("Profit_Margin > 20")
print(df)
