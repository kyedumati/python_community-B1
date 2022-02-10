# sum of digits of a given number until you get a single digit
'''
sum of digits of a given number until
you get a single digit
'''
n = int(input("enter the number you want"))
def fun1(n):
    s=0
    while n>0:
        r= n%10
        s=s+r
        n=n//10
    if s > 9:
        return fun1(s)
    else:
        return s

g=fun1(n)
print(g)