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
# #
# x=["HELLO\n","CHINNA\n","HOW R U\n"]
# f=open('Python.txt','w+')
# f.writelines(x)
# f.seek(0)
# y=f.read()     # all data read line by line where as readines wil give list[]
# print(y)
# f.close()

# Reading Character Data from text files:
# We can read character data from text file by using the following read methods.
# read() To read total data from the file (char vy char )
# read(n)  To read 'n' characters from the file ( we can read num of chars)
# readline() To read only one line
# readlines() To read all lines into a list
# Eg 1: To read total data from the file
# x=["HELLO\n","CHINNA\n","HOW R U\n"]
# f=open("abc.txt",'w')
# f.writelines(x)
# f.close()
# f=open("abc.txt",'r')
# data=f.read()
# print(data)
# f.close()
#
# Eg 2: To read only first 10 characters:
# f=open("abc.txt",'r')
# data=f.read(10)
# print(data)
# f.close()

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
# print(type(lines))
# for line in lines:
#     print(line,end='')
# f.close()

#Eg 5:
# f=open("abc.txt","r")
# f.seek(0)
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print("Remaining data")
# print(f.read())
#f.close()

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

# f=open("abc.txt","r")
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

# data="All Students are GOOD"
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

# How to check a particular file exists or not?
# We can use os library to get information about files in our computer.
# os module has path sub module,which contains isFile() function to check whether a
# particular file exists or not?
# os.path.isfile(fname)

# import os,sys
# fname="Python.txt"
# #if os.path.isfile(fname):  #
# if os.path.exists(fname):
#     print("File exists:",fname)
#     f=open(fname,"r")
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# print("The content of file is:")
# data=f.read()
# print(data)



# Handling Binary Data:
# It is very common requirement to read or write binary data like images,video files,audio
# files etc.

#  #Program to read image file and write to a new image file?
# f1=open("NAGA.jpg","rb")
# f2=open("NAGA_new.jpg","wb")
# bytes=f1.read()
# print(bytes)
# f2.write(bytes)
# print("New Image is available with the name: newpic.jpg")

# CSV==>Comma seperated values
# As the part of programming,it is very common requirement to write and read data wrt csv
# files. Python provides csv module to handle csv files.

# import csv
# # # with open("emp.csv","w",newline='') as f:
# with open("emp.csv", "w",newline='') as f:
#     w=csv.writer(f) # returns csv writer object
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])
# n=int(input("Enter Number of Employees:"))
# for i in range(n):
#     eno=input("Enter Employee No:")
#     ename=input("Enter Employee Name:")
#     esal=input("Enter Employee Salary:")
#     eaddr=input("Enter Employee Address:")
#     w.writerow([eno,ename,esal,eaddr])
#     print("Total Employees data written to csv file successfully")

# Note: If we are not using newline attribute then in the csv file blank lines will be included
# between data. To prevent these blank lines, newline attribute is required in Python-3,but
# in Python-2 just we can specify mode as 'wb' and we are not required to use newline
# attribute.

# #Reading Data from csv file:
# import csv
# f=open("emp.csv",'r')
# r=csv.reader(f) #returns csv reader object
# data=list(r)
# print(data)
# for line in data:
#     for word in line:
#         print(word,"\t",end='')
#     print()


# Zipping and Unzipping Files:
# It is very common requirement to zip and unzip files.
# The main advantages are:
# 1. To improve memory utilization
# 2. We can reduce transport time
# 3. We can improve performance.
# To perform zip and unzip operations, Python contains one in-bulit module zip file.
# This module contains a class : ZipFile
# To create Zip file:
# We have to create ZipFile class object with name of the zip file,mode and constant
# ZIP_DEFLATED. This constant represents we are creating zip file.
# Once we create ZipFile object,we can add files by using write() method.
# f.write(filename)
# from zipfile import *
# f=ZipFile("files.zip",'w',ZIP_DEFLATED)
# f.write("file1.txt")
# f.write("file2.txt")
# f.close()
# print("files.zip file created successfully")

