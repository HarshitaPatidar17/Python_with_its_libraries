import pandas as pd
# import os
# print(os.getcwd())

#read data from csv file into a data frame
df=pd.read_csv("Pandas/sales_data_sample.csv",encoding="latin1")

print(df)