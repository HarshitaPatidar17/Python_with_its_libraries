import numpy as np
#np.insert(array,index,value,axis=none)
#array=original array
# index-
# value-
# axis-
# axis=0,row-wise
# 1 column wise

# INSERT IN 1D
arr=np.array([1,2,3,4,5,6,7,8,9,0])
new_arr=np.insert(arr,2,10,axis=0)
print(new_arr)

# INSERT IN 2D
arr_2d=np.array([[1,2,3,4,5],[1,4,6,8,9]])
new_arr_2d = np.insert(arr_2d,1,[5,6,7,9,0],axis=0)
print(new_arr_2d)
# if axis=none then matrix is in one line

# APPEND--> ADD ELEMENT AT THE END OF ARRAY
arr=np.array([1,2,3,4])
new_arr=np.append(arr,[4,5,6,9])
print(new_arr)

# CONVATENATE-->ADD TWO ARRAY
arr_1=np.array([1,2,3,4,5,6,7,8,9,0])
arr_2=np.array([1,2,3,4,5,6,7,8,9,0])
add=np.concatenate((arr_1,arr_2),axis=0)
print(add)

# REMOVE ELEMENT
arr_1=np.array([1,2,3,4,5,6,7,8,9,0])
new=np.delete(arr_1,2,axis=None)
print(new)

# DELETE ELEMENT OF 2D ARRAY
arr_2d=np.array([[1,2,3,4,5],[1,4,6,8,9]])
new=np.delete(arr_2d,1,axis=0)
print(new)

# STACKING AND SPILITING
# VERTICALLY-->vstack()  row wise
# HORIZONTALLY-->hstack() column wise

arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
print(np.vstack((arr1,arr2)))#vertically stack
print(np.hstack((arr1,arr2)))#horizontally stack

# VERTICALLY-->vsplit()  row wise
# HORIZONTALLY-->hsplit() column wise
# EQUAl-->np.split()
arr1=np.array([1,2,3,4])
split=np.split(arr1,2)
print(split)
print(np.hsplit(arr1,2))
