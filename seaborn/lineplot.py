import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# x=[1,2,3,4,5,6,7]
# y=[20,30,40,50,60,30,45]

# df=pd.DataFrame({"days":x,"number of people":y})

# print(df.head(7))

# sns.lineplot(x="days",y="number of people",data=df)
# plt.show()

df=sns.load_dataset("tips")#a datset from github
print(df.head())
sns.lineplot(x="day",y="total_bill",data=df,hue="sex",style="time",palette="flare")
plt.show()