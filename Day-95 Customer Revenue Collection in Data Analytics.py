# # 1. Pareto Analysis
# # Step 1 — Sort customers by revenue
# customer = customer.sort_values("Total_Sales", ascending=False)

# # Step 2 — Calculate revenue percentage
# customer["Revenue_%"] = (
#     customer["Total_Sales"] /
#     customer["Total_Sales"].sum() * 100
# )

# # Step 3 — Calculate cumulative revenue %
# customer["Cumulative_Revenue_%"] = (
#     customer["Revenue_%"].cumsum()
# )

# # Step 4 — Find customers contributing up to 80%
# top_80 = customer[
#     customer["Cumulative_Revenue_%"] <= 80
# ]


