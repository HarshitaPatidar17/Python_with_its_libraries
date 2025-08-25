import pandas as pd
data={
    "name":['Ram','shyam','Ramshyam',"aditi","jagdish"],
    "age":[10,20,30,None,50],
    "city":['indore','bhopal','pune',None,"delhi"],
    "salary":[5000,6000,3000,None,2500],
    "performance":[29,45,67,None,98]
}
df=pd.DataFrame(data)
print(df)

# linear,polynomial,time

# df.interpolate(method="linear",axis=0,inplace=True) axis=0 row,axis=1 column
df['age']=df['age'].interpolate(method='linear')
print(df)

# df['salary']=df['salary'].interpolate(method='pad')
# df['salary']=df['salary'].interpolate(method='nearest')
print(df)