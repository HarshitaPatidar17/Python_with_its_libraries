import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=sns.load_dataset("titanic")
print(df.head())

sns.barplot(x='who',y='fare',data=df,hue='sex',palette="spring",saturation=0.2)
plt.show()