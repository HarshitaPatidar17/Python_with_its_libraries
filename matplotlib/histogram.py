import matplotlib.pyplot as plt
scores=[45,67,89,78,99,92,68,75,82,90,85,70,73,66,77]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel("score range")
plt.ylabel("number of students")
plt.title("distribution of student marks")
plt.show()