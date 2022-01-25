# def fun(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# t=fun(10,20)
# print(type(t))
# for i in t:
#     print(i,end=" ")

import math as m

#Functions:
#function is a set of instructuons or group of lines in a single unit

# two types

# in built fun #type() ,id() input() max(),min(),sub()  the fun which are comes inbuilt lib
# user defined Fun  -> user can define his own functions based on his req
#Syntx:

# def python():
#     print("SARITHA COME TO PYTHON WORLD")
# python()
#
#
# def add(x,y):   # forml args
#     print(x+y)
# add(10,20)     # the args which are passing while clling actual args







#def Functionnamr(arg1 ,agr2,arg3....):
#
# #int funname(agr) {} # args are optional

#mostly we are two keywords in functions

#def ,return

#return -> to return the value from function  # return also optional


#calling should 
# def hello():
#     print("hello python")
#     print("python is good")
# hello()

#paraenters or args 

#  n forma args -> args in function

# actual   -> args in calling fun

# def add(a,b):     # a,b r formal arg
#     return a+b
#
# c=add(10,20) # 10,20 actual args   usually used
# print(c)
#print(add(10,20))

#advntage of fun is reusuability


# def check_even(a):
#     if a%2==0:
#         print("%d is even" %a)
#     else:
#        print("%d is odd" %a)
#
# check_even(6)
# check_even(3)
# check_even(2)

#WAP TO PRINT ALL EVEN FROM LIST
# x=list(range(1,11))
# for i in x:
#     check_even(i)

# print(m.factorial(4)) #i*2*3*4=24


# def fact(a): #4
#     f=1
#     for i in range(1,a+1):   #3 (1,4)
#         f=f*i                #f=1  i=1                                                  # f=1  f=2    f=2                             #f=2   i=3    f=6
#     return f
# x=fact(4)
# print("FACT :",x)
# x=int(input("Enter num :"))
# z=fact(x)
# print(" %d fact is %d " %(x,z))
#Ass1 : print the fctorial of all even numbers from list [1,00]
#we can return num of values from fun in python

#return the mutibe valus from fun

# def add_mul(a,b):
#     x=a+b
#     y=a*b
#     return x,y
# a=add_mul(10,2)    # suppose u reyturn multible values from fun while calling if u wnt to result in single arg fun wil return tuple
# print(type(a))
# print(a)
# for i in a:
#     print(i)

#positional args

# def add(a,b):
#     print("a val is %d" %a)
#     print("b val is %d" %b)
# add(5,10)

#keyword args  # passing args with keyword

# def add(a,b):
#     print("a val is %d" %a)
#     print("b val is %d" %b)
# add(a=100,b=200)

# Defaut args -> the argment which is assigned with None
# default args shoulb b always riht side in fun def
# we can use none for defalut arg

# def add(a,b=None):
#     print(a)
#     print(b)
# add(100)

# variable len args  if we want to pass num of ele from fun we can foe variable len rgs

# def add(*a):  # variabe shoulb *
#    # z=set(a)
#     z = list(a)
#     z = [i * i for i in z]
#     return z,sum(z)
# x,y=add(1,2,3,4,5,1,2,3)
# print("x val :",x)
# print("y val :",y)

#Ass1 : print palindrom strings from strings from list

x=["madam",'Amma','Python']   #op :['madam','amma']   op:2['MaDam','AmMa']

def palindrom(a):
    print(a)
    a=list(a)
    print(a)
    a.reverse()
    print(a)
    x="".join(a)
    print(x)
    return x
y="amma"
#z=palindrom(y)
# if y==z:
#     print("Palindrom")
# else:
#     print("Not Palindrom")






# Ass2 define a with varaiabe len args and return the square and sum of num [two args should be return]

# def add(*a):   # use concept return multibe values from
#     return a
# z=add(1,2,3,6,4,5,3,2)     #op is [1,4,9,16,25,36] sum is 91

#ass3    #hint -> convert to str  -> str -> list -> list.rev  -> join(ist) -> typecsting
# reverse a num      123 #op is 321  # input shoub be integer

# ASS4 -> 123 -> 1+8+27 =36

# Ass5 : check string is palindrom or not   [madam,amma,mam]

#keyword varible len

# def python(**a):
#     #print(a)
#     return a
# z=python(b=100,a=200,c='python')
# print(z)
# print(z.keys())
# print(z.values())
# print(z.items())
# print(z.pop('a'))

#inner functions

# function inside the fun is caled inner functons

# we r clling inner fun inside the outer fun

# def python():
#     print("outer fun python")
#     def java():
#         print('JAVa is inner fun')
#         def c():
#             print("C is a language")
#         c()
#     java()
#python()

#Fun aliasing

# def add(a,b):
#     print(a+b)
# #add(10,20)
# sum=add
# print(id(sum))
# print(id(add))
#sum(10,20)


# local and variable

# local -> variable which is defind inside the fun is called local
# the variable which is defind outside the fun is called global
# if local and globl variabe having same name then firt priority is local only
# a=300
# def add():
#     global a
#     a=3500
#     x=a
#     print(x)
#     print(globals()['a'])
#     a = 100
#     print(a)
# add()

#Ananomous fun

# a fun without name is anonmous fun
# lambda i ananmous fun
# lambda dosenot  have return type
# syntax :variblename=lambda argslist : expression
# x=lambda a,b: a+b
# print(x(10,20))

# filter map,reduce
#syntax filter(Fun,list)
#map ,filter,reduce both have same syntx
#filter is used for to filter the values
# filter is ued for to filter the paryticuler ele
#
# x=eval('1+2+3')
# print(x)

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# import functools
# x=[1,2,3,4,5,6]
# # #l1=list(filter(even,x))
# # #print(l1)
# # y=list(filter(lambda a:a%2==0,x))
# # print(y)
# b=2
# y=list(map(lambda a:a*b,x))
# print(y)
# z=(functools.reduce(lambda a,b:a+b,x))
# print(z)











































