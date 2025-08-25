import numpy as np


arr_1d=np.array([1,2,3,4,5])
print("1D Array: ",arr_1d)

arr_2d=np.array([[1,2,3],[4,5,6]])
print("2D array:",arr_2d)


# NUMPY VS ARRAY
py_list=[1,2,3]
print("multiplication of list: ",py_list*2)


np_array=np.array([1,2,3])
print("multiplication of array: ",np_array*2)  #element wise multiplication

import time
start=time.time()
py_list=[i*2 for i in range(100000)]
print("list opearation time:",time.time()-start)

start=time.time()
np_array=np.arange(100000)*2
print("numpy operation time: ",time.time()-start)


# CREATION OF ARRAY WITH DEFAULT VALUES-zero
# np.zeros(shape)  (3)for 1D (3,3)for 2D

zeroes_array=np.zeros(3)
print(zeroes_array)

zeroes_array=np.zeros((3,3))
print(zeroes_array)


# CREATION OF ARRAY WITH DEFAULT VALUES-one
ones_array=np.ones((2,3))
print(ones_array)

# CREATION OF ARRAY WITH FULL FUNCTION
filled_array=np.full((2,2),7)
print(filled_array)

# NUMPY ARRAY WITH ARANGE FUNCTION
arr= np.arange(1,10,2)
print(arr)


# CREATING IDENTITY MATRIX
identity_matrix=np.eye(4)
print(identity_matrix)