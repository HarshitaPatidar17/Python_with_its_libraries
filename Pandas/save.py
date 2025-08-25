import pandas as pd
data={
    "name":['Ram','shyam','Ramshyam'],
    "age":[10,20,30],
    "city":['indore','bhopal','pune']
}
df=pd.DataFrame(data)
print(df)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
# df.to_json("output.json",index=False)
