import pandas as pd
data={
    "name":['Ram','shyam','Ramshyam',"aditi","jagdish"],
    "age":[10,20,30,40,50],
    "city":['indore','bhopal','pune',"benglore","delhi"],
    "salary":[5000,6000,3000,2000,2500],
    "performance":[29,45,67,87,98]
}
df=pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'columns name:{df.columns}')