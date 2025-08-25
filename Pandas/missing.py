import pandas as pd
data={
    "name":['Ram','shyam','Ramshyam',None,"jagdish"],
    "age":[10,20,30,None,50],
    "city":['indore','bhopal','pune',None,"delhi"],
    "salary":[5000,6000,3000,None,2500],
    "performance":[29,45,67,None,98]
}
df=pd.DataFrame(data)
print(df)


print(df.isnull())       #true if numm,falsi if present
print(df.isnull().sum())  #count of null values
