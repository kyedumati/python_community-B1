a = [1,3,4,5,60]
print(sum(a))
sum_val = 0
for i in a:
    sum_val+=i
print('list sum is ', sum_val)
list_mul = [i*i for i in a]
print('list multiply is ', list_mul)
largest_number = 0
for i in a:
    if i>largest_number:
        largest_number =i
print("largest number is ",largest_number)
