import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]

#create plot
plt.plot(x,y,color='blue',marker='o')
plt.title('simple line plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('matplotlib/line_plot.png',dpi=300,bbox_inches='tight')
plt.show()  #it is optional if want to see then use it otherwise only save it by savefig()function





