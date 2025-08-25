# vertically->row wise
# horizontally->column wise

# pd.concat([df1,df2],axis=0,ignore_index=True)


import pandas as pd
# VERTICALLY
df_region1=pd.DataFrame({
    'customerID':[1,2],
    'name':['gopal','shyam']
})
df_region2=pd.DataFrame({
    "customerID":[3,4],
    "name":["babu","sona"]
})

df_concate=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concate)