# To perform unzip operation:
# We have to create ZipFile object as follows
# f = ZipFile("files.zip","r",ZIP_STORED)
# ZIP_STORED represents unzip operation. This is default value and hence we are not
# required to specify.
# Once we created ZipFile object for unzip operation,we can get all file names present in
# that zip file by using namelist() method.
# # names = f.namelist()
# from zipfile import *
# f=ZipFile("files.zip",'r',ZIP_STORED)
# names=f.namelist()
# for name in names:
#     print( "File Name: ",name)
#     print("The Content of this file is:")
#     f1=open(name,'r')
#     print(f1.read())
#     print()
#
# Working with Directories:
# It is very common requirement to perform operations for directories like
# 1. To know current working directory
# 2. To create a new directory
# 3. To remove an existing directory
# 4. To rename a directory
# 5. To list contents of the director
#
# To perform these operations,Python provides inbuilt module os,which contains several
# functions to perform directory related operations
# To Know Current Working Directory:
# import os
# cwd=os.getcwd()
# print("Current Working Directory:",cwd)

# To create a sub directory in the current working directory
# import os
# os.mkdir("mysub")
# print("mysub directory created in cwd")

# Q3. To create a sub directory in mysub directory:
#  cwd
#  |-mysub
#  |-mysub

import os
# if os.path.isdir("mysub"):
#     os.mkdir("mysub/mysub2")
# print("mysub2 created inside mysub")
#Q4. To create multiple directories like sub1 in that sub2 in that sub3:
# import os
# os.makedirs("sub1/sub2/sub3")
# print("sub1 and in that sub2 and in that sub3 directories created")
# 5. To remove a directory:
# import os
# os.rmdir("mysub")
# print("mysub2 directory deleted")

# 6. To remove multiple directories in the path:
# import os
# os.removedirs("sub1/sub2/sub3")
# print("All 3 directories sub1,sub2 and sub3 removed")
# 7. To rename a directory:
# import os
#os.mkdir("mysub")
# os.rename("mysub","newdir")
# print("mysub directory renamed to newdir")
#
# Q8. To know contents of directory:
# os module provides listdir() to list out the contents of the specified directory. It won't
# display the contents of sub directory.

# import os
# print(os.listdir("."))

# The above program display contents of current working directory but not contents of sub
# directories.
# If we want the contents of a directory including sub directories then we should go for
# walk() function

#Q9. To know contents of directory including sub directories:

# We have to use walk() function
# [Can you please walk in the directory so that we can aware all contents of that directory]
# os.walk(path, topdown=True, onerror=None, followlinks=False)

#It returns an Iterator object whose contents can be displayed by using for loop

# path-->Directory path. cwd means .
# topdown=True --->Travel from top to bottom
# onerror=None --->on error detected which function has to execute.
# followlinks=True -->To visit directories pointed by symbolic links
# import os
# for dirpath,dirnames,filenames in os.walk('.'):
#     print("Current Directory Path:",dirpath)
#     print("Directories:",dirnames)
#     print("Files:",filenames)
#     print()

# Q. What is the difference between listdir() and walk() functions?
# In the case of listdir(), we will get contents of specified directory but not sub directory
# contents. But in the case of walk() function we will get contents of specified directory and
# its sub directories also

# Running Other programs from Python program
# os module contains system() function to run programs and commands.
# It is exactly same as system() function in C language.
#os.system("os.listdir()")
#  The argument is any command which is executing from DOS.
# import os
# #os.system("dir *.py")
# if os.path.isfile("print_max.py"):
#     os.system("py print_max.py")   # we can call one file from another file

# How to get information about a File:
# We can get statistics of a file like size, last accessed time,last modified time etc by using
# stat() function of os module.
stats = os.stat("abc.txt")
print(stats)
# The statistics of a file includes the following parameters:
# st_mode==>Protection Bits
# st_ino==>Inode number
# st_dev===>device
# st_nlink===>no of hard links
# st_uid===>userid of owner
# st_gid==>group id of owner
# st_size===>size of file in bytes
# st_atime==>Time of most recent access
# st_mtime==>Time of Most recent modification
# st_ctime==> Time of Most recent meta data change
#
# st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st
# 1970 ,12:00AM. By using datetime module fromtimestamp() function,we can get exact
# date and time.
# To print all statistics of file abc.txt:
# import os
# stats=os.stat("Python.txt")
# print(stats)

# import os
# from datetime import *
# stats=os.stat("Python.txt")
# print("File Size in Bytes:",stats.st_size)
# print("File Last Accessed Time:",datetime.fromtimestamp(stats.st_atime))
# print("File Last Modified Time:",datetime.fromtimestamp(stats.st_mtime))
