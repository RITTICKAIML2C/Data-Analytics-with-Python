# 1. RFM Scores
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5,4,3,2,1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

# 2. RFM Score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(int) +
    rfm["F_Score"].astype(int) +
    rfm["M_Score"].astype(int)
)

# 3. Business Segments
rfm["Segment"] = np.select(
    [
        (rfm["R_Score"] >= 4) & (rfm["F_Score"] >= 4),
        (rfm["R_Score"] >= 4) & (rfm["M_Score"] >= 4),
        (rfm["R_Score"] <= 2) & (rfm["F_Score"] >= 3),
        (rfm["R_Score"] <= 2) & (rfm["M_Score"] >= 3)
    ],
    [
        "Loyal Customers",
        "High Value",
        "At Risk",
        "Potential Churn"
    ],
    default="Regular"
)

