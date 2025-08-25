import pandas as pd
data={
    "name":['Ram','shyam','Ramshyam',"aditi","jagdish"],
    "age":[10,20,30,40,50],
    "city":['indore','bhopal','pune',"benglore","delhi"],
    "salary":[5000,6000,3000,2000,2500],
    "performance":[29,45,67,87,98]
}
df=pd.DataFrame(data)
 
#display the dataframe
print("sample data")
print(df)
print("names(single column return series)")
name=df['name']
print(name)

#selecting multiple columns
multiple=df[["name","salary"]]
print(multiple)

#filtering rows
high_salary=df[df['age']<50]
print(high_salary)

#combine mltiple conditions
filtered=df[(df["salary"]>2000)&(df["age"]<30)]
print(filtered)

#using or condition
filtered=df[(df["salary"]>2000)|(df["age"]<30)]
print(filtered)