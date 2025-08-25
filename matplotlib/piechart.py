import matplotlib.pyplot as plt
regions=['south','north','east','west']
revenue=[2000,3000,1500,1000]
plt.pie(revenue,labels=regions,colors=['gold','blue','red','green'],autopct='%1.1f%%')
plt.title("revenue contibution by region")
plt.show()