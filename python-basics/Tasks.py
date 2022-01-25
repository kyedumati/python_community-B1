x=input("Enter one sentence:")

y=x.split(' ')
for i in range(1,len(y)+1):
    print(y[-i],end=' ')