#Ass1 create aa class to return the sum of two lists

a=[1,2,3]
b=[4,5,6]          # [5,7,9]
# z=[]
# for i in range(len(a)):
#     z.append(a[i]+b[i])
# print(z)

# x = {'A':'B', 'B':'C', 'D':'E'}
#
# y = list(x.keys()) # ['A','B','D']
#
# z = list(x.values()) # ['B','C','E']
#
# a = y + z  # -> ['A','B','D','B','C','E']
#
# for i in x.keys():
#     print(i,a.count(i))

# write a class to get max occurence of char and count from list
x = ['ABCABAA' ,'EMBEDDED' 'HEOOOLLOOO']             # {'A':4  'D': 4  'o': 6}


# sort the each string ele in list  and make last letter if small make capital if capital make small

x = ['ABCABAA' ,'EMBEDDEd' 'HEOOOLLOOO']
x = ['ABCABAa' ,'EMBEDDED' 'HEOOOLLOOo']
x=['AAABBCa','BDDEEEMd','HELLOOOOOo']     # A-Z   65 to 90
                                          # 97 to 120






















def charcount(x):
    charlist = []
    char_count = []
    a = list(x)
    b = set(a)       # ABC
    max = 0
    for i in b:
        if a.count(i) > max:
            max = a.count(i)
            c= i
    return  c,max
y = str(x[0])
a, b = charcount(y)
print(a,b)