# Reading dynamic values from console  ,,
# input()

# a = input("Enter a value : ")   #  '20'
# b = input("Enter b value : ")   # '30'
# a = int(a)
# b = int(b)
# a = 200    # hardcoding --> it will always be same
# b = 60    # hardcoding --> it will always be same
# print("sum is ",a+b)

# raw_input()

# age = input("Enter your age : ")
# print(type(age))
# age = int(age)
# if age>=21:
#   print("You are eligible for marriage")
# else:
#   print("You are not eligible for marriage")

#How to read multiple values in a single line
# x = input("Enter 2 numbers").split('-')
# print(x)
# a= int(x[0])
# b= int(x[1])
# print("sum of a and b is ",a+b)


# eval()     ---> It takes a string as argument and evaluate the result
# x=eval(input("Enter expression"))
# print(x)

#eval() can evaluate the input to list, set, tuple based on the provided input
# l = eval(input("Enter a list: "))
# l = input("Enter a list: ")
# print(type(l))
# print(l)

#
# a = eval(input("Enter a value : "))   #  '20'
# b = eval(input("Enter b value : "))   # '30'
# a = int(a)
# b = int(b)
# print("sum is ",a+b)


# Ass1:
#1.Write a program to read 3 float numbers from console with , saperator and print their sum
#2.Write a program to read employee data(ename,esal,empno,address) and print their data
#3.Biggest of two numbers using ternary operators




# candidate_exp = [
#   {
#     "start": "2010",
#     "end": "2014",
#     "company": "A"
#   },
#   {
#     "start": "2013",
#     "end": "2016",
#     "company": "B"
#   },
#   {
#     "start": "2018",
#     "end": "2019",
#     "company": "C"
#   }
# ]
#
#
# years_worked = []
# for company in candidate_exp:
#     for i in range(int(company['start']),int(company['end'])):
#         years_worked.append(i)
# print(years_worked)
# years_worked = set(years_worked)
# print("Total years exp ",len(years_worked))

apples=50
while apples>=5:
   apples-=5  #eating 5 apples
   apples+=1  #adding 1 apple
print(apples)



