# # Mini Project
# # Employee Performance Dashboard
# # Create
# # performance = np.array([78,45,91,66,82,39,55,97,71,28])
# # Display: Original scores, Passed employees (≥40), Failed employees (<40), Excellent employees (≥85), Average employees (40–84), Replace failed scores with 40, Label each employee:, "Excellent" (≥85), "Pass" (40–84)
# # "Fail" (<40)
# # Highest score
# # Lowest score
# # Average score
import numpy as np

performance = np.array([78,45,91,66,82,39,55,97,71,28])

print("Original:", performance)
print("Passed:", performance[performance >= 40])
print("Failed:", performance[performance < 40])
print("Excellent:", performance[performance >= 85])
print("Average:", performance[(performance >= 40) & (performance < 85)])
updated = np.where(performance < 40, 40, performance)
print("Updated:", updated)
labels = np.where(performance >= 85, "Excellent",
         np.where(performance >= 40, "Pass", "Fail"))
print("Labels:", labels)
print("Highest:", np.max(performance))
print("Lowest:", np.min(performance))
print("Average:", np.mean(performance))
