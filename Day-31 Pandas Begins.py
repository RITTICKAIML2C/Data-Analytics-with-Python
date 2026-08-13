# # 1. Import Pandas 
import pandas as pd 

# # 2. Pandas Series - A Series is basically a one-dimensional labeled array.
import pandas as pd
marks = pd.Series([78, 85, 91, 67, 88])
print(marks)

# # Series with custom index 
import pandas as pd
marks = pd.Series(
    [78, 85, 91, 67], 
    index = ["A", "B", "C", "D"]
)
print(marks)
print(marks["C"])

# # 3. Important Series Attributes 
marks.values - Values inside Series
marks.index - Index labels
marks.dtype - Data type
marks.shape - Dimensions
marks.size - Number of elements

# # 4. Creating a DataFrame - A DataFrame is Pandas' main table structure.
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)
print(df)
print(df["Salary"])

# # 5. DataFrame Anatomy - A DataFrame consists of multiple Series.
#                  DataFrame
#                      ↓
#        ┌──────────────────────────┐
#        │ ID │ Salary │ Performance│
#        ├──────────────────────────┤
# Index →│ 0  │ 35000  │ 68          │
#        │ 1  │ 42000  │ 75          │
#        │ 2  │ 51000  │ 91          │
#        └──────────────────────────┘

# # 6. Selecting a Column 
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)
# a. Single Column:
print(df["Salary"])

# # b. Multiple Column 
print(df[["Salary", "Performance"]])

# # c. Important Distinction
# # 1. Series 
print(df["Salary"])

# # 2. DataFrame
print(df[["Salary"]]) 

# # 7. Basic DataFrame Inspection - These are must-know Data Analyst commands
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)
# # a. head() - Shows first 5 rowa
print(df.head())
print(df.head(3))

# # b. tail() - shows last rows
print(df.tail()) 

# # c. shape - dimensions 
print(df.shape) # 4 rows X 4 columns

# # d. columns - shows column names.
print(df.columns)

# # e. index - shows row index.
print(df.index)

# # f. dtypes - shows the datatype of every column
print(df.dtypes)

# # g. info() - useful for understanding - number of rows, columns, non-null value, datatypes, memory usage
print(df.info())

# # h. describe() - gives stastistical info about numerical columns - count, mean, std, min, 25%, 50%, 75%, maximum 
print(df.describe())

# # 8. loc[] - label-based selection 
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)

# # a. get rows with index 0
print(df.loc[0])

# # b. Multiple Rows
print(df.loc[0:2])

# # c. Specific Row + Columns
print(df.loc[0, "Salary"])

# # 9. iloc[] - Position-Based Selection
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)

# # a. First Row
print(df.iloc[0])

# # b. First row, second column
print(df.iloc[0, 1])

# # c. Row 0-2, Column 1-2
print(df.iloc[0:3, 1:3])

# # 10. Filtering Data - Extremely Powerful
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Salary": [35000, 42000, 51000, 62000],
    "Performance": [68, 75, 91, 88],
    "Experience": [1, 2, 5, 4]
}
df = pd.DataFrame(data)

# # a. Employees earning more than $50,000:
print(df[df["Salary"] > 50000])

# # b. Performance ≥ 85:
print(df[df["Performance"] >= 85])

# # c. Multiple Conditions:
# # 1. and condition
print(df[
    (df["Salary"] > 50000) &
    (df["Performance"] >= 85)
])

# # 2. or condition
print(df[
    (df["Salary"] > 50000) |
    (df["Performance"] >= 90)
])

