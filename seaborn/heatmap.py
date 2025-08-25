import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
data=np.random.randint(low=1,high=100,size=(10,10))
print(data)

sns.heatmap(data=data,cmap="GnBu",alpha=0.5,linecolor="yellow",linewidth=2,annot=True,cbar=False,xticklabels=False,yticklabels=False)
plt.show()