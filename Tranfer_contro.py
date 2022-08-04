# # break
# # break is a keyword used in loops to break the execution
# # break used for to come out fro the loop
# # for i in range(1,10):
# #     if i==1:
# #         break
# #     else:
# #         print(i, end=" ")
#
# # continue:
# # continue is a keyword and it will skip the current iteration
# # for i in range(1,6):
# #     if i==1:
# #         continue
# #     for j in range(1, 6):
# #         if j == 2:
# #             continue
# #         print(j, end='')
# #     print()
#
# # for_else
#
# # for i in range(1,5):
# #     print(i,end=" ")
# # else:
# #     print("For executed successfully")
# # i=1
# # while(i<=3):
# #     print(i,end=" ")
# #     i=i+1
# # else:
# #     print("While executd successfully ...!!\n")
# #
# # x=1
# # if x<10:
# #     pass
# # else:
# #     print(x)
# # del
# # del is a keyword in python
#
# # x=10
# # y=x*10
# # print(y)
# # del x
# # x=20
# # print(x)
# #ass7
# # wap to print power of given number without using pow()-> input take from keyboard [x,p]  x=2,p=3 output =8
#
# #ass8 wap to print amstrong numbers b/w [1-500]
#
# # ass9
# # wap to print [1-100] palindrom num
#
# a=10
# print(type(a))
# a="PYTHON"
# print(type(a))
# print(a)
# # None
# a=None
# a=10
# a=None
# a="Pyton"
# a=None
# a=12.5
# print(a)
#
#


n=156
s=0
while(n>0):
    s=s+n
    n=n//10
    print(n)
print(s)
