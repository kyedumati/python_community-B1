def finding(x):
    ls=[]
    new=""
    cnt=0
    for i in string:
        cnt+=1
        if i=="\n":
            break
    while cnt>0:
        ls.append(x[cnt-1])
        cnt-=1
    new="".join(ls)
    if x==new:
        print("pal")
    else:
        print("not pal")
string="radar"
finding(string)
