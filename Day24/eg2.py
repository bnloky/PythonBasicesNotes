class Test:
    a=10                            #static variable which can define inside the class and outside of the method
    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):                   #instance/normal method 
          print(self.a)
          print(Test.a)

    @classmethod
    def m2(cls):
         print(cls.a)
         print(Test.a)

    @staticmethod
    def m3():
         print(Test.a)

t=Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()