# Syntax errors
# x=10
# if x==10
#     print(x)
# Run time errors
# #print(10/0)
# print(10/"ten")

# print("python")
# print(10/0)
# print("java")

# What is Exception:
# An unwanted and unexpected event that disturbs normal flow of program is called
# exception.
# exception is an event it intrupts the normal flow of execution of program

# Ex :
# Q. What is an Exception?
# Q. What is the purpose of Exception Handling?
# Q. What is the meaning of Exception Handling?
#
# It is highly recommended to handle exceptions. The main objective of exception handling
# is Graceful Termination of the program

# Exception handling does not mean repairing exception. We have to define alternative way
# to continue rest of the program normally.
# Eg:
# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError
# EOFError
# SleepingError
#
# Default Exception Handing in Python:
# Every exception in Python is an object. For every exception type the corresponding classes
# are available.
# Whevever an exception occurs PVM will create the corresponding exception object and
# will check for handling code. If handling code is not available then Python interpreter
# terminates the program abnormally and prints corresponding exception information to
# the console.
# The rest of the program won't be executed

# print("python")
# print(10/0)
# print("HI")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(10/2)

# syntax:
# try :
#     s1
#     s2
#     s3
# except errorname :
#     s4
#     s4


# Control Flow in try-except:
# try:
#  stmt-1
#  stmt-2
#  stmt-3
# except XXX:
#  stmt-4
# stmt-5

# try:
#     print(10/2)
#     print("java")
#     print("C++")
# except ZeroDivisionError as e:
#     # print(10/2)
#print("Python")


# case-1: If there is no exception
#  1,2,3,5 and Normal Termination
# case-2: If an exception raised at stmt-2 and corresponding except block matched
#  1,4,5 Normal Termination
#
# case-3: If an exception raised at stmt-2 and corresponding except block not matched
#  1, Abnormal Termination
#
# case-4: If an exception raised at stmt-4 or at stmt-5 then it is always abnormal
# termination.

# Conclusions:
# 1. within the try block if anywhere exception raised then rest of the try block wont be
# executed eventhough we handled that exception. Hence we have to take only risky code
# inside try block and length of the try block should be as less as possible.
# 2. In addition to try block,there may be a chance of raising exceptions inside except and
# finally blocks also.
# 3. If any statement which is not part of try block raises an exception then it is always
# abnormal termination.

#How to print exception information:
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("exception raised and its description is:",msg)
#     #print(10/2)

#Output exception raised and its description is: division by zero

# try:
#     print("java")    # s1
#     print(10 / 0)  # s2  #ZeroDivisionError
#     print("python") #s3
# except  ValueErrror as e:
#     print(10/2)       #s4
# print("NO error")     #s5

# try with multiple except blocks:
# The way of handling exception is varied from exception to exception.Hence for every
# exception type a seperate except block we have to provide. i.e try with multiple except
# blocks is possible and recommended to use.
#print(10/'ten')

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / y)
# except (TypeError,ValueError,ZeroDivisionError)  as e:
#     print(e)
# print("PYTHON IS GOOD")
# except ValueError:
#     print("please provide int value only")

# If try with multiple except blocks available then the order of these except blocks is
# important .Python interpreter will always consider from top to bottom until matched
# except block identified
#
# single except block that can handle multiple exceptions:
# We can write a single except block that can handle multiple different types of exceptions.
# except (Exception1,Exception2,exception3,..): or
# except (Exception1,Exception2,exception3,..) as msg :
# Parenthesis are mandatory and this group of exceptions internally considered as tuple.

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / y)
# except (ZeroDivisionError,ValueError) as msg:
#     print("Plz Provide valid numbers only and problem is: ", msg)


#default except block

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / 0)
#
# except (FileNotFoundError) :
#     print("Zero Division Error : cant divide with zero"   )
# except:
#     print("Default Except : Plz provide valid input only")



# default except must be last
# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / y)
# except:
#     print("Default Except : Plz provide valid input only")
# except ZeroDivisionError :
#     print("Zero Division Error : cant divide with zero")

