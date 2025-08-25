import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("exercise")
print(df.head())
sns.scatterplot(x="time",y="pulse",data=df,hue="kind",palette="GnBu",size="diet",marker="s")
plt.show()