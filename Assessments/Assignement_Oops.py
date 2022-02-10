# # l1=[1,2,3]
# # l2=[4,5,6]
# # final=[]
# # for i in range(len(l1)):
# #     x=l1[i]+l2[i]
# #     final.append(x)
# # print(final)
#
# def maxcount(n):
#     dict={}
#     maindict={}
#     for i in n:
#         str1=i
#         dict={}
#         for j in str1:
#             if j in dict:
#                 dict[j]+=1
#             else:
#                 dict[j]=1
#
#         val=max(dict.values())
#         res=max(dict,key=dict.get)
#         maindict[res]=val
#     print(maindict)
#
#
# def sorting(n):
#     for i in range(0, len(x)):
#
#         str = sorted(x[i])
#         if str[-1].islower():
#             a = str[-1]
#             up = str[-1].upper()
#             # str = str[::-1]
#             str = str.replace(a, up, 1)
#             str = str[::-1]
#         else:
#             ax = str[-1]
#             lw = str[-1].lower()
#             # str = str[::-1]
#             str = str.replace(ax, lw, 1)
#             str = str[::-1]
#         #print(str)
#         # str = sorted(str)
#         newstr = ""
#         newstr = newstr.join(str)
#         x[i] = newstr
#     print(x)
#
# x=['ABCABAA','EMBEDDED','HEOOOLLOOD']
# # maxcount(x)
# sorting(x)



class A:
    def sum(self,a,b):
        res=[]
        for i in range(len(a)):
            res.append(a[i]+b[i])
        return res
a=[1,2,3]
b=[4,5,6]
a1=A()
# x=a1.sum(a,b)
# print("Sum of lists:",x)
# Ass 2: Write a class to get max occurances of character and its count
# from list and output should be in dictionary
class A:
    def max_Count(self,a):
        z={}
        for i in a:
            for j in i:
                if j in z.keys():
                    z[j]=z[j]+1
                else:
                    z[j]=1
        return z
a=["ABABCDCD","ABABCDEFG"]
a1=A()
# x=a1.max_Count(a)
# print(x)
# Ass 3: Sort the each string in list and change last letter as small if
# capital or change capital if it is small
class A:
    def small_capital(self,a):
        output_list=[]
        for innerlist in a:
            sorted_list = sorted(innerlist)
            if sorted_list[-1].islower():
                sorted_list[-1] = sorted_list[-1].upper()
            elif sorted_list[-1].isupper():
                sorted_list[-1] = sorted_list[-1].lower()
            output_list.append("".join(sorted_list))
        return output_list
        # print(a)
        # res=[]
        # res1=[]
        # for i in range(len(a)):
        #     b=a[i]
        #     new_str = []
        #     str1=""
        #     str2 = ""
        #     for j in range(len(b)):
        #         if j+1 == len(b):
        #             if b[j].isupper():
        #                 l=b[-1].replace(b[-1], b[-1].lower())
        #                 new_str.append(l)
        #             elif b[j].islower():
        #                 l=b[-1].replace(b[-1], b[-1].upper())
        #                 new_str.append(l)
        #     else:
        #         new_str.append(b[j])
        #         str1=str1.join(new_str)
        #         str2=str2.join(sorted(str1))
        #         res.append(str1)
        #         res1.append(str2)
        # return res,res1
# a=["HELLO","Hai","BABACAB"]
# a1=A()
# y=a1.small_capital(a)
# print(y)

# def sum(a,b=None,c="test"):
#     print("a ",a," b ",b," c ",c)
#
# sum(20,20)
#
#


#
# string=input("enter the string")
# substring=input("enter the substring")
# cmp=""
# for i in range(0,len(string)):
#     for j in range(2,len(string)):
#         if string[i:j]==substring:
#             print("the index is",i)
#         else:
#             pass

# list=[2,2,4,5,4,3,3]            #100% clarity on requirement   #duplicates remove   #
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
#     else:
#         pass
# print(new)
#
#
#
# from abc import *
# class Test:
# 	@abstractmethod
# 	def m1(self):
# 		pass
#
# t=Test()

# input :
# list=[2,2,4,5,4,3,3]
# # Output:
# # output_list = [16,16,4,4]
#
# for i in list[:]:
#     if i % 2 != 0:
#         list.remove(i)
# list = [i ** 2 for i in list]
# list.sort(reverse=True)
# print("output list ",list)



# with open('../test.txt') as f:
#     for line in f:
#         print(line)
#print(f.close())