import pandas as pd
df=pd.read_csv("Pandas/sales_data_sample.csv",encoding="latin1")
print("display 5 rows from top")
print(df.head())
print("display 7 rows from bottom")
print(df.tail(7))

