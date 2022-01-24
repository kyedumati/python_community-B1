class Student:
    '''''Developed by durga for python demo'''
    def __init__(self):
        print("inside init")
        self.name='durga'
        self.age=40
        self.marks=80

    def talk(self,age):
        print("Hello I input :", age)
        print("Hello I am :",self.name)
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)

s = Student()   # create an object
s.talk(20)