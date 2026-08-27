# # 1. plt.figure() - creates a new figure/window for your chart.
plt.figure(figsize=(8, 5))

# # 2. plt.subplot() - after every chart, we can create multiple plots inside one figure.
plt.subplot(rows, columns, position)
plt.subplot(1, 2, 1)

import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 13000, 18000]
profit = [2000, 3500, 2800, 4500]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(months, profit, marker="o")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.tight_layout()
plt.show()

# # 3. plt.tight_layout() - multiple charts are present, label can overlap 
plt.tight_layout() # automatically adjusts spacing.

# # 4. Basic Chart Customizaton 
plt.title()
plt.xlabel()
plt.ylabel()
plt.grid()
plt.xticks() # controsl the x-axis labels
plt.yticks() # control the y-axis labels

plt.xticks(rotation=45)

