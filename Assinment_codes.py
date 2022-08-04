# third largest num
x=[10,2,30,1,3,100,200,500]

# Sorting
#
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if (x[i]>x[j]):
#             temp=x[i]
#             x[i]=x[j]
#             x[j]=temp
# print(x)
# print("Third largest :",x[-3])

# # distinct ele from list without using set
# x=[2,2,4,5,4,3,3,10,30,30]
# final=[]
# index=0
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i]!=x[j] and x[i] not  in final:
#             final.append(x[i])
# print(final)

# x="Hello world"
# print(len(list(x)))
# y='llo'
# exits=False
# for i in range(len(x)):
#     for c in range(len(y)):
#         if x[i]!=y[0]:
#             break
#         else:
#             Start_index=i
#             for j in range(0,len(y)):
#                 if x[i]==y[j]:
#                     print("x->",x[i])
#                     print("y->",y[j])
#                     exits=True
#                     print(i)
#                     i=i+1
#                 else:
#                     exits=False
#                     break
#     if exits==True:
#         print("String is exits")
#         print("Strting index :",Start_index)
#         break
# else:
#     print("Not Exits")


# x="Hello"
# y="ell"
#
# # find len of given string without using len
# temp=x+'\0'
# count=0
# while(temp[count]!='\0'):
#     count=count+1
# print("len of str :",count)


# for j in range(len(x)):
#     for i in range(len(x)):
#         if x[j:(i+len(y))]==y:
#             print("index of :",(i+len(y)))
#             break

input =[0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1]

cycle_count=0
start=0
for i in range(start,len(input)):
    if input[i]==1:
        Start_index=i
        print(Start_index)
        for j in range(i,len(input)):
            if input[j]==1:
                pass
            else:
                # End_index=j
                # cycle_count=cycle_count+1
                # print("Start_index :",i)
                # print("End_index :",j)
                # print("Cycle_count :",cycle_count)
                start=j
                print(start)




























