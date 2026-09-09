# # value_counts() - tells how frequently each category appears 
import pandas as pd
df = pd.DataFrame({
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT"
    ]
})
print(df["Department"].value_counts())

# # Output : 
IT          4
HR          2
Finance     2
