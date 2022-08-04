# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)  # 1 2
#     i+=1 # i=3


# x = 'abcd'
# for i in x:
#     print(i.upper())



# i=0
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
# else:
#     print(0)

# def addItem(listParam):
#     listParam+=[1]
#     print(listParam)
#
# mylist = [1,2,3,4]
# addItem(mylist)
# print(len(mylist))


#
# list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list[1][2])
#
# def sum():
#     print("inside funcition")
#
# for i in range(10):
#     if i==5:
#         break
#     else:
#         print(i)
#         # sum()
# else:
#     print("here")

# List  = []
# set  = {}
# dict = {}
# tuple = ()

# print(id(mylist))
# for i in range(2.0): print(i)


# print("abcdef".find("cd"))
# print("cd" in "abcdef")
# print("abcdef".find("cd") == "cd" in "abcdef")


#
# string="my name nis kasi"
# for i in string.split("n"):
#     print(i,end=",")
# BODMAS
# print("abcdefcd".find("bc"))

# print("abcdef".find("bc") == ("cd" in "abcdef"))
# print(1==True)

# ls=[2, 33, 222, 14, 25]
# print(ls[::-1])  # 0:4:-1
# print(ls[-1:-6:-1])
# start pos include:exlude end pos:step
#  start:end:step


# def unpack(a,b,c,d):
#     print(a+d)
# x=[1,2,3,4]
# unpack(*x)

#
# test_dict={"kasi":1,"naga":"2","kasi":2}
# print(test_dict)

# def writer():
#     title='Sir'
#     name=(lambda x:title + ' '+x)
#     return name
#
# who=writer()
# print(who('Arthur'))