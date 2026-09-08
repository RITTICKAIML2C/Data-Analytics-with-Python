# pd.crosstab() - is useful when you want to count how often categories occur together.
Department   Status
IT           Fast
IT           Normal
HR           Fast
HR           Delayed
pd.crosstab(df["Department"], df["Status"])

Rows → first argument
Columns → second argument
Values → counts

