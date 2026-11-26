# # Create: Profit_Margin_%, AOV, Profit_per_Order, Revenue_per_Unit
# # Part B — Correlation Analysis. Create a correlation matrix containing: Sales, Profit, Orders, Quantity, Discount_%, Profit_Margin_%, AOV, Profit_per_Order, Revenue_per_Unit
# # Part C — Category Driver Analysis. Group by Category and calculate: Total Sales, Total Profit, Total Orders, Average Profit Margin, Average AOV, Average Discount
# # Part D — Discount Analysis. Create discount bands: Low, Medium, High. Compare: Average Sales, Average Profit, Average Profit Margin, Average AOV. Then determine whether higher discounts appear to be associated with weaker profitability.
# # Part E — 🧠 Driver Identification. Answer: What appears to be the strongest driver of Sales?, What appears to be the strongest driver of Profit?, Does Discount appear harmful to Profit Margin?, Which category performs best overall?, Which category requires attention?, Which products have unusually high AOV?, Which products have unusually low profit margins?
# # Part F — 💼 Executive Insights. Write 5–7 business insights. This time, follow this format: Finding → Evidence → Business implication. Example: Finding: Higher discounts are associated with weaker margins, Evidence: Discount % has a negative correlation with Profit Margin %, Implication: The company should review high-discount products and ensure discounts are justified by increased volume or customer value.
# # ⭐ Bonus Challenge — Correlation vs Business Reality. Suppose you discover: Sales ↔ Orders = 0.95 Does that mean: "Increasing orders will definitely cause sales to increase?". Explain why or why not. This is an important analytics concept and will help you avoid one of the biggest mistakes beginners make when interpreting correlations.
df = pd.DataFrame({
    "Product": [
        "A","B","C","D","E","F",
        "G","H","I","J","K","L"
    ],
    "Category": [
        "Electronics","Electronics","Furniture","Furniture",
        "Clothing","Clothing","Electronics","Furniture",
        "Clothing","Electronics","Furniture","Clothing"
    ],
    "Sales": [
        100000,120000,90000,150000,
        80000,110000,140000,95000,
        130000,105000,125000,85000
    ],
    "Profit": [
        22000,24000,18000,33000,
        12000,25000,28000,15000,
        30000,21000,25000,14000
    ],
    "Orders": [
        10,12,9,15,8,11,
        14,9,13,10,12,8
    ],
    "Quantity": [
        100,140,90,180,120,110,
        170,130,150,105,160,125
    ],
    "Discount_%": [
        5,10,8,5,15,7,
        12,20,6,10,9,18
    ]
})
df["Profit_Margin_%"] = df["Profit"] / df["Sales"] * 100
df["AOV"] = df["Sales"] / df["Orders"]
df["Profit_per_Order"] = df["Profit"] / df["Orders"]
df["Revenue_per_Unit"] = df["Sales"] / df["Quantity"]

cols = ["Sales","Profit","Orders","Quantity","Discount_%",
        "Profit_Margin_%","AOV","Profit_per_Order","Revenue_per_Unit"]

corr = df[cols].corr()

print("\n--- Part B: Correlation Matrix ---")
print(corr.round(3))

c = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)).stack()

print("\nStrongest Positive:", c.idxmax(), round(c.max(), 3))
print("Strongest Negative:", c.idxmin(), round(c.min(), 3))
print("Discount vs Profit Margin:", round(corr.loc["Discount_%","Profit_Margin_%"], 3))
print("Orders vs Sales:", round(corr.loc["Orders","Sales"], 3))

category = df.groupby("Category").agg(
    Total_Sales=("Sales","sum"),
    Total_Profit=("Profit","sum"),
    Total_Orders=("Orders","sum"),
    Avg_Profit_Margin=("Profit_Margin_%","mean"),
    Avg_AOV=("AOV","mean"),
    Avg_Discount=("Discount_%","mean")
).round(2)

print("\n--- Part C: Category Analysis ---")
print(category)

print("\nBest Category:", category["Total_Profit"].idxmax())
print("Category Requiring Attention:", category["Avg_Profit_Margin"].idxmin())

df["Discount_Band"] = pd.cut(
    df["Discount_%"],
    bins=[0,8,15,20],
    labels=["Low","Medium","High"],
    include_lowest=True
)

discount = df.groupby("Discount_Band", observed=True).agg(
    Avg_Sales=("Sales","mean"),
    Avg_Profit=("Profit","mean"),
    Avg_Profit_Margin=("Profit_Margin_%","mean"),
    Avg_AOV=("AOV","mean")
).round(2)

print("\n--- Part D: Discount Analysis ---")
print(discount)

print("\nHigher discount vs margin:",
      "Weaker profitability" if discount.loc["High","Avg_Profit_Margin"] < discount.loc["Low","Avg_Profit_Margin"] else "Not clearly weaker")

print("1. Strongest Sales Driver:", corr["Sales"].drop("Sales").abs().idxmax())
print("2. Strongest Profit Driver:", corr["Profit"].drop("Profit").abs().idxmax())
print("3. Discount harmful to Margin:",
      "Yes" if corr.loc["Discount_%","Profit_Margin_%"] < 0 else "No")

print("4. Best Category:", category["Total_Profit"].idxmax())
print("5. Attention Category:", category["Avg_Profit_Margin"].idxmin())

high_aov = df[df["AOV"] > df["AOV"].mean() + df["AOV"].std()]
low_margin = df[df["Profit_Margin_%"] < df["Profit_Margin_%"].mean() - df["Profit_Margin_%"].std()]

print("6. Unusually High AOV Products:", high_aov["Product"].tolist())
print("7. Unusually Low Margin Products:", low_margin["Product"].tolist())

print("Finding → Sales are strongly linked with Orders.")
print("Evidence → Orders have a very high positive correlation with Sales.")
print("Implication → Increasing valuable orders can be an important sales-growth strategy.")

print("Finding → Higher discounts appear to weaken margins.")
print("Evidence → Discount % has a negative relationship with Profit Margin %.")
print("Implication → High-discount products should be reviewed carefully.")

print("Finding → Electronics performs strongly.")
print("Evidence → Electronics generates strong total sales and profit.")
print("Implication → The company should continue investing in strong Electronics products.")

print("Finding → Low-margin products require attention.")
print("Evidence → Some products have profit margins significantly below the average.")
print("Implication → Pricing, costs and discount levels should be reviewed.")

print("Finding → High-AOV products generate more revenue per order.")
print("Evidence → Their Sales / Orders ratio is unusually high.")
print("Implication → These products may offer opportunities for premium-selling strategies.")

print("Finding → Quantity is an important sales factor.")
print("Evidence → Quantity has a positive correlation with Sales.")
print("Implication → Increasing units sold can support revenue growth.")

print("Sales ↔ Orders = 0.95 does NOT prove that increasing Orders will definitely cause Sales to increase.")
print("Correlation shows association, not causation.")
print("Other factors such as price, product mix, discounts, seasonality and customer behavior may affect both.")
