class TestClass:
    def talk(self):
        try:
             x=int(input("Enter First Number: "))
             y=int(input("Enter Second Number: "))
             print(x/y)
        except ZeroDivisionError :
             print("Can't Divide with Zero")
        except ValueError:
             print("please provide int value only")
        except:
            print("test")



test = TestClass()
test.talk()