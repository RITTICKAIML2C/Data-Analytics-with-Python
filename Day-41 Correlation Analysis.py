# # 1. What is correlation ?
df["Experience"].corr(df["Salary"])

# # 2. Simple Example 
import pandas as pd 
df = pd.DataFrame({
    "Experience" : [1, 2, 3, 4, 5], 
    "Salary" : [30000, 35000, 42000, 50000, 60000]
})
# correlation = df["Experience"].corr(df["Salary"])
print("Correlation:", correlation)

# # 3. Correlation Matrix 
df.corr(numeric_only=True)

