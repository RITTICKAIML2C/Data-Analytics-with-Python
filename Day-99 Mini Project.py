# # Part A — Rolling KPIs Create: Month, Sales, Profit, Rolling_3M_Sales, Rolling_3M_Profit
# # Part B — Z-Score Detection. Create:, Sales_Z_Score, Profit_Z_Score. Flag anomalies:
# # Part C — IQR Detection For both Sales and Profit: Calculate: Q1, Q3, IQR, Lower Bound, Upper Bound
# # Part D — Compare Method Create a summary: Which months are identified by Z-score?, Which months are identified by IQR?, Do both methods identify the same anomaly?, Which method is more sensitive for this dataset?
# # Part E — 📈 Business Investigation For every detected anomaly, investigate: Sales change %, Profit change %, Profit margin, Difference from rolling average
# # Part F — 💼 Analyst Insights Write 5 business insights. Your insights should answer questions like: Is the anomaly positive or negative? Does the unusual sales value also produce unusually high profit? Did profitability improve or deteriorate during the anomaly? Should the anomaly be included when forecasting future sales? What additional business information would you request before making a decision?
# # ⭐ Bonus Challenge — Robust Anomaly Detection This is closer to the idea of asking: "Is this month's sales unusually high compared with its recent history?" rather than: Is this month's sales unusual compared with the entire year?"
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],
    "Sales": [
        85000,90000,94000,98000,
        103000,108000,112000,118000,
        122000,175000,128000,133000
    ],
    "Profit": [
        17000,18000,18800,19600,
        20600,21600,22400,23600,
        24400,35000,25600,26600
    ]
})
df["Rolling_3M_Sales"] = (
    df["Sales"].rolling(3).mean()
)

df["Rolling_3M_Profit"] = (
    df["Profit"].rolling(3).mean()
)


# Sales Z-Score
df["Sales_Z_Score"] = (
    (df["Sales"] - df["Sales"].mean())
    / df["Sales"].std(ddof=0)
)

# Profit Z-Score
df["Profit_Z_Score"] = (
    (df["Profit"] - df["Profit"].mean())
    / df["Profit"].std(ddof=0)
)


# Flag anomalies
df["Sales_Anomaly"] = (
    df["Sales_Z_Score"].abs() > 2
)

df["Profit_Anomaly"] = (
    df["Profit_Z_Score"].abs() > 2
)


Q1_sales = df["Sales"].quantile(0.25)
Q3_sales = df["Sales"].quantile(0.75)

IQR_sales = Q3_sales - Q1_sales

Lower_Bound_sales = (
    Q1_sales - 1.5 * IQR_sales
)

Upper_Bound_sales = (
    Q3_sales + 1.5 * IQR_sales
)


df["Sales_IQR_Anomaly"] = (
    (df["Sales"] < Lower_Bound_sales) |
    (df["Sales"] > Upper_Bound_sales)
)

Q1_profit = df["Profit"].quantile(0.25)
Q3_profit = df["Profit"].quantile(0.75)

IQR_profit = Q3_profit - Q1_profit

Lower_Bound_profit = (
    Q1_profit - 1.5 * IQR_profit
)

Upper_Bound_profit = (
    Q3_profit + 1.5 * IQR_profit
)


df["Profit_IQR_Anomaly"] = (
    (df["Profit"] < Lower_Bound_profit) |
    (df["Profit"] > Upper_Bound_profit)
)
Q1_profit = df["Profit"].quantile(0.25)
Q3_profit = df["Profit"].quantile(0.75)

IQR_profit = Q3_profit - Q1_profit

Lower_Bound_profit = (
    Q1_profit - 1.5 * IQR_profit
)

Upper_Bound_profit = (
    Q3_profit + 1.5 * IQR_profit
)


df["Profit_IQR_Anomaly"] = (
    (df["Profit"] < Lower_Bound_profit) |
    (df["Profit"] > Upper_Bound_profit)
)
df["Profit_Margin_%"] = (
    df["Profit"] / df["Sales"] * 100
)


# Sales Change %
df["Sales_Change_%"] = (
    df["Sales"].pct_change() * 100
)


# Profit Change %
df["Profit_Change_%"] = (
    df["Profit"].pct_change() * 100
)


# Difference from Rolling Average
df["Sales_Diff_From_Rolling"] = (
    df["Sales"] - df["Rolling_3M_Sales"]
)

