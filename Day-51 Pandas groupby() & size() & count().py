# # 1. groupby().size()
import pandas as pd 
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "HR"],
    "Status": ["Completed", "Pending", "Completed", "Pending", "Completed"]
})
# # To count rows : 
print(df.groupby("Department").size())

# # For multiple columns : 
print(df.groupby(["Department", "Status"]).size())

