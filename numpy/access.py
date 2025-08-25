import numpy as np

#array[index]  for 1d array
#array[row,column] for 2d array

arr=np.array([21,34,56])
print(arr[2])

arr=np.array([[1,3,6],[5,7,9]])
print(arr[0,1])


# SLICING
#array[start:stop:step]
# arr[start:end]  ,start to end-1
# negative step,   -1 reverse
  
arr=np.array([10,20,30,40,50,60])
print(arr[1:5])  #index 1 to 4
print(arr[:4])  #index 0 to 3
print(arr[::2]) #every second element
print(arr[::-1])



#FANCY INDEXING OR FANCY SLICING
arr=np.array([10,20,30,40,50,60])
print(arr[[0,2,4]])

# BOOLEAN MASKING OR FILTERING
arr=np.array([10,20,30,40,50,60])
print(arr[arr>25])

# RESHAPE
#reshape(rows,columns) specify new shape and can only done if dimension match
arr=np.array([10,20,30,40,50,60])
reshape_arr=arr.reshape(3,2)
print(reshape_arr)



#FLATTENING ARRAY --> used to convert md array in 1D
# .reval()-->it returns views (affect original data)
# .flatten()-->it returns copy (not affect original array)
arr_2d=np.array([[10,20,30],[20,30,40]])
print(arr_2d.ravel())
print(arr_2d.flatten())
