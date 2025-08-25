import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset("tips")
print(df.head())
sns.histplot(x="total_bill",data=df,discrete=False,hue="sex",palette="spring",kde=True,edgecolor="red",linestyle="dashed")
plt.show()