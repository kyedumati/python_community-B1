x='abcde$gh'   #-> hgfed$cba

def strrev(x):
    y=list(x)
    print(y)
    pos=[]
    for i in range(len(y)):
        if x[i]=='$':
            pos.append(i)
            y.remove(x[i])
    print(pos)
    y=y[::-1]
    for i in pos:
        y.insert(i,'$')
    return y

x='abcd$$e$gh'
y=strrev(x)
print(y)



