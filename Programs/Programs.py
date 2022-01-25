x=[100,20,30,49,60]
# print(max(x))
# print(min(x))
# x.sort()
# print(x)
# print("max",x[-1])
# print("min",x[0])

# max=x[0]
# min=0
# for i in x:
#     if i>max:         #max=100
#         max=i
#     if i<min:
#         min=i
# print("max",max)
# print("min",min)

x=10             #              128 64 32 16 8 4 2 1
print(bin(x))
#
# 1
# 10
# 101
# 1010
# 10101

# def pattren(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if j%2==0:
#                 print("0",end="")
#             else:
#                 print('1',end="")
#         print()
k=1
# def pattren(n):
#     for i in range(n,1,-1):
#         for j in range(1,i):
#             print(" ",end="")
#             for k in range(k,i,-1):
#                 print("#", end="")
#                 k=k+1
#         print()
def pattern(n):
    for i in range(1,n):
      print("*"*i)
    print()

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()



 #    *
 #   **
 #  ***
 # ****


# def pattren(n):
#     for i in range(65,70):
#         for j in range(65,i+1):
#             print(chr(j),end="")
#         print()

x=eval(input("Enter num:"))
pattern(x)
