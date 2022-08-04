# Operator : it is a symbol to perform some operation   Ex: +, - ,*

# 1. Arithmatic operator    (+  - * / % // **)
# a = 10
# b = 3
# print("a+b ",a+b)   # 12  13
# print("a-b ",a-b)   # 8   7
# print("a*b ",a*b)   # 20  30
# print("a/b ",a/b)   # 5.0 3.33
# print("a%b ",a%b)   # 0   1
# print("a//b ",a//b) # floor division operator
# print("a**b ",a**b) # power operator
#
# c = "mounika"
# print("2"+c)

# 2. Relational Operators:   >  , >= , < , <=
# a = 10
# b = 10
# print("a>b ",a>b)  #False
# print("a>=b ",a>=b)  #True
# # b = 20
# print("a<b ",a<b)   # False
# print("a<=b ",a<=b)  #True
# print("a==b ",a==b)  #True

# if(a>b):
#     print("A is greateer thann b")
# else:
#     print("A is smaller than B")
# a = 10
# b = 10
# Equality operators : ==  !=
# print("a == b ", a==b) # True
# print("a != b ", a!=b) # False


# 3. Logical Operators  : and or not
# and --  if both arguments are True then only output is True
# or  --  if atleast one argument is True then output is True
# not --  complement
# a = True
# b = False
# print("a and b is ", a and b)  # False
# print("a or b is ", a or b)  # True
# print(not b)  # True
# print(not a)  # False

# 0 means False
# non-zero is True
# "" means False

# a = 0
# b = 20

# 0 and 20    False and True
# 0 or 20     False or True   --> True  20
# print(a and b) #True  # if first value is zero then result is zero otherwise result is second value
# print(a or b) #True  # if first value is True then result is first value otherwise result is second value


# 4. Assignment operators:  to assign value to a variable
#    =  += -+ *=  /=

# x = 10
# x += 20   # x = x+20
# print(x)
# x -= 20   # x = x-20
# print(x)
# x *= 20
# print(x)


# Ternary operator:     Syntax :   value if <condition> else value
# a = 30
# b = 20
# age = 11
# x= "Eligibile for vote" if age>=21 else "Not eligible for vote"
# x = 30 if a<b else 40
# print(x)


# Special operators
# --> Identity operator        is   is not
# --> Membership operator      in   not in
# a = 10
# b = 10
# print(a is b)  #True     ==  !=
# print(a is not b)  #False
#
# list1 = ['Mounika','Python','Shravani','Narasimha','Bashu','Narendra']
# print('Shravani' not in list1)
# x= "Shravani joined the class today" if 'Shravani' in list1 else "Shravani Absent"
# print(x)
# name = "Vamsee"
# print('k' in name)