# if is used for to check the condtions

a=False
#
# if(a):
#     print("python")

#
# if(a>20):
#     print("python")

# # if -else
# if(a):
#     print("python")
# else:
#     print("Java")
# if-elif -else


# a,b=10,20
#
# if (a>10):
#     print("PYTHON")
# elif(b>100):
#     print("JAVA")
# else:
#     print("C IS good")


# assi -1
# biggest of three num and take input from keyboard

# if -elif
#
# a,b=10,20
#
# if (a>=10):
#     print("PYTHON")
# elif(b>100):
#     print("JAVA")

#  ass2

#wap to check the given num in the bitween 1 and 100(take input from keyboard)


# itertive : for ,while

# Range Datatype
# by default startin index is 0 in range

# syntax of range
# range(startinx,endindex ,step)
#
# r=range(10)
# for i in r:
#     print(i,end=" ")

# # # for
# for i in range(10):  # range(num-1)
#     print(i,end=" ")
# print()
#
# for i in range(11,20):  # range(num-1)
#     print(i,end=" ")
# print()
# for i in range(11,20,3):  # range(num-1)
#     print(i,end=" ")
# print()

# x="SRAVANI"
#
# for c in x:
#     print(c,end=' ')
# print()
# # using range
#
# for c in range(len(x)):
#     # print(c,end=' ')
#     print(x[c],end=" ")
#

# strt index always lessthan end indx
# start=int(input("Enter start indx :"))
# endindx=int(input("enter end indx :"))
# for i in range(start,endindx+1):
#     if i%2==0:
#         print(i,end=' ')
# print()
#
# if start%2==0:
#     for i in range(start, endindx + 1, 2):
#         print(i, end=' ')
# else:
#     print("Please provide even start index")

# ass3
# wap to print squares of each num in range of (1,50) and take input from keyboard

# while
# while(con):
    #stt1
#     # stt2
#     #increment /decrement
# start=int(input("Enter start indx :"))
# endindx=int(input("enter end indx :"))
# if (start>0):
#     while (start <= endindx):
#         print(start, end=" ")
#         start = start + 1
# else:
#     print("dont provide 0")

# ass4
# print the sequence of numbers in reverse order with in the range and take input from keyboard

# fact of given num without using factorial fun

# x=int(input("Enter x val :"))
#
# fact=1
#
# for i in range(1,x+1):  # 1*2*3*4      # fact   i    fact
#     fact=fact*i                         #  1     1     1
#                                          # 1      2     2
#                                           # 2     3      6
#                                         # 6      4      24
# print("fact :",fact)


# wap count the digits of given num
# x=int(input("Enter x val :"))
# count =0                                     #x     x
#                                              # 123   12
# while(x>0):
#     x=x//10
#     print(x)
#     count = count + 1
# print("num of digits : ",count)

# reverse the given num

# wap count the digits of given num
# x=int(input("Enter x val :"))
# s=0
# while(x>0):
#     r=x%10
#     s=s*10+r
#     x=x//10
# print("reverse the num : ",s)

# wap to check num is palindrom or not
# after reverse the num still the num have same val is clled palindrom
# 121 ,111, 131, [1-9]

# x=int(input("Enter x val :"))
# s=0
# m=x
# while(x>0):
#     r=x%10
#     s=s*10+r
#     x=x//10
# print("reverse the num : ",s)
# if m==s:
#     print("%d is palindrom" %m)
# else:
#     print("%d is not palindrom" % m)

# amstrong :

# sum of the each digit cubes of num equal to given num
# 153 -> 3*3*3 +5*5*5 +1*1*1  = 153
#x=int(input("Enter x val :"))
# s=0
# m=x
# while(x>0):
#     r=x%10
#     s=s+r*r*r
#     x=x//10
# if m==s:
#     print("%d is amstrong" %m)
# else:
#     print("%d is not amstrong" % m)

# ass1
# wap to sum of squares of each digit of given num
# ex : 123 -> 3*3 +2*2 +1 = 14

# ass 2
# wap to printn only odd digits from given num'
# ex : 1234511  -> 1 1 5 3 1

# wap to check wheather num is prime or not

# prime num -> a num which contins only two factors called prime
# x=int(input("Enter x val :"))
# c=0
# for i in range(1,x+1):
#     if x%i==0:
#         c=c+1       # c=1  # c=2
# if c==2:
#     print("%d is prime" %x)
# else:
#     print("%d is not prime" %x)

# nested loops :
# loop inside the loop is caled nested loop

#####
#####
#####
#####
#####
#
# x=int(input("Enter x val :"))
# for i in range(1,x+1):
#     print('#'*5)
# print()

# for i in range(1,x+1):      # row
#     print("i val is ",i)
#     for j in range(1,10):  # coumns
#         print(j,end="")
#     print()

# wap to print below pattren
#ass3
# 1
# 12
# 123
# 1234
# 12345
# x=int(input("Enter x val :"))
# for i in range(1,x+1): #5
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 10101
# 10101
# 10101
# 10101
# 10101


# 1
# 23
# 456
# 78910
# 1112131415


# ass4 :
 # wap to print [1,100] prime numbers [2,3,5,7,11,13,19.....]

# nested while

# print5 the multiplication table of given num

# x=int(input("Enter x val :"))
#
# for i in range(1,11):
#     print("%d*%d=%d" %(x,i,x*i))

# ass 5

# wap to print  multiplication tables [input take from keyboard strt and end index]

# nested while
# while inside the while is clled nested while
# i=1
# while(i<=5):
#     print(i)
#     j=1
#     while(j<=5):
#         print(j,end='')
#         j=j+1
#     print()
#     i=i+1

# ass6
# wap to print the pattren using nested while
####*
####*
####*
####*
####*










































