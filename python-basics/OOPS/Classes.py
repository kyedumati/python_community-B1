class A():
    def __init__(self):
        print("init method")

    def method1(self):
        print("method1")

    @staticmethod
    def test():
        print("inside test")

obj = A()
A.test()
obj.method1()