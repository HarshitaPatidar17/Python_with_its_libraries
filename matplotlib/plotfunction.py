import matplotlib.pyplot as plt
month=[1,2,3,4]
sales=[100,200,50,400]
plt.plot(month,sales,color='blue',linestyle='dashed',linewidth=2,marker='o',label='2025 sales data')
plt.xlabel("months")
plt.ylabel("sales")
plt.title("monthly sales data report")
plt.legend(loc="lower right",fontsize=12)
plt.grid(color='red',linestyle=":",linewidth=1)
plt.xlim(1,4)
plt.ylim(0,100)
plt.xticks([1,2,3,4],['month1','month2','month3','month4'])
plt.show()
