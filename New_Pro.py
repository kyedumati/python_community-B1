x="ppython Isi gGood"
y=x.split()
print(y)
for i in range(len(y)):
    if y[i][0].islower():
        a=y[i][0]
        up=a.upper()
        x=x.replace(a,up,1)
    elif y[i][0].isupper():
        a = y[i][0]
        up = a.lower()
        x = x.replace(a, up,1)
print(x)