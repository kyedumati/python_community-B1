def max(a,b):
    if a>b:
        return a
    else:
        return b
x,y=[int(x) for x in input("Enter two Ele :").split()]
max_ele=max(x,y)
print("Max ele is :",max_ele)