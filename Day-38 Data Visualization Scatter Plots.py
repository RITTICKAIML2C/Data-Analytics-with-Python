# # 1. Scatter Plot - places individual observations as dots on a graph.
# plt.scatter(x, y)
import matplotlib.pyplot as plt
experience = [1, 2, 3, 4, 5, 6]
salary = [30000, 35000, 42000, 50000, 58000, 70000]
plt.scatter(experience, salary)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid()
plt.show()

# # 2. Scatter() vs Plot()
# # Scatter() - is better when you're investigating a relationship between two variables.
# # Plot() - which is mainly useful for trends/sequences, especially time-series data.
