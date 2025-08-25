import numpy as np
prices=np.array([100,200,300])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)

# broadcasting can be done by three ways
# 1.matching dimensions
arr=np.array([100,200,300])
result=arr*2
print(result)

# 2.expanding single element
# 1_d to 2_d array
vector=np.array([100,200,300])
matrix=np.array([[1,2,3],[4,5,6]])
result=vector+matrix
print(result)

# 3.incompatible shapes
arr1=np.array([22,33,44],[21,65,89])
arr2=np.array([21,32,45])
result=arr1+arr2
print(result)

