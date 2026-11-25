# # Q1 — Basic Correlation. Calculate correlations between: Sales and Profit, Sales and Orders, Sales and Quantity, Discount and Profit
# # Q2 — Correlation Matrix. Create a correlation matrix for: Sales, Profit, Orders, Quantity, Discount_%. Then identify: Strongest positive relationship, Strongest negative relationship
# # Q3 — Profit Margin. Then find: Highest-margin product, Lowest-margin product, Average profit margin
# # Q4 — Discount Analysis. Then calculate average: Sales, Profit, Profit Margin for each discount band.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Product": [
        "A","B","C","D","E",
        "F","G","H","I","J"
    ],
    "Sales": [
        100000,120000,90000,150000,80000,
        110000,140000,95000,130000,105000
    ],
    "Profit": [
        22000,24000,18000,33000,12000,
        25000,28000,15000,30000,21000
    ],
    "Orders": [
        10,12,9,15,8,
        11,14,9,13,10
    ],
    "Quantity": [
        100,140,90,180,120,
        110,170,130,150,105
    ],
    "Discount_%": [
        5,10,8,5,15,
        7,12,20,6,10
    ]
})
sales_profit = df["Sales"].corr(df["Profit"])
sales_orders = df["Sales"].corr(df["Orders"])
sales_quantity = df["Sales"].corr(df["Quantity"])
discount_profit = df["Discount_%"].corr(df["Profit"])

print(f"Sales vs Profit     : {sales_profit:.4f}")
print(f"Sales vs Orders     : {sales_orders:.4f}")
print(f"Sales vs Quantity   : {sales_quantity:.4f}")
print(f"Discount vs Profit  : {discount_profit:.4f}")


columns = [
    "Sales",
    "Profit",
    "Orders",
    "Quantity",
    "Discount_%"
]

corr_matrix = df[columns].corr()

print("\nCorrelation Matrix:")
print(corr_matrix.round(4))


# Find strongest positive and negative relationships
corr_no_diag = corr_matrix.copy()

# Remove diagonal values because they are always 1.0
np.fill_diagonal(corr_no_diag.values, np.nan)

# Get unique pairs only
upper_triangle = corr_no_diag.where(
    np.triu(np.ones(corr_no_diag.shape), k=1).astype(bool)
)

correlations = upper_triangle.stack()

strongest_positive_pair = correlations.idxmax()
strongest_positive_value = correlations.max()

strongest_negative_pair = correlations.idxmin()
strongest_negative_value = correlations.min()

print("\nStrongest Positive Relationship:")
print(
    f"{strongest_positive_pair[0]} vs "
    f"{strongest_positive_pair[1]} = "
    f"{strongest_positive_value:.4f}"
)

print("\nStrongest Negative Relationship:")
print(
    f"{strongest_negative_pair[0]} vs "
    f"{strongest_negative_pair[1]} = "
    f"{strongest_negative_value:.4f}"
)

f["Profit_Margin_%"] = (
    df["Profit"] / df["Sales"]
) * 100


print("\nProfit Margin by Product:")
print(
    df[
        [
            "Product",
            "Sales",
            "Profit",
            "Profit_Margin_%"
        ]
    ].round(2)
)


# Highest-margin product
highest_margin_index = df["Profit_Margin_%"].idxmax()

highest_margin_product = df.loc[
    highest_margin_index,
    "Product"
]

highest_margin = df.loc[
    highest_margin_index,
    "Profit_Margin_%"
]


# Lowest-margin product
lowest_margin_index = df["Profit_Margin_%"].idxmin()

lowest_margin_product = df.loc[
    lowest_margin_index,
    "Product"
]

lowest_margin = df.loc[
    lowest_margin_index,
    "Profit_Margin_%"
]


# Average profit margin
average_profit_margin = df["Profit_Margin_%"].mean()


print("\nHighest-Margin Product:")
print(
    f"{highest_margin_product} "
    f"= {highest_margin:.2f}%"
)

print("\nLowest-Margin Product:")
print(
    f"{lowest_margin_product} "
    f"= {lowest_margin:.2f}%"
)

print("\nAverage Profit Margin:")
print(
    f"{average_profit_margin:.2f}%"
)

df["Discount_Band"] = pd.cut(
    df["Discount_%"],
    bins=[0, 5, 10, 15, 20],
    labels=[
        "0-5%",
        "6-10%",
        "11-15%",
        "16-20%"
    ],
    include_lowest=True
)


# Group by Discount Band
discount_analysis = df.groupby(
    "Discount_Band",
    observed=True
).agg(
    Average_Sales=("Sales", "mean"),
    Average_Profit=("Profit", "mean"),
    Average_Profit_Margin=("Profit_Margin_%", "mean")
).reset_index()


print("\nDiscount Band Analysis:")
print(
    discount_analysis.round(2)
)

print(
    f"\n1. Sales vs Profit Correlation  : "
    f"{sales_profit:.4f}"
)

print(
    f"2. Sales vs Orders Correlation  : "
    f"{sales_orders:.4f}"
)

print(
    f"3. Sales vs Quantity Correlation: "
    f"{sales_quantity:.4f}"
)

print(
    f"4. Discount vs Profit Correlation: "
    f"{discount_profit:.4f}"
)

print(
    f"\n5. Strongest Positive Relationship: "
    f"{strongest_positive_pair[0]} vs "
    f"{strongest_positive_pair[1]} "
    f"({strongest_positive_value:.4f})"
)

print(
    f"6. Strongest Negative Relationship: "
    f"{strongest_negative_pair[0]} vs "
    f"{strongest_negative_pair[1]} "
    f"({strongest_negative_value:.4f})"
)

print(
    f"\n7. Highest-Margin Product: "
    f"{highest_margin_product} "
    f"({highest_margin:.2f}%)"
)

print(
    f"8. Lowest-Margin Product: "
    f"{lowest_margin_product} "
    f"({lowest_margin:.2f}%)"
)

print(
    f"9. Average Profit Margin: "
    f"{average_profit_margin:.2f}%"
)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)
