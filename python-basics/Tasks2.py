def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

input_ls = input().split()
print("input_ls ",input_ls)
result = map(int, input_ls)
print(list(result))


import math
math.factorial(5)