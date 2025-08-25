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


# UPDATE SPECIFIC LOCATION VALUES
# .loc[]
# df.loc[row_index,"column_Name"]=new+value
df.loc[0,'salary']=5500
print(df)

# UPDATE MORE VALUES 
# increasing salary by 5%['salary]
df['salary']=df['salary']*1.05
print(df)



# DELETE ROW OR COLUMN
# df.drop(columns= ['columnname'],inplace=True)

# remove single column
df.drop(columns= ["performance"],inplace=True)
print(df)

# remove multiple columns
df.drop(columns=['name','age'],inplace=True)
print(df)