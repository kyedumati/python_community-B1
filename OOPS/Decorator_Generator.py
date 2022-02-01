# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

#__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object

#next ( __next__ in Python 3) The next method returns the next value for the iterable.

# iterable_value = 'Python'
# iterable_obj = iter(iterable_value)
# for i in iterable_value:
#     print(iterable_obj.__next__())
#
# x=[1,2,3,4,5]
# y=iter(x)
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())

# genertors :
#
# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values
#genertor by default having iterator
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
#
# g=mygen()
#
# for i in g:
#     print(i)

# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# def countdown(num):
#     print("Start Countdown")
#     while(num>0):
#         yield num        # 5 4 3 2 1
#         num=num-1
# values=countdown(5)
# for x in values:
#     print(x)

# def countdown(num):
#     numlist=[]
#     print("Start Countdown")
#     while(num>0):
#         #yield num        # 5 4 3 2 1
#         numlist.append(num)
#         num=num-1
#     return numlist
# values=countdown(5)
# for x in values:
#     print(x)


# decorators:
# decorator is a function which can take a function as argument and extend its functionality
# and returns modified function with extended functionality.
# without touching existing functionality adding new feature to the fun is called decortor

# def java():
#     print("JAVA is good")
#     def python():
#         print("python")
#         return
#     return python()
# java()

# def python(fun):    #  fun arg is a function   fun is C()
#     print("Python is good ")
#     def java():
#         print("JAVA")
#         fun()            # C()
#     return java()
# @python       #-> python(C())
# def C():
#     print("C is good lanuage")

# Call_fun=python(C)
# Call_fun()

# def python(fun):    # fun is C()
#     print("Python is good ")
#     fun()
#     def java():
#         print("JAVA")
#         fun()
#     return java()
# def C():
#     print("C is good lanuage")
# python(C)


def python(fun):    # fun is C(name)
    print("Python is good ")
    def java(name):
        print("JAVA",name)
        fun(name)    # atlast it is calling
    return java
@python   # -> python(C(name))
def C(name):
    print(name," is good lanuage")
C("RUBY")























