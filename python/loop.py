# print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# print multiplication table of number n
# i=1
# num=int(input("enter the num:"))
# while i<=10:
#     print(i*num)
#     i+=1


# print the list using loop
# list=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(list):
#     print(list[idx])
#     idx+=1

# search element in a tuple
# tuple=(1,4,9,16,25,36,49,64,81,100)
# num=36
# idx=0

# while idx<len(tuple):
#     if(tuple[idx]==num):
#         print(idx)
#     idx+=1

# # brak and continue
# i=1
# while i<=10:
#     print(i)
#     if(i==4):
#         break
#     i+=1

# i=0
# while i<=5:
#     if(i==4):
#         i+=1
#         continue
#     print(i)
#     i+=1


# for loop

# list=[1,4,5,8,9]
# for char in list:
#     print(char)
# else:
#     print("end loop")

# print the list using loop
# list=[1,4,9,16,25,36,49,64,81,100]
# for ele in list:
#     print(ele)

    
# search element in a list
# list=[1,4,9,16,25,36,49,64,81,100]
# num=36
# idx=0
# for ele in list:
#     if(ele==num):
#         print(idx)
#     idx+=1
    

# num=range(5)
# for i in range(0,5,1):
#     print(num[i])

# num=range(10)
# for i in range(2,10,3):
#     print(i)

# print numbers from 1 to 100
# for i in range(0,101,1):
#     print(i)

# print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

# multiplication table of number n
# num=int(input("enter num:"))
# for i in range(1,11):
#     print(num*i)


# find sum of first n numbers using while
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
    
#     print(sum)
 
# n=7
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
#     print(sum)


# find factorial on number n
# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
#     print("factorial:",fact)


n=5
fact=1
for i in range(1,n+1):
    fact*=i
    print("factorial=",fact)