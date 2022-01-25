#recursive fun: a function call itself is called recursive function


# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*(fact(n-1))         # 3 *fact(2)
#                                      # 2* fact(1)
#                                      # 1* 1
#     return result
# print(fact(3))

# s=0
# r=None
# def reverse(n):
#     global s
#     global r
#     if n!=0:
#         r=n%10                      # r=3        s=0*10+3 s=3     n==123     n==12
#                                     # r=2        s=3*10+2  =32    n=12       n=1
#                                     # r=1        s=32*10+1 =321   n=0
#         s=s*10+r              s=s+r*r*r        153 -> 27+125+1=153
#         n=n//10
#         reverse(n)
#     return s
# print(reverse(12345))

# return used for two types
# value return
# Control return

# r=None
# s=0
# def digitsum(n):
#     global s
#     global r
#     if n!=0:
#         r=n%10               # r=3    s=0+3   n=123   n=12
#                              # r=2    s=3+2   n=12    n=1
#                              # r=1    s=3+2+1 n=1     n=0
#         s=s+r
#         n=n//10
#         digitsum(n)
#     return s
# print(digitsum(123456))

#Enumarate

# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
#
x=[0,1,2,3,4]
# for i in range(0,5):
#     print(x.index(x[i]),i)
# print()
#
# for count,i in enumerate(x):
#     print(count,i)


# for count,i in enumerate(x,6):
#     print(count,i)
#
# y=list(enumerate(x,100))
# print(y)
# print(y[2])
#
# Eval used for to give input as any val by default it wil convert the type based on u r input
# x=eval(input())
# print(type(x))
# print(x)
#
# x,y=(i for i in input().split())
# print(x)

#for loop
# 1. print even and odd num in saparte list and print the sum

# x=[2,3,4,56,33,5,7,8]
# def even_odd(x):
#     even_list = []
#     odd_list = []
#     for i in x:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return even_list,odd_list,sum(even_list),sum(odd_list)
# Even,odd,EenS,oddS=even_odd(x)
#Even=even_odd(x)  # here Even is a tuple it stotes all return values from fun in tuple format
# print("even_list",Even)
# print("odd_list",odd)
# print("Evensum",EenS)
# print("Oddsum",oddS)

# Prime num whichn is having two factors is called prime

# print num of prime and palindrom numbers from list

x=[121,3,5,111,4,88,89,93,17,222,333]    # op 121,111,333

#hint prime num in saparate list   ->prime list

#pass prime list the palindrom fum and result store in one list

# sum of digits of given input until come single digit

#Ex 12345 =15 ->1+5 =6
#ex 2: 145678 ->26 ->2+6 =8
#ex 3 : 999999999999 =108 ->1+0+8+ 8

#
# def prime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c=c+1   # c=1
#     if c==2:
#         print("%d is prime" %n)
#     else:
#         print("%d is  not prime" % n)
# prime(6)


#
# #fibanacci series  # 1 1 2 3 5 8 13
# def fib(n):
#     a = 0
#     b = 1
#     c=0
#     for i in range(1, n + 1):
#         a = b                    # a=1 b=1    c=2 b=1  -> a=1 b=2   c=3
#         b = c
#         print(c, end=" ")         # c=0        c=1   c=1
#         c = a + b
#
# fib(7)

# reverse num :

# amstrong num -> sum of the cubes of given num equals to same num
# palindrom  -> if num is same after u reverse the same num
# sum of digits of num


def pal(n):
    s=0
    while(n):
        r=n%10                    # n=153  # r=3    s=0 ->s=3
                                  # n=15   # r=5    s =3+5 s=8
                                  # n=1     # r=1    s= 8+1  =9
        s=s+r
        n=n//10
    return s
y=eval(input("enter num :"))
x=pal(y)
print("%d sum is %d" %(y,x))
# if y==x:
#     print("%d num is palindrom" %y)
# else:
#     print("%d num not is palindrom" %y)


























