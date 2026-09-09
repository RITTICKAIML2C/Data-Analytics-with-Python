# # Mini Project — Delivery Performance
# # Create a DataFrame with 12 orders: Order_ID, Department, Delivery_Days
# # Use departments: Electronics, Furniture, Clothing, IT
# # Then create: 1️⃣ Delivery Status
# # Use: df["Delivery_Status"] = ...
# # Rules:
# # Delivery_Days <= 2  → Fast
# # 3–5                 → Normal
# # > 5                 → Delayed
# # You can use np.where() as you learned earlier.
# # 2️⃣ Crosstab
# # Create:
# # pd.crosstab(
# #    df["Department"],
# #     df["Delivery_Status"]
# # )
# # 3️⃣ Business Insights Find: Department with the most Fast deliveries, Department with the most Delayed deliveries, Total number of Fast deliveries, Total number of Delayed deliveries
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Order_ID": [
        101, 102, 103,
        104, 105, 106,
        107, 108, 109,
        110, 111, 112
    ],

    "Department": [
        "Electronics", "Electronics", "Electronics",
        "Furniture", "Furniture", "Furniture",
        "Clothing", "Clothing", "Clothing",
        "IT", "IT", "IT"
    ],

    "Delivery_Days": [
        2, 4, 7,
        1, 5, 6,
        3, 2, 8,
        4, 1, 7
    ]
})
df["Delivery_Status"] = np.where(
    df["Delivery_Days"] <= 2,
    "Fast",
    np.where(
        df["Delivery_Days"] <= 5,
        "Normal",
        "Delayed"
    )
)
print(df)
delivery_table = pd.crosstab(
    df["Department"],
    df["Delivery_Status"]
)
print("Delivery Performance:")
print(delivery_table)
fast_by_department = df[df["Delivery_Status"] == "Fast"].groupby(
    "Department"
).size()
delayed_by_department = df[df["Delivery_Status"] == "Delayed"].groupby(
    "Department"
).size()
print("Department with most Fast deliveries:",
      fast_by_department.idxmax())
print("Department with most Delayed deliveries:",
      delayed_by_department.idxmax())
print("Total Fast deliveries:",
      (df["Delivery_Status"] == "Fast").sum())
print("Total Delayed deliveries:",
      (df["Delivery_Status"] == "Delayed").sum())
