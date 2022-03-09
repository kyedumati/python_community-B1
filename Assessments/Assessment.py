# x="w3resource"
# y=set(x)
# a=[]
# b=[]
# for i in y:
#     a.append(i)
#     b.append(x.count(i))
# print(dict(zip(a,b)))

# x="w3resource"    #output : {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# output = {}
# for i in x:
#     if i in output.keys():
#         output[i] += 1
#     else:
#         output[i] = 1
# print(output)


# input_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12],[1,2,3]]
# max_list = []
# max_sum = 0
# for list in input_list:
#     sum_list = 0
#     for x in list:
#         sum_list += x
#     if sum_list > max_sum:
#         max_sum = sum_list
#         max_list = list
#
# print(max_list)

#Approach 2:
# number = [[1,2,3], [4,5,6], [10,11,12]]
# print(max(number, key=sum))

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()