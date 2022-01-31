# 1. Abstract Method
# 2. Abstract class
# 3. Interface
# 4. Public,Private and Protected Members
# 5. __str__() method

#
# sometimes we don't know about implementation,still we can declare a method. Such type of
# methods are called abstract methods.i.e abstract method has only declaration but not
# implementation.
# In python we can declare abstract method by using @abstractmethod decorator as follows.
# @abstractmethod
# def m1(self): pass

# class Test:
#     @abstractmethod
#     def m1(self):
#         pass

# @abstractmethod decorator present in abc module. Hence compulsory we should import abc
# module,otherwise we will get error.
# abc==>abstract base class module
# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass


# Abstract class:
# Some times implementation of a class is not complete,such type of partially implementation
# classes are called abstract classes. Every abstract class in Python should be derived from ABC class
# which is present in abc module.
#Case-1:
# from abc import *
# class Test:
#     pass
# t=Test()
# In the above code we can create object for Test class b'z it is concrete class and it does not conatin
# any abstract method.
#Case-2:
# from abc import *
# class Test(ABC):
#     pass
# t=Test()
# In the above code we can create object,even it is derived from ABC class,b'z it does not contain
# any abstract method.
#Case-3:
# from abc import *
# class Test(ABC):
#     @abstractmethod        # it is abc
#     def m1(self):
#         pass
# t=Test()
#Case-4:
from abc import *
class Test():
    @abstractmethod
    def m1(self):
        pass
t=Test()
# We can create object even class contains abstract method b'z we are not extending ABC class.
# Case-5:
# from abc import *
# class Test():
#     @abstractmethod
#     def m1(self):
#         print('Hello')
# t=Test()
# t.m1()
#
# Conclusion: If a class contains atleast one abstract method and if we are extending ABC class then
# instantiation is not possible.
# "abstract class with abstract method instantiation is not possible"
#
# Interfaces In Python:
# In general if an abstract class contains only abstract methods such type of abstract class is
# considered as interface.
#Demo program:
from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass
    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle Database...')
    def disconnect(self):
        print('Disconnecting to Oracle Database...')
class Sybase(DBInterface):
    def connect(self):
        print('Connecting to Sybase Database...')
    def disconnect(self):
        print('Disconnecting to Sybase Database...')

# dbname=input('Enter Database Name:')     # by drfult str
# classname=globals()[dbname]
# x=classname()
# x.connect()
# x.disconnect()

# Note: The inbuilt function globals()[str] converts the string 'str' into a class name and returns the
# classname.

# #Create a File
# with open('Class.txt','w') as f:
#     f.write("Oracle\n")
#     f.write("Sybase")
#     print("File created")
# Reading class name from file

# f=open('Class.txt','r')
# dbname=f.readlines()
# print(dbname)
# for i in dbname:
#     i=i.replace("\n","")
#     classname=globals()[i]
#     x=classname()
#     x.connect()
#     x.disconnect()


# Public, Protected and Private Attributes:
# By default every attribute is public. We can access from anywhere either within the class or from
# outside of the class.
# Eg:
# name="Python"
# Protected attributes can be accessed within the class anywhere but from outside of the class only
# in child classes. We can specify an attribute as protected by prefexing with _ symbol.
# syntax:
# _variablename=value

class python:
    def __init__(self):
        self.a=100       # public
        self._b=200      # protected var can be used in same class or in child class also
        self.__c=300     #  privte we can use with in the class
    def print(self):
        print(self.a)
        print(self._b)
        print(self.__c)
class java(python):
    def java_print(self):
        print(self.a)
        print(self._b)
        #print(self.__c)
# obj=java()
# obj.java_print()
# print(obj.a)
# print(obj._b)


# How to access private variables from outside of the class:
# We cannot access private variables directly from outside of the class.
# But we can access indirectly as follows
# objectreference._classname__variablename
# Eg:
# class Test:
#     def __init__(self):
#         self.__x=10   # private var
# t=Test()
# print(t._Test__x)#10

# Whenever we are printing any object reference internally __str__() method will be called which is
# returns string in the following format
# <__main__.classname object at 0x022144B0>
# To return meaningful string representation we have to override __str__() method.

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return 'This is Student with Name:{} and Rollno:{}'.format(self.name,self.rollno)
s1=Student('RAM',101)
s2=Student('RAJU',102)
print(s1)
print(s2)

x=[1001111000]  # [1111100000]






















