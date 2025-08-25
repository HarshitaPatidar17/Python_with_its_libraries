
import pandas as pd
data={
    "name":['arun', 'sita','karan','radha','karun'],
    "age":[34,54,67,10,12],
    "salary":[200,400,500,700,320]
}
df=pd.DataFrame(data)
print(df)


#on a single column
# grouped=df.groupby("age")['salary'].sum()
# print(grouped)

#multiple column
grouped=df.groupby(["age","name"])['salary'].sum()
print(grouped)