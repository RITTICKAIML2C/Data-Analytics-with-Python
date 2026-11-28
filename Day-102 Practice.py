# # Q1 — Descriptive comparison. Calculate for each group: Sample size, Mean AOV, Median AOV, Standard deviation
# # Q2 — Difference analysis. Calculate: Absolute mean difference Percentage change in mean AOV
# # Q3 — Hypothesis test. Run Welch's independent two-sample t-test. Interpret the p-value using α=0.05.
# # Q4 — Business interpretation. Explain: Is the difference statistically significant? Did average AOV increase? Does this prove the website change caused the increase? What additional evidence would you want?
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

df = pd.DataFrame({
    "Group": [
        "Before", "Before", "Before", "Before", "Before",
        "Before", "Before", "Before", "Before", "Before",
        "After", "After", "After", "After", "After",
        "After", "After", "After", "After", "After"
    ],
    "AOV": [
        450, 480, 420, 500, 460,
        470, 440, 510, 430, 490,
        520, 550, 480, 530, 570,
        510, 540, 500, 560, 530
    ]
})
summary = df.groupby("Group")["AOV"].agg(
    Sample_Size="count",
    Mean_AOV="mean",
    Median_AOV="median",
    Std_Dev="std"
)

print(summary.round(2))

before_mean = df[df["Group"] == "Before"]["AOV"].mean()
after_mean = df[df["Group"] == "After"]["AOV"].mean()

absolute_difference = after_mean - before_mean
percentage_change = (absolute_difference / before_mean) * 100

print("Absolute mean difference:", absolute_difference)
print("Percentage change:", round(percentage_change, 2), "%")

before = df[df["Group"] == "Before"]["AOV"]
after = df[df["Group"] == "After"]["AOV"]

t_stat, p_value = ttest_ind(
    after,
    before,
    equal_var=False
)

print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

# 1. Yes
# 2. Yes
# 3. No
# 4. I would request the following evidence before recommending that the business permanently adopt the website change.
