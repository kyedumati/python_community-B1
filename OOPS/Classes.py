# oops -> object oriented programming system

# class -> collection of objects and methods n varibales

#syntax: "class keyword ,"Class name " :

class A:
    pass

# object -> object is blueprint of class
#Syntx : object name=A()
# we can create any num of objects to the class
# obj=A()
#
#
# #Ex:
#
#
# def add():
#     print("addtion")


# class B:
#     def python(self):
#         print("Python")
#     def java(self):
#         print("Java")
# obj1=B()
# obj1.python()
# obj1.java()

class B:
    # def __init__(self):
    #     print("object is created")
    def python(self):   #if there is a self in method u must call with obj ref
        print("Python")
obj1=B()
#obj1.python()
B.python(obj1)

# create






#self  -> self is a deult variable  methods in the class in which is always pointing to the current object
# using self we can access instance methods and varibles



#__int__(self)
#init method will call whenever u create object
#init method used fro intilise the varibles
# init mthod called as constructor
#using init method we can find how many objects r creted for the class
# init method dose not have return type
# atle

class B:
    def __init__(self,a,b):
        print("object is created")
        self.a=a
        self.b=b
        print("a val",self.a)
        print("b vl",self.b)
    def add(self):
       print("add",self.a+self.b)
    def mul(self):
        print("mul",self.a*self.b)
#
# obj1=B(10,20)
# obj1.add()
# obj1.mul()
# B.mul(obj1)

# create a class  which is having one init method and two objsts

# create a class  which is having one init method and intilise two variables and create instnce method (add) sum of two num




















