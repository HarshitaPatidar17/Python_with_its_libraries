# class student:
#     name="ram gopal"
#     age=12
#     def __init__(self,fullname):
#         self.name=fullname
#         # print(self) self is first parameter and it is object
#         print("adding students")

# s1=student("karan")
# print(s1.name)
# # print(s1.age)
# # print(s1)


# class student:
#     college = "apna college"
#     name="faltu he"   #class ke attributes he
#     def __init__(self,fullname,marks):
#         self.name=fullname  #object ke attributes and obj atr > class atr
#         self.marks=marks
#         print("adding students")

# s1=student("ram",12)
# print(s1.name,s1.marks)
# print(student.college)



# class methods
# class student:
#     college = "apna college"
#     name="faltu he"   #class ke attributes he
#     def __init__(self,fullname,marks):
#         self.name=fullname  #object ke attributes and obj atr > class atr
        # self.marks=marks
    
#     def welcome(self):
#         print("welcome students",self.name,self.marks)


#     def getmarks(self):
#         return self.marks
        
# s1=student("ram",12)
# # print(s1.name,s1.marks)
# s1.welcome()
# print(s1.getmarks())



# Q= create student class that takes name and marks of 3 subjects as constructor then create a method to print the average.
# class students:
    
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum +=val
#         print(self.name,"average is:",sum/3)

# s1=students("ram",[68,79,89])    
# s1.average()

# s1.name="gopal"  #can also change or manipulate the name of student#
# s1.average()




#static methods
# class student:
#     def __init__(self,name):
#         self.name=name

#     @staticmethod
#     def hello():
#         print("hello")

# s1=student("shyam")
# print(s1.name)
# s1.hello()

#create Account class with 2 Attributes-balance and account number.create methods for debit,credit and printing the balance.
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_num = acc
        

        # debit method
    def debit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was debited")
        print("total balance= ",self.get_balance())

            # credit method
    def credit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was credited")
        print("total balance= ",self.get_balance())

    def get_balance(self):
            return self.balance
        

acc1=Account(1000000,12345)
print(acc1.balance)
print(acc1.account_num)
acc1.debit(1000)
acc1.credit(500)

with open("oops2.py","w") as f:
     f.write("hello")