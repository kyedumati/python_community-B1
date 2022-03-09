# import math as m
#
# x=10/4    # 3.333
# print(x)
# print(m.floor(x)) # // floor div
# z=m.pow(2,3)
# print(z)
# y=m.factorial(4)
# print(y)
# c=m.ceil(x)
# print(c)
# a=m.sqrt(16)
# print(a)

# area of circle  pi*r*r

# pi=3.14
# r=2
# print(pi*r*r)

# input and output

# prdefined fun -> input()

#syntax : variabe=input("enter a val")

# x=input("Enter a string")
# print(x)

#syntax : variabe=int(input("enter a val"))

# x=float(input("Enter x val :"))
# print(x)

#Eval :

# x=eval(input("Enter x val :"))
# print(x)

# y="10+2+30
# print(eval(y))
# #
# x=eval(input("enter x :"))
# y=eval(input("enter y :"))
# print(x+y)
#print(eval(input("enter x :")) + eval(input("enter y :")))
#

# # pass input in single line    #1020
# a,b,c,d=[eval(x) for x in input("Python is good:").split()]
# print("val of a :",a)
# print("val of b :",b)
# print("val of a :",c)
# print("val of b :",d)


#print() -> is a output startement to print the output

# a,b,c=10,20,30
#
# print(a,b,c,sep=',')
#
# print("HELLo\nworld")
# print("HELLo\tworld")
# print("HELLO\bworld")
# print("HELLO"*2)
# print("Hello\b"+"World\n")

# %d %i %f %s

# a= 10
# b=20.4
# c=20
# x="HOW IS THE CLASS ?"
# print("value of a is %d " %a)
# print("value of a is %f " %b)
# print("value of a is %i " %c)
# print("%s " %x)
#
# print("val of a is %d and val of b is %f" %(a,b))


# x="python"
# y="JAVA"
# z="C++"
# print("{0} is good and {1} is bad and {2} is defficult ".format(x,y,z))
# print("{x} is good and {y} is bad and {z} is defficult ".format(x=x,y=y,z=z))
# print("{x} is good and {y} is bad and {z} is defficult ".format(x=y,y=z,z=x))

a,b=10,20
print("val of a : {a} val of b :{b} ".format(a=b,b=a))

















# print(a,",",b,',',c)








# swap of two num

#logic 1

# a,b=10,20
# a,b=b,a
# print("val of a :",a)
# print("val of b :",b)

# logic 2 -> swap two num using third variale '
# a,b=10,20
# temp=a    # temp=10
# a=b       # a=20
# b=temp    # b=10
# print("val of a :",a)
# print("val of b :",b)

# logic 3  swap two num without using third variale -> imp
# a,b=20,10
# a=a+b  # a=30
# b=a-b  # b=20
# a=a-b  # a=10
# print("val of a :",a)
# print("val of b :",b)

# #logic 4
# a,b=5,10
# a=a*b  # a=50
# b=a//b # b=5
# a=a//b # a=10
# print("val of a :",a)
# print("val of b :",b)

# # logic 5 -> swap num using bitwise
# a,b=5,10                            #0101   1010
# a=a^b  # a=50
# b=a^b # b=5
# a=a^b # a=10
# print("val of a :",a)
# print("val of b :",b)

# #logic -6
# a,b=20,10
# a=a-(-b)  # a=30
# b=a-b  # b=20
# a=a-b  # a=10
# print("val of a :",a)
# print("val of b :",b)

























