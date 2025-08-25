import pandas as pd

df_customers=pd.DataFrame({
    'customerID':[1,2,3],
    'name':['ramesh','suresh','animesh']
})

df_order=pd.DataFrame({
    'customerID':[1,2,4],
    'orderAmount':[234,453,456]

})

#merge
df_merged=pd.merge(df_customers,df_order,on="customerID",how="inner")
print(df_merged)

# inner,outer,left,right,cross they are joins