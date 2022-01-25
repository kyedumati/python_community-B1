# x="w3resource"
# y=set(x)
# a=[]
# b=[]
# for i in y:
#     a.append(i)
#     b.append(x.count(i))
# print(dict(zip(a,b)))


num = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
index = 0
max_index = 0
sum_max = 0
for list1 in num:
    sum_list = 0
    for x in list1:
        sum_list += x
    if sum_list > sum_max:
        sum_max = sum_list
        max_index = index
    index += 1
print(num[max_index])