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

#by aquare bracket
df["bonus"]=df['salary']*0.1
print(df)

# using insert() method
# df.insert(loc,"column name",some_data)
df.insert(0,"employee_id",[10,20,30,40,50])
print(df)