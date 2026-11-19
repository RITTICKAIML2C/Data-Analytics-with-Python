# # 1. Concepts
# # A. Profit Margin Analysis
# df["Profit_Margin_%"] = (
#     df["Profit"] / df["Sales"]
# ) * 100

# # B. KPI Comparison
# df.groupby("Category").agg(
#     Total_Sales=("Sales", "sum"),
#     Total_Profit=("Profit", "sum"),
#     Orders=("Orders", "sum")
# )
# category["Profit_Margin_%"] = (
#     category["Total_Profit"] /
#     category["Total_Sales"] * 100
# )

