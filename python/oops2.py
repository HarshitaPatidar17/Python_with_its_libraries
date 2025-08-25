# class student:
#     def __init__(self,name):
#         self.name=name


# s1=student("shyama")
# print(s1.name)
# del s1.name
# print(s1.name)

# INHERITANCE IN PYTHON

# single inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stop")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name

# car1=toyotacar("fortuner")
# car2=toyotacar("prius")

# print(car1.start())

# mulrilevel inheritance
# class car:
#     @staticmethod
#     def start():
#         print("started")
    
#     @staticmethod
#     def stop():
#         print("stop")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand



# class fortuner(toyotacar):   
#     def __init__(self,type):
#         self.type=type

# car1=fortuner("diesel")
# car1.start()

# multiple inheritance

# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="welcome to class C"

# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# super method

# class car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("started")
    
#     @staticmethod
#     def stop():
#         print("stop")

# class toyotacar(car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)
#         super().start()

# car1=toyotacar("prius","petrol")
# print(car1.type)


# CLASS METHOD
# class person:
#     name="anonymous"

#     # def changeName(self,name):
#     #     self.__class__.name="rahul"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(person.name)

# PROPERTY
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
        # self.percentage=str((self.phy+self.chem+self.maths)/3)

    # def calcpercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.maths)/3)

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.maths)/3)

# stu1=student(98,98,98)
# print(stu1.percentage)

# stu1.phy=89
# print(stu1.phy)
# # stu1.calcpercentage()
# print(stu1.percentage)


# OPERATOR OVERLOADING
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownumber(self):
#         print(self.real,"i +", self.img,"j")
    
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return complex(newReal,newImg)
# num1=complex(9,5)
# num1.shownumber()

# num2=complex(3,3)
# num2.shownumber()

# num3=num1+num2
# num3.shownumber()



# define circle with area and parameter method for area and parameter calculation.
# class circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius
#     def perimeter(self):
#         return 2*3.13*self.radius
    
# c1=circle(21)
# print(c1.area())
# print(c1.perimeter())


# employee class with attributes role department salary and showdetail method. then make class engineer and inherit it with class employee.
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print("role=",self.role)
#         print("department=",self.department)
#         print("salary=",self.salary)



# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer","IT","750000")

# eng1=Engineer("elon musk",42)
# eng1.showDetails()


# create class called order which stores item and its price
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1=Order("chips",20)
odr2=Order('tea',15)

print(odr1 > odr2)