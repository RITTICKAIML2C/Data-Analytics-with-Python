# 1. query() 
df.query("Sales > 100000")

Multiple Conditions : 
df.query("Sales > 100000 and Profit > 20000")

# 2. eval() - used for creating / calculating columns 
df.eval("Profit_Margin = Profit / Sales * 100", inplace=True)

