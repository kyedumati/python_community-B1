#classes inside classes called inner classes
#inner classes : class defind inside the another class
class A:
    def __init__(self):
        print("outer class object created")
    def python(self):
        print("Outer class Python fun ")
    def C(self):
        print("C lan")
    class B:
        def __init__(self):
            print("inner class object created")
        def java(self):
            print("inner class fun")
        def Python(self):
            print("inner classs python")
# obj=A()
# obj.python()
# obj1=obj.B()
# obj1.java()
# obj.C()
# obj1.Python()

# destructor : destructor is a special method and name should be __del__
# just before destroying an object garbage collector always calls destructor to perform clean up activities
# once destructor execution completed then garbage collector automtically destroys that object
import time
class Test:
    def __init__(self):
        print("object created")
    def __del__(self):
         print("fulfilling last wish and performing clean up activities")
# t1=Test()
# t1=None
# time.sleep(5)
# print("End of application")

#import time
class Test:
    def __init__(self):
        print("object created")
        #self.__del__()
    def __del__(self):
        print("fulfilling last wish and performing clean up activities")
# class Test1:
#     def __init__(self):
#         print(" Test1 object created")
#         #self.__del__()
#     def __del__(self):
#         print("Test1 clean up activities")

# t1=[Test(),Test()]
# print(t1)      # obj add
# t1=None
# print(t1)
#time.sleep(5)
#print("End of application")


# class A:
#     def __init__(self):
#         print("object created")
#     def __del__(self):
#         print("Destroy mem")
# x=[A(),A()]
# print(x)


# By HAS -A Relationship
# By Inheritance (IS A Relationship) # it is like a single inheritance

# HAS -A Relationship
# By using Class Name or by creating object we can access members of one class inside another class
# is nothing but composition (Has-A Relationship).
# The main advantage of Has-A Relationship is Code Reusability.


class Bus:
    def __init__(self):
        print("Bus init")
    def bus_fun(self):
        print("Bus Function")


class Auto():
    def __init__(self):
        self.busobj = Bus()
    def python(self):
        print("classs Auto method")
        self.busobj.bus_fun()

# objauto=Auto()
# objauto.python()

class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('Engine Specific Functionality')
class Car():
    def __init__(self):
        self.engine=Engine()     # creting object for class Engine
    def m2(self):
        print('Car using Engine Class Functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
# c=Car()
# c.m2()







class X:

    def python(self):
        print("Class x python")
class B(X):
    def java(self):
        print("Class B java")

# obj=B()
# obj.python()

#Is -  A relationship
# What ever variables, methods and constructors available in the parent class by default available to
# the child classes and we are not required to rewrite. Hence the main advantage of inheritance is
# Code Reusability and we can extend existing functionality with some more extra functionality.

class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    pass
# c=C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()


# Ass1 create class to find vowels in a given  string.
# String : "ABcedgEioggDDDFfefUxu"   -> list the all the vowels in string
# ['A','e','i','o','u','a','E','I','U']

# Create a class to find the no of words in a string   "PYTHON IS gOOD"  return string  like change the convert
# lower to upper or upper to lower and return the string
# op :pYTHON iS GOOD    no of words :3

#return count ,str

#Ass3 Create a innner class call inner class methods from outer class


#9) Write a program to delete a desired character in a given string.





#inheritance : aquiring the properties of one class to another class is called inheritnce
# Single,multilevel, hierarchical ,Multiple ,hybrid Inherutance

#Singe inheritance : inherting the properties of one class to another class is called single inheritance
class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
# c=C()
# c.m1()
# c.m2()

# multilevel inheritance :
# The concept of inheriting the properties from multiple classes to single class with the concept of
# one after another is known as multilevel inheritance
class A:
    def m1(self):
        print("Parent Method")
class B(A):     # m1 and m2
    def m2(self):
        print("Child Method")
class C(B):     # m1 m2 m3
    def m3(self):
        print("sub child method")

# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

#Hierarchical Inheritance:
# The concept of inheriting properties from one class into multiple classes which are present at
# same level is known as Hierarchical Inheritance

class P:
    def m1(self):
        print("class P Parent Method")
class C1(P):   # m1 m2
    def m2(self):
        print("CLASS C1 Child1 Method")
class C2(P):  # m1 ,m3
    def m3(self):
        print("CLASS C2 Child2 Method")
# c1=C1()
# c1.m1()
# c1.m2()
# c2=C2()
# c2.m1()
# c2.m3()
# obj=P()
# obj.m1()

#multiple inheritance
# the concept of inheriting the properties from multiple classes into a single class at a time, is
# known as multiple inheritance.

class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P1,P2):    # m1,m2,m3
    def m3(self):
        print("Child2 Method")
# c=C()
# c.m1()
# c.m2()
# c.m3()

# Hybrid inheritance
# the combination of single ,multible ,multilevel and hierarchical inheritance called hybrid
# combination of more than one inheritance is called hybrid

class A:
    def python(self):
        print("Class A phython")
class B(A):
    def JAVA(self):
        print("Class B JAVA")

class C(B,A):      # singe + multible
    def data(self):
        print("C Class data.....")
obj=C()
obj.python()
obj.JAVA()
obj.data()
#
# obj1=B()
# obj1.python()
# obj1.JAVA()











