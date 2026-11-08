# # 🏆 Mini Project — Business Performance Dashboard Create a complete analysis containing: Part A — Feature Engineering Add: Profit_Margin_%
# # Sales_Growth_%, Rolling_3M_Sales, Sales_Rank, Performance
# # Part B — Business Analysis Find:
# # Highest-sales month, Highest-profit month, Highest-growth month, Largest decline month, Highest rolling-average month, Best-performing category by total sales
# # Part C — Final Insights Write 5 business insights from your analysis.Example format:August recorded the highest monthly sales., July experienced the largest month-over-month decline.
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
df["Profit_Margin_%"] = (df["Profit"] / df["Sales"]) * 100

df["Sales_Growth_%"] = df["Sales"].pct_change() * 100

df["Rolling_3M_Sales"] = df["Sales"].rolling(3).mean()

df["Sales_Rank"] = df["Sales"].rank(
    ascending=False,
    method="min"
)

df["Performance"] = np.where(
    df["Profit_Margin_%"] >= 20,
    "High",
    "Low"
)
print(df)
