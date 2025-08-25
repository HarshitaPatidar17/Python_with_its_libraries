# sorting data
# sorting data in 1 column sort_values()
# df.sort_values(by="column name",true/false,inplace=True)

import pandas as pd
data={
    "name":['arun', 'sita','karan','radha'],
    "age":[34,54,67,10],
    "salary":[200,400,500,700]
}
df=pd.DataFrame(data)
print(df)

# on a single column
# df.sort_values(by='age',ascending=True,inplace=True)
# print("sorted age by descending order")
# print(df)

# on multiple column
# df.sort_values(by=["age","salary"],ascending=True,inplace=True)
df.sort_values(by=['age','salary'],ascending=[True,False],inplace=True)
print(df)



# AGGREGATION-->.mean(),.max(),.min(),.std()etc..
# df["column name"].sum()
max_age=df['age'].max()
print(max_age)