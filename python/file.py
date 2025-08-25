# open and read a file

# f=open("demo.txt","r")
# # data=f.read()
# # print(data)
# # print(type(data))
# # data=f.read(5)
# # print(data)
# data=f.readline()
# print(data)
# f.close()


# open and write a file

# f=open("demo1.txt","a")
# f.write("this is new content")
# f.write("this will add at th end")
# f.write("\n new")
# f.close()


# reading and writing at same time "r+"
# f=open("demo.txt","r+")
# f.write("abcccc")
# print(f.read())
# f.close()



# reading and writing at same time "w+"
# f=open("demo.txt","w+")
# f.write("abcccc")
# print(f.read())
# f.close()



# reading and writing at same time "a+"
# f=open("demo.txt","a+")
# # f.write("abcccc")
# print(f.read())
# f.write("abcccc")
# f.close()

# file operation with with syntax
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")


# deleting a file in python
# import os
# os.remove("demo1.txt")


# create a new file "practice.txt" usng python .add the following dta in it:
# hi everyone
# we are learing filw I/O
# using python
# i like programming in python
# with open("practice.txt","a") as f:
#     f.write("hi everyone")
#     f.write("\n we are learning file I/O \n using python \n i like programming in python")


# replace all occurance of python with pandas
# with open("practice.txt","r") as f:
#     data=f.read()

# new_data=data.replace("python","pandas")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# searching of a word in a file, exist or not
# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word) != -1 ):
#         print("found")
#     else:
#         print("not found")


# by help of function
# def check():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word) != -1 ):
#             print("found")
#         else:
#             print("not found")
# check()





# find in which line of file "learning" occur first. print -1 if word not found
# def check_line():
#     word="learning"
#     data=True
#     line_num = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
        
#             if(word in data):
#                 print(line_num)
#                 return
#             line_num +=1
#         # else:
#         #     print(-1)
#     return -1
# print(check_line())

# print count of even number from a file
count=0
with open("practice.txt","r") as f:
    data=f.read()
    # print(data)

    nums= data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)