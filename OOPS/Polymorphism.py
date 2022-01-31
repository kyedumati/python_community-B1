# an Entity which represents in multipe forms is called polymorohism
# Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one type of
# behaviour and with friends another type of behaviour.Same person but different behaviours at
# different places,which is nothing but polymorphism.
# Eg2: + operator acts as concatenation and arithmetic addition     # +
# print(1+2)       #3
# print('A'+'B')    #AB
# print(1*2)      #2
# print("A"*2)
# Eg3: * operator acts as multiplication and repetition operator
# Eg4: The Same method with different implementations in Parent class and child
# classes.(overriding)
# Related to polymorphism the following 4 topics are important

# . Duck Typing Philosophy of Python
# 2. Overloading
#  1. Operator Overloading
#  2. Method Overloading
#  3. Constructor Overloading
# 3. Overriding
#  1. Method overriding
#  2. constructor overriding
#Duck Typing Philosophy of Python
# Fun name is same but actions are different
# The problem in this approach is if obj does not contain talk() method then we will get
# AttributeError
class Duck:
    def talk(self):
        print('Quack.. Quack..')
class Dog:
    def talk(self):
        print('Bow Bow..')
class Cat:
    def talk(self):
        print('Moew Moew ..')
class Goat:
    def talk(self):
        print('Myaah Myaah ..')

# def f1(obj):
#     obj.talk()
# l=[Duck(),Cat(),Dog(),Goat()]   # 0->Duck Cat ->1 DOg->2  Goat -3
# for obj in l:
#     f1(obj)
#we can solve this problem by using hasattr() function
class Duck:
    def talk(self):
        print('Quack.. Quack..')
class Human:
    def talk(self):
        print('Hello Hi...')
class Dog:
    def bark(self):
        print('Bow Bow..')
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
# d=Duck()
# f1(d)
# h=Human()
# f1(h)
# d=Dog()
# f1(d)

# There are 3 types of overloading
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading


# ope overloding

# We can use the same operator for multiple purposes, which is nothing but operator overloading.
# Python supports operator overloading.
# Eg1: + operator can be used for Arithmetic addition and String concatenation
#  print(10+20)#30
#  print('durga'+'soft')#durgasoft
# Eg2: * operator can be used for multiplication and string repetition purposes.
#  print(10*20)#200
#  print('durga'*3)#durgadurgadurga


# '+' ope loading

class Book:
    def __init__(self,pages):
        self.pages=pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
#
# For every operator Magic Methods are available. To overload any operator we have to override
# that Method in our class.
# Internally + operator is implemented by using __add__() method.This method is called magic
# method for + operator. We have to override this method in our class.

class Book:
    def __init__(self,pages):
        self.pages=pages
        print(self.pages)
    def __add__(self,other):       # magic method
        print(self.pages)
        print(other.pages)
        return self.pages+other.pages
    def __mul__(self, other):
        return self.pages * other.pages
# b1=Book(100)       #pages=100
# b2=Book(200)       # pages=20
# print('The Total Number of Pages:',b1*b2)
# print('The Total Number of Pages:',b1+b2)


# methood over loading

#Method Overloading:
# If 2 methods having same name but different type of arguments then those methods are said to
# be overloaded methods.
# Eg: m1(int a)
#  m1(double d)
# But in Python Method overloading is not possible.
# If we are trying to declare multiple methods with same name and different number of arguments
# then Python will always consider only last method.
# Demo Program:
class Test:

    def m1(self):
        print('no-arg method')
    def m1(self,a):       #m1(self,a=None)
        print('one-arg method')
    def m1(self,a,b):     #m1(self,a=None,b=None)
        print('two-arg method')
t=Test()
# # t.m1()
# t.m1(10)
#t.m1(10,20)

#Most of the times, if method with variable number of arguments required then we can handle
#with default arguments or variable len args

class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!= None and c!= None:
            print('The Sum of 3 Numbers:',a+b+c)
        elif a!=None and b!= None:
            print('The Sum of 2 Numbers:',a+b)
        elif a!=None:
            print("A",a)
        else:
            print('Please provide 2 or 3 arguments')
# t=Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10)

# # t.m1()
# t.m1(10)
#t.m1(10,20)

class Test:
    def sum(self,*a):     # it  will return tuple
        total=0
        for x in a:
            total=total+x
        print('The Sum:',total)
# t=Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10)
# t.sum()

#  Constructor Overloading:
# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.
class Test:
    def __init__(self):
        print('No-Arg Constructor')
    def __init__(self,a):
        print('One-Arg constructor')
    def __init__(self,a,b):
        print('Two-Arg constructor')
#t1=Test(10,20)

# t1=Test(10)
# t1=Test(10,20)

#constructor with Default Arguments:
class T:
    def __init__(self,a=None,b=None,c=None,d=None):
        print('Constructor with 0|1|2|3 number of arguments')
# t1=T()
# t2=T(10)
# t3=T(10,20)
# t4=T(10,20,30)

#Constructor with Variable Number of Arguments:
class T1:
    def __init__(self,*a):
        print('Constructor with variable number of arguments')

# t1=T1()
# t2=T1(10)
# t3=T1(10,20)
# t4=T1(10,20,30)
# t5=T1(10,20,30,40,50,60)

# Method overriding:
# What ever members available in the parent class are bydefault available to the child class through
# inheritance. If the child class not satisfied with parent class implementation then child class is
# allowed to redefine that method in the child class based on its requirement. This concept is called
# overriding.
# Overriding concept applicable for both methods and constructors.
class P:
    def property(self):
        print('GOLD')
    def marry(self):
        print('SAI PALLAVI')
class C(P):
    def marry(self):      # Super().marry()
        print('ANUPAMA')
        super().marry()
# c=C()
# c.property()
# c.marry()
# From Overriding method of child class,we can call parent class method also by using super() 
# method.

class P:
    def property(self):
        print('GOLD')
    def marry(self):
        print('SAI PALLAVI')
class C(P):
    def marry(self):      # Super().marry()
        print('ANUPAMA')
        super().marry()
# c=C()
# c.property()
# c.marry()


#constructor overriding

class P:
    def __init__(self):
        print('Parent Constructor')
class C(P):
    def __init__(self):
        print('Child Constructor')
        super().__init__()       #calling parent class constr
c=C()





