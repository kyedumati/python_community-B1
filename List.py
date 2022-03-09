# list : list is a collection of hertroginious ele
#we can store multible values in list
# duplicates r allowed in list
# to access the list ele index is required [+,-]
#list having growable nature
# list index starts from zero
# -ve index starts from -1 in reverse order
#syntax : list_name=[]

# x=[]
# print(type(x))
#
# x=list()
# print(type(x))
#   0 1 2 3
# x=[5,6,5,10]
# #-4  -3  -2  -1
# print(type(x))
#
# # access the ele in list
#
# print(x[0])
# print(x[2])
# print(x[3])
# # access ele in reverse order(-ve index)
# print(x[-2])     # 8
# print(x[-4])     # 5


# create a list by ele from keyboard
# # append() -> add ele into the list
# y=[]
# for i in range(1,6):
#     x=int(input(" enter x val :"))
#     y.append(x)
# print(y)

# # slicing
# x=[10,20,30,40,50]
# # syntax x[start:end:step]
#
# print(x[:])
# print(x[2:])
# print(x[1:4])
# print(x[:3])
# print(x[-4:])
# print(x[-5:-2])
# print(x[:-3])
# print(x[-4:])
# print(x[::2])
# print(x[1::2])
# print(x[:4])  # [10,20,30,40]
# print(x[:5:3])  # [10,20,30,40,50]
#
# x=[10,20,30,40,50]
# print(x[1:100:2])  # [10,20,30,40,50]

# x=[10,100,30]
# x.append(40)  # append ele i added at lst
# print(x)
# x.append(100)
# print(x)
# print(len(x))
# # pop()  -> pop() always remove the lst ele
# x.pop()
# print(x)
# x.append(100)
# x.append(100)
# x.pop()
# print(x)

# count() -> count to the ele how many times it is existed in list
# x=[100,20,30]
# print(x.count(100))
# # index -> retrive the index of perticuler ele in the list
# # print(x.index(100))
# # print(x.index(30))
# # print(x.index(20))
# # insert - > insert wil take 2 args (pos,ele)  # x.insert(pos,ele)
# x.insert(3,1000)
# print(x)
# x.insert(2,2000)
# print(x)      #    [100,20,2000,30,1000]
# x.insert(1,10000)   #[100,10000,20,2000,30,1000]
# print(x)
#remove -> remove fun to remove the perticuler ele
x=[10,20,30,40]
#
# for i in x:
#     print(x.index(i),i)

# x.remove(20)
# print(x)

# remove the desired ele from list and input take from keyboard

# y=int(input("Enter y val :"))

# if y in x:
#     x.remove(y)
# print(x)
#
# # using loops
# #
# for i in x:   # range is not required
#     if i==y:
#         x.remove(y) # x[i]
# print(x)

#reverse
x=[20,3,30,6,8]
# x.reverse()
# print(x)
# without using reverse method reverse the list
#print(x[::-1])
# sort  -> sort will do to sort the ele [default it wil sort in acending]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
#
# y=[100,200,300,400]
# x.extend(y)
# print(x)
# print(x[-1])
# print(x[8])
#
# x=[1,2,3]
# y=["PYthon",'JAVA']
# # x.append(y)
# # print(x)
# # print(x[3])
# # print(x[3][0])
# # print(x[3][1])

# nested list -> list inside the list is called
x=[[1,2],[3,4],[5,6]]
# print(x[2][-1])
# print(x[1])
# print(x[-2])

# ass1 -> x=[[10,30],[20,40],[70,60]]  -> output [10,30,20,40,70,60]  # hint -> extend
# output 2 =[70,60,40,30,20,10]

#ass2 =input -> [[1,2],[3,4],[5,6]]  # output -> [[1,4],[9,16],[25,36]]

# x.clear()   # x=[]
#
# print(x)
# x.extend([10,20,30])
# print(x[1])
# print(x)

# copy
#x=[[1,2],[3,4],[5,6]]
# y=x
# print(y)
# y=x.copy()
# print(y)
# z=[]
# z.extend(y)
# print(z)
#
# Ass 4
z=[10,20,[[1,2],[3,4],[5,6]]]     # [10,20,1,2,3,4,5,6]


# # copy -> copy one list to anotherlist
#
# a=z # z copying to a
#
# a=z.copy()
# print(a)
#
# print(z[::-1])
# print(z.pop())
# print(z.remove(20))
# x=[1,2,3,4,5,6,7]
# y=100
#
# if y in x:
#     print("EXITS")
# else:
#     print("Not exits")

# list comprehensiion:

# syntx : [expression for item in list if con]

x=[1,2,3]  # [1,4,9]
x=[i*i for i in x]
print(x)
x=[i*i*i for i in x]
print(x)

x=[1,2,3,4,5,6,7,8]
y=x.copy()
x=[i for i in x if i%2==0]
print(x)
x=[2,4,6,8]   #even list
y=[i for i in y if i%2!=0]
print(y)

# asss

#wap to print palindrom numbers from list
# input x=[121,111,221,344,444,222]
# output =[121,111,444,222]

# wap to swap last nd frst index of list
# input -> [10,20,30,40]
# output -> [40,20,30,10]

# y=[[1,2,4],[3,2,6],[5,2,4]] ->[1+3+5,2+2+2,4+6+4] [9,6,14]

# for i in range(len(x)):
#     x[i]=x[i]*x[i]
# print(x)

# x.append(["python",'JAVA'])
#append ,pop,insert,remove,count,reverse,Extend,sor,clear,copy,index