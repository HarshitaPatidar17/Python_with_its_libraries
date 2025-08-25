import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("tips")
print(df.head())
sns.countplot(x="sex",data=df,hue="smoker")
plt.show()