# The following are various possible combinations of except blocks
# except ZeroDivisionError:
# except ZeroDivisionError as msg:
# except (ZeroDivisionError,ValueError) :
# except (ZeroDivisionError,ValueError) as msg:
# except :

# Finally block :

#purpose of finally block
# it is not recommended to maintain or clean up the code inside try block because there is no guarentee for the execution
# of every statement inside try block always.
# it is not recommended to maintain or clean up the code inside Except block because there is no guarentee for the execution of except block
# if there is no exception then except block wont be execute
# Hence we required some place to maintain clean up code which should be executed
# always irrespective of whether exception raised or not raised and whether exception
# handled or not handled. Such type of best place is nothing but finally block.
# syntax:
# try:
#  Risky Code
# except:
#  Handling Code
# finally:
#  Cleanup code
#case 1
# try:
#     print("try")
# except:
#     print("except")
# finally:
#     print("finally")

#case 2 :
# try:
#     print("try")
#     print(10/0)
# except ZeroDivisionError:
#     print("except")
# finally:
#     print("finally")

#case 3
# there is a exception raised but not handled
# try:
#     print("try")
#     print(10/0)
# except ValueError:
#     print("except")
# finally:
#     print("finally")


# *** Note: There is only one situation where finally block won't be executed ie whenever
# we are using os._exit(0) function.
# Whenever we are using os._exit(0) function then Python Virtual Machine itself will be
# shutdown.In this particular case finally won't be executed.

# import os
# try:
#     print("try")
#     os._exit(0)
# except ValueError:
#     print("except")
# finally:
#     print("finally")


# nested try-except-finlly blocks    -> one try except and finally block contains another try except and finally block called nested try-exxcept-finally block
#syntax
# try:
#  ----------
#  ----------
#  ----------
#  try:
#  -------------
#  --------------
#  --------------
#  except:
#  --------------
#  --------------
#  --------------
#  ------------
# finally:
# --------
# ---------
# except:
#  -----------
#  -----------
# finally:
# --------
# ---------


# try:
#     print("outer try block") # s1
#     print(10 / 0)
#     try:
#         print("Inner try block") #s2
#     except ZeroDivisionError:
#         print("Inner except block") #s3
#     finally:
#         print("Inner finally block") #s4
# except ZeroDivisionError:
#     print("outer except block")   #s5
# finally:
#     print("outer finally block")  #s5

# else block with try-except-finally

# We can use else block with try-except-finally blocks.
# else block will be executed if and only if there are no exceptions inside try block.
# try:
# Risky Code
# except:
# will be executed if exception inside try
# else:
# will be executed if there is no exception inside try
# finally:
# will be executed whether exception raised or not raised and handled or not handled

# try:
#     print("try")
#    # print(10/0)   #
# except :            # default except
#     print("Except")
# else:
#     print("else")
# finally:
#     print("Finally")

# predefind and user defined Exceptions

# Predefined
# The exceptions which are raised automatically by Python virtual machine whenver a
# particular event occurs, are called pre defined exceptions.
#print(int("Ten"))  # value error

# user defined Exceptions:

# Also known as Customized Exceptions or Programatic Exceptions
# Some time we have to define and raise exceptions explicitly to indicate that something
# goes wrong ,such type of exceptions are called User Defined Exceptions or Customized
# Exceptions
# Programmer is responsible to define these exceptions and Python not having any idea
# about these. Hence we have to raise explicitly based on our requirement by using "raise"
# keyword.
#syntax:
# class classname(predefined exception class name):
#  def __init__(self,arg):
#  self.msg=arg

# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
# age=int(input("Enter Age:"))
# if age<18:
#     raise TooYoungException("Plz wait some more time you will get best match soon!!!")
# elif age>35:
#     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
# else:
#     print("You will get match details soon by email!!!")
# # Note:
# # raise keyword is best suitable for customized exceptions but not for pre defined
# # exceptions
#















































