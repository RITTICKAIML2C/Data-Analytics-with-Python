# # 1. Missing Values 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. detect missing values 
print(df.isnull())
print(df.isna())

# # b. count missing values 
print(df.isnull().sum())

# # 2. notna() - find values that are not missing 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
print(df.notna())

# # You can also filter:
print(df[df["Salary"].notna()])

# # 3. Removing Missing Data
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. Remove rows containing missing values
print(df.dropna())

# # b. Remove rows only when a particular column is missing
print(df.dropna(subset = ["Salary"]))

# # 4. Filling Missing Values - Instead of deleting rows, we can replace missing values.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. Fill with a fixed value 
df["Salary"] = df["Salary"].fillna(50000)
print(df["Salary"])

# # b. Fill with mean 
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

# # c. Fill with median 
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df["Salary"])

# # 5. Duplicates 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. Check Duplicate Rows:
print(df.duplicated())

# # b. Count Duplicate Rows:
print(df.duplicated().sum())

# # c. Remove them
print(df.drop_duplicates())

# # d. Check Duplicates based on Columns 
print(df.duplicated(subset = ["Salary"]))

# # 6. Creating & Modifying Columns
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. Create new columns directly.
df["Bonus"] = df["Salary"] * 0.10
print(df)

# # 7. apply() - lets you apply a function to every value
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
df["Salary"] = df["Salary"].apply(lambda x: x + 5000)
print(df)

df["Performance_Level"] = df["Performance"].apply(lambda x: "Excellent" if x >= 85 else "Needs Improvement")
print(df)

# # 8. Sorting 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. Sort by Salary
print(df.sort_values("Salary"))

# # b. Highest Salary first:
print(df.sort_values("Salary", ascending=False))

# # c. Sort using Multiple Columns:
print(df.sort_values(["Name", "Salary"], ascending=[True, False]))

# # 9. value_counts() - Extremely useful for categorical analysis
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
print(df["Salary"].value_counts())

# # 10. unique() & nunique()
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. unique performance
print(df["Performance"].unique())

# # b. count unique performance 
print(df["Performance"].nunique())

# # 11. replace() 
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Aman", "Riya ", "Rahul", "Neha"],
    "Salary": [35000, np.nan, 52000, 68000],
    "Performance": [72, 85, np.nan, 88]
})
# # a. replace incorrect/inconsistent values:
df["Name"] = df["Name"].replace("Riya ", "Riya")
print(df)

# # b. You can replace multiple values:
df["Name"] = df["Name"].replace({"Aman" : "Suraj", "Neha" : "Saumya"})
print(df)

