# # 1. Concepts
# # A. Population vs Sample 
# Population: The entire group you want to understand.
# Sample: A subset of that group used for analysis

# # B. Null and Alternative Hypotheses
# H0 — Null hypothesis: the new website does not change average AOV.
# H1 — Alternative hypothesis: the new website changes average AOV.

# # C. P-value
# A p-value measures how compatible the observed data (or more extreme data) are with the null hypothesis, assuming the null hypothesis and test assumptions hold.

# # D. Independent Two-Sample t-test
# from scipy.stats import ttest_ind
# statistic, p_value = ttest_ind(
#     group_a,
#     group_b,
#     equal_var=False
# )

# # E. Effect Size 
# difference = mean_b - mean_a
# change_pct = (
#     (mean_b - mean_a) / mean_a
# ) * 100
