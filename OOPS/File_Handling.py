# types of files
# Text Files
# binary Files
# Opening a file

# Opening a File:
# Before performing any operation (like read or write) on the file,first we have to open that
# file.For this we should use Python's inbuilt function open()
# But at the time of open, we have to specify mode,which represents the purpose of
# # opening file.
# f = open(filename, mode)
# The allowed modes in Python are
# 1. r  open an existing file for read operation. The file pointer is positioned at the
# beginning of the file.If the specified file does not exist then we will get
# FileNotFoundError.This is default mode

# f=open("Python.txt",'r')
# print(f.read())
# f.close()

# 2. w  open an existing file for write operation. If the file already contains some data
# then it will be overridden. If the specified file is not already avaialble then this mode will
# create that file.
#
# f=open("Python.txt",'w')
# f.write("HELLO JAVA")
# f.close()


# 3. a  open an existing file for append operation. It won't override existing data.If the
# specified file is not already avaialble then this mode will create a new file.

# f=open("Python.txt",'a')
# f.write("Hello JAVA")
# f.write('\n')
# f.write("HELLO PYTHON")
# f.close()

# 4. r+  To read and write data into the file. The previous data in the file will not be
# deleted.The file pointer is placed at the beginning of the file.
# f=open("Python.txt",'r+')
# print(f.read())
# f.write("\nHELLO WORLD")
# f.close()

# 5. w+  To write and read data. It will override existing data.
# f=open("Python.txt",'w+')
# f.write("HELLOWORLD")
# f.seek(0)
# print(f.read())
#
# 6. a+  To append and read data from the file.It wont override existing data.
# f=open("Python.txt",'a+')
# f.write("HELLO PYTHON")
# f.seek(0)
# print(f.read())
# f.close()

#7. x  To open a file in exclusive creation mode for write operation. If the file already
# exists then we will get FileExistsError.

#f=open("Python.txt",'x')


# Note: All the above modes are applicable for text files. If the above modes suffixed with
# 'b' then these represents for binary files.
#
# f=open('Python.txt','a+')
# f.write("HELLO CHINNA")
# f.write("HELLO RAMA")
# f.seek(0)   # char position set
# y=f.readline()
# print(y)
# f.close()


# Various properties of File Object:
# Once we opend a file and we got file object,we can get various details related to that file
# by using its properties.
# name  Name of opened file
# mode  Mode in which the file is opened
# closed  Returns boolean value indicates that file is closed or not
# readable() Retruns boolean value indicates that whether file is readable or not
# writable() Returns boolean value indicates that whether file is writable or not.
#f.closed -> returns true if it is already closed else false

#
# f=open("abc.txt",'w')
# print("File Name: ",f.name)
# print("File Mode: ",f.mode)
# print("Is File Readable: ",f.readable())
# print("Is File Writable: ",f.writable())
# print("Is File Closed : ",f.closed)
# f.close()
# print("Is File Closed : ",f.closed)
#
# x=["HELLO\n","CHINNA\n","HOW R U\n"]
# f=open('Python.txt','w+')
# f.writelines(x)
# f.seek(0)
# y=f.read()     # all data read line by line where as readines wil give list[]
# print(y)
# f.close()

# Reading Character Data from text files:
# We can read character data from text file by using the following read methods.
# read() To read total data from the file
# read(n)  To read 'n' characters from the file
# readline() To read only one line
# readlines() To read all lines into a list
# Eg 1: To read total data from the file
# f=open("abc.txt",'r')
# data=f.read()
# print(data)
# f.close()
#
# Eg 2: To read only first 10 characters:
#  f=open("abc.txt",'r')
#  data=f.read(10)
#  print(data)
#  f.close()

#Eg 3: To read data line by line:
# f=open("abc.txt",'r')
# line1=f.readline()
# print(line1,end='')
# line2=f.readline()
# print(line2,end='')
# line3=f.readline()
# print(line3,end='')
# f.close()


#Eg 4: To read all lines into list:
# f=open("abc.txt",'r')
# lines=f.readlines()
# for line in lines:
#     print(line,end='')
# f.close()

#Eg 5:
# f=open("Python.txt","r")
# f.seek(0)
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print("Remaining data")
# print(f.read())

# The with statement:
# The with statement can be used while opening a file.We can use this to group file
# operation statements within a block.
# The advantage of with statement is it will take care closing of file,after completing all
# operations automatically even in the case of exceptions also, and we are not required to
# close explicitly.
#Eg:
# with open("abc.txt","w") as f:
#     f.write("Python\n")
#     f.write("JAVA\n")
#     f.write("C LAN\n")
#     print("Is File Closed: ",f.closed)
#     print("Is File Closed: ",f.closed)

# The seek() and tell() methods:
# tell():
# ==>We can use tell() method to return current position of the cursor(file pointer) from
# beginning of the file. [ can you plese telll current cursor position]
# The position(index) of first character in files is zero just like string index

# f=open("Python.txt","r")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())

# seek():
# We can use seek() method to move cursor(file pointer) to specified location.
# [Can you please seek the cursor to a particular location]
# f.seek(offset, fromwhere)
# offset represents the number of positions
# The allowed values for second attribute(from where) are
# 0---->From beginning of file(default value)
# 1---->From current position
# 2--->From end of the file

# data="All Students are STUPIDS"
# f=open("abc.txt","w")
# f.write(data)
# with open("abc.txt","r+") as f:
#     text=f.read()
#     print(text)
#     print("The Current Cursor Position: ",f.tell())
#     f.seek(17)
#     print("The Current Cursor Position: ",f.tell())
#     f.write("GEMS!!!")
#     f.seek(0)
#     text=f.read()
#     print("Data After Modification:")
#     print(text)


# Ass1 : read and extract the keywords from python file and write keywords in anotherfile called keywords.txt

# file.py

# def python(a,b)
   # return a+b
# if a>b:
#    print(a)
#   else:
#    print(b)
# def python(a,b)
   # return a+b

