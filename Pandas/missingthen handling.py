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



# REMOVE NULL VALUE
# df.dropna(axis=0,inplace=True) removes rows value

# df.dropna(axis=1,inplace=True)  removes columns values
# print(df)

# FILL NULL VALUE

# fill default value
# df.fillna(0,inplace=True)
# print(df)

#fill calculated value
df['age'].fillna(df['age'].mean(),inplace=True)
df['salary'].fillna(df['salary'].mean(),inplace=True)
print(df)