df["Profit_Diff_From_Rolling"] = (
    df["Profit"] - df["Rolling_3M_Profit"]
)


rolling_mean = (
    df["Sales"]
    .shift(1)
    .rolling(3)
    .mean()
)

rolling_std = (
    df["Sales"]
    .shift(1)
    .rolling(3)
    .std()
)

df["Rolling_Z"] = (
    (df["Sales"] - rolling_mean)
    / rolling_std
)


# Rolling Z-Score anomaly
df["Rolling_Z_Anomaly"] = (
    df["Rolling_Z"].abs() > 2
)


print("\n" + "=" * 80)
print("COMPLETE SALES ANOMALY DETECTION DATASET")
print("=" * 80)

print(df.to_string(index=False))


print("\n" + "=" * 80)
print("IQR STATISTICS")
print("=" * 80)

print("\nSALES")
print("Q1:", Q1_sales)
print("Q3:", Q3_sales)
print("IQR:", IQR_sales)
print("Lower Bound:", Lower_Bound_sales)
print("Upper Bound:", Upper_Bound_sales)

print("\nPROFIT")
print("Q1:", Q1_profit)
print("Q3:", Q3_profit)
print("IQR:", IQR_profit)
print("Lower Bound:", Lower_Bound_profit)
print("Upper Bound:", Upper_Bound_profit)

print("\n" + "=" * 80)
print("ANOMALY METHOD COMPARISON")
print("=" * 80)

print(summary.to_string(index=False))

print("\n" + "=" * 80)
print("SALES ANOMALIES")
print("=" * 80)

sales_anomalies = df[
    df["Sales_Anomaly"] | df["Sales_IQR_Anomaly"]
]

print(
    sales_anomalies[
        [
            "Month",
            "Sales",
            "Sales_Z_Score",
            "Sales_Anomaly",
            "Sales_IQR_Anomaly"
        ]
    ].to_string(index=False)
)

print("\n" + "=" * 80)
print("PROFIT ANOMALIES")
print("=" * 80)

profit_anomalies = df[
    df["Profit_Anomaly"] | df["Profit_IQR_Anomaly"]
]

print(
    profit_anomalies[
        [
            "Month",
            "Profit",
            "Profit_Z_Score",
            "Profit_Anomaly",
            "Profit_IQR_Anomaly"
        ]
    ].to_string(index=False)
)


print("\n" + "=" * 80)
print("PROFIT ANOMALIES")
print("=" * 80)

profit_anomalies = df[
    df["Profit_Anomaly"] | df["Profit_IQR_Anomaly"]
]

print(
    profit_anomalies[
        [
            "Month",
            "Profit",
            "Profit_Z_Score",
            "Profit_Anomaly",
            "Profit_IQR_Anomaly"
        ]
    ].to_string(index=False)
)

print("\n" + "=" * 80)
print("BUSINESS INVESTIGATION")
print("=" * 80)

business_investigation = df[
    df["Sales_Anomaly"] |
    df["Profit_Anomaly"] |
    df["Sales_IQR_Anomaly"] |
    df["Profit_IQR_Anomaly"]
][
    [
        "Month",
        "Sales",
        "Profit",
        "Sales_Change_%",
        "Profit_Change_%",
        "Profit_Margin_%",
        "Rolling_3M_Sales",
        "Sales_Diff_From_Rolling",
        "Rolling_3M_Profit",
        "Profit_Diff_From_Rolling"
    ]
]

print(
    business_investigation.to_string(index=False)
)
print("\n" + "=" * 80)
print("ROLLING Z-SCORE ANALYSIS")
print("=" * 80)

print(
    df[
        [
            "Month",
            "Sales",
            "Rolling_Z",
            "Rolling_Z_Anomaly"
        ]
    ].to_string(index=False)
)
print("\n" + "=" * 80)
print("BUSINESS INSIGHTS")
print("=" * 80)

print("""
1. October is the major positive sales anomaly in the dataset.

2. October's unusually high sales are accompanied by unusually
   high profit, so the anomaly is not simply revenue growth
   without profitability.

3. October maintains approximately a 20% profit margin, which
   suggests profitability did not deteriorate during the anomaly.

4. October should not automatically be treated as the new normal
   when forecasting future sales. The reason behind the spike
   should first be investigated.

5. Additional information such as orders, average order value,
   discounts, promotions, marketing campaigns, major customers,
   product-level sales, and one-time transactions should be
   investigated before making a forecasting decision.
""")
