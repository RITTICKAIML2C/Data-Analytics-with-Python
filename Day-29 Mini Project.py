# # Mini Project -Student Ranking Dashboard
# # 📊 Basic Analysis : Original student IDs, Original marks Ascending marks Descending marks Highest marks Lowest marks Average marks
# # 🏆 Ranking : Using np.argsort(): Ranking indices Student IDs sorted by marks Marks sorted from highest → lowest Top 3 student IDs Top 3 marks Bottom 3 student IDs Bottom 3 marks
import numpy as np
student_id = np.array([
    101, 102, 103, 104, 105, 106, 107, 108
])
marks = np.array([
    78, 92, 65, 88, 95, 71, 84, 90
])
print("Original student IDs:")
print(student_id)
print("Original marks:")
print(marks)
ascending_marks = np.sort(marks)
print("Ascending marks:")
print(ascending_marks)
descending_marks = np.sort(marks)[::-1]
print("Descending marks:")
print(descending_marks)
highest_marks = np.max(marks)
print("Highest marks:")
print(highest_marks)
lowest_marks = np.min(marks)
print("Lowest marks:")
print(lowest_marks)
average_marks = np.mean(marks)
print("Average marks:")
print(average_marks)
ranking_indices = np.argsort(marks)[::-1]
print("Ranking indices:")
print(ranking_indices)
sorted_student_ids = student_id[ranking_indices]
print("Student IDs sorted by marks:")
print(sorted_student_ids)
sorted_marks = marks[ranking_indices]
print("Marks sorted from highest → lowest:")
print(sorted_marks)
top_3_indices = ranking_indices[:3]
print("Top 3 student IDs:")
print(student_id[top_3_indices])
print("Top 3 marks:")
print(marks[top_3_indices])
bottom_3_indices = ranking_indices[-3:]
print("Bottom 3 student IDs:")
print(student_id[bottom_3_indices])
print("Bottom 3 marks:")
print(marks[bottom_3_indices])



