import pandas as pd
df=pd.read_csv("Pandas/sales_data_sample.csv",encoding="latin1")
print("displaying info of data set")
print(df.info())


data={
    "name":['Ram','shyam','Ramshyam'],
    "age":[10,20,30],
    "city":['indore','bhopal','pune']
}
df=pd.DataFrame(data)
print(df.info())
