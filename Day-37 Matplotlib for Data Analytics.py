# # 1. What is Matplotlib ?
pip install matplotlib

# # 2. Basic Line Chart - a line chart is useful for showing trends overs time.
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 14000, 18000, 22000]
plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# # 3.  Adding Markers - we can show the individual data points
plt.plot(months, sales, marker="o")
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# # 4. Grid - makes values easier to read.
plt.grid()
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 14000, 18000, 22000]
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

# # 5. Bar Chart - is mainly used to compare categories 
import matplotlib.pyplot as plt
departments = ["IT", "HR", "Finance", "Marketing"]
sales = [85000, 52000, 73000, 64000]
plt.bar(departments, sales)
plt.title("Sales by Department")
plt.xlabel("Department")
plt.ylabel("Sales")
plt.show()

# # 6. Finding Insights with Pandas - Matplotlin is for visualization, but we still use Pandas for calculations.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Sales": [85000, 52000, 73000, 64000]
})
print(df["Sales"].max())
highest = df.loc[df["Sales"].idxmax()]
print(highest)
plt.bar(df["Department"], df["Sales"])
plt.title("Sales by Department")
plt.xlabel("Department")
plt.ylabel("Sales")
plt.show()
