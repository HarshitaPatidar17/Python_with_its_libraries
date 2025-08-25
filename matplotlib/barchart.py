import matplotlib.pyplot as plt
product=['A','B','C',"D"]
sales=[1500,1000,800,1200]
plt.bar(product,sales,color="red",label="sales 2025")
plt.xlabel("product")
plt.ylabel("sales")
plt.title("product sale comparison is")
plt.legend()
plt.show()