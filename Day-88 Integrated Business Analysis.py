import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Category": ["Electronics","Furniture","Electronics","Furniture",
                 "Electronics","Furniture","Electronics","Furniture"],
    "Sales": [50000,60000,55000,70000,75000,80000,72000,90000],
    "Profit": [10000,12000,11000,14000,15000,16000,14500,18000],
    "Orders": [50,55,52,60,65,70,68,75]
})
# # 1. Profit Margin
df["Profit_Margin_%"] = (df["Profit"] / df["Sales"]) * 100

# # 2. Month-over-Month Growth
df["Sales_Growth_%"] == df["Sales"].pct_change() * 100

# # 3. 3-Month Rolling Average
df["Rolling_3M_Sales"] = df["Sales"].rolling(3).mean()

# # 4, Performance Flag
df["Performance"] = np.select(
    [
        df["Sales_Growth_%"] >= 10,
        df["Sales_Growth_%"] >= 0
    ],
    ["High Growth", "Stable"],
    default="Declining"
)
