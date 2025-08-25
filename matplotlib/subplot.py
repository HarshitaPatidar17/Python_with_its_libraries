#BY SUBPLOT() FUNCTION

# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[10,20,15,25]
# plt.subplot(1,2,1)  #1row,2column,1st subplot
# plt.plot(x,y)
# plt.title("line chart")


# plt.subplot(1,2,2)  #1row.2column,2nd subplot
# plt.bar(x,y)
# plt.title("bar chart")


# plt.tight_layout()
# plt.show()


#BY OBJECT ORIENTED APPROACH
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(10,5))
x=[1,2,3,4]
y=[10,20,15,25]
ax[0].plot(x,y,color='blue')
ax[0].set_title('line plot')

ax[1].bar(x,y,color='green')
ax[1].set_title('bar chart')

fig.suptitle("comparison of line and bar chart")
plt.tight_layout()
plt.show()