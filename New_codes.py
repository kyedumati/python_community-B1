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

input = "ab$c$de$gh"
output=[]
index=-1
input = list(input)
print("",input)
for i in range(len(input)-1,int(len(input)/2),-1):
    if input[i]!="$":
        temp=input[i]
        while True:
            index+=1
            if input[index]!="$":
                input[i] = input[index]
                input[index] = temp
                break

print(input)

