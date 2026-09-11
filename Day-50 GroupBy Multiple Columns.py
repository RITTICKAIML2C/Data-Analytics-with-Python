# # So far you've done:
df.groupby("Department")["Sales"].sum()

# # We can do:
df.groupby(["Department", "Status"])["Sales"].sum()
