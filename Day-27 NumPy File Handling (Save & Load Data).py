# # 1. np.save() - Save a NumPy Array
import numpy as np
marks = np.array([78, 85, 91, 67])
np.save("marks.npy", marks)
print("File Saved Successfully")

# # 2. np.load() - Load a NumPy Array
import numpy as np 
loaded = np.load("marks.npy")
print(loaded)

# # 3. np.savetxt() - Save as Text File
import numpy as np 
sales = np.array([1200, 1500, 1800])
np.savetxt("sales.txt", sales)
# # Save with Comma Seperator 
np.savetxt("sales.csv", sales, delimiter = ",")

# # 4. np.loadtxt() - Load Text or CSV File 
import numpy as np 
data = np.loadtxt("sales.csv", delimiter = ",")
print(data)

# # 5. Save Integers Properly 
import numpy as np 
marks = np.array([78, 85, 91, 67])
np.savetxt("marks.txt", marks, fmt = "%d")

# # 6. Save Floating Point Numbers 
import numpy as np 
prices = np.array([10.4567, 20.7834])
np.savetxt("prices.txt", prices, fmt = "%.2f")

# # 7. Load 2D Arrays
import numpy as np 
matrix = np.array([
    [10, 20], 
    [30, 40]
])
np.savetxt("matrix.csv", matrix, delimiter = ",")
loaded = np.loadtxt("matrix.csv", delimiter = ",")
print(loaded)
