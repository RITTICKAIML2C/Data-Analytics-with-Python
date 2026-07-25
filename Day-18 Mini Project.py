# # 🚀 Mini Project
# # Student Marks Preprocessing Dashboard
# # Create
# # marks = np.array([
# # 78,
# # 85,
# # 92,
# # 67,
# # 88,
# # 95,
# # 73,
# # 81
# # ])
# # Display
# # Original marks
# # Marks after adding 5 grace marks
# # Marks after multiplying by 1.05
# # Normalized marks
# # Standardized marks
# # Highest mark
# # Lowest mark
# # Average mark
# # Standard deviation
import numpy as np
marks = np.array([
78,
85,
92,
67,
88,
95,
73,
81
])
print("Original Marks:", marks)
print("Marks after adding 5 grace amrks:", marks + 5)
print("Marks after multiplying by 1.05:", marks * 1.05)
print("Normalized Marks:", (marks - marks.min()) / (marks.max() - marks.min()))
print("Standardized Marks:", (marks - marks.mean()) / marks.std())
print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())
print("Average Marks:", marks.mean())
print("Standard Deviation:", marks.std())
