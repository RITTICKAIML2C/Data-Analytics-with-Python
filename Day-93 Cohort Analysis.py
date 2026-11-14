# # Cohort Analysis 
# # 1. First Purchase Month
# df.groupby("Customer")["Order_Date"].transform("min")

# # 2. Cohort Month
# df["Cohort_Month"] = df.groupby("Customer")["Order_Date"].transform("min").dt.to_period("M")

# # 3. Purchase Month
# df["Purchase_Month"] = df["Order_Date"].dt.to_period("M")

# # 4. Cohort Age
# df["Cohort_Index"] = (
    # (df["Purchase_Month"].dt.year - df["Cohort_Month"].dt.year) * 12
    # + (df["Purchase_Month"].dt.month - df["Cohort_Month"].dt.month)
# )
