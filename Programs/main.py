import numpy as np
x=np.array([1,2,3,4])
print(x)

print("Two dimensional Array")

x=np.array([[1,2,3,4],[5,6,7,8]])
print(x)

print("print using eye 3*3")

x=np.eye(3)  # 3*3
print(x)
print(x*10)  # each ele multiplied by 10
print("print series using arrange()")
x=np.arange(1,10)
print(x)
print("CONVERT ARRAY TO 3*3 MATRIX")
x=np.arange(1,10).reshape(3,3)
print(x)
print("PRINT ROWS IN MATRIX")
for i in x :
    print(i)
print("PRINT COLUMNS IN MATRIX")
for i in range(3):
     print(x[:,i])
print("PRINT SINGLE COLUMN IN MATRIX")
print(x[:,0])
print(x[:,1])
print("PRINT PARTICULER RANGE OF ELEMENTS FROM MATRIX")
print(x[1:3:,1:3])
print("PRINT SUM OF  MARRIX")
print(np.sum(x))
print("PRINT SUM OF ROW WISE MARRIX")
print(np.sum(x,axis=1))   # row wise -> use sum(x) also
print("PRINT SUM OF COLUMN WISE MARRIX")
print(np.sum(x,axis=0))   # COLUMN WISE

print("ADD TWO MATRIXS USING ROW WISE")
y=np.array(np.arange(1,10)).reshape(3,3)
z=np.array(np.arange(11,20)).reshape(3,3)
a=np.hstack((y,z))  # Addded two matrix horizantally
print(a)
print("ADD TWO MATRIXS USING COLUMN WISE")
a=np.vstack((y,z))  # Addded two matrix horizantally
print(a)
print("ADD TWO MATRIXS USING ROW WISE")
a=np.hstack((y,z))  # Addded two matrix horizantally
print(a)
print(a*10) # multiply all elements by using 10
print(x)
print("ROW WISE MEAN")
print(np.mean(x,axis=1))
print("COLUMN WISE MEAN")
print(np.mean(x,axis=0))
print("CUMSUM ADD NEXT ELE OF MATRIX :")
print(np.cumsum(x))
print("CUMPRODUCT MUL NEXT ELE OF MATRIX :")
print(np.cumproduct(x))
print("ROW WISE MIN ELE")
print(np.min(x,axis=1))
print("COLUMN WISE MIN ELE")
print(np.min(x,axis=0))
print("ROW WISE MAX ELE")
print(np.max(x,axis=1))
print("COLUMN WISE MAX ELE")
print(np.max(x,axis=0))

print("MATRIX MUL:")
print(y)
print(z)
print("MATRIX MUL")
print(y*z)
print("ACTUAL MULTIPLICATION")
print(y.dot(z))

print("EXAMPLE OF SHALLOW COPY -> IF U CHANGE C VALUE D VALUE ALSO WILL CHNAGE")

C=np.array(np.arange(1,5))
d=C
d[0]=1000
print("C IS :",C)
print("d is :",d)

print("EXAMPLE OF DEEP COPY -> IF U CHANGE C VALUE C ONLY WILL CHANGE WONT EFFECT ON D")
C=np.array(np.arange(1,5))
d=C.copy()
d[0]=1000
print("C IS :",C)
print("d is :",d)
print("OPERATIONS ON NUMPY ARRAY ")
C=np.array(np.arange(1,5))
print(C)
print(np.append(C,1000))
print("ROW WISE APPEND ")
d=np.append(x,[[100,200,300]],axis=0)      # ROW WISE APPEND
print(d)
print("COLUMN WISE APPEND ")
d=np.append(x,[[100],[200],[300]],axis=1)   # COLUMN WISE APPEND
print(d)

print("INSERT DATA")
x=np.array([1,2,3,4])
print(np.insert(x,1,10000))
print(y)
print("INSERT A ROW ROW WISE :")
z=np.insert(y,2,[1000,2000,3000],axis=0) #row wise
print(z)
print("INSERT A COLUMN COLUMN WISE :")
y=np.insert(y,1,[[1000]],axis=1)
print(y)

print("TAIL")
e=np.tile(y,(1,2))
print(e)

print("SPLIT ELE FROM MATRIX ROW WISE")

f=np.split(y,3,axis=0)
print(f)

print("SPLIT ELE FROM MATRIX COLUMN WISE")
f=np.split(y,2,axis=1)
print(f)

print("CONCATENATE 2 MATRIX ROW WISE:")

g=np.concatenate((y,y),axis=0)    #by default it will concatinate row wise
print(g)

print("CONCATENATE 2 MATRIX COLUMN WISE:")
g=np.concatenate((y,y),axis=1)
print(g)

print("REPEAT ELEMENT ")
h=[1,2,3,4,5]
print(np.repeat(h,2))

print("REPEAT MATRIX 2 TIMES ROW WISE")
print(np.repeat(y,2,axis=0))
print("REPEAT MATRIX 2 TIMES COLUMN WISE")
print(np.repeat(y,2,axis=1))

print("RANGE OF ELEMENTS")
print(y)
print(y[1:3,2:4])