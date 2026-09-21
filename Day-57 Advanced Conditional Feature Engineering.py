# # 1. np.select()
# # The general structure is:
conditions = [
    condition_1,
    condition_2,
    condition_3
]

choices = [
    "Category 1",
    "Category 2",
    "Category 3"
]

df["New_Column"] = np.select( 
    conditions,
    choices,
    default="Other"
)

# # ⚠️ Important - np.select() checks conditions from top to bottom.
# # For example:
conditions = [
    df["Performance"] >= 90,
    df["Performance"] >= 75,
    df["Performance"] >= 60
]

# A performance of 95 satisfies all three conditions, but it gets: Excellent because the first condition is checked first.
