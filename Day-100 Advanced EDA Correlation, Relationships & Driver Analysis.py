# # 1. Concepts
# # A. Correlation
# df["Sales"].corr(df["Profit"])

# # B. Correlation Matrix 
# corr = df[
#     ["Sales", "Profit", "Orders", "Discount", "Quantity"]
# ].corr()

# # C. Profit Margin as a Driver
# df["Profit_Margin_%"] = (
#     df["Profit"] / df["Sales"] * 100
# )

# # D. Group-Based Driver Analysis 
# df.groupby("Discount_Band")["Profit_Margin_%"].mean()

