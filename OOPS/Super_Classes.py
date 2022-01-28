# super() is a built-in method which is useful to call the super class constructors,variables and
# methods from the child class.
class Person:
    def __init__(self,name,age):        #  getting values from sub class init method
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):      #once u crete object
        super().__init__(name,age)          #  parent class constrctor   calling with args
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()                        # super class display method
        print('Roll No:',self.rollno)
        print('Marks:',self.marks)

# s1=Student("python",22,101,90)
#s1.display()


class P:
    a=10          # static var
    def __init__(self):
        self.b=10
    def m1(self):        # instance methid
        print('Parent instance method')
    @classmethod          # class method
    def m2(cls):
        print('Parent class method')
    @staticmethod       #   we can define  like normal fun
    def m3():
        print('Parent static method')
class C(P):
    a=888
    def __init__(self):
        super().__init__()     # calling parent class construtor
        print(super().a)       #   10
        super().m1()
        super().m2()
        super().m3()

    def python(self):
        super().m1()
        super().m2()
        super().m3()
#
# c=C()
# c.python()

# crete a class to remove desired char from string  -> take input from keyboard
#Input :# embedded     >  mbddd
            # character: 'd'
            #  Output : embee
# create a class remove duplicate ele from string  -> take input from keyboard
# ass2    Input : vecteeovvorr
#              Output : vector

#Ass1


class A :
    def python(self):
        print("Python clas A")
class B(A) :
    def JAVA(self):
        print("JAVA clas B")
        super().python()

obj=B()
obj.JAVA()





