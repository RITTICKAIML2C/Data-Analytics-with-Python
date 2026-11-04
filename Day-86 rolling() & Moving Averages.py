# 1. Core Concepts
# a. Simple Rolling Average
df["Rolling_Avg"] = df["Sales"].rolling(window=3).mean()

# b. Rolling Sum
df["Rolling_Sales"] = df["Sales"].rolling(3).sum()

# c. Rolling Maximum
df["Rolling_Max"] = df["Sales"].rolling(3).max()

# d. min_periods
df["Rolling_Avg"] = df["Sales"].rolling(window=3, min_periods=1).mean()

