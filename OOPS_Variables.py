# diff b/w method and constructor

# method name can be any name / Constructor should b alwys __init__()
# method will be executed if we call the method / constructor will executed at the time of object creation
# per obj method can call any num of times / per object constructor will execute only once
# inside method we can write bussiness logic / inside constructor we have to decalre and initilise the instance varible

#types of variabes
# instance ,class varibles(class varibles)
#instance :  if the value of varible
# If the value of a variable is varied from object to object, then such type of variables are called
# instance variables.
# For every object a separate copy of instance variables will be created.

# here we can declare Instance variables:
# 1. Inside Constructor by using self variable
# 2. Inside Instance Method by using self variable
# 3. Outside of the class by using object reference variable

# #Ex :
# class A:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def python(self):
#         self.c=300
# obj=A()
# obj.x=400
# print(obj.__dict__)
# obj.python()
# print(obj.__dict__)


# How to access instance varible
# we can access instance variables with in the class by using self variable and outside of the class by
# using object reference.

class A:
    def __init__(self):
        self.a=10
        self.b=20
    def python(self):
        self.c=300
        print(self.a)
        print(self.b)
        print(self.c)
# obj=A()
# obj.x=400
# obj.python()
# print(obj.a,obj.b,obj.c,obj.x)

# static varible

# if the value of a variable is not varied from object to object, such type of variables we have to
# declare with in the class directly but outside of methods. Such type of variables are called Static
# variables.
# For total class only one copy of static variable will be created and shared by all objects of that
# class.
# We can access static variables either by class name or by object reference. But recommended to
# use class name.
# object not reuired to access static varibles if sttic varible exits in init or instance method then obj required

# Various places to declare static variables:
# 1. In general we can declare within the class directly but from out side of any method
# 2. Inside constructor by using class name
# 3. Inside instance method by using class name
# 4. Inside classmethod by using either class name or cls variable
# 5. Inside static method by using class name
# class Test:
#     a=10
#     # def __init__(self):
#     #     Test.b=20
#     # def m1(self):
#     #     Test.c=30
#     @classmethod
#     def m2(cls):
#         cls.d1=40
#         Test.d2=400
#     @staticmethod
#     def m3():
#         Test.e=50
#         print(Test.a)
# # t=Test()
# # t.m1()
# Test.m2()
# Test.m3()
# Test.f=60
# print(Test.__dict__)

#How to access
#
# 1. inside constructor: by using either self or classname
# 2. inside instance method: by using either self or classname
# 3. inside class method: by using either cls variable or classname
# 4. inside static method: by using classname
# 5. From outside of class: by using either object reference or classnmae

# class Test:
#     a=10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m1(self):
#         print(self.a)
#         print(Test.a)
#     @classmethod
#     def m2(cls):
#         print(cls.a)
#         print(Test.a)
#     @staticmethod
#     def m3():
#         print(Test.a)
# t=Test()
# print(Test.a)
# print(t.a)
# t.m1()
# t.m2()
# t.m3()

#local varibles :
# the variabes which are declared inside the method is called local varible.
# local varibles will b created at the time of method executioin
#local variables cant access outside of the method

# if there is no init method then by default init method will b created internaly
# class A:
#     def Python(self):
#         a=1000 # a,b r local
#         b=2000
#         print(a,b)
#     def java(self):
#         c=200
#         print(c)
# obj=A()
# obj.Python()
# obj.java()

# types of methods
# instance method ,class,static

#instance method
# Inside method implementation if we are using instance variables then such type of methods are
# called instance methods.
# Inside instance method declaration,we have to pass self variable.
#  def m1(self):
# By using self variable inside method we can able to access instance variables.
# Within the class we can call instance method by using self variable and from outside of the class
# we can call by using object reference.
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b




# class method
# inside method implementation if we are using only class variables (static variables), then such type
# of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.
# For class method we should provide cls variable at the time of declaration
# we can call class method using classnme or object reference
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))

# count the no of objects creted for class
class T:
    count=0
    def __init__(self):
        T.count=T.count+1
    @classmethod
    def obj_count(cls):
        print("The num of objects creted :",cls.count)


if __name__=='__main__':
    # obj=A(10,20)
    # x=obj.add()
    # print("ADDTION",x)
    # y=obj.mul()
    # print("MUL",y)
    obj1=T()
    obj2=T()
    T.obj_count()

    # Animal.walk('Dog')
    # Animal.walk('cat')


















